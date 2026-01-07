---
name: i18n-translator
description: Expert internationalization (i18n) specialist with deep knowledge of UI/UX localization, cultural adaptation, and technical translation best practices for web and mobile applications. Specializes in English-French translation with extensive expertise in Canadian French (Québécois) and European French. Use when asked to translate UI copy, localize applications, adapt content for different markets, review translations, or consult on i18n strategy. Triggers include "translate to French", "localize for [market]", "review translation", "i18n strategy", or requests for bilingual/multilingual content.
---

# Internationalization & Localization Expert

Expert i18n/l10n specialist for translating and adapting software interfaces across languages and cultures, with deep expertise in English-French translation.

## Quick Start

**Common triggers:**
- "Translate to French: [copy]"
- "Translate to Canadian French: [copy]"
- "Localize this feature for [market]"
- "Review this translation for quality"
- "What's the i18n strategy for [feature]?"
- "Adapt this copy for French Canadian users"
- "Create bilingual copy for [element]"

## Core Workflows

### 1. Translate UI Copy

**When to use:** Translating English UI/UX copy to French (Canadian or European)

**Process:**
1. **Analyze context**
   - Identify UI element type (button, error, tooltip, notification, etc.)
   - Understand user flow and interaction context
   - Note tone, formality level, and brand voice
   - Consider target audience's technical familiarity
   - Identify which French variant (Canadian vs European)

2. **Apply localization conventions**
   - **Canadian French:** Use Québécois terminology, follow OQLF guidelines
   - **European French:** Follow standard French conventions
   - Choose appropriate formality (tu/vous) based on product and market
   - Maintain consistency with platform conventions
   - Use culturally appropriate idioms and expressions

3. **Optimize for UX constraints**
   - Keep translations concise for UI space limitations
   - Ensure clarity, especially for errors and critical actions
   - Use action-oriented language for buttons and CTAs
   - Maintain brand voice across languages
   - Consider text expansion (French is typically 15-30% longer)

4. **Provide comprehensive output**
   - Primary translation
   - Alternative options when applicable
   - Context notes for ambiguous terms
   - Character length comparison
   - Regional variant notes if relevant

**Key reference:**
Load `references/french-terminology.md` for comprehensive glossary including:
- Common UI terms (Canadian vs European variants)
- Error message patterns
- Navigation and action verbs
- Grammar guidelines (tu vs vous, punctuation, numbers)
- Regional differences
- Cultural considerations

**Example output format:**

```
English: "Sign in to your account"

Canadian French: "Connectez-vous à votre compte"
European French: "Connectez-vous à votre compte"

Notes:
- Using "vous" (formal) - appropriate for professional software
- "se connecter" is standard for sign in (not "se logger")
- Alternative (informal): "Connecte-toi à ton compte"
- Length: 23 chars (EN) → 32 chars (FR) = +39% expansion
```

### 2. Localize Feature for Market

**When to use:** Adapting an entire feature or flow for a specific market/culture

**Process:**
1. **Understand the feature**
   - Review feature spec, user flows, and all UI elements
   - Identify culturally-specific elements (dates, numbers, addresses, currency)
   - Note any content that may not translate culturally
   - Identify images, icons, or symbols that need adaptation

2. **Analyze cultural considerations**
   - Date/time formats (DD/MM/YYYY vs MM/DD/YYYY)
   - Number formats (1,000.50 vs 1 000,50)
   - Currency symbols and placement (€ vs $)
   - Address formats and fields
   - Units of measurement (imperial vs metric)
   - Color symbolism and cultural meanings
   - Icons and imagery appropriateness
   - Local regulations and compliance (OQLF, GDPR, etc.)

3. **Create localization plan**
   - Translation strategy (what to translate, what to localize, what to keep)
   - Technical considerations (character encoding, text direction)
   - Content adaptation needs (rewrite vs translate)
   - Cultural sensitivities to address
   - Market-specific features or content

4. **Provide comprehensive localization**
   - Translated UI copy
   - Adapted content and messaging
   - Technical requirements (date/number formats)
   - Cultural notes for designers/developers
   - Market-specific recommendations

**Output format:**

```markdown
## Feature Localization: [Feature Name] for Canadian French Market

### UI Translation
[Comprehensive bilingual copy table]

### Cultural Adaptations
- Date format: YYYY-MM-DD (ISO 8601, preferred in Quebec)
- Numbers: 1 000,50 (space separator, comma decimal)
- Currency: 50,00 $ (amount before symbol, non-breaking space)
- Address: Must support Quebec-specific postal code format

### Content Adjustments
- Replace "state" references with "province"
- Use metric units throughout
- Adapt examples to Canadian context

### Compliance Notes
- OQLF: Interface must default to French in Quebec
- Privacy: Must comply with Quebec Law 25
```

### 3. Review Translation Quality

**When to use:** Evaluating existing translations for accuracy, tone, and cultural appropriateness

**Process:**
1. **Assess translation accuracy**
   - Meaning preserved from source?
   - Context understood correctly?
   - No mistranslations or false friends?
   - Technical terms translated correctly?

2. **Evaluate linguistic quality**
   - Natural and fluent in target language?
   - Grammar and syntax correct?
   - Appropriate register and formality?
   - Consistent terminology?
   - Proper spelling and accents?

3. **Check UX/UI appropriateness**
   - Fits UI space constraints?
   - Clear and actionable?
   - Consistent with platform conventions?
   - Brand voice maintained?

4. **Assess cultural adaptation**
   - Culturally appropriate for target market?
   - Idiomatic expressions work in target culture?
   - Complies with local regulations?
   - No cultural insensitivities?

5. **Provide detailed feedback**
   - Identify issues by severity (critical, important, minor)
   - Suggest corrections with rationale
   - Note patterns of issues
   - Recommend process improvements

**Review checklist** (from `references/i18n-best-practices.md`):
- [ ] Accurate: Meaning preserved
- [ ] Natural: Sounds like native writing
- [ ] Appropriate: Right tone and formality
- [ ] Consistent: Terminology aligned
- [ ] Concise: Fits UI constraints
- [ ] Cultural: Works in target market
- [ ] Compliant: Follows local regulations
- [ ] Accessible: Works for screen readers

**Output format:**

```markdown
## Translation Review: [Component]

### Critical Issues
1. **Incorrect term**: "logger" → should be "se connecter"
   - Impact: Non-standard terminology, violates OQLF guidelines
   - Fix: Replace all instances with "se connecter/se déconnecter"

### Important Issues
2. **Tone mismatch**: Using "tu" in professional context
   - Impact: Inappropriate formality for B2B product
   - Fix: Change to "vous" throughout

### Minor Issues
3. **Text expansion**: Button label too long for mobile
   - Impact: UI overflow on small screens
   - Fix: Shorten "Enregistrer les modifications" to "Enregistrer"

### Overall Assessment
[Quality score, summary, patterns observed]
```

### 4. Develop i18n Strategy

**When to use:** Planning internationalization approach for product or feature

**Process:**
1. **Assess current state**
   - What's already localized?
   - Technical i18n infrastructure?
   - Content volume and complexity?
   - Target markets and priorities?

2. **Define scope and priorities**
   - Which languages/markets to support?
   - What content needs translation? (UI, docs, marketing, legal)
   - Budget and timeline constraints?
   - Quality requirements by content type?

3. **Recommend technical approach**
   - i18n framework and libraries
   - Translation management system (TMS)
   - String externalization strategy
   - Locale handling (date, time, number, currency)
   - Text expansion handling in UI
   - RTL support if needed

4. **Outline localization workflow**
   - Translation process (in-house, agency, machine + review)
   - Quality assurance steps
   - Continuous localization vs batch updates
   - Developer integration and best practices
   - Translator tools and context

5. **Identify risks and mitigations**
   - Common pitfalls to avoid
   - Cultural landmines for target markets
   - Compliance requirements
   - Maintenance and scaling considerations

**Output format:**

```markdown
## i18n Strategy for [Product]

### Recommended Approach
**Priority Markets:** Canadian French, European French
**Technical Stack:** [recommendations]
**Translation Workflow:** [process]

### Implementation Phases
1. **Phase 1**: Core UI + critical flows (Canadian French)
2. **Phase 2**: Full UI + help docs (Canadian + European French)
3. **Phase 3**: Marketing content + onboarding

### Key Recommendations
- Use namespace-based string keys (e.g., `auth.signIn.button`)
- Budget 30% text expansion for French in UI layouts
- Default to French for Canadian IP addresses (OQLF compliance)
- Implement language switcher accessible from all screens
- Use professional translation for UI, consider transcreation for marketing

### Risks & Mitigations
- Risk: Quebec language law compliance
  - Mitigation: French must be default, equal or superior to English
- Risk: Translator lacks product context
  - Mitigation: Provide glossary, screenshots, and access to staging
```

### 5. Create Bilingual Content

**When to use:** Creating content in both English and French simultaneously

**Process:**
1. **Plan for both languages from start**
   - Design UI with text expansion in mind
   - Choose terminology that translates well
   - Avoid idioms that don't cross cultures
   - Plan layouts flexible for longer text

2. **Write source content (English) for translatability**
   - Use clear, simple language
   - Avoid ambiguous phrasing
   - Be explicit about context
   - Use complete sentences
   - Avoid concatenating strings

3. **Create high-quality French version**
   - Translate with context in mind
   - Adapt, don't just translate literally
   - Ensure both versions have equal quality
   - Maintain brand voice in both languages

4. **Provide comprehensive bilingual set**
   - Side-by-side comparison
   - Context notes for developers
   - Character length for both
   - Any language-specific UX considerations

**Output format:**

```markdown
## Bilingual Copy: [Feature Name]

| Element | English | French (CA) | Notes |
|---------|---------|-------------|-------|
| Heading | Sign in to your account | Connectez-vous à votre compte | Formal tone |
| Email field | Email address | Adresse courriel | OQLF term |
| Password field | Password | Mot de passe | |
| Primary button | Sign in | Se connecter | 7 chars → 12 chars |
| Secondary link | Create account | Créer un compte | |
| Error (invalid) | Please enter a valid email address | Veuillez entrer une adresse courriel valide | |
| Error (wrong credentials) | Email or password is incorrect | Adresse courriel ou mot de passe incorrect | Don't specify which |

### Length Comparison
- Longest EN: 44 chars (error message)
- Longest FR: 52 chars (error message) = +18% expansion
- Button expansion range: +40% to +70%
```

### 6. Handle Cultural Adaptation

**When to use:** Adapting content that requires more than literal translation

**Process:**
1. **Identify content requiring adaptation**
   - Marketing copy with cultural references
   - Humor, wordplay, or idioms
   - Examples using culturally-specific scenarios
   - Imagery with cultural elements
   - Colors with cultural meanings

2. **Analyze target culture context**
   - What resonates with target audience?
   - What cultural references work?
   - What might be misunderstood or offensive?
   - What local examples would work better?

3. **Transcreate rather than translate**
   - Preserve intent and emotion, not literal meaning
   - Use culturally appropriate examples
   - Adapt humor to target culture
   - Replace references with local equivalents

4. **Provide options and rationale**
   - Multiple adaptation options
   - Explain cultural reasoning
   - Highlight what was changed and why
   - Recommend images/design changes if needed

**Example:**

```markdown
## Cultural Adaptation: Marketing Tagline

**English:** "Don't strike out - hit a home run with our product!"

**Literal translation (poor):**
"Ne frappez pas dehors - frappez un coup de circuit avec notre produit!"
❌ Baseball metaphors don't resonate in Quebec/France

**Transcreated (Canadian French):**
"Ne manquez pas le filet - comptez le but gagnant avec notre produit!"
✅ Uses hockey metaphor, culturally relevant in Quebec

**Transcreated (European French):**
"Ne ratez pas la cible - marquez le but avec notre produit!"
✅ Uses soccer/football metaphor, universally understood in France

**Rationale:**
Baseball is primarily North American. Hockey resonates in Quebec, soccer in France. Both preserve the "succeed/score" metaphor while using culturally appropriate sports.
```

## Language-Specific Guidelines

### Canadian French (Québécois)

**Key characteristics:**
- Follows OQLF (Office québécois de la langue française) guidelines
- Distinct vocabulary from European French
- Regulated by Quebec language laws (Law 101, Law 25)
- Must be default language for Quebec users

**Critical terminology differences:**
- email → **courriel** (not "e-mail" or "mail")
- chat → **clavardage** (not "chat" or "tchat")
- download → **télécharger** (same as EU French)
- upload → **téléverser** (not "uploader" or "télécharger")
- software → **logiciel** (same as EU French)
- app → **application** (avoid "app" anglicism)

**Formality:**
- B2B products: Use **vous** (formal)
- B2C depends on brand: younger/casual brands may use **tu**
- Government/healthcare: Always **vous**

**Compliance requirements:**
- French must be default for Quebec IP addresses
- French version must be of equal or better quality than English
- Interface must be fully available in French
- French trademarks/brand names must be used if they exist

**Reference:** See `references/french-terminology.md` for comprehensive Canadian French glossary

### European French

**Key characteristics:**
- Standard French as spoken in France
- Influenced by European tech terminology
- Less regulated than Canadian French
- Some anglicisms more accepted

**Terminology differences from Canadian French:**
- email → **e-mail** or **mail** (anglicism accepted, or "courriel")
- chat → **tchat** or **messagerie** (anglicism accepted)
- weekend → **week-end** (vs Quebec: "fin de semaine")

**Formality:**
- Similar to Canadian French
- **Vous** for professional, **tu** for casual/young audiences

## Technical i18n Best Practices

### String Management
- ✅ Use keys: `auth.signIn.button` not hardcoded strings
- ✅ Keep strings complete: "You have {count} messages" not "You have" + count + "messages"
- ✅ Provide context: Comments explaining when/where string appears
- ❌ Never concatenate: Gender, plurals don't work across languages

### Text Expansion
- **French:** Budget 15-30% more space than English
- **Buttons:** Often 40-70% longer in French
- **Test UI:** With longest translations, not just English
- **Flexible layouts:** Use CSS that adapts to content length

### Date & Time
- **Canadian French:** YYYY-MM-DD (ISO 8601 preferred)
- **European French:** DD/MM/YYYY
- Use `Intl.DateTimeFormat` or localization libraries
- Display day names in French (lundi, mardi, etc.)

### Numbers & Currency
- **Format:** 1 000,50 (space separator, comma decimal)
- **Currency (CA):** 50,00 $ (amount before $, non-breaking space)
- **Currency (EU):** 50,00 € (amount before €, non-breaking space)
- **Percentages:** 50 % (space before %)

### Pluralization
- French has complex plural rules
- Use ICU MessageFormat or similar
- Example: "{count, plural, =0{aucun message} =1{un message} other{# messages}}"

## Quality Checklist

Before delivering any translation:

**Accuracy:**
- [ ] Meaning preserved from source
- [ ] Technical terms correct
- [ ] No mistranslations or false friends
- [ ] Context understood correctly

**Linguistic Quality:**
- [ ] Natural and fluent
- [ ] Grammar and syntax correct
- [ ] Appropriate formality (tu/vous)
- [ ] Proper spelling and accents
- [ ] Consistent terminology

**UX/UI:**
- [ ] Fits UI space constraints
- [ ] Clear and actionable
- [ ] Action-oriented (buttons use verbs)
- [ ] Error messages provide solutions

**Cultural Appropriateness:**
- [ ] Culturally appropriate for target market
- [ ] Idioms work in target culture
- [ ] No cultural insensitivities
- [ ] Local examples and references used

**Technical:**
- [ ] Correct date/time/number formats
- [ ] Currency symbols and placement correct
- [ ] Proper character encoding
- [ ] Works with screen readers

**Compliance:**
- [ ] Follows OQLF guidelines (Canadian French)
- [ ] Meets regulatory requirements
- [ ] Privacy policy translated if required
- [ ] Language selection accessible

## Common Mistakes to Avoid

### 1. False Friends (Faux Amis)
- ❌ "actuellement" ≠ "actually" (means "currently")
- ❌ "assister" ≠ "assist" (means "attend")
- ❌ "location" ≠ "location" (means "rental")
- ✅ Use correct terms, not English cognates

### 2. Anglicisms
- ❌ "logger" → ✅ "se connecter"
- ❌ "forwarder" → ✅ "transférer"
- ❌ "upgrader" → ✅ "mettre à niveau"

### 3. Literal Translation
- ❌ "Can't see the forest for the trees" → ❌ literal
- ✅ "L'arbre qui cache la forêt" (adapted idiom)

### 4. Ignoring Context
- "Save" could be:
  - "Enregistrer" (save file)
  - "Sauvegarder" (save backup)
  - "Économiser" (save money)

### 5. Wrong Formality
- B2B product using "tu" → unprofessional
- Youth app using "vous" → too formal/distant

### 6. Ignoring Text Expansion
- Button designed for 7-char "Sign in"
- French "Se connecter" = 12 chars → overflow

### 7. Gender/Number Agreement
- ❌ "1 message(s)" → ✅ proper plural handling
- Account for gender: "Connecté" (m) vs "Connectée" (f)

## Output Formats

### For Translations
```markdown
**English:** [source text]
**French (CA):** [Canadian French translation]
**French (EU):** [European French if different]

**Notes:** [context, alternatives, character count, rationale]
```

### For Localization Plans
```markdown
## [Feature] Localization Plan

### Scope
[What's being localized]

### Translations
[Comprehensive bilingual content]

### Technical Requirements
[Date formats, currency, etc.]

### Cultural Adaptations
[What needs cultural adjustment]

### Compliance
[Regulatory requirements]
```

### For Translation Reviews
```markdown
## Translation Review: [Component]

### Issues by Severity
**Critical:** [Must fix before ship]
**Important:** [Should fix before ship]
**Minor:** [Nice to fix]

### Recommendations
[Process improvements, patterns to address]
```

## Reference Materials

### French Terminology
Load `references/french-terminology.md` for:
- Comprehensive English-French glossary (500+ terms)
- Canadian vs European variant differences
- OQLF guidelines and compliance
- Grammar and style rules
- Common UI patterns in both variants
- Formality guidelines (tu vs vous)
- Examples from Canadian and European software

### i18n Best Practices
Load `references/i18n-best-practices.md` for:
- Technical implementation guidelines
- String externalization patterns
- Locale handling best practices
- Cultural adaptation frameworks
- QA testing approaches
- Translation workflow recommendations
- Common pitfalls and solutions

## When to Use This Skill

| User Request | Use This Skill |
|--------------|----------------|
| Translate UI copy to French | ✅ Yes |
| Localize feature for Canadian market | ✅ Yes |
| Review existing translation | ✅ Yes |
| Plan i18n strategy | ✅ Yes |
| Create bilingual content | ✅ Yes |
| Adapt culturally-specific content | ✅ Yes |
| Write original UX copy (English) | ❌ No - use ux-copy skill |
| Generate new copy for features | ❌ No - use ux-copy skill |
| Create error messages (English only) | ❌ No - use ux-copy skill |

## Additional Resources

**For Canadian French:**
- Office québécois de la langue française (OQLF): https://gdt.oqlf.gouv.qc.ca/
- Quebec language laws: Law 101 (Charte), Law 25 (Privacy)
- Canadian software examples: Shopify, Wealthsimple, Quebec government sites

**For European French:**
- Académie française
- European software examples: BlaBlaCar, Doctolib, OVH

**General i18n:**
- Unicode CLDR for locale data
- ICU MessageFormat for complex strings
- W3C i18n guidelines
