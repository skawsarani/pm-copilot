---
allowed-tools: list_tasks, Glob, Read
argument-hint: [optional: number of days, default 7]
description: Get tasks due in the next 7 days
---

## Context

You have access to the task-manager-mcp server with tools to query tasks by due date.

Tasks are stored in markdown files in the `tasks/` directory with YAML frontmatter containing `due_date`.

Today's date: 2026-01-06

## Your task

Show all tasks due in the next 7 days (or custom timeframe if specified).

If the user provided a custom number of days: $ARGUMENTS

**Steps:**

1. **Determine timeframe**:
   - Default: next 7 days (2026-01-06 to 2026-01-13)
   - If $ARGUMENTS provided, use that number of days instead

2. **Try MCP first**: Attempt to use `list_tasks` MCP tool and filter by date range

3. **Failover if needed**: If MCP tools fail or aren't available:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Filter for tasks where `due_date` is between today and end of timeframe
   - Exclude overdue tasks (those are for /today command)
   - Mention in output: "Note: Using direct file reading (MCP unavailable)"

4. **Group by date**: Organize tasks by their due date in chronological order

5. **Format output**: Display grouped by date with priority indicators:
   - Date headers (e.g., "Tomorrow", "Monday Jan 13", etc.)
   - Task priority, status, category
   - File path for reference

**Example output format:**
```
📅 Upcoming Tasks (Next 7 Days)

Tomorrow (2026-01-07)
  [n] Task name (P0, Category)
      tasks/filename.md

Wednesday (2026-01-08)
  [s] Task name (P1, Category)
      tasks/filename.md
  [n] Task name (P2, Category)
      tasks/filename.md

Friday (2026-01-10)
  [n] Task name (P1, Category)
      tasks/filename.md

---
Total: X tasks across Y days
```

**Important:**
- Prefer MCP tools, fall back to file reading if needed
- Use relative dates when helpful (Tomorrow, This Friday, etc.)
- Highlight P0/P1 tasks for visibility
- If no tasks in timeframe, suggest reviewing task priorities and deadlines
- Group "Today" and "Overdue" separately if found (suggest using /today instead)
