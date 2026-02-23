---
name: gemini-peer-review
description: "Get a second opinion from Gemini on code, architecture, debugging, or security. Calls the Gemini API directly — no external tools needed. Trigger with 'ask gemini', 'gemini review', 'second opinion', 'peer review', or 'consult gemini'."
compatibility: claude-code-only
---

# Gemini Peer Review

Consult Gemini as a coding peer for a second opinion on code quality, architecture decisions, debugging, or security reviews. Calls the Gemini API directly via `curl` — no CLI tools or wrappers required.

## Prerequisites

- A Gemini API key set as `GEMINI_API_KEY` or `GOOGLE_API_KEY` environment variable
- Get one at https://aistudio.google.com/apikey if needed

## How It Works

1. Claude reads the relevant code/context
2. Constructs an AI-to-AI prompt (see [prompt templates](references/prompt-templates.md))
3. Calls the Gemini REST API directly via `curl`
4. Parses the response and presents findings with Claude's own perspective

## API Call Pattern

Resolve the API key, select the model, and call the API:

```bash
# Resolve API key
API_KEY="${GEMINI_API_KEY:-$GOOGLE_API_KEY}"

# Select model (flash for speed, pro for complex reasoning)
MODEL="gemini-2.5-flash"  # or gemini-2.5-pro for architecture/security

# Make the API call
curl -s "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg prompt "$PROMPT" '{
    "contents": [{"parts": [{"text": $prompt}]}],
    "generationConfig": {"temperature": 0.2, "maxOutputTokens": 8192}
  }')"
```

Parse the response text from: `.candidates[0].content.parts[0].text`

```bash
echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text'
```

If jq is not available, use python3:

```bash
python3 -c "import json,sys; r=json.load(sys.stdin); print(r['candidates'][0]['content']['parts'][0]['text'])" <<< "$RESPONSE"
```

## Modes

### Code Review

Review specific files for bugs, logic errors, security vulnerabilities, performance issues, and best practice violations.

**Model**: gemini-2.5-flash
**Context**: Read the target files and include their full contents in the prompt.

### Architecture Advice

Get feedback on design decisions with trade-off analysis.

**Model**: gemini-2.5-pro
**Context**: Include project structure, relevant config files, and the specific question.

### Debugging Help

Analyse errors when stuck after 2+ failed fix attempts. Gemini sees the code fresh without your debugging context bias.

**Model**: gemini-2.5-flash
**Context**: Include the problematic file(s), error messages, and what was already tried.

### Security Scan

Scan code for security vulnerabilities (injection, auth bypass, data exposure).

**Model**: gemini-2.5-pro
**Context**: Include all files in the target directory/path.

### Quick Question

Fast question without file context.

**Model**: gemini-2.5-flash
**Context**: Just the question text.

### Project Review

Full project analysis using Gemini's large context window.

**Model**: gemini-2.5-pro
**Context**: Include project structure and key source files.

## Workflow

1. **Check API key**: Verify `GEMINI_API_KEY` or `GOOGLE_API_KEY` is set. If not, ask the user to set it.
2. **Gather context**: Read the relevant files based on the mode.
3. **Build prompt**: Use the AI-to-AI prompt template from [references/prompt-templates.md](references/prompt-templates.md). Include file contents directly in the prompt.
4. **Select model**: Use flash for reviews/debugging/quick questions, pro for architecture/security/project reviews.
5. **Call the API**: Use the curl pattern above. Use `jq` to build the JSON payload (handles escaping of code content).
6. **Parse response**: Extract text from the JSON response.
7. **Present findings**: Show Gemini's analysis, add your own perspective (agree/disagree), and let the user decide what to implement.

## When to Use

**Good use cases**:
- Before committing major changes (final review)
- When stuck debugging after multiple attempts
- Architecture decisions with multiple valid options
- Security-sensitive code review
- "What am I missing?" moments

**Avoid using for**:
- Simple syntax checks (Claude handles these faster)
- Every single edit (too slow, unnecessary)
- Questions with obvious answers

## Model Selection

| Mode | Model | Use When |
|------|-------|----------|
| review, debug, quick | gemini-2.5-flash | Default for most tasks |
| architect, security-scan, project-review | gemini-2.5-pro | Complex reasoning needed |

Override by setting `GEMINI_MODEL` env var — if set, use that model for all modes.

## Error Handling

- **No API key**: Tell the user to set `GEMINI_API_KEY` or `GOOGLE_API_KEY`
- **401/403**: API key is invalid or expired
- **429**: Rate limited — wait a moment and retry
- **Empty response**: Check that the prompt isn't being blocked by safety filters — simplify if needed

## Reference Files

| When | Read |
|------|------|
| AI-to-AI prompt templates, model details | [references/prompt-templates.md](references/prompt-templates.md) |
