#!/usr/bin/env python3
"""
PM Co-Pilot Task Management MCP Server

Provides programmatic access to task management through Model Context Protocol.
Exposes 10 tools for CRUD operations, deduplication, priority enforcement, and statistics.
"""

import asyncio
import re
from datetime import datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Optional

import yaml
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
TASKS_DIR = PROJECT_ROOT / "tasks"
CONFIG_FILE = PROJECT_ROOT / "core" / "config.yaml"

# Initialize MCP server
app = Server("pm-tasks")


# Helper Functions

def load_config() -> dict:
    """Load configuration from core/config.yaml"""
    if not CONFIG_FILE.exists():
        return {
            "priority_caps": {"P0": 3, "P1": 7, "P2": 15, "P3": 999},
            "task_aging": {"prune_completed_after": 90, "flag_stale_after": 14},
            "deduplication": {
                "similarity_threshold": 0.6,
                "check_categories": True,
                "check_keywords": True,
            },
            "category_keywords": {},
        }

    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)


def parse_yaml_frontmatter(file_path: Path) -> tuple[dict, str]:
    """Parse YAML frontmatter and markdown body from a task file"""
    if not file_path.exists():
        return {}, ""

    with open(file_path, "r") as f:
        content = f.read()

    # Match YAML frontmatter between --- delimiters
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter_str, body = match.groups()
    try:
        frontmatter = yaml.safe_load(frontmatter_str) or {}
    except yaml.YAMLError:
        frontmatter = {}

    return frontmatter, body.strip()


def write_task_file(file_path: Path, frontmatter: dict, body: str):
    """Write task file with YAML frontmatter"""
    yaml_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    content = f"---\n{yaml_str}---\n\n{body}\n"

    with open(file_path, "w") as f:
        f.write(content)


def get_all_tasks() -> list[dict]:
    """Get all tasks with metadata"""
    tasks = []

    if not TASKS_DIR.exists():
        return tasks

    for task_file in TASKS_DIR.glob("*.md"):
        if task_file.name == "README.md":
            continue

        frontmatter, body = parse_yaml_frontmatter(task_file)
        task = {
            "file": task_file.name,
            "path": str(task_file),
            "title": frontmatter.get("title", ""),
            "priority": frontmatter.get("priority", "P3"),
            "status": frontmatter.get("status", "n"),
            "category": frontmatter.get("category", ""),
            "keywords": frontmatter.get("keywords", []),
            "due_date": frontmatter.get("due_date"),
            "created_date": frontmatter.get("created_date"),
            "updated_date": frontmatter.get("updated_date"),
            "body": body,
        }
        tasks.append(task)

    return tasks


def calculate_similarity(task1: dict, task2: dict, config: dict) -> float:
    """Calculate similarity score between two tasks (0-1 scale)"""
    # Title similarity using SequenceMatcher
    title1 = task1.get("title", "").lower()
    title2 = task2.get("title", "").lower()
    title_score = SequenceMatcher(None, title1, title2).ratio()

    # Keyword overlap if enabled
    keyword_score = 0.0
    if config["deduplication"]["check_keywords"]:
        keywords1 = set(k.lower() for k in task1.get("keywords", []))
        keywords2 = set(k.lower() for k in task2.get("keywords", []))

        if keywords1 and keywords2:
            overlap = len(keywords1 & keywords2)
            total = len(keywords1 | keywords2)
            keyword_score = overlap / total if total > 0 else 0.0

    # Category match if enabled
    category_match = 1.0
    if config["deduplication"]["check_categories"]:
        cat1 = task1.get("category", "").lower()
        cat2 = task2.get("category", "").lower()
        category_match = 1.0 if cat1 == cat2 else 0.5

    # Weighted average: title (60%), keywords (30%), category (10%)
    similarity = (title_score * 0.6 + keyword_score * 0.3) * category_match
    return similarity


def auto_categorize(title: str, body: str, config: dict) -> str:
    """Auto-categorize task based on keywords in config"""
    text = f"{title} {body}".lower()
    category_keywords = config.get("category_keywords", {})

    # Count keyword matches for each category
    matches = {}
    for category, keywords in category_keywords.items():
        count = sum(1 for keyword in keywords if keyword.lower() in text)
        if count > 0:
            matches[category] = count

    # Return category with most matches
    if matches:
        return max(matches, key=matches.get)

    return ""


def get_task_by_file(filename: str) -> Optional[dict]:
    """Get task by filename"""
    task_file = TASKS_DIR / filename
    if not task_file.exists():
        return None

    frontmatter, body = parse_yaml_frontmatter(task_file)
    return {
        "file": filename,
        "path": str(task_file),
        "title": frontmatter.get("title", ""),
        "priority": frontmatter.get("priority", "P3"),
        "status": frontmatter.get("status", "n"),
        "category": frontmatter.get("category", ""),
        "keywords": frontmatter.get("keywords", []),
        "due_date": frontmatter.get("due_date"),
        "created_date": frontmatter.get("created_date"),
        "updated_date": frontmatter.get("updated_date"),
        "body": body,
    }


# MCP Tool Handlers

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools"""
    return [
        Tool(
            name="list_tasks",
            description="List and filter tasks by priority, status, category, or age. Returns task summaries.",
            inputSchema={
                "type": "object",
                "properties": {
                    "priority": {
                        "type": "string",
                        "description": "Filter by priority (P0, P1, P2, P3)",
                        "enum": ["P0", "P1", "P2", "P3"],
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (n=not started, s=started, b=blocked, d=done)",
                        "enum": ["n", "s", "b", "d"],
                    },
                    "category": {
                        "type": "string",
                        "description": "Filter by category (technical, outreach, research, writing, admin)",
                    },
                    "days_old": {
                        "type": "integer",
                        "description": "Filter tasks created more than N days ago",
                    },
                },
            },
        ),
        Tool(
            name="get_task",
            description="Get full details of a specific task by filename",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Task filename (e.g., 'fix-auth-bug.md')",
                    }
                },
                "required": ["filename"],
            },
        ),
        Tool(
            name="create_task",
            description="Create a new task with YAML frontmatter. Auto-categorizes if category not provided. Checks priority caps.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Task title"},
                    "priority": {
                        "type": "string",
                        "description": "Priority (P0, P1, P2, P3)",
                        "enum": ["P0", "P1", "P2", "P3"],
                    },
                    "category": {
                        "type": "string",
                        "description": "Category (optional, will auto-categorize if not provided)",
                    },
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Keywords for deduplication and categorization",
                    },
                    "body": {
                        "type": "string",
                        "description": "Task description in markdown",
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Due date (YYYY-MM-DD format)",
                    },
                },
                "required": ["title", "priority", "body"],
            },
        ),
        Tool(
            name="update_task_status",
            description="Update task status (n=not started, s=started, b=blocked, d=done)",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Task filename (e.g., 'fix-auth-bug.md')",
                    },
                    "status": {
                        "type": "string",
                        "description": "New status",
                        "enum": ["n", "s", "b", "d"],
                    },
                },
                "required": ["filename", "status"],
            },
        ),
        Tool(
            name="update_task_priority",
            description="Update task priority. Checks priority caps before updating.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Task filename (e.g., 'fix-auth-bug.md')",
                    },
                    "priority": {
                        "type": "string",
                        "description": "New priority",
                        "enum": ["P0", "P1", "P2", "P3"],
                    },
                },
                "required": ["filename", "priority"],
            },
        ),
        Tool(
            name="get_task_summary",
            description="Get task statistics (counts by priority, status, category)",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="find_stale_tasks",
            description="Find tasks marked as started but not updated recently (uses flag_stale_after from config)",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="find_overdue_tasks",
            description="Find tasks past their due date",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="prune_completed_tasks",
            description="Delete tasks with status 'd' (done) older than specified days (uses prune_completed_after from config)",
            inputSchema={
                "type": "object",
                "properties": {
                    "dry_run": {
                        "type": "boolean",
                        "description": "If true, only list tasks that would be deleted without deleting them",
                    }
                },
            },
        ),
        Tool(
            name="check_duplicates",
            description="Check for similar existing tasks before creating a new one. Uses similarity scoring.",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Proposed task title"},
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Proposed keywords",
                    },
                    "category": {
                        "type": "string",
                        "description": "Proposed category",
                    },
                },
                "required": ["title"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""
    config = load_config()

    if name == "list_tasks":
        tasks = get_all_tasks()

        # Apply filters
        if "priority" in arguments:
            tasks = [t for t in tasks if t["priority"] == arguments["priority"]]

        if "status" in arguments:
            tasks = [t for t in tasks if t["status"] == arguments["status"]]

        if "category" in arguments:
            tasks = [t for t in tasks if t["category"] == arguments["category"]]

        if "days_old" in arguments:
            cutoff = datetime.now() - timedelta(days=arguments["days_old"])
            tasks = [
                t
                for t in tasks
                if t.get("created_date")
                and datetime.fromisoformat(t["created_date"]) < cutoff
            ]

        # Format output
        result = f"Found {len(tasks)} tasks:\n\n"
        for task in tasks:
            result += f"- **{task['title']}** ({task['file']})\n"
            result += f"  Priority: {task['priority']} | Status: {task['status']} | Category: {task['category']}\n\n"

        return [TextContent(type="text", text=result)]

    elif name == "get_task":
        filename = arguments["filename"]
        task = get_task_by_file(filename)

        if not task:
            return [TextContent(type="text", text=f"Task not found: {filename}")]

        result = f"# {task['title']}\n\n"
        result += f"**File:** {task['file']}\n"
        result += f"**Priority:** {task['priority']}\n"
        result += f"**Status:** {task['status']}\n"
        result += f"**Category:** {task['category']}\n"
        result += f"**Keywords:** {', '.join(task['keywords'])}\n"
        result += f"**Due Date:** {task.get('due_date', 'None')}\n"
        result += f"**Created:** {task.get('created_date', 'Unknown')}\n"
        result += f"**Updated:** {task.get('updated_date', 'Unknown')}\n\n"
        result += f"## Description\n\n{task['body']}\n"

        return [TextContent(type="text", text=result)]

    elif name == "create_task":
        # Check priority caps
        priority = arguments["priority"]
        priority_caps = config["priority_caps"]
        current_tasks = get_all_tasks()
        current_count = len([t for t in current_tasks if t["priority"] == priority])

        if current_count >= priority_caps.get(priority, 999):
            return [
                TextContent(
                    type="text",
                    text=f"Cannot create task: {priority} cap ({priority_caps[priority]}) would be exceeded. Current {priority} tasks: {current_count}",
                )
            ]

        # Auto-categorize if category not provided
        category = arguments.get("category", "")
        if not category:
            category = auto_categorize(
                arguments["title"], arguments.get("body", ""), config
            )

        # Generate filename from title
        filename = re.sub(r"[^a-z0-9]+", "-", arguments["title"].lower())
        filename = filename.strip("-") + ".md"
        task_file = TASKS_DIR / filename

        # Check if file already exists
        if task_file.exists():
            return [
                TextContent(
                    type="text", text=f"Task file already exists: {filename}"
                )
            ]

        # Create frontmatter
        now = datetime.now().isoformat()
        frontmatter = {
            "title": arguments["title"],
            "priority": priority,
            "status": "n",
            "category": category,
            "keywords": arguments.get("keywords", []),
            "created_date": now,
            "updated_date": now,
        }

        if "due_date" in arguments:
            frontmatter["due_date"] = arguments["due_date"]

        # Write task file
        write_task_file(task_file, frontmatter, arguments["body"])

        result = f"Task created: {filename}\n"
        result += f"Priority: {priority}\n"
        result += f"Category: {category}\n"
        result += f"Status: n (not started)\n"

        return [TextContent(type="text", text=result)]

    elif name == "update_task_status":
        filename = arguments["filename"]
        task_file = TASKS_DIR / filename

        if not task_file.exists():
            return [TextContent(type="text", text=f"Task not found: {filename}")]

        frontmatter, body = parse_yaml_frontmatter(task_file)
        frontmatter["status"] = arguments["status"]
        frontmatter["updated_date"] = datetime.now().isoformat()

        write_task_file(task_file, frontmatter, body)

        return [
            TextContent(
                type="text",
                text=f"Updated {filename} status to: {arguments['status']}",
            )
        ]

    elif name == "update_task_priority":
        filename = arguments["filename"]
        new_priority = arguments["priority"]
        task_file = TASKS_DIR / filename

        if not task_file.exists():
            return [TextContent(type="text", text=f"Task not found: {filename}")]

        # Get current task
        frontmatter, body = parse_yaml_frontmatter(task_file)
        old_priority = frontmatter.get("priority", "P3")

        # Check priority caps (excluding current task from count)
        priority_caps = config["priority_caps"]
        current_tasks = get_all_tasks()
        current_count = len(
            [
                t
                for t in current_tasks
                if t["priority"] == new_priority and t["file"] != filename
            ]
        )

        if current_count >= priority_caps.get(new_priority, 999):
            return [
                TextContent(
                    type="text",
                    text=f"Cannot update priority: {new_priority} cap ({priority_caps[new_priority]}) would be exceeded. Current {new_priority} tasks: {current_count}",
                )
            ]

        frontmatter["priority"] = new_priority
        frontmatter["updated_date"] = datetime.now().isoformat()

        write_task_file(task_file, frontmatter, body)

        return [
            TextContent(
                type="text",
                text=f"Updated {filename} priority from {old_priority} to {new_priority}",
            )
        ]

    elif name == "get_task_summary":
        tasks = get_all_tasks()

        # Count by priority
        priority_counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}
        for task in tasks:
            priority_counts[task["priority"]] += 1

        # Count by status
        status_counts = {"n": 0, "s": 0, "b": 0, "d": 0}
        for task in tasks:
            status_counts[task["status"]] += 1

        # Count by category
        category_counts = {}
        for task in tasks:
            cat = task["category"] or "uncategorized"
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Format output
        result = f"# Task Summary\n\n"
        result += f"**Total Tasks:** {len(tasks)}\n\n"

        result += f"## By Priority\n"
        for priority in ["P0", "P1", "P2", "P3"]:
            cap = config["priority_caps"].get(priority, 999)
            count = priority_counts[priority]
            result += f"- {priority}: {count}/{cap}\n"

        result += f"\n## By Status\n"
        status_names = {"n": "Not Started", "s": "Started", "b": "Blocked", "d": "Done"}
        for status, count in status_counts.items():
            result += f"- {status_names[status]}: {count}\n"

        result += f"\n## By Category\n"
        for category, count in sorted(category_counts.items()):
            result += f"- {category}: {count}\n"

        return [TextContent(type="text", text=result)]

    elif name == "find_stale_tasks":
        tasks = get_all_tasks()
        flag_stale_after = config["task_aging"]["flag_stale_after"]
        cutoff = datetime.now() - timedelta(days=flag_stale_after)

        stale_tasks = [
            t
            for t in tasks
            if t["status"] == "s"
            and t.get("updated_date")
            and datetime.fromisoformat(t["updated_date"]) < cutoff
        ]

        if not stale_tasks:
            return [
                TextContent(
                    type="text",
                    text=f"No stale tasks found (started but not updated in {flag_stale_after}+ days)",
                )
            ]

        result = f"Found {len(stale_tasks)} stale tasks (started but not updated in {flag_stale_after}+ days):\n\n"
        for task in stale_tasks:
            days_old = (
                datetime.now() - datetime.fromisoformat(task["updated_date"])
            ).days
            result += f"- **{task['title']}** ({task['file']})\n"
            result += f"  Last updated: {days_old} days ago | Priority: {task['priority']}\n\n"

        return [TextContent(type="text", text=result)]

    elif name == "find_overdue_tasks":
        tasks = get_all_tasks()
        today = datetime.now().date()

        overdue_tasks = [
            t
            for t in tasks
            if t.get("due_date")
            and datetime.fromisoformat(t["due_date"]).date() < today
            and t["status"] != "d"
        ]

        if not overdue_tasks:
            return [TextContent(type="text", text="No overdue tasks found")]

        result = f"Found {len(overdue_tasks)} overdue tasks:\n\n"
        for task in overdue_tasks:
            days_overdue = (today - datetime.fromisoformat(task["due_date"]).date()).days
            result += f"- **{task['title']}** ({task['file']})\n"
            result += f"  Due: {task['due_date']} ({days_overdue} days overdue) | Priority: {task['priority']} | Status: {task['status']}\n\n"

        return [TextContent(type="text", text=result)]

    elif name == "prune_completed_tasks":
        tasks = get_all_tasks()
        prune_after = config["task_aging"]["prune_completed_after"]
        cutoff = datetime.now() - timedelta(days=prune_after)
        dry_run = arguments.get("dry_run", False)

        completed_tasks = [
            t
            for t in tasks
            if t["status"] == "d"
            and t.get("updated_date")
            and datetime.fromisoformat(t["updated_date"]) < cutoff
        ]

        if not completed_tasks:
            return [
                TextContent(
                    type="text",
                    text=f"No completed tasks older than {prune_after} days found",
                )
            ]

        result = f"{'Would delete' if dry_run else 'Deleting'} {len(completed_tasks)} completed tasks older than {prune_after} days:\n\n"
        for task in completed_tasks:
            days_old = (
                datetime.now() - datetime.fromisoformat(task["updated_date"])
            ).days
            result += f"- {task['title']} ({task['file']}) - completed {days_old} days ago\n"

            if not dry_run:
                task_file = TASKS_DIR / task["file"]
                task_file.unlink()

        if dry_run:
            result += f"\n(Dry run - no files deleted. Run without dry_run to delete)"

        return [TextContent(type="text", text=result)]

    elif name == "check_duplicates":
        existing_tasks = get_all_tasks()
        threshold = config["deduplication"]["similarity_threshold"]

        proposed_task = {
            "title": arguments["title"],
            "keywords": arguments.get("keywords", []),
            "category": arguments.get("category", ""),
        }

        # Find similar tasks
        similar_tasks = []
        for task in existing_tasks:
            similarity = calculate_similarity(proposed_task, task, config)
            if similarity >= threshold:
                similar_tasks.append((task, similarity))

        if not similar_tasks:
            return [
                TextContent(
                    type="text",
                    text=f"No duplicate tasks found (threshold: {threshold})",
                )
            ]

        # Sort by similarity (highest first)
        similar_tasks.sort(key=lambda x: x[1], reverse=True)

        result = f"Found {len(similar_tasks)} similar tasks (threshold: {threshold}):\n\n"
        for task, similarity in similar_tasks:
            result += f"- **{task['title']}** ({task['file']})\n"
            result += f"  Similarity: {similarity:.2f} | Priority: {task['priority']} | Status: {task['status']}\n\n"

        result += "Consider updating an existing task instead of creating a duplicate."

        return [TextContent(type="text", text=result)]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
