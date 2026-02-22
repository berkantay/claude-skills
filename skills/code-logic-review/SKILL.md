---
name: code-logic-review
description: "Review code for logic correctness, requirements fulfilment, maintainability, and engineering quality. Use when asked to review code, audit logic, check if code meets requirements, find refactoring opportunities, or assess code maintainability and extensibility."
---

# Code & Logic Review

Systematic review of code that goes beyond linting and structure. Evaluates whether code actually does what it's supposed to, follows good engineering practices, and is built to last.

This is not a style guide check. It's about correctness, intent, and craft.

## Prerequisites

Before starting any review, gather context:

1. **Read project docs** — Check for CLAUDE.md, README, PRD, specs, requirements docs, or issue descriptions that state what the code should do
2. **Identify the tech stack** — Framework, language version, key libraries, testing tools
3. **Understand the scope** — Is this a single file, a feature, a module, or the full codebase?

## Operating Modes

### Mode 1: Quick Review

**When**: User says "review this file", "check this function", "does this look right", or points at a specific file/component.

**Steps**:
1. Read the target file(s) completely
2. Identify the code's stated or implied purpose
3. Walk through the logic path by path — trace conditionals, loops, early returns, error branches
4. Check each dimension from the review checklist (load `references/review-checklist.md`)
5. Report findings inline using the short format (severity + file:line + finding + suggestion)

**Output**: Inline findings, grouped by severity. No separate report file unless asked.

### Mode 2: Full Audit

**When**: User says "audit the codebase", "full review", "review the project", or targets a large module/feature area.

**Steps**:
1. Map the codebase — identify entry points, core modules, shared utilities, data flow
2. Read project requirements/specs if they exist
3. Review each module systematically using the full checklist (`references/review-checklist.md`)
4. Cross-reference against requirements — flag gaps, partial implementations, dead code
5. Identify cross-cutting concerns: duplication across modules, inconsistent patterns, missing abstractions
6. Generate a structured report using `references/report-template.md`

**Output**: A review report file written to the project root or a location the user specifies.

### Mode 3: Requirements Check

**When**: User says "does this meet the requirements", "check against the spec", "verify the implementation", or provides a requirements document/issue to compare against.

**Steps**:
1. Read the requirements source (PRD, issue, spec doc, user description)
2. Extract a checklist of discrete requirements
3. For each requirement, trace through the code to verify it's implemented
4. Flag: fully met, partially met (with what's missing), not implemented, or implemented but divergent
5. Check for scope creep — code that does things not in the requirements
6. Report as a requirements traceability table

**Output**: Requirements matrix showing status of each requirement against the code.

## Review Dimensions

Each review evaluates these seven dimensions. See `references/review-checklist.md` for detailed criteria.

| Dimension | Core Question |
|---|---|
| **Logic correctness** | Do conditionals, loops, and state transitions produce the right outcomes for all inputs? |
| **Requirements fulfilment** | Does the code deliver what was asked for — no more, no less? |
| **Polymorphism & patterns** | Are OOP/functional patterns used where they reduce complexity, not just for show? |
| **Refactoring opportunities** | Is there duplication, unnecessary complexity, or code that could be simplified? |
| **Shared components & reuse** | Are common patterns extracted into reusable pieces? Is there copy-paste across modules? |
| **Commenting & documentation** | Do comments explain *why*, not *what*? Are complex algorithms documented? |
| **Maintainability & extensibility** | Can a new developer understand and extend this without archaeology? |

## Severity Levels

Use these consistently across all findings:

- **Critical** — Logic bug, data loss risk, security hole, or requirement not met. Must fix.
- **Major** — Significant maintainability issue, missing error handling, or pattern that will cause problems at scale. Should fix.
- **Minor** — Improvement opportunity, mild duplication, naming that could be clearer. Nice to fix.
- **Note** — Observation, suggestion, or positive callout. Not a problem.

## Autonomy Rules

**Do without asking**:
- Read any file in the project to understand context
- Load reference files from this skill
- Generate review findings and reports
- Highlight positive patterns (not just problems)

**Ask before doing**:
- Modifying any code (review is read-only by default)
- Creating fix branches or PRs
- Running tests or build commands (the user may have specific workflows)

**Always do**:
- Start with what the code does well before listing problems
- Tie findings to concrete file:line locations
- Provide actionable suggestions, not just complaints
- Consider the project's stage — a prototype doesn't need enterprise patterns

## Tips

- **Trace, don't skim**: Follow actual execution paths. The bug is in the path you didn't read.
- **Check the edges**: Empty arrays, null values, zero, negative numbers, unicode, concurrent access. Most logic errors live at boundaries.
- **Question the happy path**: Code that only works when everything goes right is code that doesn't work.
- **Look for what's missing**: The hardest bugs to spot are the things that should be there but aren't — missing validation, unhandled states, absent error recovery.
- **Respect context**: A 200-line script doesn't need dependency injection. A startup MVP doesn't need enterprise architecture. Match recommendations to the project's reality.

## Reference Files

| File | When to Load |
|---|---|
| `references/review-checklist.md` | Every review — detailed per-dimension checklist |
| `references/report-template.md` | Full Audit mode — structured report format |
