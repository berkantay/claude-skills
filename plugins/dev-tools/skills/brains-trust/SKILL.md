---
name: brains-trust
description: >
  Get a second opinion from leading AI models on code, architecture, strategy, prompting, or anything.
  Queries models via OpenRouter, Gemini, or OpenAI APIs. Supports single opinion, multi-model consensus,
  and devil's advocate patterns. Trigger with 'brains trust', 'second opinion', 'ask gemini', 'ask gpt',
  'peer review', 'consult', 'challenge this', or 'devil's advocate'.
triggers:
  - brains trust
  - second opinion
  - ask gemini
  - ask gpt
  - peer review
  - consult
  - challenge this
  - devil's advocate
  - what does gemini think
  - what does gpt think
user-invocable: true
argument-hint: "[question or topic]"
compatibility: claude-code-only
---

# Brains Trust

Consult other leading AI models for a second opinion. Not limited to code — works for architecture, strategy, prompting, debugging, writing, or any question where a fresh perspective helps.

## Setup

Set at least one API key as an environment variable:

```bash
# Recommended — one key covers all providers
export OPENROUTER_API_KEY="your-key"

# Optional — direct access (often faster/cheaper)
export GEMINI_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
```

OpenRouter is the universal path — one key gives access to Gemini, GPT, Qwen, DeepSeek, Llama, Mistral, and more.

## Current Models

**Do not use hardcoded model IDs.** Before every consultation, fetch the current leading models:

```
https://models.flared.au/llms.txt
```

This is a live-updated, curated list of ~40 leading models from 11 providers, filtered from OpenRouter's full catalogue. Use it to pick the right model for the task.

For programmatic use in the generated Python script: `https://models.flared.au/json`

## Consultation Patterns

| Pattern | When | What happens |
|---------|------|-------------|
| **Single** (default) | Quick second opinion | Ask one model, synthesise with your own view |
| **Consensus** | Important decision, want confidence | Ask 2-3 diverse models in parallel, compare where they agree/disagree |
| **Devil's advocate** | Challenge an assumption | Ask a model to explicitly argue against your current position |

For consensus, pick models from different providers (e.g. one Google, one OpenAI, one Qwen) for maximum diversity of perspective.

## Modes

| Mode | When | Model tier |
|------|------|-----------|
| Code Review | Review files for bugs, patterns, security | Flash |
| Architecture | Design decisions, trade-offs | Pro |
| Debug | Stuck after 2+ failed attempts | Flash |
| Security | Vulnerability scan | Pro |
| Strategy | Business, product, approach decisions | Pro |
| Prompting | Improve prompts, system prompts, KB files | Flash |
| General | Any question, brainstorm, challenge | Flash |

**Pro tier**: The most capable model from the chosen provider (e.g. `google/gemini-3.1-pro-preview`, `openai/gpt-5.4`).
**Flash tier**: Fast, cheaper models for straightforward analysis (e.g. `google/gemini-3-flash-preview`, `qwen/qwen3.5-flash-02-23`).

## Workflow

1. **Detect available keys** — check `OPENROUTER_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY` in environment. If none found, show setup instructions and stop.

2. **Fetch current models** — `WebFetch https://models.flared.au/llms.txt` and pick appropriate models based on mode (pro vs flash) and consultation pattern (single vs consensus). If user requested a specific provider ("ask gemini"), use that.

3. **Read target files** into context (if code-related). For non-code questions (strategy, prompting, general), skip file reading.

4. **Build prompt** using the AI-to-AI template from [references/prompt-templates.md](references/prompt-templates.md). Include file contents inline with `--- filename ---` separators. **Do not set output token limits** — let models reason fully.

5. **Write prompt to file** at `.claude/artifacts/brains-trust-prompt.txt` — never pass code inline via bash arguments (shell escaping breaks it).

6. **Generate and run Python script** at `.claude/scripts/brains-trust.py` using patterns from [references/provider-api-patterns.md](references/provider-api-patterns.md):
   - Reads prompt from `.claude/artifacts/brains-trust-prompt.txt`
   - Calls the selected API(s)
   - For consensus mode: calls multiple APIs in parallel using `concurrent.futures`
   - Saves each response to `.claude/artifacts/brains-trust-{model}.md`
   - Prints results to stdout

7. **Synthesise** — read the responses, present findings to the user. Note where models agree and disagree. Add your own perspective (agree/disagree with reasoning). Let the user decide what to act on.

## When to Use

**Good use cases**:
- Before committing major architectural changes
- When stuck debugging after multiple attempts
- Architecture decisions with multiple valid options
- Reviewing security-sensitive code
- Challenging your own assumptions on strategy or approach
- Improving system prompts or KB files
- Any time you want a fresh perspective

**Avoid using for**:
- Simple syntax checks (Claude handles these)
- Every single edit (too slow, costs money)
- Questions with obvious, well-known answers

## Critical Rules

1. **Never hardcode model IDs** — always fetch from `models.flared.au` first
2. **Never cap output tokens** — don't set `max_tokens` or `maxOutputTokens`
3. **Always write prompts to file** — never pass via bash arguments
4. **Include file contents inline** — attach code context directly in the prompt
5. **Use AI-to-AI framing** — the model is advising Claude, not talking to the human

## Reference Files

| When | Read |
|------|------|
| Building prompts for any mode | [references/prompt-templates.md](references/prompt-templates.md) |
| Generating the Python API call script | [references/provider-api-patterns.md](references/provider-api-patterns.md) |
