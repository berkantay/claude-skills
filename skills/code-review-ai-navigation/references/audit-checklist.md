# AI Navigation & Accessibility Audit Checklist

Use this checklist when reviewing each page. Work through each category, noting pass/fail and specific issues.

## How to Use

For each check:
- **Pass**: The page meets the requirement
- **Fail**: Note the specific issue and severity
- **N/A**: The check doesn't apply to this page type

---

## 1. Document Structure

```
[ ] Single <h1> — exactly one per page, describes page purpose
    FAIL example: Two <h1> tags, or <h1> says "Welcome" instead of "Plumbing Services in Newcastle"
    FIX: Ensure one <h1> that an agent could use as a page summary

[ ] Heading hierarchy — no skipped levels
    FAIL example: <h1> followed by <h3> (skipping h2)
    FIX: Fill in missing levels. Headings are an outline — skipping levels breaks the tree

[ ] Semantic sections — content in <section>, <article>, <aside>
    FAIL example: <div class="services-section"> instead of <section>
    FIX: Replace wrapper <div>s with appropriate semantic elements

[ ] Section headings — every <section> has a heading or aria-label
    FAIL example: <section> with no heading (agent can't label the zone)
    FIX: Add a heading (can be visually hidden) or aria-label="Section purpose"

[ ] Meaningful id attributes — key sections have descriptive IDs
    FAIL example: <section id="s3"> or no id at all
    FIX: <section id="our-services"> — enables deep linking and agent targeting
```

## 2. Landmark Regions

```
[ ] <header> present — contains site identity (logo, site name)
    FAIL: No <header>, or logo/nav in a plain <div>

[ ] <nav> present — primary navigation in <nav> element
    FAIL: Navigation links in a <div> or <ul> without <nav> wrapper
    Multi-nav: If multiple <nav> elements, each needs aria-label
    e.g., <nav aria-label="Main"> and <nav aria-label="Footer">

[ ] <main> present — exactly one per page
    FAIL: No <main>, or multiple <main> elements
    FIX: Wrap primary content in <main>. Only one per page.

[ ] <footer> present — page footer in <footer> element
    FAIL: Footer content in a plain <div>

[ ] <aside> used correctly — supplementary content in <aside>
    FAIL: Sidebar in a <div class="sidebar"> instead of <aside>
    N/A if page has no sidebar/supplementary content
```

## 3. Content Clarity

```
[ ] Descriptive link text — no orphaned "click here" or "read more"
    FAIL examples:
      <a href="/services">Click here</a>
      <a href="/blog/post-1">Read more</a>
    FIX:
      <a href="/services">View our plumbing services</a>
      <a href="/blog/post-1">Read: How to prevent blocked drains</a>
    WHY: An agent reading link text out of context needs to know the destination

[ ] Image alt text — content images meaningful, decorative empty
    FAIL: <img src="team.jpg"> (no alt) or <img src="divider.png" alt="decorative line">
    FIX: <img src="team.jpg" alt="The Jezweb team in our Newcastle office">
         <img src="divider.png" alt="">
    WHY: Alt text is the only way an agent "sees" images

[ ] Table structure — data tables use <thead>, <th scope>, <caption>
    FAIL: Data in <div> grid, or <table> without headers
    FIX:
      <table>
        <caption>Service pricing</caption>
        <thead><tr><th scope="col">Service</th><th scope="col">Price</th></tr></thead>
        <tbody>...</tbody>
      </table>
    N/A if no data tables on page

[ ] Lists for list content — <ul>/<ol> for actual lists
    FAIL: A series of <div>s that are conceptually a list
    FIX: Wrap in <ul>/<ol> with <li> items
    WHY: Agents parse list semantics to understand item collections

[ ] Code blocks annotated — language class on <code>/<pre>
    FAIL: <pre><code>const x = 1</code></pre>
    FIX: <pre><code class="language-javascript">const x = 1</code></pre>
    N/A if no code on page

[ ] Abbreviations marked — <abbr> for non-obvious acronyms
    FAIL: "We comply with WCAG standards" (WCAG undefined)
    FIX: "We comply with <abbr title="Web Content Accessibility Guidelines">WCAG</abbr> standards"
    N/A if no abbreviations used
```

## 4. Navigation Predictability

```
[ ] Consistent nav structure — same pattern across all pages
    FAIL: Homepage has horizontal nav, inner pages have sidebar nav
    Check: Compare <nav> markup across 3+ pages

[ ] Breadcrumbs on inner pages — using <nav aria-label="Breadcrumb">
    FAIL: No breadcrumbs, or breadcrumbs in a plain <div>
    FIX:
      <nav aria-label="Breadcrumb">
        <ol>
          <li><a href="/">Home</a></li>
          <li><a href="/services">Services</a></li>
          <li aria-current="page">Emergency Plumbing</li>
        </ol>
      </nav>
    N/A for single-page sites or homepage

[ ] Canonical URLs — <link rel="canonical"> on every page
    FAIL: Missing canonical tag
    FIX: <link rel="canonical" href="https://example.com/services">
    WHY: Agents need to know the authoritative URL

[ ] Internal link consistency — no mixed relative/absolute paths
    FAIL: Some links use "/about", others use "https://example.com/about", others use "../about"
    FIX: Pick one pattern (absolute paths preferred) and use it everywhere

[ ] Sitemap available — sitemap.xml exists and lists all pages
    FAIL: No sitemap.xml, or sitemap missing pages
    FIX: Generate sitemap.xml with all public pages, reference in robots.txt
```

## 5. Structured Data

```
[ ] JSON-LD present — at least one schema block
    FAIL: No <script type="application/ld+json"> on the page
    FIX: Add appropriate schema (see examples below)
    WHY: JSON-LD is the most reliable way for agents to extract structured facts

[ ] Schema type appropriate — matches page content
    FAIL: LocalBusiness schema on a blog post (should be Article)
    Common mappings:
      Homepage → Organization or LocalBusiness
      Service page → Service
      Blog post → Article or BlogPosting
      FAQ page → FAQPage
      Product page → Product
      Contact page → LocalBusiness (with contact info)

[ ] Meta description — present and meaningful
    FAIL: Missing, or generic ("Welcome to our website")
    FIX: 150-160 chars summarising what this specific page offers
    WHY: Agents use meta description as a page summary

[ ] Open Graph tags — og:title, og:description, og:type present
    FAIL: Missing OG tags
    FIX: Add at minimum og:title, og:description, og:type, og:url
    WHY: Social agents and preview generators depend on these

[ ] <title> descriptive — unique per page, not just site name
    FAIL: <title>My Website</title> on every page
    FIX: <title>Emergency Plumbing Services | My Website</title>
```

## 6. Accessibility Fundamentals

```
[ ] Contrast ratios — WCAG AA minimum
    Normal text: 4.5:1 ratio minimum
    Large text (18px+ bold or 24px+): 3:1 ratio minimum
    UI components and borders: 3:1 ratio minimum
    Check: Use browser dev tools or contrast checker

[ ] Focus styles visible — all interactive elements
    FAIL: outline: none with no replacement, or invisible focus ring
    FIX: Visible focus indicator (outline, box-shadow, or border change)
    Test: Tab through the entire page — can you always see where focus is?

[ ] Skip link — first focusable element
    FAIL: No skip link, or skip link target missing
    FIX:
      <a href="#main-content" class="skip-link">Skip to main content</a>
      ...
      <main id="main-content">

[ ] Form labels — every input has an associated label
    FAIL: <input type="email" placeholder="Email"> (placeholder is not a label)
    FIX: <label for="email">Email address</label><input id="email" type="email">
    Or: <input type="email" aria-label="Email address">

[ ] ARIA on interactive elements — toggles, icon buttons, dynamic content
    FAIL: <button><svg>...</svg></button> (no accessible name)
    FIX: <button aria-label="Open menu"><svg>...</svg></button>
    FAIL: Hamburger without aria-expanded
    FIX: <button aria-expanded="false" aria-controls="nav-menu">

[ ] Language declared — <html lang="...">
    FAIL: <html> with no lang attribute
    FIX: <html lang="en"> (or appropriate language code)

[ ] Keyboard navigable — all interactive elements reachable via Tab
    Test: Unplug the mouse. Can you do everything with keyboard?
    FAIL: Custom dropdowns, modals, or tabs not keyboard accessible
    FIX: Use native elements where possible; add tabindex and key handlers

[ ] Touch targets — minimum 44x44px
    FAIL: Small icon buttons, tight navigation links
    FIX: Ensure minimum size via padding if needed
    Test: Check at mobile viewport (375px)

[ ] No autoplay media — no auto-playing audio/video
    FAIL: <video autoplay> or background audio
    FIX: Remove autoplay or add muted + controls

[ ] Error identification — form errors linked to fields
    FAIL: Generic "There was an error" with no field association
    FIX: aria-describedby linking error message to input
    N/A if no forms on page
```

## 7. Bonus: Agent-Friendly Extras

```
[ ] RSS/Atom feed — available for content sites
    +5 if present: <link rel="alternate" type="application/rss+xml" href="/feed.xml">
    N/A for non-content sites

[ ] API endpoints documented — /api/ routes or OpenAPI spec
    +5 if present: Link to API docs or embedded OpenAPI spec
    N/A for static sites

[ ] robots.txt with sitemap reference
    +3 if present and references sitemap:
      Sitemap: https://example.com/sitemap.xml

[ ] Semantic class names — describe purpose not appearance
    +4 for consistent semantic naming:
      GOOD: .product-card, .service-list, .contact-form
      BAD: .blue-box, .left-col, .big-text

[ ] data-* attributes for state — interactive state in data attributes
    +3 for using data attributes:
      GOOD: <div data-status="open"> (agent can read state)
      BAD: State only in CSS classes like .is-open
```

## Quick Reference: Overlap Matrix

| Check | AI Nav | A11y | Both |
|-------|--------|------|------|
| Heading hierarchy | | | Both |
| Landmark regions | | | Both |
| Descriptive link text | | | Both |
| Image alt text | | | Both |
| Form labels | | | Both |
| ARIA attributes | | | Both |
| JSON-LD structured data | AI Nav | | |
| Meta/OG tags | AI Nav | | |
| Sitemap/canonical | AI Nav | | |
| Consistent nav | AI Nav | | |
| Contrast ratios | | A11y | |
| Focus styles | | A11y | |
| Skip link | | A11y | |
| Keyboard navigation | | A11y | |
| Touch targets | | A11y | |
