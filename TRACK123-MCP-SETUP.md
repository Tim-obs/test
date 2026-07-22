# Track123 MCP Setup

This repo includes a project-level MCP config (`.mcp.json`) that connects Claude
to Track123's hosted MCP server for live order/shipment tracking.

- Server: `https://shp.track123.com/shopify/mcp` (HTTP transport)
- Store UUID: `tccji6-p0` (hardcoded in `.mcp.json` — not a secret)
- API key: read from the `TRACK123_API_KEY` environment variable so it never
  lives in git. Get it from the Track123 dashboard under
  **Settings → General → API & Webhook**.

## Claude Code on the web (this environment)

1. Open the environment settings at claude.ai/code for this repo's environment.
2. Add an environment variable: `TRACK123_API_KEY` = your key.
3. In the environment's **network policy**, allow the domain
   `shp.track123.com` (it is currently blocked, so the MCP server cannot
   connect from web sessions until this is allowed).
4. Start a new session and approve the `track123` project MCP server when
   prompted.

## Claude Code CLI / desktop (local)

Either set the env var before launching:

```bash
export TRACK123_API_KEY=your-key-here
claude
```

...and approve the project server when prompted, or register it user-wide
without the repo config:

```bash
claude mcp add --transport http track123 https://shp.track123.com/shopify/mcp \
  --header "X-Api-Key: your-key-here" \
  --header "X-Store-Uuid: tccji6-p0"
```

## Claude.ai (chat) custom connectors

Claude.ai custom connectors only support plain-URL or OAuth remote servers —
they cannot send custom headers like `X-Api-Key`, so this server can't be added
there directly. Use Claude Code (web, CLI, or desktop) instead.
