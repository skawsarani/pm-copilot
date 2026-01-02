---
name: ux-copy
description: Create and refine UX/UI copy for software interfaces with Canadian French (Québécois) localization. Use when asked to create, translate, or review user interface copy including buttons, labels, error messages, tooltips, notifications, onboarding flows, empty states, or any user-facing text. Triggers include "translate to Canadian French", "create UI copy for [feature]", "review this copy", "create error messages", "create microcopy", "create onboarding copy", "create notification copy", or requests for bilingual UI text. Follows OQLF guidelines and software localization best practices.
---

# UX Copy & Canadian French Localization

Create effective UX copy for software interfaces and translate to Canadian French (Québécois).

## Quick Start

**Common triggers:**
- "Translate to Canadian French: [copy]"
- "Create UI copy for [feature]"
- "Review this copy for clarity and tone"
- "Create error messages for [scenario]"
- "Create microcopy for [UI element]"
- "Create onboarding copy for [feature]"
- "Create notification copy for [event]"

## Core Workflows

### 1. Translate to Canadian French

**When to use:** Translating any English UI/UX copy to Canadian French (Québécois)

**Process:**
1. **Analyze context**
   - Identify UI element type (button, error, tooltip, etc.)
   - Understand user flow and context
   - Note tone and formality level
   - Consider target user's technical familiarity

2. **Apply Canadian French conventions**
   - Use Québécois terminology (see `references/canadian-french-terminology.md`)
   - Follow OQLF guidelines for software
   - Use appropriate formality (tu/vous) based on context
   - Maintain consistency with Canadian software patterns

3. **Optimize for UX**
   - Keep translations concise for UI constraints
   - Ensure clarity (especially in errors/notifications)
   - Use action-oriented language for buttons
   - Maintain brand voice

4. **Provide translation with context**
   - Primary translation
   - Alternative options if applicable
   - Context notes for ambiguous terms
   - Character length considerations if relevant

**Key terminology reference:**
Load `references/canadian-french-terminology.md` for comprehensive glossary of:
- Common UI terms (email→courriel, chat→clavardage, upload→téléverser)
- Error messages
- Navigation and actions
- Grammar guidelines (tu vs vous, punctuation, numbers)
- Common patterns

**Example output format:**

```
English: "Sign in to your account"
Canadian French: "Connectez-vous à votre compte"

Notes:
- Using "vous" (formal) - appropriate for professional software
- "se connecter" is standard for sign in (not "se logger")
- Alternative (informal): "Connecte-toi à ton compte"
```

### 2. Create UI Copy for Feature

**When to use:** Generating complete UI copy set for new features or flows

**Process:**
1. **Understand the feature**
   - Review feature spec or brief if available
   - Identify all UI elements needing copy
   - Understand user flows and interactions
   - Note technical constraints

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

3. **Create bilingual set**
   - English version (primary)
   - Canadian French translation
   - Maintain consistency in tone and terminology
   - Ensure both fit UI constraints

4. **Organize by context**
   - Group by user flow or screen
   - Include context notes for developers
   - Provide character length limits if needed
   - Note dynamic content placeholders

**Output format:**

Organize as table or grouped list:

```markdown
## Login Screen

| Element | English | French (CA) | Notes |
|---------|---------|-------------|-------|
| Heading | Sign in to your account | Connectez-vous à votre compte | Formal tone |
| Email field | Email address | Adresse courriel | |
| Password field | Password | Mot de passe | |
| Primary button | Sign in | Se connecter | |
| Secondary link | Create account | Créer un compte | |
| Error (invalid) | Please enter a valid email address | Veuillez entrer une adresse courriel valide | |
| Error (wrong credentials) | Email or password is incorrect | Adresse courriel ou mot de passe incorrect | Don't specify which |
```

### 3. Review and Refine Copy

**When to use:** Before finalizing any user-facing copy

**Process:**
1. **Assess clarity**
   - Is the message clear and unambiguous?
   - Will users understand the action/information?
   - Are technical terms explained or avoided?
   - Is language appropriate for audience?

2. **Evaluate tone**
   - Does it match product voice?
   - Is formality level appropriate?
   - Is it friendly/professional/technical as needed?
   - Is it consistent with other product copy?

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
```

### 4. Create Error Messages

**When to use:** Creating error messages, validation messages, or system notifications

**Error message anatomy:**
1. What went wrong (clear and specific)
2. Why it happened (if helpful)
3. How to fix it (actionable)

**Error types and patterns:**

**Validation errors:**
- ✅ "Password must be at least 8 characters"
- ✅ "Email address must include '@' symbol"
- ❌ "Invalid input"

**System errors:**
- ✅ "We're having trouble connecting. Check your internet and try again."
- ✅ "Something went wrong on our end. We're working to fix it."
- ❌ "Error 500"

**Permission errors:**
- ✅ "You don't have permission to delete this file. Contact the owner to request access."
- ❌ "Access denied"

**Business logic errors:**
- ✅ "You can't delete your account while you have an active subscription. Cancel your subscription first."
- ❌ "Cannot delete"

**Translation considerations:**
Load `references/canadian-french-terminology.md` for error message patterns in French.

**Tone guidelines:**
- Don't blame the user
- ❌ "You entered invalid data"
- ✅ "Please check your email format"
- Be empathetic for frustrating errors
- Offer solutions when possible
- Keep consistent format across all errors

### 5. Create Microcopy

**When to use:** Creating tooltips, help text, empty states, loading messages

**Microcopy types:**

**Tooltips:**
- Keep under 10 words
- ✅ "Your private workspace for saving ideas"
- Use for definitions or extra context
- Don't use for critical information

**Inline help:**
- ✅ "We'll never share your email address"
- ✅ "You can change this later"
- Provide reassurance or clarification

**Empty states:**
Structure: Why empty + What to do + CTA
```
No files yet
Upload your first file to get started.
[Upload file]
```

**Loading states:**
- ✅ "Loading your projects..."
- ✅ "Uploading... 45%"
- Tell users what's loading, not just "Loading..."

**Character counters:**
- ✅ "125/280 characters"
- ✅ "15 characters remaining"

**Time stamps:**
- ✅ "2 hours ago"
- ✅ "Last saved at 2:30 PM"

See `references/ux-copy-best-practices.md` for detailed microcopy patterns.

### 6. Create Onboarding Copy

**When to use:** Creating welcome messages, feature introductions, tutorial text

**Onboarding structure:**
1. Welcome message
2. Step-by-step guidance (3-5 steps max)
3. Progress indicators
4. Completion celebration

**Tone:**
- Warm and welcoming
- Encouraging, not demanding
- ✅ "Welcome! Let's get you set up."
- ✅ "Great! You're ready to go."
- ❌ "You must complete these steps"

**Pattern:**
```
Welcome to [Product]!
Let's create your first project.

Step 1 of 3: Add team members
Invite your team to collaborate.

Step 2 of 3: Upload files
Drag and drop your files here.

Step 3 of 3: Set your preferences
Customize your workspace.

You're all set! Start creating.
```

**Bilingual considerations:**
- Keep both English and French versions warm
- Maintain consistent tone
- Ensure cultural appropriateness
- Use appropriate formality level (tu/vous)

### 7. Create Notification Copy

**When to use:** Creating in-app notifications, email notifications, push notifications

**Notification types:**

**Push notifications** (ultra-concise, <50 chars):
- ✅ "Sarah commented on your post"
- ✅ "Your order has shipped"
- ❌ "You have a new notification"

**Email notifications:**
- Subject: Clear and specific (30-50 chars)
- Body: Context + action
- ✅ Subject: "Sarah invited you to join Workspace"

**In-app notifications:**
- Success: "✓ File uploaded"
- Warning: "⚠ Connection unstable"
- Error: "✗ Upload failed. Try again."
- Info: "ℹ New features available"

**Patterns:**

| Type | Pattern | Example |
|------|---------|---------|
| Activity | [Who] [did what] | "John shared a file" |
| Status | [What] [status] | "Export complete" |
| Request | [Who] [requests] | "Sarah invited you" |
| Reminder | [Action] [context] | "Meeting in 10 minutes" |

**Translation:**
- Keep French versions equally concise
- Maintain urgency/tone
- Ensure both fit channel constraints

## When to Use Which Copy Type

| Need | Copy Type | Process |
|------|-----------|---------|
| Translate existing copy | Translate to French | Workflow 1 |
| New feature copy | Create UI copy | Workflow 2 |
| Review before launch | Review & refine | Workflow 3 |
| Form validation | Create error messages | Workflow 4 |
| Tooltips, help text | Create microcopy | Workflow 5 |
| Welcome new users | Create onboarding | Workflow 6 |
| Alert users | Create notifications | Workflow 7 |

## Voice & Tone Guidelines

### Voice (consistent)
Determine product voice:
- Professional? Friendly? Playful? Authoritative?
- Match company brand
- Stay consistent across all copy

### Tone (varies by context)

**Celebrations (success):**
- ✅ "Nice work! Changes saved."
- Be cheerful and encouraging

**Problems (errors):**
- ✅ "We couldn't save your changes. Please try again."
- Be empathetic and helpful

**Warnings:**
- ✅ "This action cannot be undone."
- Be serious and clear

**Information:**
- ✅ "Your plan renews on January 15."
- Be neutral and factual

### Formality (tu vs. vous in French)

**Use "vous" (formal):**
- Professional/business software
- Financial services
- Healthcare, government
- B2B products

**Use "tu" (informal):**
- Consumer/casual apps
- Social media, gaming
- Youth-focused products
- Friendly brand voice

## Reference Materials

### Canadian French Terminology
Load `references/canadian-french-terminology.md` for:
- Comprehensive glossary (300+ terms)
- OQLF guidelines
- Grammar and style rules
- Common patterns
- Formality guidelines (tu vs vous)
- Punctuation rules
- Examples from Canadian software

### UX Copy Best Practices
Load `references/ux-copy-best-practices.md` for:
- Core principles (clarity, conciseness, helpfulness)
- Detailed patterns for all copy types
- Length guidelines
- Accessibility considerations
- Localization tips
- Common mistakes to avoid
- Review checklist

## Quality Checklist

Before delivering any UX copy:

**Clarity:**
- [ ] Message is immediately clear
- [ ] No jargon or technical terms (unless necessary)
- [ ] Users will understand what to do

**Conciseness:**
- [ ] Every word earns its place
- [ ] No filler words
- [ ] Fits UI constraints

**Helpfulness:**
- [ ] Guides users to success
- [ ] Provides context when needed
- [ ] Errors suggest solutions

**Consistency:**
- [ ] Same terms used throughout
- [ ] Matches existing product copy
- [ ] Tone aligns with brand

**Action-oriented:**
- [ ] Buttons use verbs
- [ ] Clear what will happen
- [ ] Specific, not vague

**Translation (if bilingual):**
- [ ] French follows OQLF guidelines
- [ ] Appropriate formality (tu/vous)
- [ ] Both versions fit UI
- [ ] Tone consistent across languages

**Accessibility:**
- [ ] Works for screen readers
- [ ] Plain language
- [ ] Descriptive link text

## Output Format

**For translations:**
Provide side-by-side comparison with notes:
```
English: [original]
French: [translation]
Notes: [context, alternatives, character count]
```

**For new copy:**
Organize by context (screen, flow) with bilingual table or grouped list.

**For reviews:**
Show original → revised with rationale for changes.

**For complete feature copy:**
Group by screen/flow with comprehensive bilingual set covering all UI elements.

## Common Patterns Library

**Buttons:**
- Save: "Enregistrer" / "Enregistrer les modifications"
- Cancel: "Annuler"
- Delete: "Supprimer"
- Confirm: "Confirmer"
- Continue: "Continuer"

**Confirmations:**
- "Êtes-vous sûr ?" / "Are you sure?"
- "Cette action est irréversible" / "This action cannot be undone"

**Success:**
- "✓ Modifications enregistrées" / "✓ Changes saved"
- "✓ Envoyé" / "✓ Sent"

**Errors:**
- "Une erreur s'est produite" / "Something went wrong"
- "Veuillez réessayer" / "Please try again"

**Empty states:**
- "Aucun [item]. [Action] pour commencer." / "No [items]. [Action] to get started."

## Best Practices Summary

1. **Be clear** - Users should understand immediately
2. **Be concise** - Respect their time and attention
3. **Be helpful** - Guide them to success
4. **Be consistent** - Use same terms throughout
5. **Be action-oriented** - Tell them what will happen
6. **Be human** - Sound natural, not robotic
7. **Be specific** - "Save changes" not "Save"
8. **Check both languages** - Ensure quality in English and French
9. **Test with users** - Validate clarity and tone
10. **Iterate** - Improve based on feedback

## Additional Resources

**When working on Canadian French:**
- Always reference `canadian-french-terminology.md` for terminology
- Follow OQLF guidelines strictly
- Look at Canadian software examples (Shopify, Wealthsimple, Quebec government)
- When in doubt, prefer clarity over literal translation

**When working on UX copy:**
- Reference `ux-copy-best-practices.md` for detailed guidelines
- Read copy aloud to check naturalness
- Test with actual UI to check length
- Review with team for consistency
- Check accessibility with screen reader
