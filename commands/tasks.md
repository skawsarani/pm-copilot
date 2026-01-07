---
allowed-tools: list_tasks, get_task_summary, Glob, Read
argument-hint: [optional filters: priority, status, category]
description: Get all tasks with their details
---

## Context

You have access to the task-manager MCP server with tools to query tasks.

Tasks are stored in markdown files in the `tasks/` directory with YAML frontmatter.

## Your task

Display all tasks with their details in a clear, organized format.

If the user provided filters as arguments, use them: $ARGUMENTS

**Steps:**

1. **Try MCP first**: Attempt to use `get_task_summary` and `list_tasks` MCP tools

2. **Failover if needed**: If MCP tools fail or aren't available:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Mention in output: "Note: Using direct file reading (MCP unavailable)"

3. **Apply filters**: If $ARGUMENTS provided, filter by:
   - Priority: P0, P1, P2, P3
   - Status: n (not started), s (started), b (blocked), d (done)
   - Category

4. **Format output**: Display tasks grouped by priority (P0 → P1 → P2 → P3) with:
   - Task title
   - Status (n/s/b/d)
   - Category
   - Due date (if applicable)
   - File path for reference

5. **Highlight important items**:
   - Flag overdue tasks (compare due_date to today: 2026-01-06)
   - Show P0 tasks prominently
   - Indicate blocked tasks
   - Show priority cap status (P0: max 3, P1: max 7, P2: max 15)

**Example output format:**
```
📊 Task Summary: X total tasks (P0: X/3, P1: X/7, P2: X/15, P3: X)

🔴 P0 (Critical) - Max 3
  [s] Task name (Category) - Due: YYYY-MM-DD
      tasks/filename.md

🟡 P1 (High) - Max 7
  [n] Task name (Category)
      tasks/filename.md

...
```

**Important:**
- Prefer MCP tools, fall back to file reading if needed
- Keep output scannable and actionable
- If no tasks found, suggest checking BACKLOG.md or creating new tasks
