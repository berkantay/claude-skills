---
name: code-review-ai-navigation
description: "Audit HTML pages and code output for AI agent navigability and accessibility. Checks semantic structure, landmark regions, heading hierarchy, structured data, link clarity, and WCAG compliance. Produces dual-scored reports with concrete fixes. Trigger with 'ai navigation audit', 'ai-ready check', 'check ai navigability', or 'accessibility and ai audit'."
compatibility: claude-code-only
---

# Code Review: AI Navigation & Accessibility

Audit HTML pages and rendered output to verify they are well-structured for both AI agent consumption and human accessibility. AI agents (LLM crawlers, MCP tools, automated scrapers, assistive tech) need predictable structure to parse, navigate, and act on content. This skill checks that structure exists, scores it, and produces a report with fixes.

## What You Produce

A report file (`docs/ai-nav-audit-YYYY-MM-DD.md`) containing:
- Per-page dual scores: **AI Navigability** (0-100) and **Accessibility** (0-100)
- Findings ranked by severity (Critical, High, Medium, Low)
- Concrete fix suggestions with code snippets
- Summary scorecard across all audited pages

## Operating Modes

### Mode 1: Full Audit

**When**: "ai navigation audit", "audit pages for ai", "full ai-ready check"

Comprehensive review of all HTML pages in the project.

1. **Discover pages**: Find all `.html` files, check router config for SPA routes, or ask the user which pages to audit
2. **Create a task list** of pages to review
3. **For each page**, run all checks from the [audit checklist](references/audit-checklist.md):
   - Document structure
   - Semantic landmarks
   - Heading hierarchy
   - Content clarity
   - Navigation predictability
   - Structured data
   - Accessibility fundamentals
4. **Score each page** using the scoring rubric
5. **Write report** to `docs/ai-nav-audit-YYYY-MM-DD.md` using the [report template](references/report-template.md)

### Mode 2: Page Check

**When**: "check this page", "is this page ai-navigable?", "review [filename] for ai"

Targeted review of a single page or component.

1. Read the specified file
2. Run all checklist items against it
3. Report findings inline with scores (no separate file unless requested)

### Mode 3: Pre-Ship Review

**When**: "pre-ship ai check", "is this ready for agents?", "final ai-nav review"

Quick pass focused on blockers — only Critical and High severity items.

1. Scan all pages for Critical/High issues only
2. Report as a pass/fail table inline
3. Suggest the top 3-5 fixes that would most improve agent navigability

## Audit Categories

### 1. Document Structure (AI Nav: 25pts)

An AI agent needs to understand what a page is and how it's organised.

| Check | Weight | What to look for |
|-------|--------|-------------------|
| Single `<h1>` | 5 | Exactly one per page, describes page purpose |
| Heading hierarchy | 5 | No skipped levels (h1 > h2 > h3, never h1 > h3) |
| Semantic sections | 5 | Content wrapped in `<section>`, `<article>`, `<aside>` — not bare `<div>` |
| Section headings | 5 | Every `<section>` has a heading or `aria-label` |
| Meaningful `id` attributes | 5 | Key sections have descriptive IDs for deep linking |

### 2. Landmark Regions (AI Nav: 15pts, A11y: 15pts)

Landmarks let agents jump to page zones without parsing every element.

| Check | Weight | What to look for |
|-------|--------|-------------------|
| `<header>` present | 3 | Page has a `<header>` with site identity |
| `<nav>` present | 3 | Primary navigation in `<nav>`, labelled if multiple |
| `<main>` present | 3 | Exactly one `<main>` element |
| `<footer>` present | 3 | Page has a `<footer>` |
| `<aside>` used correctly | 3 | Sidebar/supplementary content in `<aside>`, not `<div>` |

### 3. Content Clarity (AI Nav: 20pts, A11y: 15pts)

Can an agent understand content without rendering it visually?

| Check | Weight | What to look for |
|-------|--------|-------------------|
| Descriptive link text | 5 | No "click here", "read more", "learn more" without context |
| Image alt text | 4 | Content images have meaningful alt; decorative have `alt=""` |
| Table structure | 4 | Data tables use `<thead>`, `<th scope>`, `<caption>` |
| Lists for list content | 3 | `<ul>`/`<ol>` for actual lists, not `<div>` sequences |
| Code blocks annotated | 2 | `<code>` and `<pre>` with language class where applicable |
| Abbreviations marked | 2 | `<abbr title="...">` for non-obvious acronyms |

### 4. Navigation Predictability (AI Nav: 20pts)

An agent visiting multiple pages needs consistent patterns to build a mental model.

| Check | Weight | What to look for |
|-------|--------|-------------------|
| Consistent nav structure | 5 | Same navigation pattern across all pages |
| Breadcrumbs | 4 | Present on inner pages, using `<nav aria-label="Breadcrumb">` |
| Canonical URLs | 3 | `<link rel="canonical">` on every page |
| Internal link consistency | 4 | Links use consistent paths (no mix of relative/absolute, no broken anchors) |
| Sitemap available | 4 | `sitemap.xml` exists and lists all pages |

### 5. Structured Data (AI Nav: 20pts)

Machine-readable metadata that agents can parse without understanding layout.

| Check | Weight | What to look for |
|-------|--------|-------------------|
| JSON-LD present | 5 | At least one `<script type="application/ld+json">` block |
| Schema type appropriate | 5 | Schema matches content (LocalBusiness, Article, Product, FAQ, etc.) |
| Meta description | 3 | `<meta name="description">` present and meaningful |
| Open Graph tags | 3 | `og:title`, `og:description`, `og:type` present |
| `<title>` descriptive | 4 | Unique, descriptive title per page (not just site name) |

### 6. Accessibility Fundamentals (A11y: 50pts)

Checks that also benefit AI agents using accessibility APIs as input.

| Check | Weight | What to look for |
|-------|--------|-------------------|
| Contrast ratios | 8 | Text meets WCAG AA (4.5:1 normal, 3:1 large) |
| Focus styles visible | 6 | All interactive elements have visible focus indicators |
| Skip link | 4 | First focusable element skips to `<main>` |
| Form labels | 6 | Every input has an associated `<label>` or `aria-label` |
| ARIA on interactive elements | 5 | `aria-expanded` on toggles, `aria-label` on icon buttons |
| Language declared | 3 | `<html lang="en">` (or appropriate language) |
| Keyboard navigable | 8 | All interactive elements reachable and operable via keyboard |
| Touch targets | 5 | Minimum 44x44px on interactive elements |
| No autoplay media | 3 | No auto-playing audio/video without controls |
| Error identification | 2 | Form errors programmatically associated with fields |

### 7. Bonus: Agent-Friendly Extras (up to 20 bonus pts)

Not required, but significantly improve agent experience.

| Check | Bonus | What to look for |
|-------|-------|-------------------|
| RSS/Atom feed | 5 | Feed available for content-heavy sites |
| API endpoint documented | 5 | `/api/` routes or OpenAPI spec available |
| robots.txt with sitemap ref | 3 | `robots.txt` exists and references sitemap |
| Semantic class names | 4 | Classes describe purpose (`.product-card`) not appearance (`.blue-box`) |
| `data-*` attributes for state | 3 | Interactive state in `data-*` attributes, not just CSS classes |

## Scoring Rubric

### AI Navigability Score (0-100)

| Range | Rating | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Agent can fully parse, navigate, and extract data |
| 70-89 | Good | Agent can navigate with minor ambiguity |
| 50-69 | Fair | Agent can extract some data but structure is unreliable |
| 30-49 | Poor | Agent struggles to identify page zones and content purpose |
| 0-29 | Failing | Essentially opaque to automated agents |

### Accessibility Score (0-100)

| Range | Rating | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Meets WCAG AA across all checks |
| 70-89 | Good | Minor gaps, mostly compliant |
| 50-69 | Fair | Several issues affecting assistive tech users |
| 30-49 | Poor | Significant barriers to access |
| 0-29 | Failing | Unusable with assistive technology |

### Severity Levels

- **Critical** — An agent cannot determine page purpose or navigate at all; a user with assistive tech is blocked
- **High** — Significant ambiguity for agents; notable friction for assistive tech users
- **Medium** — Agent can work around it but loses accuracy; minor a11y gaps
- **Low** — Polish items that improve agent confidence or user experience

## When to Use

| Scenario | Mode |
|----------|------|
| After building a multi-page site | Full Audit |
| Reviewing a single component or page | Page Check |
| Before deploying to production | Pre-Ship Review |
| After major refactoring | Full Audit |
| Quick sanity check on AI readability | Page Check |

**Pair with**: `web-design-methodology` (build it right), `seo-local-business` (structured data), `ux-audit` (usability), `context-manager` (project docs structure).

## Autonomy Rules

- **Just do it**: Read files, analyse structure, score pages, report findings
- **Brief confirmation**: Before writing report files, before auditing more than 10 pages
- **Ask first**: Before modifying any source files to fix issues

## Tips

- Run this after `web-design-methodology` to verify the output meets agent standards
- AI navigability and accessibility overlap ~60% — fixing one usually helps the other
- Heading hierarchy is the single highest-impact fix for both scores
- JSON-LD structured data is the biggest AI-only win (no a11y benefit, huge agent benefit)
- For SPAs, check the rendered DOM (via browser tools) not just the source HTML

## Reference Files

| When | Read |
|------|------|
| Running checks on a page | [references/audit-checklist.md](references/audit-checklist.md) |
| Writing the audit report | [references/report-template.md](references/report-template.md) |
