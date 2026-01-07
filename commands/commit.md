---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git branch:*), Bash(git log:*)
argument-hint: [optional commit message]
description: Create a git commit with context-aware message
---

## Context

- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit following the repository's commit message style.

If the user provided a commit message as an argument, use it: $ARGUMENTS

Otherwise, analyze the changes and create an appropriate commit message that:
1. Summarizes the nature of changes (new feature, enhancement, bug fix, refactoring, docs, etc.)
2. Is concise (1-2 sentences) and focuses on "why" rather than "what"
3. Accurately reflects the changes and their purpose

**Important:**
- Add relevant untracked files to staging area before committing
- Do NOT push to remote unless explicitly asked
- Follow the git commit protocol from the system instructions
