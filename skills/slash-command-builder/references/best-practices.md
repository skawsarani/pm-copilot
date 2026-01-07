# Slash Command Best Practices

## Quick Reference

**Slash commands** are markdown files that create reusable prompt snippets. Use them for frequently used prompts that fit in one file. For complex workflows or multiple files, use Skills instead.

## Directory Structure

**This Project:**
- **Create commands in:** `commands/` (root directory)
- This folder is symlinked to `.claude/commands` and `.cursor/commands`
- Allows commands to work across both Claude Code and Cursor
- Example: `commands/git/commit.md` creates `/commit` with description "(project:git)"

**General Best Practices:**
- **Project commands**: `.claude/commands/` (shared with team via git)
- **Personal commands**: `~/.claude/commands/` (user-specific)
- **Namespacing**: Use subdirectories to group related commands

## Naming Conventions

- Command names derive from filename (without `.md`)
- Use lowercase for consistency
- Project commands override personal commands with same name

## Frontmatter Fields

```yaml
---
allowed-tools: Bash(git add:*), Bash(git status:*)
argument-hint: [message]
description: Create a git commit
model: claude-3-5-haiku-20241022
---
```

| Field | Purpose | Default |
|-------|---------|---------|
| `allowed-tools` | Tools the command can use | Inherits from conversation |
| `argument-hint` | Expected arguments for auto-complete | None |
| `description` | Brief command description | First line from prompt |
| `model` | Specific AI model to use | Inherits from conversation |
| `disable-model-invocation` | Prevent auto-invocation | false |

## Arguments

### $ARGUMENTS (All Arguments)

Captures everything passed to the command:

```markdown
# Fix issue #$ARGUMENTS following our coding standards
```

Usage: `/fix-issue 123 high-priority` → `$ARGUMENTS` = "123 high-priority"

### Positional Arguments ($1, $2, etc.)

Access specific arguments individually:

```markdown
---
argument-hint: [pr-number] [priority]
---

Review PR #$1 with priority $2.
```

Usage: `/review-pr 456 high` → `$1` = "456", `$2` = "high"

**Use positional arguments when:**
- Arguments appear in different parts of the command
- Providing defaults for missing arguments
- Building structured commands with specific parameter roles

## Advanced Features

### Bash Command Execution

Include bash output in command context using `!` prefix:

```markdown
---
allowed-tools: Bash(git status:*)
---

Current git status: !`git status`

Based on the above, create a commit.
```

**Requirements:**
- Must include `allowed-tools` with the `Bash` tool
- Specify exactly which bash commands are allowed

### File References

Include file contents using `@` prefix:

```markdown
# Review the implementation in @src/utils/helpers.js

# Compare @src/old-version.js with @src/new-version.js
```

### Extended Thinking

Trigger extended thinking by including keywords like "think deeply," "carefully consider," etc.

## When to Use Slash Commands vs Skills

### Use Slash Commands for:
- Quick, frequently used prompts
- Simple instructions fitting in one file
- Quick reminders or templates

### Use Skills for:
- Complex workflows with multiple steps
- Capabilities requiring scripts or utilities
- Knowledge organized across multiple files
- Team workflows requiring standardization
- When Claude should discover automatically

## Design Principles

1. **Clear Descriptions**: Write descriptive frontmatter for discoverability
2. **Meaningful Argument Hints**: Help users understand expected arguments
3. **Tool Restrictions**: Only allow necessary tools for security
4. **Consistent Naming**: Use clear, descriptive command names
5. **Keep It Simple**: If the command is getting complex, consider a Skill instead

## SlashCommand Tool Integration

To enable Claude to auto-invoke commands:
- Reference the command by name (with `/`) in prompts or `CLAUDE.md`
- Example: "Run `/write-unit-test` when about to start writing tests"

**Requirements:**
- Must have `description` frontmatter field
- Can disable with `disable-model-invocation: true`

## Character Budget

- Default: 15,000 characters for command metadata
- Configurable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable
- Warning shows "M of N commands" when exceeded

## Common Patterns

### Git Operations
- Include `!git status` and `!git diff` for context
- Restrict tools to specific git commands
- Use argument hints for commit messages or PR numbers

### Code Review
- Reference specific files with `@` syntax
- Include context like recent commits or test results
- Use positional arguments for PR numbers or file paths

### Documentation
- Reference source files to document
- Include style guide or template context
- Use arguments for section names or focus areas

### Testing
- Reference the code to test
- Include test framework preferences
- Use arguments for test types or coverage goals
