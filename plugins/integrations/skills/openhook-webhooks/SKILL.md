---
name: openhook-webhook-listener
description: Listen for webhooks from GitHub, Stripe, Linear, Slack, and more. Use this skill when the user wants to receive real-time webhook events from external platforms and react to them automatically.
metadata:
  openclaw:
    emoji: "🪝"
    requires:
      bins: ["openhook"]
    install:
      - id: openhook-cli
        kind: shell
        command: "curl -fsSL https://openhook.dev/install.sh | sh"
  claude-code:
    version: "1.0.0"
    triggers:
      - "webhook"
      - "listen for events"
      - "github push notification"
      - "stripe payment webhook"
      - "receive webhooks"
---

# openhook Webhook Listener

Receive real-time webhook events from GitHub, Stripe, Linear, Slack, and other platforms directly to your AI agent.

## When to Use

- User wants to listen for GitHub events (pushes, PRs, issues)
- User wants to receive Stripe payment notifications
- User wants to track Linear issues and updates
- User wants to monitor Slack messages
- User asks to "watch" or "listen" for external events
- User wants their AI agent to react to webhooks

## Prerequisites

1. **Install openhook CLI**:
```bash
curl -fsSL https://openhook.dev/install.sh | sh
```

2. **Authenticate**:
```bash
# Get your API key from https://openhook.dev/dashboard
openhook auth login --key YOUR_API_KEY
```

3. **Connect platforms** at https://openhook.dev/dashboard

## Quick Reference

```bash
# Subscribe to GitHub events
openhook subscribe github --repo owner/repo --events push,pull_request,issues

# Subscribe to Stripe events
openhook subscribe stripe --events payment_intent.succeeded,checkout.session.completed

# Subscribe to Linear events
openhook subscribe linear --team TEAM_ID --events issue.created,issue.updated

# List subscriptions
openhook list

# Start as background daemon (recommended)
openhook daemon start --openclaw

# Or run in foreground
openhook listen
```

## Daemon Mode (Recommended)

Run openhook as a background service that starts automatically and reconnects if disconnected:

```bash
# Start daemon
openhook daemon start --openclaw

# Check status
openhook daemon status

# View logs
openhook daemon logs -f

# Stop daemon
openhook daemon stop
```

## Usage with OpenClaw (Native Support)

openhook has built-in OpenClaw integration. Events are automatically forwarded to your AI agent.

### One-time setup:
```bash
npx openclaw config set hooks.enabled true
npx openclaw config set hooks.token "your-secret-token"
npx openclaw config set hooks.allowRequestSessionKey true
```

### Start listening:
```bash
export OPENCLAW_HOOKS_TOKEN="your-secret-token"
openhook listen --openclaw
```

When a webhook arrives, OpenClaw receives a structured message like:
```
Webhook event received from github:

Event: push
Summary: Push to main (3 commits) by alice

Full payload:
{...}

Please process this event appropriately.
```

## Usage with Claude Code

Pipe JSON output to process events programmatically:

```bash
openhook listen --format json | while read event; do
  echo "$event" | jq '.type'
  # Process each event
done
```

## Supported Platforms

| Platform | Example Events |
|----------|---------------|
| GitHub | push, pull_request, issues, workflow_run, release |
| Stripe | payment_intent.succeeded, checkout.session.completed, subscription.* |
| Linear | issue.created, issue.updated, comment.created |
| Slack | message, reaction, app_mention |

## Examples

### React to GitHub pushes
```bash
# Subscribe
openhook subscribe github --repo myorg/myapp --events push

# Listen and forward to OpenClaw
openhook listen --openclaw
```

### Monitor Stripe payments
```bash
# Subscribe
openhook subscribe stripe --events payment_intent.succeeded

# Listen
openhook listen
```

## Troubleshooting

**"not authenticated" error**:
```bash
openhook auth login --key YOUR_API_KEY
```

**No events received**:
1. Check subscription: `openhook list`
2. Verify platform is connected at https://openhook.dev/dashboard
3. Ensure tunnel is running: `openhook listen`

**OpenClaw not receiving events**:
1. Verify hooks are enabled: `npx openclaw config get hooks`
2. Check token matches: `OPENCLAW_HOOKS_TOKEN` env var must match config
