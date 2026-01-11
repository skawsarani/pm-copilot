---
allowed-tools: process_backlog, clear_backlog, check_duplicates, create_task, list_tasks, Glob, Read, Write
argument-hint:
description: Process BACKLOG.md into organized tasks, opportunities, and references
---

## Context

Configuration for backlog processing is in `core/config.yaml`:
- Priority caps: P0 max 3, P1 max 7, P2 max 15
- Category keywords for auto-assignment
- Duplicate detection thresholds

Today's date: $TODAY

## Your Task

Process all items from `BACKLOG.md` into organized tasks, opportunities, and references.

## Using MCP Tools (Preferred)

If the task-manager MCP server is available, use these tools:

1. **process_backlog** (auto_create=false) - Preview with:
   - Automatic categorization
   - Duplicate detection
   - Ambiguity checking

2. Review ambiguous items and duplicates with user

3. **process_backlog** (auto_create=true) - Create approved tasks

4. **clear_backlog** - Archive and clear BACKLOG.md

## Manual Processing (Fallback)

If MCP tools unavailable, mention "Note: Using direct file reading (MCP unavailable)" and follow these steps:

### Step 1: Read BACKLOG.md

Read all items from `BACKLOG.md` (root file).

### Step 2: Categorize Each Item

Assign each item to one category:

**Tasks** - Actionable, time-bound work → `tasks/` folder
- Examples: "Email Sarah about Q4 goals", "Review PRD draft", "Update roadmap"
- Must have clear action and completion criteria

**Opportunities** - Strategic ideas to explore → `knowledge/opportunities/` folder
- Examples: "Mobile performance issues", "Enterprise SSO request", "AI-powered search"
- Product opportunities, features, strategic initiatives

**References** - Useful context, links, info → `knowledge/references/`
- Examples: Competitor analysis, articles, links, research notes
- No action needed, just context to save

**Uncategorized** - Everything else stays in BACKLOG.md (will be archived)
- Examples: Meeting notes, random thoughts, incomplete ideas

### Step 3: Check for Duplicates

Before creating new files, check against existing items:

- Scan existing tasks in `tasks/`
- Scan existing opportunities in `knowledge/opportunities/`
- Scan existing references in `knowledge/references/`
- If similar item exists, suggest merging or linking instead of duplicating

### Step 4: Create Task Files

For each task, create file in `tasks/` with frontmatter:

```yaml
---
title: Task name
category: auto-assigned from core/config.yaml keywords
priority: P0/P1/P2/P3
status: n
created_date: YYYY-MM-DD
due_date: YYYY-MM-DD (if mentioned in backlog)
---

## Context
[Why this task matters, link to relevant goal from GOALS.md]

## Next Actions
- [ ] First step
- [ ] Second step

## Progress Log
- YYYY-MM-DD: Task created
```

**Priority assignment:**
- P0 (Critical): Urgent, blocks other work, time-sensitive
- P1 (High): Important, has deadline this week
- P2 (Medium): Normal work, this month
- P3 (Low): Nice to have, backlog

**Auto-categorization:**
- Use `category_keywords` from `core/config.yaml` to auto-assign
- Default to "other" if no keywords match

### Step 5: Enforce Priority Caps

Check caps from `core/config.yaml`:
- P0: Max 3 tasks
- P1: Max 7 tasks
- P2: Max 15 tasks
- P3: Unlimited

If caps exceeded:
1. Count existing tasks at each priority level
2. Ask user: "You already have [N] P0 tasks. Should I demote one to P1, or make this new task P1 instead?"
3. Show current P0/P1 tasks for context
4. Wait for user decision before proceeding

### Step 6: Create Opportunity Files

For each opportunity, create file in `knowledge/opportunities/`:

```markdown
# [Opportunity Name]

## Description
[What this opportunity is about]

## Strategic Context
[Why it matters, alignment with product vision]

## What We Know
- Current data, insights, evidence
- User feedback or requests
- Business impact

## What We Should Research
- Open questions
- Validation needed
- Assumptions to test

## Initial Thoughts
[Potential approaches, not decisions - exploratory]
```

### Step 7: Create/Update References

For references:
- Add to existing reference file if related topic exists
- Create new file in `knowledge/references/` if new topic
- Use descriptive filenames: `competitor-analysis.md`, `pricing-research.md`

### Step 8: Archive & Clear

After processing all items:
1. Archive remaining BACKLOG.md content to `knowledge/notes/YYYY-MM-DD.md`
2. Clear `BACKLOG.md` completely
3. Summarize what was created:
   - "Created X tasks (P0: N, P1: N, P2: N, P3: N)"
   - "Created N opportunities"
   - "Added N references"
   - "Archived remaining items to knowledge/notes/YYYY-MM-DD.md"

## Key Reminders

- Ask for clarification on ambiguous items BEFORE creating
- Link tasks to goals from GOALS.md in the Context section
- If no goal fits an item, ask user whether to create a new goal or clarify why the work matters
- Better to create fewer, clearer items than many vague ones
