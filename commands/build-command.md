---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [command name or description]
description: Create a slash command with guided workflow
---

## Context

Slash commands are quick, reusable prompts that can invoke tools and include dynamic context.

The slash-command-builder skill provides expert guidance for building effective commands.

## Your task

Guide the user through creating a new slash command following best practices.

User input: $ARGUMENTS

**Steps:**

1. **Invoke slash-command-builder**: Use the Skill tool to launch the slash-command-builder skill

2. **Pass user context**: Include $ARGUMENTS to provide context about what command they want to create

**Example invocation:**
- `/build-command backlog-summary` → Create a command to summarize the backlog
- `/build-command` → Interactive workflow to design a new command
- `/build-command update tasks` → Update existing tasks command

**Important:**
- The slash-command-builder will handle the full workflow (asking questions, creating files, etc.)
- Commands are stored in `commands/` directory as markdown files
- Each command includes frontmatter (allowed-tools, description) and prompt instructions
- See existing commands in `commands/` for reference patterns
