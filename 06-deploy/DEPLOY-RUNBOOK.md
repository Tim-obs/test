# DEPLOY RUNBOOK — CalmWalk funnel → GoHighLevel
Phases 6–7 could not run from this cloud session (no `GHL_PIT_TOKEN`, GHL domains blocked by
the environment's network allowlist, and no logged-in Chrome profile — the builder half of GHL
has no write API). This runbook turns deploy into a ~2-hour paint-by-numbers job, either by a
human or by re-running the mission on a machine with a logged-in Chrome profile.

## 0. Prerequisites
- GHL sub-account (STAGING first), Stripe connected (test mode for the dry run).
- Private Integration token scoped to: products/prices, payments, medias, contacts, tags
  (set as `GHL_PIT_TOKEN`).
- Pick `SUPPORT_EMAIL` and (optionally) a funnel domain.

## 1. Via API (PIT token)
1. **Media:** upload the 5 files in `05-creative/pages/` to Media Library
   (`POST https://services.leadconnectorhq.com/medias/upload-file`, header `Authorization: Bearer $GHL_PIT_TOKEN`,
   `Version: 2021-07-28`). Record each URL.
2. **Files:** upload the 3 PDFs in `03-products/` the same way (or host on any file storage —
   delivery emails just need stable URLs). Record URLs.
3. **Products + prices** (`POST /products/` then `/products/{id}/price`):
   - `CALMWALK-FE` — The 21-Day Calm Walks Plan — one-time **$27**
   - `CALMWALK-U1` — The Calm Walks Toolkit — one-time **$97**
   - `CALMWALK-U2` — The Hard Cases Manual — one-time **$47**
   - `CALMWALK-DS` — The Calm Walks Toolkit (Half-Price) — one-time **$47**
4. **Tags:** create `fe-buyer, u1-buyer, u2-buyer, ds-buyer, abandoned-cart`.

## 2. Pages
1. Run `python3 04-pages/swap_tokens.py` once to emit `deploy-config.json`; fill in the media
   URLs from step 1.1, support email, and (after step 3.1) each funnel step's path; re-run to
   emit deploy-ready HTML in `04-pages/deploy/`.
2. Note: decline links must point at the **next step's full URL** per the routing table below.

## 3. In the GHL builder (manual / Playwright-on-logged-in-profile)
1. Sites → Funnels → **New Funnel "CalmWalk"** → six steps named exactly:
   `Sales Page, Checkout, Upsell 1, Downsell, Upsell 2, Thank You`.
2. Each step: builder → one full-width section → **Custom Code/HTML element** → paste the
   matching file from `04-pages/deploy/` → save → preview → screenshot to `/evidence/`.
3. **Checkout step:** insert the native **order-form element** where the
   `<!-- GHL ORDER FORM HERE -->` placeholder block sits; attach `CALMWALK-FE`; enable
   post-purchase one-click upsells.
4. **Upsell 1 / Downsell / Upsell 2 steps:** add the one-click upsell element; attach
   `CALMWALK-U1` / `CALMWALK-DS` / `CALMWALK-U2`; wire the YES buttons to the upsell element's
   action and the decline links to the next step URL per this routing:

```
Sales → Checkout(FE) → Upsell1 ──accept──→ Upsell2 ──accept/decline──→ ThankYou
                          │decline
                          ▼
                       Downsell ──accept/decline──→ Upsell2
```

5. **Domain** (operator-gated): attach it, or record the default funnel URLs.

## 4. Automations (EMAIL delivery mode)
Create 4 workflows: trigger **Order Submitted [product]** → add tag → send email (within 60s).
The DS workflow sends the SAME files as U1. Plus one abandoned-cart workflow:
trigger order-form-started without purchase → 15-min wait → tag `abandoned-cart` → email 5.

### Email 1 — FE (trigger: CALMWALK-FE · tag `fe-buyer`)
- Subject: **[Your Calm Walks Plan] — download inside**
- Body:
  > You're in. Here's your book:
  > **Download The 21-Day Calm Walks Plan (PDF):** {FE_FILE_URL}
  >
  > Do this tonight — it takes 15 minutes: read pages 7–15 ("Why Everything Failed").
  > Tomorrow morning is Day 1: a 20-minute scout walk where you change nothing and just
  > measure. The plan does the thinking from there.
  >
  > Save this email. The link doesn't expire.
  > Stuck on anything? Reply — a human reads these. — CalmWalk

### Email 2 — U1 (trigger: CALMWALK-U1 · tag `u1-buyer`)
- Subject: **[Your Calm Walks Toolkit] — download inside**
- Body:
  > Smart upgrade. Here's the done-for-you layer:
  > **Download The Calm Walks Toolkit (PDF):** {U1_FILE_URL}
  >
  > Print page 27 first (the pocket cards) and this week's day cards. Grayscale is fine.
  > Tomorrow: grab Card 1, pouch, leash — the book stays on the shelf. — CalmWalk

### Email 3 — U2 (trigger: CALMWALK-U2 · tag `u2-buyer`)
- Subject: **[Your Hard Cases Manual] — download inside**
- Body:
  > The certainty layer, delivered:
  > **Download The Hard Cases Manual (PDF):** {U2_FILE_URL}
  >
  > Don't read it cover to cover — open page 3 (triage), pick your ONE daily-fire case, and
  > read just its four pages. And read Case 9 once now, before you need it. — CalmWalk

### Email 4 — DS (trigger: CALMWALK-DS · tag `ds-buyer`) — same files as U1
- Subject: **[Your Calm Walks Toolkit] — download inside**
- Body: identical to Email 2.

### Email 5 — abandoned cart (15 min after form start, no purchase)
- Subject: **Your plan is still on the table**
- Body:
  > You were 30 seconds from the download when life happened — it does that.
  > The 21-Day Calm Walks Plan is still $27, still instant, still covered by the 30-day
  > keep-the-book guarantee: {CHECKOUT_URL}
  >
  > If you hesitated because you've already tried everything: page 8 explains why everything
  > you tried was used on the wrong side of a line nobody drew for you. That page alone is
  > worth the $27. — CalmWalk

## 5. Verification (Phase 6.3 + Phase 7)
1. Load all six step URLs at 390px viewport: images render, zero `{{...}}` tokens survive,
   CTAs route per the table, footers intact. Screenshots → `/evidence/`.
2. **Test purchase** (Stripe test mode): buy FE → accept U1 → land U2 → decline → Thank You.
   Verify 2 charges, both delivery emails < 60s, links download the right PDFs, tags applied.
3. **Decline path:** buy FE → decline U1 → Downsell renders at $47 → decline → U2 renders.
4. Log everything with screenshots. A funnel you didn't buy from is a funnel you didn't finish.

## To run the original Phase 6–7 automation instead
Re-run the mission on a machine with: Chrome profile logged into GHL, `GHL_PIT_TOKEN` exported,
and unrestricted egress (or this environment with `services.leadconnectorhq.com`,
`*.gohighlevel.com`, and the higgsfield CDN host added to the network allowlist).
`STATE.json` will resume it at Phase 6 without rebuilding anything.
