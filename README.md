# PM Co-Pilot

> Turn your AI assistant into a product management partner. Process ideas, generate specs, prioritize strategically.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What is This?

PM Co-Pilot is a simple system that turns AI assistants (Cursor, Claude Code) into PM tools:

- **Priority-Focused Workflow** - Max 3 P0 tasks keeps you focused
- **Backlog Processing** - Brain dump → Organized tasks/opportunities
- **Document Generation** - Specs, briefs, PRDs from conversation
- **Research Synthesis** - Transform interviews into insights
- **Voice Training** - Match your writing style

---

## Quick Start (10 minutes)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd pm-copilot
./setup.sh
cursor .    # Or your AI assistant
```

Tell your AI:
```
Read @AGENTS.md to understand how to help me as a PM Co-Pilot.
```

### 2. Add Your Context (15 minutes)

Fill in these essential files created by setup:

- `knowledge/product-strategy/current-strategy.md` - Vision, priorities, metrics
- `knowledge/company-context/company-overview.md` - Mission, products, team
- `knowledge/about-me/about-me.md` - Background, working style, preferences

See `templates/` for examples.

### 3. Start Using It

**Brain dump to BACKLOG.md:**
```markdown
## Mobile Performance Issues
- Source: Support tickets (15 this week)
- Context: Android app slow on startup
- Impact: 4.2⭐ rating drop

## Follow up with Sarah about Q4 goals
- Need to align on OKRs by end of week
```

**Process your backlog:**
```
/backlog
```

AI categorizes into:
- **Tasks** → `tasks/` (P0-P3 priority, max 3 P0 tasks)
- **Opportunities** → `knowledge/opportunities/` (ideas to explore)
- **References** → `knowledge/references/` (useful context)

**Generate docs when ready:**
```
/prd mobile-performance
/spec mobile-performance
/user-stories mobile-performance
```

---

## Core Workflow

```
BACKLOG.md → /backlog → Tasks (P0≤3) / Opportunities / References
```

1. **Brain dump** to `BACKLOG.md` throughout the day
2. **Process** with `/backlog` - AI categorizes and enforces priority caps
3. **Work** - Focus on your 3 P0 tasks, explore opportunities, generate docs

---

## Priority System

Tasks use P0-P3 with strict caps to prevent overwhelm:

- **P0** (Critical): Max 3 tasks - Today's focus
- **P1** (High): Max 7 tasks - This week
- **P2** (Medium): Max 15 tasks - This month
- **P3** (Low): Unlimited - Backlog

When `/backlog` processing would exceed caps, AI asks you to deprioritize.

---

## Skills (Auto-Invoked)

Skills are specialized tools AI uses automatically:

**Product Docs (`product-docs` skill):**
- `/prd [name]`, `/spec [name]`, `/brief [name]`
- `/user-stories [name]`, `/decision [topic]`
- Auto-pulls context from knowledge base

**UX Copy (`ux-copy` skill):**
- Translate to Canadian French (Québécois)
- Create UI copy, error messages, microcopy
- Follows OQLF guidelines

**User Research (`user-research-analysis` skill):**
- Analyze interviews and transcripts
- Synthesize research, create personas

**Prototyping (`prototype-builder` skill):**
- Build working prototypes from specs

**Internal Comms (`internal-comms` skill):**
- Status reports, updates, FAQs

---

## Common Commands

**Daily:**
- "What should I work on today?" - Review P0/P1 tasks
- `/backlog` - Process ideas into tasks/opportunities

**Tasks:**
- "Mark task [name] as complete"
- "Find stale tasks"
- "Prune completed tasks" - Delete tasks older than 90 days

**Documents:**
- `/prd [name]` - Generate PRD
- `/spec [name]` - Generate spec
- `/brief [name]` - Generate brief

**Natural language works too:**
- "Create a spec for the mobile performance opportunity"
- "Analyze the user interviews in knowledge/transcripts/"
- "What are my P0 tasks?"

---

## Voice Training

Train AI to match your writing style:

1. Add 5-10 writing samples to `knowledge/voice-samples/`
2. Ask AI to analyze patterns
3. AI will adapt to your voice automatically

See `templates/voice-samples/` for examples.

---

## Directory Structure

```
pm-copilot/
├── BACKLOG.md              # Daily inbox (gitignored)
├── AGENTS.md               # AI instructions
├── config.yaml             # Priority caps, categories
├── setup.sh                # Setup script
│
├── tasks/                  # Your tasks (gitignored)
├── knowledge/              # Your context (gitignored)
│   ├── about-me/
│   ├── product-strategy/
│   ├── company-context/
│   ├── frameworks/
│   ├── opportunities/
│   ├── briefs-and-specs/
│   ├── transcripts/
│   ├── voice-samples/
│   ├── references/
│   └── notes/             # Archived backlog snapshots
│
├── templates/              # Document templates
├── workflows/              # Workflow files
├── mcp/                    # MCP servers (optional)
└── code/                   # Prototypes (gitignored)
```

---

## What Gets Committed vs. Gitignored

**Committed (shared structure):**
- Directory structure
- Documentation, templates
- `config.yaml`, `AGENTS.md`

**Gitignored (your data):**
- `BACKLOG.md`
- Content in `knowledge/`, `tasks/`, `code/`

---

## Best Practices

**Daily:**
- Morning: "What should I work on today?"
- Throughout day: Brain dump to BACKLOG.md
- Weekly: `/backlog` to process

**Context:**
- Start small - add context as you go
- Process backlog weekly, not daily
- Update voice samples quarterly

**Tips:**
- Use @ mentions: `@knowledge/product-strategy/`
- Process 3-5 backlog items at a time, not 50
- Let priority caps guide you - max 3 P0 tasks

**Troubleshooting:**
- Generic responses? Add more to `knowledge/`
- AI not using context? Use @ mentions explicitly
- Too many tasks? Let AI enforce priority caps

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to share templates or improvements.
