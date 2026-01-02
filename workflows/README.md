# Workflows

PM Co-Pilot workflows for common tasks.

---

## Available Workflows

### Process Backlog

**Command:** `/backlog` or "Process my backlog"

**What it does:**
- Reads `BACKLOG.md`
- Categorizes into Tasks (P0-P3), Opportunities, References
- Enforces priority caps (P0≤3, P1≤7, P2≤15)
- Archives uncategorized items to `knowledge/notes/YYYY-MM-DD.md`
- Clears `BACKLOG.md`

**See:** [process-backlog.md](process-backlog.md)

---

## Skills (Auto-Invoked)

Most PM work is handled by skills that AI invokes automatically:

**Product Docs (`product-docs` skill):**
- `/prd [name]`, `/spec [name]`, `/brief [name]`
- `/user-stories [name]`, `/decision [topic]`

**UX Copy (`ux-copy` skill):**
- Translate to Canadian French
- Create UI copy, microcopy

**User Research (`user-research-analysis` skill):**
- Analyze interviews, create personas

**Prototyping (`prototype-builder` skill):**
- Build working prototypes

**Internal Comms (`internal-comms` skill):**
- Status reports, updates

---

## Natural Language

You don't need to memorize commands. AI understands natural language:

**Instead of:**
```
/backlog
/prd mobile-performance
```

**You can say:**
```
Process my backlog
Create a spec for the mobile performance opportunity
```

Talk to your AI like a colleague. It knows when to invoke workflows and skills.

---

## Common Patterns

**Monday morning:**
```
What should I work on today?
Process my backlog
```

**Feature kickoff:**
```
1. Add idea to BACKLOG.md
2. /backlog
3. /prd [opportunity-name]
4. /user-stories [opportunity-name]
```

**Research synthesis:**
```
Analyze the user interviews in knowledge/transcripts/
Create opportunities from the key insights
```

---

Workflows are starting points. The AI is smart - just tell it what you need.
