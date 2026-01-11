---
name: slash-command-builder
description: Expert guide for creating effective slash commands following best practices. Use when users want to create a new slash command, build a custom command workflow, or need guidance on slash command structure. Triggers include requests like "create a slash command for...", "help me build a /command", "make a command that...", or questions about slash command best practices. Provides opinionated guidance, asks clarifying questions, and uses templates to ensure commands follow established patterns.
---

# Slash Command Builder

Build effective, well-structured slash commands following best practices from the official Claude Code documentation.

## Workflow

### Step 1: Understand the Need

Before creating a slash command, ask these questions to understand the user's need:

1. **What task should this command perform?** Get a clear description of what the command should do.
2. **What arguments or inputs will it need?** Determine if it needs arguments and how they'll be used.
3. **Will it need to execute bash commands?** Identify if the command needs to run git, npm, or other CLI tools.
4. **Will it reference files?** Determine if the command should include file contents.

**When to suggest a Skill instead:**
- The workflow requires multiple steps or complex logic
- It needs scripts or utilities
- Knowledge is organized across multiple files
- It's a team workflow requiring standardization

If a Skill is more appropriate, explain why and offer to help create a Skill instead.

### Step 2: Choose the Right Template

Based on the user's needs, select the most appropriate template from `assets/`:

**Git Operations** → `assets/git-commit.md`
- For git commits, branch management, PR operations
- Includes bash command execution with `!` prefix
- Pre-configured with git tool permissions

**Code Review** → `assets/code-review.md`
- For reviewing code quality, security, performance
- Uses arguments to specify files or PR numbers
- Structured feedback format

**Documentation** → `assets/doc-generator.md`
- For generating documentation, README files, API docs
- Comprehensive documentation structure
- Follows project documentation style

**Testing** → `assets/test-writer.md`
- For writing unit tests, integration tests
- Covers happy path, edge cases, error handling
- Follows project testing patterns

**Simple Command** → `assets/simple-command.md`
- For straightforward prompts without complex features
- Minimal structure for quick customization
- Good starting point for custom commands

### Step 3: Customize the Command

**Location:**
- **Always create commands in:** `workflows/` (root directory)
- This folder is symlinked to `.claude/commands` and `.cursor/commands` (if set up)
- Sharing via symlinks allows commands to work across both Claude Code and Cursor
- Use subdirectories for namespacing: `workflows/git/commit.md`

**Naming:**
- Use lowercase filenames: `review-pr.md` → `/review-pr`
- Keep names clear and descriptive
- Avoid special characters

**Frontmatter Customization:**

```yaml
---
# Required: Brief description for discoverability
description: Create a git commit with context-aware message

# Optional: Expected arguments (improves auto-complete)
argument-hint: [optional commit message]

# Optional: Tools the command can use (security restriction)
allowed-tools: Bash(git add:*), Bash(git status:*)

# Optional: Specific model to use
model: claude-3-5-haiku-20241022

# Optional: Disable auto-invocation by Claude
disable-model-invocation: false
---
```

**Prompt Customization:**

1. **For arguments**, use:
   - `$ARGUMENTS` for all arguments: "Fix issue #$ARGUMENTS"
   - `$1, $2, $3` for positional: "Review PR #$1 with priority $2"

2. **For bash execution**, use `!` prefix:
   ```markdown
   Current status: !`git status`
   Current diff: !`git diff HEAD`
   ```
   *Requires `allowed-tools: Bash(git status:*)` in frontmatter*

3. **For file references**, use `@` prefix:
   ```markdown
   Review the code in @src/utils/helpers.js
   ```

### Step 4: Verify Best Practices

Before finalizing, check that the command follows best practices:

✅ **Clear Description**: Frontmatter includes descriptive `description` field
✅ **Argument Hints**: If using arguments, `argument-hint` is specified
✅ **Tool Restrictions**: If using bash, `allowed-tools` lists only necessary commands
✅ **Simplicity**: Command fits in one file (if not, suggest a Skill)
✅ **Naming**: Filename is lowercase and descriptive

**Security Check:**
- Never allow unrestricted bash access: `allowed-tools: Bash(*)` ❌
- Always specify exact commands: `allowed-tools: Bash(git status:*)` ✅

### Step 5: Create and Test

1. **Create the file** at the chosen location
2. **Test the command** by running it: `/your-command-name`
3. **Iterate** based on results

## Common Patterns

### Pattern: Context-Aware Git Commands

```yaml
---
allowed-tools: Bash(git status:*), Bash(git diff:*)
description: Smart git commit with context
---

Status: !`git status`
Diff: !`git diff HEAD`

Create a commit based on the above changes.
```

### Pattern: Parameterized Code Review

```yaml
---
argument-hint: [pr-number]
description: Review pull request
---

Review PR #$1 for:
- Code quality
- Security issues
- Performance concerns
```

### Pattern: File-Specific Documentation

```yaml
---
argument-hint: [file-path]
description: Generate documentation for file
---

Generate comprehensive documentation for @$1
```

## Reference Documentation

For comprehensive best practices, see [references/best-practices.md](references/best-practices.md) which covers:

- Directory structure and organization
- Naming conventions
- Frontmatter fields (all options)
- Argument usage patterns
- Bash command execution
- File references
- Extended thinking triggers
- When to use slash commands vs skills
- SlashCommand tool integration
- Character budget limits
- Common patterns for git, code review, documentation, and testing

## Opinionated Recommendations

**DO:**
- ✅ Start with a template from `assets/`
- ✅ Always include a `description` in frontmatter
- ✅ Use `argument-hint` when your command takes arguments
- ✅ Restrict bash tools to only necessary commands
- ✅ Keep commands simple and focused on one task
- ✅ Test the command before considering it complete

**DON'T:**
- ❌ Create a slash command for complex multi-step workflows (use a Skill)
- ❌ Allow unrestricted bash access for security
- ❌ Use vague or unclear command names
- ❌ Skip the frontmatter description
- ❌ Create overly complex commands that are hard to maintain

## Example: Building a PR Review Command

**User request:** "Create a command to review pull requests"

**Clarifying questions:**
1. "What aspects should the review focus on?" → Code quality, security, performance
2. "Should it take the PR number as an argument?" → Yes
3. "Any specific coding standards to check?" → Follow project conventions

**Template choice:** `assets/code-review.md`

**Customization:**
```yaml
---
argument-hint: [pr-number]
description: Review pull request for quality, security, and performance
---

Review PR #$1 focusing on:

1. Code Quality & Project Conventions
2. Security Vulnerabilities (OWASP Top 10)
3. Performance Implications
4. Test Coverage

Provide specific, actionable feedback.
```

**File location:** `workflows/review-pr.md`

**Result:** User can now run `/review-pr 123` to get comprehensive PR reviews.
