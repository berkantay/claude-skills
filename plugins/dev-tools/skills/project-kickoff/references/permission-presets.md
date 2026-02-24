# Permission Presets

Curated permission presets for `settings.local.json`. Each preset is a JSON array of permission strings grouped with `//` comments.

## Syntax Reference

| Pattern | Meaning |
|---------|---------|
| `Bash(git *)` | Space before `*` = word boundary (current preferred syntax) |
| `Bash(git:*)` | Colon syntax (deprecated, still works) |
| `Bash(git*)` | No space = no boundary (matches `gitk` too) |
| `WebFetch(domain:example.com)` | Domain-scoped web access |
| `WebSearch` | Blanket web search (no specifiers) |
| `mcp__server__tool` | Specific MCP tool |

**Critical**: Project `settings.local.json` SHADOWS global settings (does not merge). If a project has its own allow list, it completely replaces the global one.

---

## Universal Base

Every project gets these. Git and GitHub CLI are needed for all development work.

```json
"// --- Git ---",
"Bash(git *)",

"// --- GitHub CLI ---",
"Bash(gh *)",
"Bash(gh repo:*)",
"Bash(gh issue:*)",
"Bash(gh pr:*)",
"Bash(gh api:*)",
"Bash(gh search:*)",
"Bash(gh run:*)",
"Bash(gh release:*)",
"Bash(gh label:*)",
"Bash(gh workflow:*)",

"// --- Web ---",
"WebSearch"
```

Note: `Bash(gh *)` has a known bug where some subcommands don't match. Include both the broad pattern and explicit subcommand patterns as a workaround.

---

## Cloudflare Worker

For projects using Cloudflare Workers, D1, R2, KV. Add to Universal Base.

```json
"// --- Wrangler ---",
"Bash(npx wrangler *)",
"Bash(wrangler *)",

"// --- Package Managers ---",
"Bash(pnpm *)",
"Bash(npm *)",
"Bash(npx *)",

"// --- Cloudflare Docs ---",
"mcp__claude_ai_cloudflare-docs__search_cloudflare_documentation",
"WebFetch(domain:developers.cloudflare.com)",

"// --- Build & Dev ---",
"Bash(curl *)",
"Bash(node *)"
```

### Cloudflare Account Note

Default account: Jezweb Team `0460574641fdbb98159c98ebf593e2bd`. Add `account_id` to `wrangler.jsonc` to avoid interactive prompts — don't put it in permission patterns.

---

## Vercel App

For Next.js or other Vercel-deployed projects. Add to Universal Base.

```json
"// --- Vercel CLI ---",
"Bash(npx vercel *)",
"Bash(vercel *)",

"// --- Package Managers ---",
"Bash(pnpm *)",
"Bash(npm *)",
"Bash(npx *)",

"// --- Database ---",
"Bash(npx prisma *)",
"Bash(prisma *)",

"// --- Build & Dev ---",
"Bash(curl *)",
"Bash(node *)"
```

### Vercel Account Note

Always use the Jezweb team account. Run `vercel switch jezweb` before deploying.

---

## Node Generic

For generic Node.js projects without a specific deployment target. Add to Universal Base.

```json
"// --- Package Managers ---",
"Bash(pnpm *)",
"Bash(npm *)",
"Bash(npx *)",

"// --- Runtime ---",
"Bash(node *)",
"Bash(npx tsx *)"
```

---

## Python

For Python projects using uv or pip. Add to Universal Base.

```json
"// --- Python ---",
"Bash(python3 *)",
"Bash(python *)",
"Bash(pip *)",
"Bash(uv *)",

"// --- Testing ---",
"Bash(pytest *)",
"Bash(mypy *)"
```

---

## Ops / Admin

For operational repos (like HQ, Anthro) that interact with many MCP services. Add to Universal Base.

```json
"// --- Gmail ---",
"mcp__claude_ai_google-gmail-jez__gmail_messages",
"mcp__claude_ai_google-gmail-jez__gmail_threads",
"mcp__claude_ai_google-gmail-jez__gmail_labels",
"mcp__claude_ai_google-gmail-jez__gmail_drafts",
"mcp__claude_ai_google-gmail-jez__gmail_contacts",
"mcp__claude_ai_google-gmail-anthro__gmail_messages",
"mcp__claude_ai_google-gmail-anthro__gmail_threads",
"mcp__claude_ai_google-gmail-anthro__gmail_labels",
"mcp__claude_ai_google-gmail-anthro__gmail_drafts",
"mcp__claude_ai_google-gmail-anthro__gmail_contacts",

"// --- Google Chat ---",
"mcp__claude_ai_google-chat-jez__chat_spaces",
"mcp__claude_ai_google-chat-jez__chat_messages",
"mcp__claude_ai_google-chat-jez__chat_members",
"mcp__claude_ai_google-chat-anthro__chat_spaces",
"mcp__claude_ai_google-chat-anthro__chat_messages",
"mcp__claude_ai_google-chat-anthro__chat_members",

"// --- Google Docs ---",
"mcp__claude_ai_google-docs-jez__docs_documents",
"mcp__claude_ai_google-docs-jez__docs_content",
"mcp__claude_ai_google-docs-jez__docs_format",
"mcp__claude_ai_google-docs-jez__docs_collaborate",
"mcp__claude_ai_google-docs-anthro__docs_documents",
"mcp__claude_ai_google-docs-anthro__docs_content",
"mcp__claude_ai_google-docs-anthro__docs_format",
"mcp__claude_ai_google-docs-anthro__docs_collaborate",

"// --- Google Sheets ---",
"mcp__claude_ai_google-sheets-jez__sheets_spreadsheets",
"mcp__claude_ai_google-sheets-jez__sheets_values",
"mcp__claude_ai_google-sheets-jez__sheets_data",
"mcp__claude_ai_google-sheets-jez__sheets_format",
"mcp__claude_ai_google-sheets-anthro__sheets_spreadsheets",
"mcp__claude_ai_google-sheets-anthro__sheets_values",
"mcp__claude_ai_google-sheets-anthro__sheets_data",
"mcp__claude_ai_google-sheets-anthro__sheets_format",

"// --- Calendar ---",
"mcp__claude_ai_calendar__calendar_calendars",
"mcp__claude_ai_calendar__calendar_events",

"// --- Google Tasks ---",
"mcp__claude_ai_google-tasks-jez__tasks_lists",
"mcp__claude_ai_google-tasks-jez__tasks_tasks",
"mcp__claude_ai_google-tasks-anthro__tasks_lists",
"mcp__claude_ai_google-tasks-anthro__tasks_tasks",

"// --- Google Search Console ---",
"mcp__claude_ai_google-search-console__search_console_analytics",
"mcp__claude_ai_google-search-console__search_console_sitemaps",
"mcp__claude_ai_google-search-console__search_console_sites",

"// --- Brain (CRM) ---",
"mcp__claude_ai_brain__brain_clients",
"mcp__claude_ai_brain__brain_sites",
"mcp__claude_ai_brain__brain_contacts",
"mcp__claude_ai_brain__brain_issues",
"mcp__claude_ai_brain__brain_knowledge",
"mcp__claude_ai_brain__brain_comms",
"mcp__claude_ai_brain__brain_documents",
"mcp__claude_ai_brain__brain_billing",
"mcp__claude_ai_brain__brain_admin",
"mcp__claude_ai_brain__brain_recall",
"mcp__claude_ai_brain__brain_client_get",
"mcp__claude_ai_brain__brain_site_get",
"mcp__claude_ai_brain__brain_projects",
"mcp__claude_ai_brain__brain_tasks",

"// --- Vault ---",
"mcp__claude_ai_Vault__secret_get",
"mcp__claude_ai_Vault__secret_set",
"mcp__claude_ai_Vault__secret_list",
"mcp__claude_ai_Vault__secret_delete",
"mcp__claude_ai_Vault__remember",
"mcp__claude_ai_Vault__recall",
"mcp__claude_ai_Vault__knowledge_list",
"mcp__claude_ai_Vault__forget",
"mcp__claude_ai_Vault__update_knowledge",

"// --- Rocket.net ---",
"mcp__claude_ai_rocket__rocketnet_sites",
"mcp__claude_ai_rocket__rocketnet_performance",
"mcp__claude_ai_rocket__rocketnet_backups",
"mcp__claude_ai_rocket__rocketnet_domains",
"mcp__claude_ai_rocket__rocketnet_wordpress",
"mcp__claude_ai_rocket__rocketnet_credentials",
"mcp__claude_ai_rocket__rocketnet_activity",
"mcp__claude_ai_rocket__rocketnet_access",

"// --- Synergy Wholesale ---",
"mcp__claude_ai_synergy_wholesale__synergy_domains",
"mcp__claude_ai_synergy_wholesale__synergy_dns",
"mcp__claude_ai_synergy_wholesale__synergy_hosting",
"mcp__claude_ai_synergy_wholesale__synergy_email",
"mcp__claude_ai_synergy_wholesale__synergy_contacts",
"mcp__claude_ai_synergy_wholesale__synergy_transfers",
"mcp__claude_ai_synergy_wholesale__synergy_account",
"mcp__claude_ai_synergy_wholesale__synergy_credentials",
"mcp__claude_ai_synergy_wholesale__synergy_discovery",

"// --- Network ---",
"mcp__claude_ai_network__network_check",
"mcp__claude_ai_network__network_lookup",

"// --- Australian Business ---",
"mcp__claude_ai_australian_business__australia_business",
"mcp__claude_ai_australian_business__australia_datetime",
"mcp__claude_ai_australian_business__australia_ip",

"// --- Cloudflare Docs ---",
"mcp__claude_ai_cloudflare-docs__search_cloudflare_documentation",

"// --- GitHub MCP ---",
"mcp__claude_ai_github__github_repos",
"mcp__claude_ai_github__github_issues",
"mcp__claude_ai_github__github_pulls",
"mcp__claude_ai_github__get_user_info",

"// --- Scraper ---",
"mcp__claude_ai_scraper__web_scraper",
"mcp__claude_ai_scraper__web_crawler",

"// --- YouTube ---",
"mcp__claude_ai_youtube__youtube_video",
"mcp__claude_ai_youtube__youtube_search",
"mcp__claude_ai_youtube__youtube_channel",
"mcp__claude_ai_youtube__youtube_playlist",

"// --- Weather ---",
"mcp__claude_ai_weather__weather",

"// --- Web ---",
"WebFetch(domain:github.com)",
"WebFetch(domain:developers.cloudflare.com)",
"WebFetch(domain:rocket.net)",

"// --- Bash ---",
"Bash(curl *)",
"Bash(playwright-cli *)",
"Bash(pm2 *)",
"Bash(claude *)",
"Bash(dig *)",
"Bash(node *)",
"Bash(python3 *)"
```

---

## Combining Presets

Presets stack. A Cloudflare Worker project gets: Universal + Cloudflare Worker. An ops project gets: Universal + Ops/Admin.

When merging, deduplicate and keep the grouped `//` comment structure. The final `settings.local.json` should look like:

```json
{
  "permissions": {
    "allow": [
      "// --- Git ---",
      "Bash(git *)",
      "// --- GitHub CLI ---",
      "Bash(gh *)",
      ...
    ],
    "deny": []
  }
}
```
