# Code & Logic Review Checklist

Use this checklist systematically during reviews. Not every item applies to every codebase — skip what's irrelevant to the tech stack or project stage.

---

## 1. Logic Correctness

### Control Flow
- [ ] Conditionals cover all expected cases (no missing else/default branches)
- [ ] Switch/match statements handle all variants and have sensible defaults
- [ ] Loops terminate correctly — no off-by-one, no infinite loops on edge inputs
- [ ] Early returns and guard clauses are used consistently (not mixed with deep nesting)
- [ ] Negation logic is correct — double negatives, inverted conditions, `!==` vs `!=`

### State Management
- [ ] State transitions are valid — no impossible states, no orphaned states
- [ ] Initialisation is correct — variables aren't used before being set
- [ ] Mutable state is modified in predictable order — no race conditions in async code
- [ ] Derived state is recalculated when source state changes
- [ ] State cleanup happens — subscriptions unsubscribed, timers cleared, connections closed

### Data Handling
- [ ] Null/undefined/empty checks are present where data can be absent
- [ ] Array operations handle empty arrays without throwing
- [ ] Type coercion is intentional, not accidental (especially in JS/TS/Python)
- [ ] Numeric operations handle zero, negative, overflow, and floating-point precision
- [ ] String operations handle unicode, empty strings, and whitespace correctly
- [ ] Date/time handling accounts for timezones, DST, and edge dates

### Error Paths
- [ ] Errors are caught at appropriate boundaries (not swallowed, not over-caught)
- [ ] Error messages are useful — they say what went wrong and what to do about it
- [ ] Async errors are handled (unhandled promise rejections, missing try/catch in async)
- [ ] Partial failure is handled — what happens when step 3 of 5 fails?
- [ ] Recovery logic actually recovers (retry doesn't retry the same broken thing forever)

---

## 2. Requirements Fulfilment

### Coverage
- [ ] Each stated requirement has corresponding implementation
- [ ] Acceptance criteria (if defined) are testable in the code
- [ ] Edge cases mentioned in requirements are handled
- [ ] No gold-plating — features not in requirements are either justified or removed

### Completeness
- [ ] Forms validate all required fields with appropriate rules
- [ ] CRUD operations cover create, read, update, AND delete (not just create/read)
- [ ] User-facing messages match requirements (labels, error text, confirmations)
- [ ] Permissions/authorisation checks match the access control requirements
- [ ] Data persistence matches requirements (what's saved, what's transient)

### Behavioural Accuracy
- [ ] Business rules are implemented as specified, not approximated
- [ ] Calculations produce correct results (verify with example inputs from requirements)
- [ ] Sorting, filtering, and search behave as specified
- [ ] Pagination, limits, and thresholds match requirements
- [ ] Integrations send/receive the correct data format

---

## 3. Polymorphism & Design Patterns

### Appropriate Use
- [ ] Inheritance is used for genuine "is-a" relationships, not just code sharing
- [ ] Composition is preferred over inheritance where it simplifies things
- [ ] Interfaces/protocols define contracts where multiple implementations exist
- [ ] Abstract classes aren't overused — a single implementation doesn't need an abstraction
- [ ] Generic/template types are used where they prevent duplication without hurting readability

### Pattern Application
- [ ] Design patterns solve actual problems (not applied for resume-driven development)
- [ ] Strategy/command patterns are used where behaviour varies by type (instead of switch chains)
- [ ] Observer/event patterns are used where loose coupling between components matters
- [ ] Factory patterns are justified — is construction actually complex enough to warrant them?
- [ ] Patterns are implemented correctly (not cargo-culted half-implementations)

### Anti-Patterns
- [ ] No God objects/classes that do everything
- [ ] No feature envy — methods that use another class's data more than their own
- [ ] No shotgun surgery — a single change shouldn't require touching 10+ files
- [ ] No speculative generality — abstractions exist for current needs, not hypothetical futures

---

## 4. Refactoring Opportunities

### Duplication
- [ ] No copy-pasted blocks with minor variations (extract and parameterise)
- [ ] Similar logic across files is consolidated into shared functions/utilities
- [ ] Repeated conditional patterns are replaced with data-driven approaches or lookup tables
- [ ] Test setup code is shared where appropriate (fixtures, factories, helpers)

### Complexity
- [ ] Functions/methods do one thing (under ~40 lines as a guideline, not a rule)
- [ ] Nesting depth is manageable (generally ≤3 levels of indentation)
- [ ] Complex boolean expressions are extracted into named variables or functions
- [ ] Long parameter lists are replaced with option objects or builder patterns
- [ ] Cyclomatic complexity is reasonable — too many branches means too many responsibilities

### Naming
- [ ] Names reveal intent — `getUserPermissions()` not `getData()`
- [ ] Boolean variables/functions read as questions — `isValid`, `hasPermission`, `canEdit`
- [ ] Consistent vocabulary — don't use "user", "account", "member" for the same concept
- [ ] No misleading names — `processItems()` that also saves and sends email
- [ ] Abbreviations are avoided unless domain-standard (`url`, `id`, `api` are fine)

### Dead Code
- [ ] No commented-out code blocks left in production code
- [ ] No unused imports, variables, functions, or parameters
- [ ] No unreachable code after returns/throws
- [ ] No feature flags for features that shipped long ago
- [ ] No TODO/FIXME comments older than the current sprint without a tracking issue

---

## 5. Shared Components & Reuse

### Component Design
- [ ] Reusable UI components accept props/parameters rather than hardcoding values
- [ ] Shared components have clear, minimal interfaces
- [ ] Components don't make assumptions about their parent/context
- [ ] Utility functions are pure where possible (same input = same output)
- [ ] Shared code lives in a sensible location (utils/, shared/, lib/, common/)

### Library Usage
- [ ] Dependencies are used for their intended purpose (not importing lodash for one function)
- [ ] Framework features are used instead of reinventing them (routing, state management, validation)
- [ ] Third-party libraries are at reasonable versions (not wildly outdated or bleeding-edge)
- [ ] No duplicate libraries solving the same problem (e.g., moment AND dayjs AND date-fns)
- [ ] Heavy libraries are justified — is the full library needed or just a small utility?

### API & Interface Design
- [ ] Internal APIs are consistent in naming, parameter order, and return types
- [ ] Error contracts are consistent — same kind of error, same shape of response
- [ ] Module boundaries are clear — no circular dependencies
- [ ] Public vs private is intentional — only expose what consumers need
- [ ] Breaking changes to shared interfaces are coordinated across consumers

---

## 6. Commenting & Documentation

### Comment Quality
- [ ] Comments explain *why*, not *what* (the code shows what, comments show intent)
- [ ] Complex algorithms have a brief explanation or link to reference material
- [ ] Business rules in code reference their source (ticket, spec, regulation)
- [ ] Workarounds and hacks are documented with context on why they exist
- [ ] No stale comments that contradict the current code

### Self-Documenting Code
- [ ] Function signatures communicate purpose through names and types
- [ ] Constants are named, not magic numbers/strings (`MAX_RETRIES` not `3`)
- [ ] Enums/constants define valid values rather than raw strings throughout the code
- [ ] Complex data structures have type definitions (TypeScript interfaces, Python dataclasses, etc.)
- [ ] Public API functions have doc comments describing parameters, returns, and throws

### Missing Documentation
- [ ] Non-obvious configuration is documented (env vars, feature flags, thresholds)
- [ ] Integration points document the expected contract (API shapes, webhook payloads)
- [ ] Deployment or build steps that aren't standard are documented
- [ ] Known limitations or constraints are noted where relevant

---

## 7. Maintainability & Extensibility

### Readability
- [ ] Code reads top-to-bottom without jumping around to understand flow
- [ ] Related code is co-located (not spread across distant files for "organisation")
- [ ] Consistent code style within the project (formatting, naming conventions, file structure)
- [ ] Test names describe the behaviour being tested, not the implementation

### Changeability
- [ ] Adding a new variant/type doesn't require modifying existing code in many places
- [ ] Configuration is externalised where it varies by environment
- [ ] Feature additions have clear extension points (add a new handler, not modify a switch)
- [ ] Database schema supports likely future changes (nullable fields, junction tables, etc.)

### Testability
- [ ] Dependencies are injectable (not hardcoded global singletons)
- [ ] Side effects are isolated at boundaries (not scattered throughout business logic)
- [ ] Functions return values rather than mutating external state where possible
- [ ] Code under test doesn't require complex setup or mocking infrastructure
- [ ] Test coverage exists for critical paths and non-obvious edge cases

### Operational Readiness
- [ ] Logging exists at key decision points (not just errors, also important state changes)
- [ ] Monitoring hooks are present for critical operations (latency, error rates, queue depth)
- [ ] Graceful degradation is implemented where external dependencies can fail
- [ ] Configuration changes don't require code changes and redeployment
