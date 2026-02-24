# CLAUDE.md Templates

Templates for generating project CLAUDE.md files. Each template includes Jez's defaults pre-filled.

## Detection Heuristics

Detect project type from file presence (first match wins, types can stack):

| Indicator | Project Type |
|-----------|-------------|
| `wrangler.jsonc` or `wrangler.toml` | cloudflare-worker |
| `vercel.json` or `next.config.*` | vercel-app |
| `package.json` with no deploy target | node-generic |
| `pyproject.toml` or `setup.py` | python |
| `.claude/agents/` + operational scripts | ops-admin |

---

## Cloudflare Worker Template

```markdown
# [Project Name]

**Repository**: https://github.com/jezweb/[repo-name]
**Last Updated**: [date]

## Stack

- Cloudflare Workers + Static Assets
- Vite + React 19 + @cloudflare/vite-plugin
- Tailwind v4 + shadcn/ui (neutral palette)
- D1 (SQLite) + Drizzle ORM
- Hono (API routing)
- pnpm

## Commands

| Command | Purpose |
|---------|---------|
| `pnpm dev` | Local dev server (Vite + Miniflare) |
| `pnpm build` | Production build |
| `pnpm deploy` | Deploy to Cloudflare |
| `pnpm db:migrate:local` | Run D1 migrations locally |
| `pnpm db:migrate:remote` | Run D1 migrations on production |

## Directory Structure

[Fill in after scaffolding]

## Cloudflare

- **Account**: Jezweb Team (`0460574641fdbb98159c98ebf593e2bd`)
- **Compatibility flags**: `nodejs_compat` (never use `node_compat`)
- Always use Workers + Static Assets (never Cloudflare Pages)

## Critical Rules

- Run migrations on BOTH local AND remote before testing
- Set `account_id` in wrangler.jsonc to avoid interactive prompts
- D1 bulk inserts: batch into chunks of ~10 rows (parameter limit)
- `wrangler secret put` does NOT auto-deploy — run `wrangler deploy` after

## Gotchas

[Add as discovered]
```

---

## Vercel App Template

```markdown
# [Project Name]

**Repository**: https://github.com/jezweb/[repo-name]
**Last Updated**: [date]

## Stack

- Next.js / Vite + React 19
- Tailwind v4 + shadcn/ui (neutral palette)
- Vercel (Jezweb team account)
- pnpm

## Commands

| Command | Purpose |
|---------|---------|
| `pnpm dev` | Local dev server |
| `pnpm build` | Production build |
| `vercel deploy` | Deploy to Vercel |
| `vercel deploy --prod` | Deploy to production |

## Vercel

- **Team**: jezweb (always use team account)
- Run `vercel switch jezweb` before deploying
- Run `vercel link --yes` to connect project

## Gotchas

[Add as discovered]
```

---

## Node Generic Template

```markdown
# [Project Name]

**Repository**: https://github.com/jezweb/[repo-name]
**Last Updated**: [date]

## Stack

- Node.js + TypeScript (ES modules)
- pnpm

## Commands

| Command | Purpose |
|---------|---------|
| `pnpm dev` | Local dev server |
| `pnpm build` | Production build |
| `pnpm test` | Run tests |

## Directory Structure

[Fill in after scaffolding]

## Gotchas

[Add as discovered]
```

---

## Python Template

```markdown
# [Project Name]

**Repository**: https://github.com/jezweb/[repo-name]
**Last Updated**: [date]

## Stack

- Python 3.12+
- uv (package management)

## Commands

| Command | Purpose |
|---------|---------|
| `uv run python main.py` | Run the application |
| `uv sync` | Install dependencies |
| `uv run pytest` | Run tests |

## Directory Structure

[Fill in after scaffolding]

## Gotchas

[Add as discovered]
```

---

## Ops / Admin Template

```markdown
# [Project Name]

**Repository**: https://github.com/jezweb/[repo-name]
**Last Updated**: [date]

## Purpose

[What this operational project does]

## MCP Servers

This project uses the following MCP integrations:

| Server | Purpose |
|--------|---------|
| Brain | Client/site/contact CRM |
| Vault | Secrets and knowledge store |
| Rocket.net | WordPress hosting management |
| Synergy Wholesale | Domain registration and DNS |
| Gmail (Jez + Anthro) | Email management |
| Google Chat (Jez + Anthro) | Team messaging |
| Google Docs/Sheets | Document management |
| Calendar | Event management |

## Anthro Persona

When communicating with Jezweb staff via Google Chat or email, use the Anthro persona. See `~/Documents/anthro/ANTHRO.md` for full briefing.

## Gotchas

[Add as discovered]
```

---

## .gitignore Templates

### Cloudflare Worker / Node

```
node_modules/
.wrangler/
dist/
.dev.vars
*.log
.DS_Store
.env
.env.local
.claude/settings.local.json
```

### Python

```
__pycache__/
*.pyc
.venv/
dist/
*.egg-info/
.env
.env.local
.DS_Store
.claude/settings.local.json
```

### Ops / Admin

```
.DS_Store
.env
.env.local
.claude/settings.local.json
```
