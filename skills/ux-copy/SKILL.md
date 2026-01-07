---
name: ux-copy
description: Expert UX copywriter for creating effective, user-friendly copy for software interfaces. Use when asked to create, review, or refine user interface copy including buttons, labels, error messages, tooltips, notifications, onboarding flows, empty states, or any user-facing text in English. Triggers include "create UI copy for [feature]", "write error messages for [scenario]", "review this copy", "create microcopy", "write onboarding copy", "create notification copy", or requests for UX writing. Does NOT handle translation - use i18n-translator skill for translating copy to other languages.
---

# UX Copywriting Expert

Create effective, user-friendly copy for software interfaces that guides users to success.

## Quick Start

**Common triggers:**
- "Create UI copy for [feature]"
- "Write error messages for [scenario]"
- "Review this copy for clarity and tone"
- "Create microcopy for [UI element]"
- "Write onboarding copy for [feature]"
- "Create notification copy for [event]"
- "Write empty state copy for [screen]"

**NOT for:**
- Translation (use i18n-translator skill instead)
- Localization (use i18n-translator skill instead)
- Bilingual content creation (use i18n-translator skill instead)

## Core Workflows

### 1. Create UI Copy for Feature

**When to use:** Generating complete UI copy set for new features or flows

**Process:**
1. **Understand the feature**
   - Review feature spec or brief if available
   - Identify all UI elements needing copy
   - Understand user flows and interactions
   - Note technical constraints (character limits, etc.)

2. **Generate copy elements**
   - Button labels (primary, secondary, destructive actions)
   - Form labels and placeholders
   - Error messages and validation text
   - Success messages and confirmations
   - Tooltips and help text
   - Page titles and headings
   - Navigation labels
   - Empty states
   - Loading states

3. **Organize by context**
   - Group by user flow or screen
   - Include context notes for developers
   - Provide character length limits if needed
   - Note dynamic content placeholders

4. **Apply UX copywriting principles**
   - Clear: Meaning immediately obvious
   - Concise: No unnecessary words
   - Helpful: Guides users to success
   - Consistent: Matches terminology elsewhere
   - Action-oriented: Uses active verbs
   - Human: Sounds natural, not robotic

**Output format:**

Organize as table or grouped list:

```markdown
## Login Screen

| Element | Copy | Notes |
|---------|------|-------|
| Heading | Sign in to your account | |
| Email field label | Email address | |
| Email placeholder | you@example.com | Show example format |
| Password field label | Password | |
| Primary button | Sign in | Action-oriented |
| Secondary link | Create account | |
| Forgot password link | Forgot password? | |
| Error (invalid email) | Please enter a valid email address | Specific and helpful |
| Error (wrong credentials) | Email or password is incorrect | Don't specify which for security |
| Success message | Welcome back! | Friendly confirmation |
```

### 2. Review and Refine Copy

**When to use:** Before finalizing any user-facing copy

**Process:**
1. **Assess clarity**
   - Is the message clear and unambiguous?
   - Will users understand the action/information?
   - Are technical terms explained or avoided?
   - Is language appropriate for audience?

2. **Evaluate tone**
   - Does it match product voice?
   - Is it friendly/professional/technical as needed?
   - Is it consistent with other product copy?
   - Does it sound human, not robotic?

3. **Check UX best practices**
   - Is it concise enough for UI constraints?
   - Does it guide users to right action?
   - Are error messages helpful, not just descriptive?
   - Does it reduce cognitive load?

4. **Suggest improvements**
   - Provide revised copy with rationale
   - Offer alternatives if applicable
   - Flag concerns or questions

**Review against checklist** (from `references/ux-copy-best-practices.md`):
- [ ] Clear: Meaning immediately obvious
- [ ] Concise: No unnecessary words
- [ ] Helpful: Guides users to success
- [ ] Consistent: Matches terminology elsewhere
- [ ] Action-oriented: Uses active verbs
- [ ] Human: Sounds natural
- [ ] Accessible: Screen reader friendly
- [ ] On-brand: Matches product voice

**Output format:**

```markdown
## Original Copy Review

**Original:** "Error: Invalid input detected"

**Issues:**
- Too technical ("invalid input detected")
- Doesn't explain what's wrong
- Doesn't provide solution
- Sounds robotic

**Suggested revision:** "Please enter a valid email address"

**Rationale:**
- Specific about what field has the issue
- Clear about the requirement
- More human tone
- Action-oriented ("Please enter")

**Alternative:** "That doesn't look like an email address. Please check and try again."
- Even more human and friendly
- Explains the problem
- Provides gentle guidance
```

### 3. Create Error Messages

**When to use:** Creating error messages, validation messages, or system notifications

**Error message anatomy:**
1. **What went wrong** (clear and specific)
2. **Why it happened** (if helpful)
3. **How to fix it** (actionable)

**Error types and patterns:**

**Validation errors:**
- ✅ "Password must be at least 8 characters"
- ✅ "Email address must include '@' symbol"
- ✅ "Please select a date in the future"
- ❌ "Invalid input"

**System errors:**
- ✅ "We're having trouble connecting. Check your internet and try again."
- ✅ "Something went wrong on our end. We're working to fix it."
- ✅ "This page isn't loading. Please refresh or try again later."
- ❌ "Error 500"

**Permission errors:**
- ✅ "You don't have permission to delete this file. Contact the owner to request access."
- ✅ "This action requires admin access. Ask your team admin for permission."
- ❌ "Access denied"
- ❌ "403 Forbidden"

**Business logic errors:**
- ✅ "You can't delete your account while you have an active subscription. Cancel your subscription first."
- ✅ "You've reached the maximum of 5 projects on the free plan. Upgrade to create more."
- ❌ "Cannot delete"
- ❌ "Limit reached"

**Network/connectivity errors:**
- ✅ "No internet connection. Check your network and try again."
- ✅ "Request timed out. Please try again."
- ❌ "Network error"

**Tone guidelines:**
- **Don't blame the user**
  - ❌ "You entered invalid data"
  - ✅ "Please check your email format"
- **Be empathetic for frustrating errors**
  - ✅ "We're sorry, but something went wrong. Our team has been notified."
- **Offer solutions when possible**
  - ✅ "...Check your internet and try again"
  - ✅ "...Contact support@example.com if this keeps happening"
- **Keep consistent format across all errors**

### 4. Create Microcopy

**When to use:** Creating tooltips, help text, empty states, loading messages, placeholders

**Microcopy types:**

**Tooltips:**
- Keep under 10 words
- ✅ "Your private workspace for saving ideas"
- ✅ "Visible to team members only"
- Use for definitions or extra context
- Don't use for critical information (might be missed)

**Inline help:**
- ✅ "We'll never share your email address"
- ✅ "You can change this later"
- ✅ "Changes save automatically"
- Provide reassurance or clarification
- Reduce anxiety about actions

**Empty states:**
Structure: Why empty + What to do + CTA

```markdown
No files yet
Upload your first file to get started.
[Upload file]

---

No team members
Invite people to collaborate on your projects.
[Invite team]

---

No notifications
You're all caught up! We'll notify you when there's something new.
```

**Loading states:**
- ✅ "Loading your projects..."
- ✅ "Uploading... 45%"
- ✅ "Processing payment..."
- ✅ "Saving changes..."
- ❌ "Loading..." (too vague)
- Tell users what's loading, not just "Loading..."

**Placeholders:**
- ✅ "Search by name or email..."
- ✅ "Enter your company name"
- ✅ "e.g., Annual Marketing Report"
- Show examples or format hints
- Don't repeat the label

**Character counters:**
- ✅ "125/280 characters"
- ✅ "15 characters remaining"
- ✅ "280 characters max"

**Time stamps:**
- ✅ "2 hours ago"
- ✅ "Last saved at 2:30 PM"
- ✅ "Updated yesterday"
- ✅ "Edited just now"

See `references/ux-copy-best-practices.md` for detailed microcopy patterns.

### 5. Create Onboarding Copy

**When to use:** Creating welcome messages, feature introductions, tutorial text, first-run experiences

**Onboarding structure:**
1. Welcome message (warm, inviting)
2. Step-by-step guidance (3-5 steps max)
3. Progress indicators (show advancement)
4. Completion celebration (encourage and celebrate)

**Tone:**
- Warm and welcoming
- Encouraging, not demanding
- ✅ "Welcome! Let's get you set up."
- ✅ "Great! You're ready to go."
- ✅ "Nice work! One more step."
- ❌ "You must complete these steps"
- ❌ "Required: Setup"

**Pattern:**
```markdown
Welcome to [Product]!
Let's create your first project.

Step 1 of 3: Add team members
Invite your team to collaborate.
[Skip] [Invite team]

Step 2 of 3: Upload files
Drag and drop your files here.
[Skip] [Upload files]

Step 3 of 3: Set your preferences
Customize your workspace.
[Skip] [Continue]

You're all set! Start creating.
[Go to dashboard]
```

**Best practices:**
- Keep it brief (users want to start using the product)
- Make it skippable (don't force it)
- Show progress (users know how much is left)
- Focus on value (why this step matters)
- Allow do-it-later option for non-critical setup

**Feature announcements:**
```markdown
New: Dark mode
Toggle between light and dark themes in Settings > Appearance.
[Try it now] [Dismiss]
```

### 6. Create Notification Copy

**When to use:** Creating in-app notifications, email notifications, push notifications

**Notification types:**

**Push notifications** (ultra-concise, <50 chars):
- ✅ "Sarah commented on your post"
- ✅ "Your order has shipped"
- ✅ "New message from Alex"
- ❌ "You have a new notification"
- ❌ "Update available"

**Email notifications:**
- **Subject:** Clear and specific (30-50 chars)
  - ✅ "Sarah invited you to join Workspace"
  - ✅ "Your export is ready"
  - ❌ "Notification"
- **Body:** Context + action
  - Short explanation
  - Clear call-to-action
  - Link to relevant page

**In-app notifications:**
- **Success:** "✓ File uploaded"
- **Warning:** "⚠ Connection unstable"
- **Error:** "✗ Upload failed. Try again."
- **Info:** "ℹ New features available"

**Patterns:**

| Type | Pattern | Example |
|------|---------|---------|
| Activity | [Who] [did what] | "John shared a file with you" |
| Status | [What] [status] | "Export complete" |
| Request | [Who] [requests what] | "Sarah invited you to join Team" |
| Reminder | [Action] [context] | "Meeting in 10 minutes" |
| Achievement | [What] [accomplished] | "You completed 10 tasks this week!" |

**Notification copy best practices:**
- **Be specific:** "Sarah commented" not "New activity"
- **Be timely:** Include time context if relevant
- **Be actionable:** Make it clear what to do next
- **Be scannable:** Users glance, not read
- **Be respectful:** Don't over-notify or use clickbait

### 7. Write Button and CTA Copy

**When to use:** Creating calls-to-action, button labels, link text

**Button types:**

**Primary actions** (high emphasis):
- ✅ "Create account"
- ✅ "Save changes"
- ✅ "Continue to checkout"
- ✅ "Start free trial"
- Be specific about what happens

**Secondary actions** (medium emphasis):
- ✅ "Cancel"
- ✅ "Go back"
- ✅ "Skip for now"
- ✅ "Learn more"

**Destructive actions** (requires caution):
- ✅ "Delete account"
- ✅ "Remove file"
- ✅ "Discard changes"
- Be explicit about consequences

**Best practices:**
- **Use verbs:** "Create", "Save", "Send", not nouns
- **Be specific:** "Save changes" not just "Save"
- **Keep short:** 1-3 words ideal, max 5 words
- **Front-load keywords:** "Create account" not "Account creation"
- **Avoid generic:** "Submit", "OK" (what does it do?)
- **Match voice:** Formal products use "Sign in", casual use "Log in"

**Examples:**

| Context | ❌ Bad | ✅ Good | Why |
|---------|---------|---------|-----|
| Signup form | Submit | Create account | Specific action |
| File upload | OK | Upload | Clear intent |
| Delete confirm | Yes | Delete | Explicit consequence |
| Save form | Save | Save changes | Specific what's being saved |
| Cancel modal | No | Cancel | Clear what happens |
| Learn about feature | Click here | Learn more | Descriptive, not generic |

## Voice & Tone Guidelines

### Voice (consistent across product)

**Determine product voice:**
- Professional? Friendly? Playful? Authoritative?
- Match company brand
- Stay consistent across all copy

**Example voices:**
- **Professional (B2B):** Clear, efficient, expert
  - "Configure your workspace settings"
- **Friendly (Consumer):** Warm, approachable, helpful
  - "Let's set up your workspace"
- **Playful (Games/Social):** Fun, energetic, casual
  - "Time to make your space awesome!"

### Tone (varies by context)

**Celebrations (success):**
- ✅ "Nice work! Changes saved."
- ✅ "Welcome aboard!"
- ✅ "You're all set!"
- Be cheerful and encouraging
- Celebrate user achievements

**Problems (errors):**
- ✅ "We couldn't save your changes. Please try again."
- ✅ "Oops! Something went wrong."
- Be empathetic and helpful
- Don't be overly cute about serious errors
- Always provide next steps

**Warnings (caution):**
- ✅ "This action cannot be undone."
- ✅ "You have unsaved changes."
- Be serious and clear
- No jokes or playfulness
- Help users avoid mistakes

**Information (neutral):**
- ✅ "Your plan renews on January 15."
- ✅ "Last updated 2 hours ago."
- Be neutral and factual
- Clear and straightforward

## Quality Checklist

Before delivering any UX copy:

**Clarity:**
- [ ] Message is immediately clear
- [ ] No jargon or technical terms (unless necessary)
- [ ] Users will understand what to do
- [ ] Meaning is unambiguous

**Conciseness:**
- [ ] Every word earns its place
- [ ] No filler words ("just", "simply", "please" unless needed)
- [ ] Fits UI constraints
- [ ] Gets to the point quickly

**Helpfulness:**
- [ ] Guides users to success
- [ ] Provides context when needed
- [ ] Errors suggest solutions
- [ ] Reduces friction and anxiety

**Consistency:**
- [ ] Same terms used throughout
- [ ] Matches existing product copy
- [ ] Tone aligns with brand
- [ ] Follows established patterns

**Action-oriented:**
- [ ] Buttons use verbs
- [ ] Clear what will happen
- [ ] Specific, not vague
- [ ] Empowers user action

**Human:**
- [ ] Sounds natural, not robotic
- [ ] Shows empathy where appropriate
- [ ] Avoids corporate speak
- [ ] Conversational (when appropriate)

**Accessible:**
- [ ] Works for screen readers
- [ ] Plain language
- [ ] Descriptive link text (not "click here")
- [ ] No reliance on color alone to convey meaning

## Common Copy Patterns

### Confirmations

**Delete/remove:**
```
Are you sure you want to delete this file?
This action cannot be undone.

[Delete] [Cancel]
```

**Leave without saving:**
```
You have unsaved changes.
Do you want to leave without saving?

[Leave without saving] [Cancel]
```

**Irreversible actions:**
```
This will permanently delete your account and all your data.
This action cannot be undone.

Type "DELETE" to confirm.

[Delete my account] [Cancel]
```

### Success Messages

- "✓ Changes saved"
- "✓ File uploaded"
- "✓ Message sent"
- "✓ Account created. Welcome!"

### Empty States

```
No [items] yet
[Short explanation of what goes here]
[Call to action]

Examples:
- No projects yet
  Create your first project to get started.
  [New project]

- No search results
  Try adjusting your search terms.
  [Clear search]

- All caught up!
  You have no new notifications.
  [Explore features]
```

### Loading States

- "Loading..."
- "Loading your projects..."
- "Uploading file..."
- "Processing payment..."
- "Saving changes..."

## Reference Materials

### UX Copy Best Practices

Load `references/ux-copy-best-practices.md` for:
- Core principles (clarity, conciseness, helpfulness)
- Detailed patterns for all copy types
- Length guidelines
- Accessibility considerations
- Common mistakes to avoid
- Comprehensive review checklist

## Best Practices Summary

1. **Be clear** - Users should understand immediately
2. **Be concise** - Respect their time and attention
3. **Be helpful** - Guide them to success
4. **Be consistent** - Use same terms throughout
5. **Be action-oriented** - Tell them what will happen
6. **Be human** - Sound natural, not robotic
7. **Be specific** - "Save changes" not "Save"
8. **Be empathetic** - Especially in error states
9. **Test with users** - Validate clarity and tone
10. **Iterate** - Improve based on feedback

## When to Use This Skill

| User Request | Use This Skill |
|--------------|----------------|
| Write UI copy for a feature | ✅ Yes |
| Create error messages | ✅ Yes |
| Write button labels | ✅ Yes |
| Review copy for clarity | ✅ Yes |
| Create onboarding flow copy | ✅ Yes |
| Write notification messages | ✅ Yes |
| Create empty state copy | ✅ Yes |
| Write microcopy/tooltips | ✅ Yes |
| Translate copy to another language | ❌ No - use i18n-translator |
| Localize for different markets | ❌ No - use i18n-translator |
| Create bilingual content | ❌ No - use i18n-translator |

## Additional Tips

**Working with UX copy:**
- Read copy aloud to check naturalness
- Test in actual UI to check length
- Review with team for consistency
- Check accessibility with screen reader
- Get feedback from users when possible

**Collaboration:**
- Work with designers on character limits
- Work with developers on dynamic content
- Work with product on feature understanding
- Work with i18n-translator skill for translations

**Continuous improvement:**
- Monitor user feedback and support tickets
- Look for patterns in user confusion
- Update copy based on real usage
- A/B test important copy when possible
- Build a terminology glossary for consistency
