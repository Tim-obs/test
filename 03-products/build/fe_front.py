"""FE book — cover, read-this-first, safety, TOC slots."""
from design import *

PARTCOLORS = {"I": PALETTE["sage"], "II": PALETTE["amber"], "III": PALETTE["forest2"],
              "IV": PALETTE["clay"], "V": PALETTE["mut"]}

def cover():
    arcs = f'''<svg width="816" height="330" viewBox="0 0 816 330" xmlns="http://www.w3.org/2000/svg">
<circle cx="408" cy="430" r="150" fill="{PALETTE['clay']}" fill-opacity="0.85"/>
<circle cx="408" cy="430" r="250" fill="{PALETTE['gold']}" fill-opacity="0.5"/>
<circle cx="408" cy="430" r="360" fill="{PALETTE['sage']}" fill-opacity="0.35"/>
<circle cx="408" cy="430" r="250" fill="none" stroke="{PALETTE['gold']}" stroke-width="2"/>
<circle cx="408" cy="430" r="360" fill="none" stroke="{PALETTE['sage']}" stroke-width="2"/>
</svg>'''
    body = f'''
<div style="background:{PALETTE['forest']};width:816px;height:1056px;position:relative;">
  <div style="padding:96px 84px 0 84px;">
    <div style="font-size:13px;letter-spacing:5px;color:{PALETTE['gold']};font-weight:bold;">CALMWALK</div>
    <div style="border-top:3px solid {PALETTE['amber']};width:72px;margin:26px 0;"></div>
    <div style="font-size:15px;letter-spacing:4px;color:{PALETTE['sage']};font-weight:bold;">THE GREEN ZONE METHOD&#8482;</div>
    <div style="font-family:'Roboto Slab',serif;font-size:64px;line-height:1.1;color:{PALETTE['cream']};
         font-weight:bold;margin:18px 0 26px 0;">The 21-Day<br/>Calm Walks Plan</div>
    <div style="font-size:19px;line-height:1.6;color:{PALETTE['pale']};max-width:560px;">
      A measured, day-by-day system for walking your reactive dog past the things
      that used to blow up your walk &#8212; built on one number you can count on any street.</div>
    <div style="margin-top:34px;">
      <span style="background:{PALETTE['amber']};color:{PALETTE['ink']};border-radius:14px;
        padding:7px 18px;font-size:13px;font-weight:bold;letter-spacing:2px;">MAP &#183; ANCHOR &#183; SHRINK</span>
    </div>
  </div>
  <div style="position:absolute;bottom:0;left:0;">{arcs}</div>
  <div style="position:absolute;bottom:30px;left:0;right:0;text-align:center;font-size:11px;
       letter-spacing:3px;color:{PALETTE['pale']};">A WORKBOOK &#183; PRINT IT &#183; WALK IT</div>
</div>'''
    return {"raw": page(body, chrome=False)}

def read_first():
    b = pad(
        kicker("BEFORE PAGE ONE")
        + h1("Read this first. It takes three minutes.")
        + dropcap("You bought a plan, not a library. This book is built to be walked, not studied. "
                  "Every day for the next 21 days you get one page: the goal, the exact reps, "
                  "a pass check, and what to do when it goes sideways. That's the whole system.")
        + h3("How to use it")
        + cklist([
            "<b>Read Part I tonight</b> (pages 7&#8211;15). It explains why nothing has worked yet. It is short on purpose.",
            "<b>Read Part II tomorrow</b> (pages 17&#8211;26). It teaches the three moves you will use every day.",
            "<b>Then walk the plan</b> (pages 28&#8211;52), one page per day, about 16 minutes per session.",
            "Keep Part IV folded into your pocket-memory: when a walk goes wrong, there is a script for it.",
        ])
        + h3("What you need")
        + p("A 6-foot leash (not retractable), a front-clip harness or flat collar, a treat pouch, "
            "and 100 pea-sized soft treats per session &#8212; cut-up hot dogs, cheese, or chicken. "
            "Kibble will not be enough pay for this work. Total gear cost if you own none of it: about $40.")
        + callout("key", "&#9733; THE HONEST PROMISE",
            p("This book shows you the same structure a behavior trainer charges $100&#8211;$250 per "
              "session to run: find the distance where your dog can think, build a new habit there, "
              "and shrink that distance on a strict rule. No book can promise what your dog will do. "
              "What this plan promises is that <b>you will know exactly what to do every day</b> &#8212; "
              "and you will have it on paper, measured, where a bad day can't lie to you."))
        + h3("One rule above all the others")
        + p("<b>Never work your dog over threshold on purpose.</b> If you remember nothing else, "
            "remember that the whole method lives inside that one sentence. Page 10 will show you "
            "exactly where the line is.")
    )
    return {"html": b, "toc": None}

def safety():
    b = pad(
        kicker("THE SAFETY PAGE")
        + h1("Who this plan is for &#8212; and who needs more than a book")
        + p("Most leash reactivity is fear or frustration, not aggression. Barking, lunging, "
            "spinning, and hackles at the sight of dogs or strangers &#8212; while calm at home &#8212; "
            "is the picture this plan is built for.")
        + callout("warn", "&#9888; STOP AND GET A PROFESSIONAL FIRST IF ANY OF THESE ARE TRUE",
            "<ul><li>Your dog has <b>bitten and broken skin</b> &#8212; on a person or a dog.</li>"
            "<li>The reactivity started <b>suddenly in an adult dog</b>. Sudden change is a medical "
            "sign until a vet says otherwise. Pain makes dogs reactive.</li>"
            "<li>Your dog goes after <b>children, joggers, or cyclists with a hard, silent stare</b> "
            "rather than noisy barking.</li>"
            "<li>You are <b>afraid of your own dog</b> at home.</li></ul>"
            + p("Look for a credentialed professional: a veterinary behaviorist (DACVB), a Certified "
                "Applied Animal Behaviorist (CAAB), or a certified trainer (CPDT-KA, KPA-CTP, IAABC) "
                "who says the words &ldquo;under threshold&rdquo; in the first conversation. "
                "This book pairs well with that work; it does not replace it."))
        + h3("Three safety rules for every session in this book")
        + cklist([
            "<b>Equipment check before every walk:</b> two points of contact if your dog has ever slipped gear; "
            "buckles checked; leash clipped, never looped over a wrist.",
            "<b>A basket muzzle is kindness, not cruelty,</b> if your dog has ever made contact. A muzzled dog "
            "trained to love the muzzle gets MORE freedom, not less. (Muzzle intro plan: page 65.)",
            "<b>Obey leash laws and distance:</b> never let anyone &#8212; human or dog &#8212; greet your dog "
            "during this plan. &ldquo;He's in training&rdquo; is a complete sentence.",
        ])
        + callout("note", "&#9998; THE LEGAL LINE",
            small("This workbook is educational material about common, evidence-based training practices "
                  "(desensitization and counterconditioning). It is not veterinary advice, not a diagnosis, "
                  "and not a substitute for in-person professional help. You know your dog; when in doubt, "
                  "choose the cautious option. CalmWalk is not affiliated with Meta or any platform you "
                  "may have found us on."))
    )
    return {"html": b, "toc": None}

def pages():
    return [
        cover(),
        read_first(),
        safety(),
        {"tocslot": 1},
        {"tocslot": 2},
    ]
