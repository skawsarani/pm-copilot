# Tasks

Actionable tasks created from backlog processing or directly.

## Task Structure

Frontmatter fields:
- **title** - Task name
- **category** - technical, outreach, research, writing, admin, other
- **priority** - P0 (Critical), P1 (High), P2 (Normal), P3 (Low)
- **status** - n (not_started), s (started), b (blocked), d (done)
- **created_date** - YYYY-MM-DD
- **due_date** - YYYY-MM-DD (optional)
- **resource_refs** - Links to related files

Content:
- **Context** - Goals and references
- **Next Actions** - Steps to complete
- **Progress Log** - Notes, blockers, decisions

## Managing Tasks

**Update:**
- "Mark task [name] as complete"
- "Change task [name] status/priority/category"

**Find:**
- "Find tasks older than [N] days"
- "Find stale tasks"

**Prune:**
- "Prune completed tasks older than [N] days"

Tasks are marked complete with `status: d`. No file movement needed.

