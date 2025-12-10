# PM Co-Pilot Workflows

AI-powered workflows for product management. These are your slash commands for Cursor and Claude Code.

---

## Quick Reference

### 🚀 Daily Workflows

```
/plan           → "What should I work on today?"
/backlog        → Process BACKLOG.md into initiatives
/prioritize     → Prioritize work based on strategy
```

### 📋 Initiatives & Documents

```
/expand-initiative [name]  → Add research and details before PRD
/spec [initiative]         → Generate product spec from initiative
/prd [initiative]          → Generate full PRD from initiative
/stories [initiative]      → Generate user stories from initiative
/brief [project]           → Create project brief
```

### 💬 Communication

```
/exec-update    → Draft executive update with metrics
/team-update    → Write team update
/stakeholder    → Prepare for stakeholder meeting
/faq [topic]    → Generate FAQ
```

### 📊 Research & Analysis

```
/synthesize     → Synthesize research from knowledge/transcripts/
/insights [file]→ Extract key insights
/feedback       → Analyze customer feedback
/competitive    → Competitive analysis and competitor research
/metrics        → Query and analyze metrics
```

### 🔍 Decision & Planning

```
/decide [decision] → Document decision
/evaluate          → Evaluate options
/sprint            → Plan next sprint
/roadmap           → Create/update roadmap
/weekly            → Plan this week
/okrs              → Create and manage OKRs
```

### 📝 Technical Writing

```
/api-docs          → Create API documentation
/guide [topic]     → Write developer guide
/reference [topic] → Create reference docs
/recipe [task]     → Create code recipe
/publish-docs      → Prepare docs for publishing
```

### 🔧 MCP Development

```
/mcp-server [api]  → Generate MCP server from API docs
/create-mcp [tool] → Create MCP server implementation
/mcp-env [server]  → Generate .env template for MCP server
```

### 🛠️ Prototyping

```
/prototype [feature] → Create working code prototype from spec/brief
```

---

## Workflow Index (Action-Based)

Browse workflows by action:

### Process & Organize
- [process-backlog.md](process-backlog.md) - Process backlog items into initiatives, tasks, references (includes archiving)

### Generate & Create
- [product-docs.md](product-docs.md) - Generate and manage specs, PRDs, briefs, user stories, and document decisions

### Plan & Prioritize
- [roadmap.md](roadmap.md) - Create and manage strategic roadmaps
- [gtm-launch.md](gtm-launch.md) - Plan and execute GTM launches with implementation planning
- [okrs.md](okrs.md) - Create and manage strategic OKRs
- [task-manager.md](task-manager.md) - Prioritize and manage tasks and personal todos

### Research & Analyze
- [user-research.md](user-research.md) - Synthesize user research, interviews, and customer feedback
- [competitor-research.md](competitor-research.md) - Research competitors and track changes
- [metrics.md](metrics.md) - Track, analyze, and query metrics

### Communicate
- [product-updates.md](product-updates.md) - Write product updates and communications

### Manage & Collaborate
- [bugs.md](bugs.md) - Manage and prioritize bugs and incidents
- [eng-manager.md](eng-manager.md) - EM expert for technical requirements and architecture
- [team-onboarding.md](team-onboarding.md) - Onboard team members and prepare handoffs
- [product-processes.md](product-processes.md) - Expert in product processes and operating models

### Development & Operations
- [github.md](github.md) - Manage git and GitHub operations
- [prototype.md](prototype.md) - Create working code prototypes from specs/briefs using Shadcn/ui

### Technical Writing
- [technical-writing.md](technical-writing.md) - Create API docs, developer guides, references, and code recipes

### MCP Development
- [mcp-generator.md](mcp-generator.md) - Generate MCP servers from API docs/SDKs with .env configuration

---

## Setup Slash Commands

### For Cursor

You can create a `.cursorrules` file in the project root to configure slash commands. Add instructions like:

```markdown
When I use shortcuts like /plan, /backlog, /spec, read the corresponding
workflow file in examples/workflows/ and execute it.
```

**Usage**: Just type `/plan` or `/backlog` in Cursor chat!

**Add Your Own**:
Create or edit `.cursorrules` to add custom workflows.

### For Claude Code

Add to project instructions:

```markdown
When I use shortcuts like /plan, /backlog, /spec, read the corresponding
workflow file in examples/workflows/ and execute it.

Always reference:
- @AGENTS.md for behavior
- @templates/ for document structure
- @knowledge/ for context
```

---

## Core Workflows Explained

### 1. Process Backlog

**Trigger**: `/backlog` or "Process my backlog"

**Workflow**: [process-backlog.md](process-backlog.md)

**What it does**:
1. Reads items from `BACKLOG.md`
2. Creates initiative files in `initiatives/` folder
3. Each initiative has opportunity assessment format:
   - Objective
   - Target customer
   - Success metrics
   - What we know
   - What we should research
   - Solution ideas
   - Risks
   - Questions to validate
4. Prioritizes as P0-P3
5. Clears processed items from BACKLOG.md

**When to use**: Weekly, or when BACKLOG.md has 5+ items

**Example**:
```
/backlog
→ Creates initiatives/mobile-performance.md
→ Creates initiatives/enterprise-sso.md
→ Clears BACKLOG.md
```

---

### 2. Expand Initiative

**Trigger**: `/expand-initiative [name]`

**Workflow**: Use [product-docs.md](product-docs.md) or [user-research.md](user-research.md) for research expansion

**What it does**:
Before generating a PRD, expand the initiative with:
- Detailed research plan
- More solution options
- Risk analysis
- Validation approach
- Effort estimates

**When to use**: After creating initiative, before committing to build

**Example**:
```
/expand-initiative mobile-performance
→ Adds detailed technical analysis needed
→ Adds user research plan
→ Evaluates 3-4 solution options
→ Flags gaps and questions
```

---

### 3. Generate PRD from Initiative

**Trigger**: `/prd [initiative-name]`

**Workflow**: [product-docs.md](product-docs.md)

**What it does**:
Converts initiative to full Product Requirements Document:
- Uses initiative's objective → problem statement
- Uses target customer → user personas
- Uses success metrics → KPIs
- Uses solution ideas → requirements
- Adds technical details, user stories, launch plan

**When to use**: After initiative is expanded and validated

**Example**:
```
/prd mobile-performance
→ Reads @initiatives/mobile-performance.md
→ Uses @templates/spec-template.md  
→ Generates comprehensive PRD
→ Saves to initiatives/mobile-performance/prd.md
```

---

## Common Patterns

### Monday Morning

```
1. /plan
   "What should I work on this week?"

2. /backlog
   "Process weekend ideas"

3. /prioritize
   "Help me prioritize based on @knowledge/product-strategy/"
```

### Feature Kick-off

```
1. Create initiative (from backlog or manually)
2. /expand-initiative [name]
3. Review and validate assumptions
4. /prd [name]
5. /stories [name]
6. /tech-req [name]
7. /brief [name]
```

### Research Synthesis

```
1. Add transcripts to knowledge/transcripts/
2. /synthesize (uses user-research.md)
3. /insights
4. Create initiatives from top opportunities
5. Use roadmap.md or task-manager.md to prioritize
```

### Weekly Update

```
1. /metrics (uses metrics.md)
   "Get latest numbers from @knowledge/product-analytics/"

2. /exec-update (uses product-updates.md)
   "Draft update for leadership"

3. (Iterate)
   "Make it more concise"
   "Add more on blockers"
```

---

## Tips for Success

### 1. Be Specific
❌ `/spec`  
✅ `/spec mobile-onboarding-redesign`

### 2. Add Context
❌ `/update`  
✅ `/exec-update on Q1 mobile initiative including latest metrics from @knowledge/product-analytics/`

### 3. Reference Files
Always use @ mentions:
```
/spec mobile-redesign using insights from @knowledge/briefs-and-specs/mobile-study.md
```

### 4. Chain Workflows
```
"First /backlog to process ideas,
then /prioritize based on strategy,
then /spec for top 2 P0 initiatives"
```

### 5. Iterate
Don't expect perfection first try:
```
/spec feature-name
→ "Add more detail on success metrics"
→ "Make technical requirements more specific"
→ "Add competitive analysis section"
```

---

## All Workflow Files

Each `.md` file in this directory contains detailed workflows:

**Process & Organize**:
- **process-backlog.md** - Process backlog items into initiatives, tasks, references (includes archiving)

**Generate & Create**:
- **product-docs.md** - Generate and manage specs, PRDs, briefs, user stories, and document decisions

**Plan & Prioritize**:
- **roadmap.md** - Create and manage strategic roadmaps
- **gtm-launch.md** - Plan and execute GTM launches with implementation planning
- **okrs.md** - Create and manage strategic OKRs
- **task-manager.md** - Prioritize and manage tasks and personal todos

**Research & Analyze**:
- **user-research.md** - Synthesize user research, interviews, and customer feedback
- **competitor-research.md** - Research competitors and track changes
- **metrics.md** - Track, analyze, and query metrics

**Communicate**:
- **product-updates.md** - Write product updates and communications

**Manage & Collaborate**:
- **bugs.md** - Manage and prioritize bugs and incidents
- **eng-manager.md** - EM expert for technical requirements and architecture
- **team-onboarding.md** - Onboard team members and prepare handoffs
- **product-processes.md** - Expert in product processes and operating models

**Development & Operations**:
- **github.md** - Manage git and GitHub operations
- **prototype.md** - Create working code prototypes from specs/briefs using Shadcn/ui

**Technical Writing**:
- **technical-writing.md** - Create API documentation, developer guides, reference docs, and code recipes

**MCP Development**:
- **mcp-generator.md** - Generate MCP servers from API documentation or SDKs with .env configuration

---

## Related

- **Tutorials**: See `examples/tutorials/` for step-by-step guides
- **Examples**: See `examples/example_files/` for sample outputs
- **Templates**: See `templates/` for document templates
- **AGENTS.md**: How AI processes these workflows (lean reference guide)
- **BACKLOG.md**: Your inbox for raw ideas
- **initiatives/**: Where processed ideas live

---

**Remember**: These workflows are starting points. AI understands natural language, so talk to it like a colleague. The slash commands are shortcuts, not rigid syntax.
