# Accessibility Check Criteria

Detailed evaluation criteria for the two audiences: human users and AI agents.

## Human Usability Checks

### 1. Horizontal Overflow
**How to check**: Look at the DOM snapshot for elements wider than the viewport width. Check for `overflow-x: scroll` on the body. In screenshots, look for content extending beyond the right edge.

**Common culprits**:
- Tables without responsive wrapper (`overflow-x: auto`)
- Images without `max-width: 100%`
- Preformatted code blocks without wrapping
- Fixed-width elements (px instead of %, vw, or clamp())
- Flexbox children without `min-width: 0` or `overflow: hidden`

**Severity**: High (forces horizontal scrolling, breaks layout)

### 2. Text Readability
**How to check**: In the DOM snapshot, look for computed font sizes below 12px. In screenshots, check for overlapping text, truncated labels, and text running outside containers.

**Common culprits**:
- Font size set in px without responsive scaling
- Long words without `overflow-wrap: break-word`
- Ellipsis truncation hiding critical content
- Low contrast text on background (check against WCAG 4.5:1 ratio)

**Severity**: High (content becomes inaccessible)

### 3. Touch Targets
**Applies to**: Widths below 768px (mobile/tablet)
**How to check**: In the DOM snapshot, look for interactive elements (buttons, links, inputs) and check their dimensions. Minimum 44x44px per WCAG 2.5.5.

**Common culprits**:
- Icon-only buttons without padding
- Inline text links in paragraphs
- Close (X) buttons that are too small
- Table row action buttons

**Severity**: Medium on tablet, High on mobile

### 4. CTA Visibility
**How to check**: In the above-the-fold screenshot, identify the primary call-to-action. If it requires scrolling to see, it fails.

**What counts as CTA**:
- Sign up / Register buttons
- Add to cart / Buy buttons
- Contact / Get started buttons
- The primary action the page is designed to drive

**Severity**: High (conversion impact)

### 5. Image Scaling
**How to check**: Look for images overflowing their containers in screenshots. In DOM, check for images without `max-width: 100%` or `object-fit`.

**Common culprits**:
- Hero images without responsive sizing
- Product images with fixed dimensions
- Background images without `background-size: cover/contain`
- SVGs without `viewBox` and explicit width

**Severity**: Medium (visual issue, content usually still accessible)

### 6. Navigation
**How to check**: At mobile widths, verify a hamburger menu or equivalent exists and is tappable. At desktop widths, verify all nav items are visible without wrapping.

**Common culprits**:
- Nav items wrapping to second line at medium widths
- Hamburger menu missing at mobile widths
- Dropdown submenus inaccessible on touch devices
- Active state not visible on current page

**Severity**: Critical if nav is inaccessible, Medium if it wraps

### 7. Stacking Order
**How to check**: On narrow viewports, content should stack vertically in a logical reading order. Compare the visual order (screenshot) to the DOM order (snapshot).

**Common culprits**:
- Sidebar appearing above main content on mobile
- Footer content appearing mid-page
- CSS `order` property creating confusing reflows
- Absolutely positioned elements overlapping

**Severity**: Medium (content still there, but order is confusing)

### 8. Whitespace
**How to check**: On wide viewports (1440+), look for excessive empty space around content. On narrow viewports, look for cramped elements with no breathing room.

**Common culprits**:
- Missing `max-width` on containers at large viewports
- Fixed margins/padding not scaling down for mobile
- Grid gaps too wide or too narrow at certain breakpoints

**Severity**: Low (aesthetic, not functional)

### 9. Sticky Elements
**How to check**: Scroll through the page and verify sticky headers/footers remain in position. Check they don't overlap content or cover interactive elements.

**Common culprits**:
- Sticky header covering content below it (missing scroll offset)
- Multiple sticky elements stacking and eating viewport space on mobile
- Sticky footer hiding bottom-of-page content
- z-index issues with sticky elements and modals

**Severity**: High if content is hidden behind sticky elements

### 10. Content Priority
**How to check**: On mobile, the most important content should appear first (near top of page). Compare what's above the fold at 320px vs 1440px.

**Common culprits**:
- Promotional banners pushing main content down on mobile
- Cookie consent banners covering significant viewport area
- Sidebar content appearing before main content
- Hero images taking full viewport height with no content visible

**Severity**: Medium (content is there but buried)

## AI Agent Accessibility Checks

### 1. Semantic HTML
**How to check**: In the DOM snapshot, verify presence of landmark elements.

**Required landmarks**:
- `<nav>` -- at least one navigation region
- `<main>` -- exactly one main content area
- `<footer>` -- page footer
- `<header>` -- page header
- `<aside>` -- for sidebar/complementary content (if present)

**Why it matters for agents**: Agents use landmarks to understand page structure and navigate directly to content regions without visual parsing.

### 2. Labelled Inputs
**How to check**: Every `<input>`, `<select>`, and `<textarea>` must have one of:
- Associated `<label>` element (via `for` attribute)
- `aria-label` attribute
- `aria-labelledby` attribute
- Wrapping `<label>` element

**Why it matters for agents**: Agents identify form fields by their labels. Unlabelled inputs are invisible or ambiguous to automated interaction.

### 3. ARIA Roles
**How to check**: Interactive custom elements should have appropriate roles:
- Custom buttons: `role="button"`
- Tab interfaces: `role="tablist"`, `role="tab"`, `role="tabpanel"`
- Modals/dialogs: `role="dialog"` with `aria-modal="true"`
- Expandable sections: `aria-expanded` on triggers

**Why it matters for agents**: Native HTML elements carry implicit roles. Custom elements without explicit roles are opaque to agents.

### 4. Heading Hierarchy
**How to check**: Headings should follow a logical order: h1 > h2 > h3. No skipped levels (h1 > h3). Exactly one h1 per page.

**Why it matters for agents**: Agents use heading hierarchy to build a mental model of page structure, similar to a table of contents.

### 5. Link Text
**How to check**: Links should have descriptive text content. Flag:
- "Click here"
- "Read more"
- "Learn more" (without context)
- Empty links (icon-only without aria-label)

**Why it matters for agents**: Agents decide which links to follow based on link text. Generic text provides no signal.

### 6. Alt Text
**How to check**: All `<img>` elements should have `alt` attributes. Decorative images should have `alt=""`. Informational images should have descriptive alt text.

**Why it matters for agents**: Agents that can't process images rely on alt text to understand visual content.

### 7. DOM Navigability
**How to check**: Content should be reachable via standard DOM traversal. Flag:
- Content rendered only via CSS (`content:` property with meaningful text)
- Text embedded in images without alt text
- Content only accessible via JavaScript interaction (hover-only tooltips)
- iframes without titles

**Why it matters for agents**: Agents traverse the DOM tree. Content outside the DOM is invisible.

### 8. Data Attributes
**How to check**: Structured data should use semantic markup:
- Tables: `<th>` with `scope="col"` or `scope="row"`
- Lists: `<ul>`/`<ol>` with `<li>` (not divs styled as lists)
- Definitions: `<dl>` for key-value pairs

**Why it matters for agents**: Semantic data markup enables agents to extract and understand structured information (table columns, list items, definitions).

### 9. Focus Indicators
**How to check**: Tab through interactive elements and verify visible focus styles. Check that `outline: none` isn't used without a replacement style.

**Why it matters for agents**: While agents don't "see" focus rings, focus order determines keyboard/programmatic navigation sequence. Proper focus management indicates well-structured interactivity.

### 10. Skip Links
**How to check**: Look for a "Skip to main content" or equivalent link as the first focusable element in the DOM.

**Why it matters for agents**: Skip links signal content structure and allow agents to bypass repetitive navigation blocks, just as they help keyboard users.

## Viewport-Specific Check Priorities

Not all checks matter equally at every breakpoint:

| Check | Mobile (320-375) | Tablet (768-1024) | Desktop (1280+) |
|-------|:-:|:-:|:-:|
| Touch targets | **Critical** | Important | N/A |
| Horizontal overflow | **Critical** | **Critical** | Important |
| Navigation | **Critical** | **Critical** | Important |
| Stacking order | **Critical** | Important | N/A |
| Text readability | **Critical** | Important | Important |
| Whitespace | Low | Medium | **Important** |
| Content priority | **Critical** | Important | Low |
| Image scaling | Important | Important | Important |
| Semantic HTML | Same priority across all widths |
| ARIA / Labels | Same priority across all widths |
