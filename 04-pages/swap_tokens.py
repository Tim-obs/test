#!/usr/bin/env python3
"""Produce deploy-ready funnel pages: swap {{IMG:*}}, {{URL:*}}, {{SUPPORT_EMAIL}} tokens.

Usage: fill deploy-config.json (see template below, created on first run), then:
    python3 swap_tokens.py
Deploy-ready files land in 04-pages/deploy/.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = os.path.join(HERE, "deploy-config.json")
TEMPLATE = {
    "SUPPORT_EMAIL": "support@yourdomain.com",
    "IMG": {
        "hero": "https://<ghl-media-url>/hero.png",
        "mockup-trio": "https://<ghl-media-url>/mockup-trio.png",
        "inthewild": "https://<ghl-media-url>/inthewild.png",
        "toolkit-stack": "https://<ghl-media-url>/toolkit-stack.png",
        "manual-mock": "https://<ghl-media-url>/manual-mock.png",
    },
    "URL": {
        "CHECKOUT": "/checkout",
        "U1_ACCEPT": "#one-click-upsell",        # replaced by GHL upsell element action
        "U1_DECLINE": "/downsell",
        "DS_ACCEPT": "#one-click-upsell",
        "DS_DECLINE": "/upsell-2",
        "U2_ACCEPT": "#one-click-upsell",
        "U2_DECLINE": "/thank-you",
    },
}

if not os.path.exists(CFG):
    json.dump(TEMPLATE, open(CFG, "w"), indent=2)
    sys.exit("Created deploy-config.json — fill in real URLs, then re-run.")

cfg = json.load(open(CFG))
outdir = os.path.join(HERE, "deploy")
os.makedirs(outdir, exist_ok=True)
for f in sorted(os.listdir(HERE)):
    if not f.endswith(".html"):
        continue
    html = open(os.path.join(HERE, f)).read()
    html = html.replace("{{SUPPORT_EMAIL}}", cfg["SUPPORT_EMAIL"])
    for k, v in cfg["IMG"].items():
        html = html.replace("{{IMG:%s}}" % k, v)
    for k, v in cfg["URL"].items():
        html = html.replace("{{URL:%s}}" % k, v)
    left = sorted(set(re.findall(r"{{[A-Z_]+(?::[\w-]+)?}}", html)))
    open(os.path.join(outdir, f), "w").write(html)
    print(f, "->", "deploy/" + f, ("UNRESOLVED: " + ", ".join(left)) if left else "clean")
