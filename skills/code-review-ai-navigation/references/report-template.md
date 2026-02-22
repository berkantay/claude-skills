# AI Navigation & Accessibility Audit Report Template

Use this template when writing audit reports to `docs/ai-nav-audit-YYYY-MM-DD.md`.

---

## Template

```markdown
# AI Navigation & Accessibility Audit

**Date**: YYYY-MM-DD
**Project**: [Project name]
**Pages audited**: [Count]
**Auditor**: Claude (code-review-ai-navigation skill)

## Summary Scorecard

| Page | AI Nav Score | A11y Score | Critical | High | Medium | Low |
|------|-------------|------------|----------|------|--------|-----|
| index.html | 82/100 | 75/100 | 0 | 2 | 3 | 1 |
| about.html | 71/100 | 68/100 | 1 | 1 | 2 | 4 |
| services.html | 65/100 | 72/100 | 0 | 3 | 1 | 2 |
| contact.html | 88/100 | 80/100 | 0 | 0 | 2 | 1 |
| **Average** | **76/100** | **74/100** | **1** | **6** | **8** | **8** |

### Overall Rating

- **AI Navigability**: [Rating] — [One-sentence summary]
- **Accessibility**: [Rating] — [One-sentence summary]

---

## Top Priority Fixes

The following changes would most improve both scores:

1. **[Fix description]** — Affects [N] pages, improves AI Nav by ~[X]pts, A11y by ~[Y]pts
2. **[Fix description]** — Affects [N] pages, ...
3. **[Fix description]** — Affects [N] pages, ...

---

## Detailed Findings

### [page-name.html]

**Scores**: AI Nav [X]/100 | A11y [Y]/100

#### Critical

> **[Finding title]**
> Category: [Document Structure | Landmarks | Content Clarity | Navigation | Structured Data | Accessibility]
> Impact: AI Nav [+Xpts if fixed] | A11y [+Ypts if fixed]
>
> **Issue**: [What's wrong and why it matters for agents/users]
>
> **Current**:
> ```html
> [The problematic code]
> ```
>
> **Fix**:
> ```html
> [The corrected code]
> ```

#### High

> [Same format as Critical]

#### Medium

> [Same format]

#### Low

> [Same format]

---

### [next-page.html]

[Repeat per page]

---

## Category Breakdown

### Document Structure

| Page | h1 | Hierarchy | Semantic | Section headings | IDs | Score |
|------|----|-----------|----------|-----------------|-----|-------|
| index.html | Pass | Pass | Fail | Pass | Fail | 15/25 |

### Landmark Regions

| Page | header | nav | main | footer | aside | Score |
|------|--------|-----|------|--------|-------|-------|
| index.html | Pass | Pass | Pass | Pass | N/A | 12/15 |

### Content Clarity

| Page | Links | Alt text | Tables | Lists | Code | Abbr | Score |
|------|-------|----------|--------|-------|------|------|-------|
| index.html | Fail | Pass | N/A | Pass | N/A | N/A | 12/20 |

### Navigation Predictability

| Page | Consistent nav | Breadcrumbs | Canonical | Link style | Sitemap | Score |
|------|---------------|-------------|-----------|------------|---------|-------|
| index.html | Pass | N/A | Fail | Pass | Fail | 9/20 |

### Structured Data

| Page | JSON-LD | Schema type | Meta desc | OG tags | Title | Score |
|------|---------|-------------|-----------|---------|-------|-------|
| index.html | Fail | N/A | Pass | Fail | Pass | 7/20 |

### Accessibility Fundamentals

| Page | Contrast | Focus | Skip | Labels | ARIA | Lang | Keyboard | Touch | Media | Errors | Score |
|------|----------|-------|------|--------|------|------|----------|-------|-------|--------|-------|
| index.html | Pass | Fail | Fail | Pass | Fail | Pass | Pass | Pass | N/A | N/A | 35/50 |

### Bonus Points

| Page | RSS | API | robots.txt | Classes | data-* | Bonus |
|------|-----|-----|-----------|---------|--------|-------|
| index.html | N/A | N/A | Pass | Pass | N/A | +7 |

---

## Recommendations

### Quick Wins (< 30 minutes each)

1. [Specific fix with estimated impact]
2. [...]

### Medium Effort (1-2 hours)

1. [Specific fix]
2. [...]

### Larger Improvements (half day+)

1. [Specific fix]
2. [...]
```

---

## Scoring Notes

When calculating scores:

- **AI Navigability** = Document Structure (25) + Landmark Regions AI portion (8) + Content Clarity AI portion (10) + Navigation Predictability (20) + Structured Data (20) + shared items from Accessibility (17) = 100
- **Accessibility** = Landmark Regions A11y portion (7) + Content Clarity A11y portion (10) + Accessibility Fundamentals (50) + shared items from other categories (33) = 100
- **Bonus points** are additive (can exceed 100, cap display at 100+N bonus)

Items that count for both scores (the ~60% overlap):
- Heading hierarchy, semantic sections, section headings
- Landmark regions (all)
- Descriptive links, alt text, tables, lists
- Form labels, ARIA attributes, language declaration

Items that are AI Nav only:
- Meaningful IDs, JSON-LD, meta/OG tags, canonical URLs, sitemap, consistent nav, breadcrumbs, link consistency

Items that are Accessibility only:
- Contrast ratios, focus styles, skip link, keyboard navigation, touch targets, autoplay media, error identification
