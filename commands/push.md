---
allowed-tools: Bash(git push:*), Bash(git branch:*), Bash(git status:*)
argument-hint: [optional flags like --force]
description: Push current branch to remote repository
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status`

## Your task

Push the current branch to the remote repository.

$ARGUMENTS

**Important:**
- If the branch doesn't have an upstream, set it with `-u origin <branch-name>`
- If the user provided flags (like --force), include them: $ARGUMENTS
- NEVER use `--force` on main/master branches unless explicitly confirmed by user
- Show the push output to confirm success
