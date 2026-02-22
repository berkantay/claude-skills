---
name: responsiveness-check
description: "Test web page responsiveness across breakpoints using Playwright. Screenshots pages at standard device widths (320-2560px) or sweeps every 160px to catch transitional layout breaks. Checks above-the-fold and scrolled content. Validates for both human usability and AI agent accessibility. Trigger with 'responsiveness check', 'check responsive', 'breakpoint test', 'viewport test', or 'responsive sweep'."
compatibility: claude-code-only
---

# Responsiveness Check

Systematically test web pages across viewport widths to catch layout breaks, overflow issues, and responsiveness gaps. Uses Playwright for browser automation with parallel sub-agents for speed.

## Browser Tool Detection

Before starting, detect available browser tools:

1. **Playwright MCP** (`mcp__plugin_playwright_playwright__*`) -- preferred, supports resize natively.
2. **playwright-cli** -- for scripted flows and sub-agent tasks.
3. **Chrome MCP** (`mcp__claude-in-chrome__*`) -- works but single-session, no parallelism.

If none are available, inform the user and suggest installing Playwright.

See [references/breakpoints.md](references/breakpoints.md) for breakpoint definitions and device context.

## Operating Modes

### Mode 1: Standard Check

**When**: "responsiveness check", "check responsive", "breakpoint test", "viewport test"

Tests 8 key breakpoints that cover real device boundaries plus the in-between widths where layouts commonly break.

**Breakpoints**: 320, 375, 768, 1024, 1280, 1440, 1920, 2560

**Process**:

1. **Collect URLs** -- ask the user for the URL(s) or route(s) to test. Accept a single URL, a comma-separated list, or a sitemap path.
2. **Launch parallel sub-agents** -- one per breakpoint. Each sub-agent:
   a. Opens a Playwright session (`playwright-cli -s=bp-{width} open {url}`)
   b. Resizes to `{width} x 900`
   c. **Above-the-fold check** -- screenshot + DOM snapshot at initial scroll position
   d. **Scroll check** -- scroll to bottom in 1-viewport increments, screenshot at each stop if layout changes are detected
   e. Runs the check matrix (see below)
   f. Closes session
3. **Merge results** -- collect all sub-agent findings into a single report
4. **Write report** to `docs/responsiveness-check-YYYY-MM-DD.md` using [references/report-template.md](references/report-template.md)

### Mode 2: Sweep

**When**: "responsive sweep", "sweep breakpoints", "check every viewport", "full sweep"

Tests every 160px from 320 to 2560 -- that's 15 viewports. Catches the transitional layout breaks that happen between standard breakpoints (e.g., content that wraps awkwardly at 1100px).

**Breakpoints**: 320, 480, 640, 800, 960, 1120, 1280, 1440, 1600, 1760, 1920, 2080, 2240, 2400, 2560

**Process**: Same as Standard Check but with 15 breakpoints. Sub-agents still run in parallel. Best for pages with complex layouts (dashboards, multi-column content, data tables).

### Mode 3: Targeted Range

**When**: "check between 768 and 1024", "test tablet breakpoints", "sweep from X to Y"

Tests a user-specified range at 160px increments. Useful when you already know roughly where a layout breaks and want to pinpoint it.

**Process**: Same parallel sub-agent approach, scoped to the requested range.

## Check Matrix

At every breakpoint, evaluate both audiences. See [references/accessibility-checks.md](references/accessibility-checks.md) for detailed criteria.

### Human Usability

| Check | What to look for |
|-------|-----------------|
| Horizontal overflow | Content wider than viewport causing horizontal scroll |
| Text readability | Truncated text, overlapping text, unreadable font sizes (< 12px) |
| Touch targets | Interactive elements smaller than 44x44px on mobile widths (< 768px) |
| CTA visibility | Primary call-to-action visible above the fold |
| Image scaling | Images overflowing containers or distorting aspect ratio |
| Navigation | Menu accessible and usable (hamburger on mobile, full on desktop) |
| Stacking order | Content stacking logically on narrow viewports |
| Whitespace | Excessive empty space or cramped content |
| Sticky elements | Headers/footers behaving correctly during scroll |
| Content priority | Most important content visible first on smaller viewports |

### AI Agent Accessibility

| Check | What to look for |
|-------|-----------------|
| Semantic HTML | Proper use of landmarks (`nav`, `main`, `aside`, `footer`) |
| Labelled inputs | All form inputs have associated `label` or `aria-label` |
| ARIA roles | Interactive elements have appropriate roles |
| Heading hierarchy | Logical h1-h6 structure, no skipped levels |
| Link text | Descriptive link text (not "click here") |
| Alt text | Images have meaningful alt attributes |
| DOM navigability | Content reachable via standard DOM traversal |
| Data attributes | Tables use `th` with scope, lists use semantic `ul`/`ol` |
| Focus indicators | Visible focus styles on interactive elements |
| Skip links | Skip-to-content link present for keyboard/agent navigation |

## Scroll Position Checks

At each breakpoint, check two scroll states:

### Above the Fold
- Hero/header layout intact
- Navigation visible and functional
- Primary CTA visible without scrolling
- No content clipping at viewport edge
- Logo and branding elements properly positioned

### Scrolled Content
- Sticky header remains visible and doesn't overlap content
- Content reflows correctly as user scrolls
- Lazy-loaded images appear without layout shift
- Footer renders completely
- No orphaned elements (single words on a line, isolated buttons)
- Infinite scroll or pagination works at all widths
- Back-to-top controls visible on long pages

## Parallelisation Strategy

This skill is designed for maximum use of sub-agents:

```
Main agent
├── Sub-agent: 320px  ─┐
├── Sub-agent: 375px   │
├── Sub-agent: 768px   │  All run concurrently
├── Sub-agent: 1024px  │  Each has its own Playwright session
├── Sub-agent: 1280px  │  Named session: -s=bp-{width}
├── Sub-agent: 1440px  │
├── Sub-agent: 1920px  │
└── Sub-agent: 2560px ─┘
         │
         ▼
    Merge results into single report
```

Each sub-agent receives:
- The URL to test
- The viewport width to use
- The check matrix to evaluate
- Instructions to screenshot and return findings

The main agent collects all results and produces the final report.

**For sweep mode** (15 breakpoints), launch all 15 sub-agents concurrently. Playwright handles separate sessions cleanly.

## Sub-Agent Prompt Template

When launching each breakpoint sub-agent, use this structure:

```
Test {url} at viewport width {width}px.

1. Open: playwright-cli -s=bp-{width} open {url}
2. Resize: playwright-cli -s=bp-{width} resize {width} 900
3. Screenshot above-the-fold: playwright-cli -s=bp-{width} screenshot --filename=resp-{width}-above.png
4. Get DOM snapshot: playwright-cli -s=bp-{width} snapshot
5. Evaluate the check matrix against the snapshot and screenshot
6. Scroll down one viewport height, screenshot again if layout changes
7. Continue scrolling until page bottom, noting any scroll-related issues
8. Close: playwright-cli -s=bp-{width} close

Return a structured finding for this breakpoint:
- Width tested
- Above-the-fold issues (list)
- Scroll issues (list)
- Human usability issues (list with severity)
- AI agent accessibility issues (list with severity)
- Screenshot filenames captured
```

## Severity Levels

- **Critical** -- layout completely broken, content inaccessible or unusable
- **High** -- significant usability problem (horizontal scroll, overlapping content, hidden CTA)
- **Medium** -- noticeable but not blocking (awkward wrapping, excessive whitespace, minor overflow)
- **Low** -- polish items (alignment, spacing inconsistencies, minor visual issues)

## Autonomy Rules

- **Just do it**: Take screenshots, resize viewports, read DOM snapshots, analyse layout
- **Brief confirmation**: Before starting a full sweep (15 viewports), before writing report files
- **Ask first**: Before interacting with forms or clicking destructive actions on the page

## Tips

- Start with Standard mode. Only sweep when you see something suspicious between breakpoints.
- Pay special attention to the 768-1024 range -- this is where most desktop-to-tablet transitions break.
- The 1280-1440 range catches issues on smaller laptops that designers on 27" monitors miss.
- For SPAs, wait for client-side rendering to complete before screenshotting.
- If a page has multiple sections with different layouts, scroll through the full page at each breakpoint.
- Compare screenshots side-by-side in the report -- a visual diff catches issues faster than text descriptions.

## Reference Files

| When | Read |
|------|------|
| Understanding breakpoint rationale | [references/breakpoints.md](references/breakpoints.md) |
| Writing the responsiveness report | [references/report-template.md](references/report-template.md) |
| Detailed check criteria | [references/accessibility-checks.md](references/accessibility-checks.md) |
