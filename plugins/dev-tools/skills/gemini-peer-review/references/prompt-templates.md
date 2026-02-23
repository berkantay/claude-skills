# Prompt Templates

## AI-to-AI Prompting Format

Always use this format when constructing prompts for Gemini. It prevents role confusion — Gemini knows it's advising Claude Code, not talking to the human.

```
[Claude Code consulting Gemini for peer review]

Task: [Specific task description]

[File contents or context]

Provide direct analysis with file:line references. I will synthesize your findings with mine before presenting to the developer.
```

## Constructing the API Call

For every mode, follow this pattern:

1. Read the relevant files into a shell variable or construct the prompt string
2. Use `jq` to safely encode the prompt (handles special characters in code)
3. Call the API and extract the response

```bash
API_KEY="${GEMINI_API_KEY:-$GOOGLE_API_KEY}"
MODEL="gemini-2.5-flash"  # or gemini-2.5-pro

RESPONSE=$(curl -s "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg prompt "$PROMPT" '{
    "contents": [{"parts": [{"text": $prompt}]}],
    "generationConfig": {"temperature": 0.2, "maxOutputTokens": 8192}
  }')")

# Extract the text
RESULT=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text // "No response received"')
echo "$RESULT"
```

## Per-Mode Templates

### Code Review

**Model**: gemini-2.5-flash

```
[Claude Code consulting Gemini for peer review]

Task: Code review — check for bugs, logic errors, security vulnerabilities (SQL injection, XSS, etc.), performance issues, best practice violations, type safety problems, and missing error handling.

Files to review:

--- [filename] ---
[file contents]
---

[If reference docs available:]
Check against these official docs:
- [URL]

Provide direct analysis with file:line references. I will synthesize your findings with mine before presenting to the developer.
```

### Architecture Advice

**Model**: gemini-2.5-pro

```
[Claude Code consulting Gemini for peer review]

Task: Architecture advice — [description of the decision or problem]

Project structure:
[tree output or file listing]

Relevant files:
--- [filename] ---
[file contents]
---

Analyse for: architectural anti-patterns, scalability concerns, maintainability issues, better alternatives, potential technical debt.

Provide specific, actionable recommendations and rationale. I will synthesize your findings with mine before presenting to the developer.
```

### Debugging Help

**Model**: gemini-2.5-flash

```
[Claude Code consulting Gemini for peer review]

Task: Debug analysis — identify root cause (not just symptoms), explain why it's happening, suggest specific fix with code example, and how to prevent in future.

Error: [error message/description]
What was tried: [previous attempts if any]

Files:
--- [filename] ---
[file contents]
---

Provide direct analysis with file:line references. I will synthesize your findings with mine before presenting to the developer.
```

### Security Scan

**Model**: gemini-2.5-pro

```
[Claude Code consulting Gemini for peer review]

Task: Security audit — check for injection vulnerabilities, authentication/authorisation issues, data exposure, insecure defaults, missing input validation, CORS misconfiguration, and credential handling.

Files:
--- [filename] ---
[file contents]
---

Provide direct analysis with file:line references and severity ratings (critical/high/medium/low). I will synthesize your findings with mine before presenting to the developer.
```

### Quick Question

**Model**: gemini-2.5-flash

```
[Claude Code consulting Gemini for peer review]

Task: [The question]

Provide a direct, concise answer. I will synthesize your response with my own analysis before presenting to the developer.
```

### Project Review

**Model**: gemini-2.5-pro

```
[Claude Code consulting Gemini for peer review]

Task: Project review — [specific focus area or "general architecture and code quality review"]

Project structure:
[tree output]

Key files:
--- [filename] ---
[file contents]
---

Analyse for: architecture quality, code organisation, dependency choices, testing coverage, security posture, performance concerns, and maintainability.

Provide a structured report with prioritised recommendations. I will synthesize your findings with mine before presenting to the developer.
```

## Flash vs Pro

- **Flash** (gemini-2.5-flash): Faster, good for code reviews, debugging, quick questions. Use as default.
- **Pro** (gemini-2.5-pro): Better reasoning, preferred for complex architecture decisions, security reviews, and full project analysis.

Both models have similar quality on straightforward tasks. Pro's advantage shows on complex reasoning where trade-off analysis matters.
