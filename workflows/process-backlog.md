# Process Backlog Workflow

When user says `/backlog` or "process my backlog", follow these steps:

## Steps

### 1. Read BACKLOG.md
Read all items from `BACKLOG.md` (root file).

### 2. Categorize Each Item

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

### 3. Check for Duplicates

Before creating new files, check against existing items using settings from `config.yaml`:

**Deduplication settings:**
- `similarity_threshold` - How similar before flagging (0-1 scale, default 0.6)
- `check_categories` - Consider category when matching (default true)
- `check_keywords` - Use keyword overlap for matching (default true)

**Process:**
- Scan existing tasks in `tasks/`
- Scan existing opportunities in `knowledge/opportunities/`
- Scan existing references in `knowledge/references/`
- Apply similarity threshold and matching rules from config
- If similar item exists, suggest merging or linking instead of duplicating

### 4. Create Task Files

For each task, create file in `tasks/` with frontmatter:

```yaml
---
title: Task name
category: auto-assigned from config.yaml keywords
priority: P0/P1/P2/P3
status: n
created_date: YYYY-MM-DD
due_date: YYYY-MM-DD (if mentioned in backlog)
---

## Context
[Why this task matters, background info]

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
- Use `category_keywords` from `config.yaml` to auto-assign task category
- Match task description against keyword lists for each category
- If multiple categories match, choose the most specific one
- Default to "other" if no keywords match

### 5. Enforce Priority Caps

Check priority caps from `config.yaml`:
- P0: Max 3 tasks
- P1: Max 7 tasks
- P2: Max 15 tasks
- P3: Unlimited

If caps exceeded when creating new tasks:
1. Count existing tasks at each priority level
2. If new task would exceed cap, ask user: "You already have [N] P0 tasks. Should I demote one to P1, or make this new task P1 instead?"
3. Show user current P0/P1 tasks for context
4. Wait for user decision before proceeding

### 6. Create Opportunity Files

For each opportunity, create file in `knowledge/opportunities/` with this structure:

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

### 7. Create/Update References

For references:
- Add to existing reference file if related topic exists
- Create new file in `knowledge/references/` if new topic
- Use descriptive filenames: `competitor-analysis.md`, `pricing-research.md`

### 8. Archive & Clear

After processing all items:
1. Archive remaining BACKLOG.md content to `knowledge/notes/YYYY-MM-DD.md`
   - This preserves uncategorized items (meeting notes, random thoughts)
2. Clear `BACKLOG.md` completely
3. Summarize what was created:
   - "Created X tasks (P0: N, P1: N, P2: N, P3: N)"
   - "Created N opportunities"
   - "Added N references"
   - "Archived remaining items to knowledge/notes/YYYY-MM-DD.md"

## Tips

- When uncertain about categorization, ask user
- Better to create fewer, clearer items than many vague ones
- If backlog item lacks context, ask user for clarification before creating
- Use context from `knowledge/product-strategy/` to inform priority decisions
- Reference `knowledge/frameworks/` for prioritization methodology
- All configurable values (priority caps, deduplication thresholds, task aging) come from `config.yaml`
- Users can customize these settings by editing `config.yaml`
