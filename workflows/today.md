---
allowed-tools: find_overdue_tasks, list_tasks, Glob, Read
argument-hint:
description: Get all tasks due today or past due
---

## Context

You have access to the task-manager-mcp server with tools to query tasks by due date.

Tasks are stored in markdown files in the `tasks/` directory with YAML frontmatter containing `due_date`.

Today's date: 2026-01-06

## Your task

Show all tasks that are due today or overdue, prioritized by urgency.

**Steps:**

1. **Try MCP first**: Attempt to use `find_overdue_tasks` and `list_tasks` MCP tools

2. **Failover if needed**: If MCP tools fail or aren't available:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Filter for tasks where `due_date` is today (2026-01-06) or earlier
   - Mention in output: "Note: Using direct file reading (MCP unavailable)"

3. **Combine and prioritize**: Sort by:
   - Overdue tasks first (most overdue at top)
   - Today's tasks second
   - Within each group, sort by priority (P0 → P1 → P2 → P3)

4. **Format output**: Display with clear visual indicators:
   - Show how many days overdue (if applicable)
   - Highlight P0/P1 tasks
   - Include status, category, and file path

**Example output format:**
```
⏰ Due Today & Overdue Tasks

🚨 OVERDUE
  [s] Task name (P0, Category) - 3 days overdue
      tasks/filename.md

  [n] Task name (P1, Category) - 1 day overdue
      tasks/filename.md

📅 DUE TODAY
  [s] Task name (P0, Category)
      tasks/filename.md

---
Total: X overdue, Y due today
```

**Important:**
- Prefer MCP tools, fall back to file reading if needed
- If no tasks are due/overdue, say so clearly and suggest reviewing P0/P1 tasks
- Recommend specific next actions based on what's found
