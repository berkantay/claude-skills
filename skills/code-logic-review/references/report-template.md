# Code & Logic Review Report Template

Use this template when generating a Full Audit report. Write the report as a markdown file in the project.

---

```markdown
# Code & Logic Review Report

**Project**: [project name]
**Date**: [YYYY-MM-DD]
**Scope**: [what was reviewed — full codebase / specific module / feature area]
**Tech Stack**: [language, framework, key libraries]

---

## Executive Summary

[2-3 sentences: overall health of the codebase, biggest strengths, biggest risks. Written for someone who won't read the full report.]

**Overall Assessment**: [Solid / Needs Attention / Significant Concerns]

---

## What's Done Well

[Start positive. List 3-5 things the codebase does right. Be specific — "good separation of API routes from business logic in src/services/" not just "good structure".]

- ...
- ...
- ...

---

## Findings

### Critical

[Must-fix issues: logic bugs, data loss risks, security holes, unmet requirements.]

| # | Location | Finding | Recommendation |
|---|----------|---------|----------------|
| C1 | `file:line` | Description of the issue | What to do about it |

### Major

[Should-fix issues: significant maintainability problems, missing error handling, patterns that will cause problems at scale.]

| # | Location | Finding | Recommendation |
|---|----------|---------|----------------|
| M1 | `file:line` | Description of the issue | What to do about it |

### Minor

[Nice-to-fix: improvement opportunities, mild duplication, naming that could be clearer.]

| # | Location | Finding | Recommendation |
|---|----------|---------|----------------|
| m1 | `file:line` | Description of the issue | What to do about it |

---

## Requirements Coverage

[Include this section when requirements/specs are available. Remove if no requirements were provided.]

| Requirement | Status | Implementation | Notes |
|-------------|--------|---------------|-------|
| [requirement text] | Met / Partial / Not Met / Divergent | `file:line` or module | [what's missing or different] |

---

## Dimension Summary

| Dimension | Rating | Key Observations |
|-----------|--------|-----------------|
| Logic Correctness | Strong / Adequate / Weak | [1 sentence] |
| Requirements Fulfilment | Strong / Adequate / Weak | [1 sentence] |
| Polymorphism & Patterns | Strong / Adequate / Weak | [1 sentence] |
| Refactoring Opportunities | Few / Moderate / Many | [1 sentence] |
| Shared Components & Reuse | Strong / Adequate / Weak | [1 sentence] |
| Commenting & Documentation | Strong / Adequate / Weak | [1 sentence] |
| Maintainability & Extensibility | Strong / Adequate / Weak | [1 sentence] |

---

## Recommended Actions

[Prioritised list of what to tackle first. Group by effort level.]

### Quick Wins (< 1 hour each)
1. ...

### Medium Effort (hours)
1. ...

### Larger Refactors (days)
1. ...

---

## Scope & Limitations

[What was and wasn't reviewed. Any areas that were skipped and why. Anything that needs deeper investigation.]

- Reviewed: ...
- Not reviewed: ...
- Needs further investigation: ...
```

---

## Usage Notes

- **Be specific**: Every finding must reference a file and line number. "The error handling could be better" is not a finding.
- **Be actionable**: Every finding must include what to do about it. "This is duplicated" becomes "Extract into a shared utility in `src/utils/validation.ts`".
- **Be proportionate**: A 500-line script gets a shorter report than a 50-file application. Scale the report to the codebase.
- **Start positive**: The "What's Done Well" section isn't filler — it builds trust and identifies patterns to preserve.
- **Cut empty sections**: If there are no Critical findings, remove the Critical table. Don't write "None found" for every empty section.
