# Responsiveness Report Template

Use this template when writing the final report to `docs/responsiveness-check-YYYY-MM-DD.md`.

---

```markdown
# Responsiveness Check Report

**URL**: {url}
**Date**: {YYYY-MM-DD}
**Mode**: {Standard / Sweep / Targeted Range}
**Breakpoints tested**: {list of widths}

## Summary

| Breakpoint | Status | Critical | High | Medium | Low |
|-----------|--------|----------|------|--------|-----|
| 320px | {Pass/Fail} | {n} | {n} | {n} | {n} |
| 375px | {Pass/Fail} | {n} | {n} | {n} | {n} |
| ... | | | | | |

**Overall**: {Pass / Fail — N issues found across M breakpoints}

## Critical Issues

{List any Critical severity issues first, with breakpoint, description, and screenshot reference}

### {Issue title}
- **Breakpoint**: {width}px
- **Scroll position**: {Above the fold / Scrolled — Npx from top}
- **Severity**: Critical
- **Description**: {What's broken}
- **Screenshot**: {filename}
- **Recommendation**: {How to fix}

## Breakpoint Details

### 320px — Mobile S

**Above the fold**:
- {Finding or "No issues"}

**Scrolled content**:
- {Finding or "No issues"}

**Human usability**:
| Check | Status | Notes |
|-------|--------|-------|
| Horizontal overflow | Pass/Fail | {details} |
| Text readability | Pass/Fail | {details} |
| Touch targets | Pass/Fail | {details} |
| CTA visibility | Pass/Fail | {details} |
| Image scaling | Pass/Fail | {details} |
| Navigation | Pass/Fail | {details} |
| Stacking order | Pass/Fail | {details} |
| Whitespace | Pass/Fail | {details} |
| Sticky elements | Pass/Fail | {details} |
| Content priority | Pass/Fail | {details} |

**AI agent accessibility**:
| Check | Status | Notes |
|-------|--------|-------|
| Semantic HTML | Pass/Fail | {details} |
| Labelled inputs | Pass/Fail | {details} |
| ARIA roles | Pass/Fail | {details} |
| Heading hierarchy | Pass/Fail | {details} |
| Link text | Pass/Fail | {details} |
| Alt text | Pass/Fail | {details} |
| DOM navigability | Pass/Fail | {details} |
| Data attributes | Pass/Fail | {details} |
| Focus indicators | Pass/Fail | {details} |
| Skip links | Pass/Fail | {details} |

**Screenshots**: resp-320-above.png, resp-320-scroll-1.png

{Repeat ### block for each breakpoint tested}

## Transition Analysis

{Only for Sweep and Targeted Range modes}

Comparing adjacent breakpoints to identify where layout transitions occur:

| Transition | What changes | Clean? | Notes |
|-----------|-------------|--------|-------|
| 320 → 480 | {description} | Yes/No | {details} |
| 480 → 640 | {description} | Yes/No | {details} |
| ... | | | |

## Recommendations

### Immediate (Critical + High)
1. {Recommendation with affected breakpoints}

### Should Fix (Medium)
1. {Recommendation}

### Nice to Have (Low)
1. {Recommendation}

## Screenshots

All screenshots saved to: `{screenshot_directory}/`

| Filename | Breakpoint | Scroll Position | Notes |
|----------|-----------|----------------|-------|
| resp-320-above.png | 320px | Above fold | {notes} |
| resp-320-scroll-1.png | 320px | 900px | {notes} |
| ... | | | |
```

---

## Notes for Claude

- **Always include the summary table** at the top -- this is the first thing people look at.
- **Critical issues get their own section** before the breakpoint details.
- **Only include the Transition Analysis section** for Sweep and Targeted Range modes.
- **Screenshots**: Use consistent naming: `resp-{width}-above.png`, `resp-{width}-scroll-{n}.png`
- **Be specific** in recommendations -- reference CSS properties, elements, and exact breakpoints.
- **Pass means no issues** at that breakpoint. Fail means at least one Medium+ severity issue.
