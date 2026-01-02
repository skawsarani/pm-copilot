# Contributing to PM Co-Pilot

Thank you for your interest in contributing! This guide outlines how to contribute to PM Co-Pilot.

---

## Ways to Contribute

### 1. Share Templates
Document templates that work well for your PM workflow (specs, briefs, decision docs, etc.)

### 2. Share Skills
Custom skills that extend PM Co-Pilot's capabilities (see `skills/` directory)

### 3. Improve Documentation
- Fix typos or unclear instructions
- Add examples or clarifications
- Update outdated references

### 4. Share Your Experience
Write about how you use PM Co-Pilot in your workflow

### 5. Suggest Improvements
Open an issue to discuss:
- New features or capabilities
- Better organization
- Missing documentation

---

## Getting Started

### Prerequisites
- Familiarity with Markdown
- Experience using AI assistants (Cursor, Claude Code, etc.)
- PM experience (for PM-specific contributions)

### Setup
1. Fork the repository
2. Clone your fork locally
3. Create a branch for your changes
4. Make your changes
5. Test with your AI assistant
6. Submit a pull request

---

## Contribution Types

### 📄 Templates

**What to include:**
1. Template file in `templates/`
2. Clear structure with sections
3. Inline instructions
4. Example content
5. When to use this template

**Example:**
```
templates/
├── pricing-strategy-template.md
└── competitive-analysis-template.md
```

**Format:**
- Use clear section headers
- Include placeholders: `[DESCRIPTION]`, `[YOUR ANSWER]`
- Add comments to guide users
- Show example content

### 🎯 Skills

**What to include:**
1. Skill directory in `skills/your-skill-name/`
2. `SKILL.md` with skill description and instructions
3. Supporting files in `assets/`, `references/`, or `scripts/`
4. Clear documentation on when to invoke

**Example structure:**
```
skills/your-skill-name/
├── SKILL.md              # Main skill instructions
├── assets/               # Templates, examples
├── references/           # Reference docs
└── scripts/              # Helper scripts (optional)
```

See existing skills in `skills/` for examples.

### 📚 Documentation

**What to improve:**
- README.md
- AGENTS.md
- workflows/README.md
- Knowledge folder READMEs

**Requirements:**
- Clear, concise language
- Include examples
- Test instructions before submitting
- Follow existing style

### 🎨 Voice Samples

**What to include:**
1. Voice sample in `templates/voice-samples/`
2. Different formats (email, spec intro, blog post, etc.)
3. 150-300 words per sample
4. Natural, authentic writing

---

## Content Standards

### ✅ What We Accept

- Generic PM workflows applicable to many teams
- Template structures (without proprietary content)
- Process frameworks (RICE, OKRs, etc.)
- Learning resources
- Voice sample formats

### ❌ What We Don't Accept

- Proprietary company information
- Confidential product details
- Personal identifying information
- Customer data
- API keys or secrets

### Quality Standards

- Tested with AI assistants
- Clear and well-organized
- Follows simplified structure
- Includes examples
- No typos or broken links

---

## Submission Process

### 1. Create an Issue (Optional but Recommended)

For significant changes, create an issue to discuss:
- What you want to add
- Why it's valuable
- How it fits into the structure

### 2. Make Your Changes

- Work in a dedicated branch
- Follow the style guide
- Keep changes focused
- Write clear commit messages

### 3. Test Your Changes

- Test with AI assistant (Cursor, Claude Code, etc.)
- Verify all links work
- Check formatting renders correctly
- Ensure examples are accurate

### 4. Submit Pull Request

**PR Title Format:**
- ✅ `feat: add RICE scoring framework template`
- ✅ `docs: improve backlog processing guide`
- ✅ `feat: add competitor analysis skill`
- ❌ `updates`

**PR Description Template:**
```markdown
## What
[Brief description of changes]

## Why
[Why this improvement is valuable]

## Changes
- [Specific change 1]
- [Specific change 2]

## Testing
[How you tested these changes]

## Checklist
- [ ] Tested with AI assistant
- [ ] Documentation updated if needed
- [ ] Examples included
- [ ] Follows style guide
```

---

## Style Guide

### File Naming
- Regular files: `lowercase-with-hyphens.md`
- Directories: `lowercase-with-hyphens/`
- Special docs: `UPPERCASE.md` (README, AGENTS)

### Markdown Style
- Clear, direct language
- Active voice: "Create a spec" not "A spec should be created"
- Scannable format: headers, bullets, tables
- Specific examples over abstract descriptions

### Documentation Tone
- Direct and friendly
- Concise (avoid fluff)
- Helpful, not prescriptive
- Action-oriented

---

## Review Process

### What We Look For

1. **Value**: Does this help PMs work better with AI?
2. **Quality**: Is it well-written and clear?
3. **Consistency**: Follows the simplified structure?
4. **Completeness**: Has examples and context?

### Timeline

- Initial review: Within 1 week
- Feedback provided if changes needed
- Merged when approved

### If Changes Requested

- Address feedback in same branch
- Push updates
- Comment when ready for re-review

---

## Code of Conduct

### Our Standards

**Be respectful:**
- Assume good intent
- Provide constructive feedback
- Welcome newcomers

**Be collaborative:**
- Discuss significant changes
- Credit others' work
- Share learnings

**Be professional:**
- No harassment or discrimination
- Keep discussions on-topic
- Respect privacy

---

## Questions?

### Where to Ask
- Open an issue for project questions
- Start a discussion for ideas
- Comment on PRs for specific feedback

### Response Time
- Issues: Within 1 week
- PRs: Within 1 week for initial review
- Discussions: Best effort

---

## Recognition

Contributors will be:
- Listed in commit history
- Credited in relevant documentation
- Acknowledged in releases (if significant)

---

## License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) as the project.

---

## Getting Help

### Resources
- [README.md](README.md) - Project overview and quick start
- [AGENTS.md](AGENTS.md) - AI instructions and style guide

### Stuck?
Open an issue with:
- What you're trying to do
- What you've tried
- Where you're stuck

We're here to help!

---

**Thank you for making PM Co-Pilot better for everyone!** 🚀
