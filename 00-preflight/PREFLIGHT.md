# PHASE 0 — PREFLIGHT REPORT
Date: 2026-06-10 · Environment: Claude Code remote container (ephemeral, repo `Tim-obs/test`, branch `claude/pensive-einstein-1sw3x5`)

## Verdict: RED — GHL bench is broken. Local build bench is GREEN.

Per mission §3 ("any red = stop and report"), Phases 6–7 (GHL deploy + test purchase)
cannot run in this session. Phases 1–5 (research → offer → products → pages → creative)
are fully executable here.

## Checks

| Check | Status | Detail |
|---|---|---|
| Node 18+ | ✅ GREEN | v22.22.2 |
| Python 3 | ✅ GREEN | /usr/local/bin/python3 |
| wkhtmltopdf | ✅ GREEN | 0.12.6 (installed via apt this session) |
| pdftoppm (poppler) | ✅ GREEN | installed via apt this session |
| montage (imagemagick) | ✅ GREEN | installed via apt this session |
| Disk space | ✅ GREEN | 31 GB free |
| higgsfield MCP | ✅ GREEN | connector live; cost preflight returned 2 credits (nano_banana_pro 1K); balance **2,550.1 credits, Ultra plan** |
| Web research (WebSearch/WebFetch) | ✅ GREEN | available |
| Git push path | ✅ GREEN | origin → Tim-obs/test via session proxy |
| `GHL_PIT_TOKEN` | ❌ RED | env var not set in this environment |
| GHL API reachability | ❌ RED | `services.leadconnectorhq.com` → **403** through the container's egress proxy (network policy blocks it) |
| GHL app reachability | ❌ RED | `app.gohighlevel.com` → **403** (same) |
| Logged-in Chrome profile for GHL | ❌ RED | fresh cloud container — no Chrome installed, no Playwright browsers, no GHL session cookies. Cannot exist here without operator-side setup. |
| `GHL_LOCATION` | ❌ RED | variable empty; mission requires operator confirmation of staging vs live regardless |
| `/skills/` (market-research, copy-writing, fb-image-ad-strategist, meta-eval) | ⚠️ ABSENT | not in repo; mission says "if present" → defaults apply |
| `SUPPORT_EMAIL`, `FUNNEL_DOMAIN` | ⚠️ UNSET | placeholders will be used; listed in operator to-dos |

## What this means

- **Executable in this session:** Phase 1 (research, NICHE="PICK" → I choose), Phase 2 (offer
  architecture), Phase 3 (three QA'd PDFs), Phase 4 (six funnel pages as single-file HTML),
  Phase 5 (page imagery + 24 Meta ads via higgsfield, meta-eval-style scoring).
- **Blocked in this session:** Phase 6 (GHL deploy — needs PIT token + network allowlist for the
  API half, and a logged-in browser for the builder half, which a cloud container cannot have),
  Phase 7 (test purchase — depends on Phase 6).
- **To unblock the API half of Phase 6:** set `GHL_PIT_TOKEN` in the environment settings and
  allowlist `*.leadconnectorhq.com` in the environment's network policy.
- **To unblock the browser half (funnel steps, page paste, upsell wiring, workflows):** run the
  deploy phase on a machine with a Chrome profile logged into GHL — this container can instead
  produce an exact click-by-click deploy runbook.

## Gate decision
Stopped at the Phase 0 gate per mission §3 and asked the operator whether to proceed with
Phases 1–5 (deferring deploy) or hold until the GHL bench is fixed.
