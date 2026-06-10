#!/usr/bin/env python3
"""Emit the 6 CalmWalk funnel pages as single-file mobile-first HTML.
Tokens: {{IMG:name}} swapped after GHL media upload; {{URL:STEP}} swapped to
funnel-step URLs in the builder; {{SUPPORT_EMAIL}} swapped at deploy."""
import os

F, F2, SG, PL, CR, AM, CL, GD, INK, MUT = ("#1B4332", "#2D6A4F", "#74A892", "#DCE8DF",
    "#FAF7F0", "#E8A13C", "#C45B4C", "#E5C45C", "#26241F", "#6B675C")

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
 color:{INK};background:{CR};font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:680px;margin:0 auto;padding:0 20px}}
.bar{{background:{INK};color:{CR};text-align:center;font-size:13.5px;font-weight:700;
 letter-spacing:.4px;padding:10px 14px}}
.bar b{{color:{GD}}}
.logo{{text-align:center;padding:18px 0 6px 0;font-weight:900;letter-spacing:5px;font-size:15px;color:{F}}}
.logo span{{color:{AM}}}
.kicker{{text-align:center;font-size:12px;letter-spacing:2.5px;font-weight:800;color:{AM};
 text-transform:uppercase;margin:14px 0 10px 0}}
h1{{font-family:Georgia,'Times New Roman',serif;font-size:clamp(27px,5.6vw,40px);line-height:1.16;
 text-align:center;color:{F};margin:8px 0 14px 0}}
h2{{font-family:Georgia,serif;font-size:clamp(22px,4.5vw,29px);line-height:1.22;color:{F};margin:34px 0 12px 0}}
h3{{font-size:14px;letter-spacing:2px;text-transform:uppercase;color:{F2};margin:24px 0 8px 0}}
p{{margin:0 0 14px 0}}
.sub{{text-align:center;font-size:clamp(16px,3.4vw,19px);color:{MUT};max-width:560px;margin:0 auto 18px auto}}
.xstrip{{background:#fff;border:2px solid {PL};border-radius:14px;padding:16px 18px;margin:18px 0}}
.xstrip div{{padding:5px 0;font-weight:600;font-size:15.5px}}
.xstrip span{{color:{CL};font-weight:900;margin-right:8px}}
.ckl{{list-style:none;margin:10px 0}}
.ckl li{{padding:7px 0 7px 34px;position:relative}}
.ckl li:before{{content:"\\2713";position:absolute;left:0;top:7px;background:{F2};color:#fff;
 width:22px;height:22px;border-radius:50%;text-align:center;line-height:22px;font-size:13px;font-weight:900}}
.xl{{list-style:none;margin:10px 0}}
.xl li{{padding:7px 0 7px 34px;position:relative}}
.xl li:before{{content:"\\2715";position:absolute;left:0;top:7px;background:{CL};color:#fff;
 width:22px;height:22px;border-radius:50%;text-align:center;line-height:22px;font-size:13px;font-weight:900}}
.img{{width:100%;border-radius:14px;display:block;margin:10px 0}}
.cta{{display:block;background:{AM};color:{INK};text-align:center;text-decoration:none;
 font-size:clamp(17px,3.8vw,21px);font-weight:900;padding:18px 22px;border-radius:14px;
 box-shadow:0 4px 0 #B97F25;margin:10px 0 6px 0}}
.cta small{{display:block;font-size:13px;font-weight:700;color:#5d4710;margin-top:3px}}
.cta-g{{background:{F2};color:#fff;box-shadow:0 4px 0 #1B4332}}
.cta-g small{{color:{PL}}}
.micro{{text-align:center;font-size:12.5px;color:{MUT};margin-bottom:18px}}
.box{{background:#fff;border:2px solid {PL};border-radius:16px;padding:22px;margin:20px 0}}
.box-dark{{background:{F};color:{CR};border-radius:16px;padding:24px;margin:20px 0}}
.box-dark h2,.box-dark h3{{color:{CR}}}
.phase{{display:flex;gap:14px;margin:18px 0;align-items:flex-start}}
.phase .n{{font-family:Georgia,serif;font-size:34px;font-weight:700;color:{AM};min-width:54px}}
.phase b.t{{display:block;font-size:18px;color:{F};margin-bottom:4px}}
.fasc li{{margin-bottom:12px}}
.fasc b{{color:{F}}}
.stack{{width:100%;border-collapse:collapse;margin:10px 0}}
.stack td{{padding:9px 4px;border-bottom:1px dashed {PL};font-size:15.5px}}
.stack td:last-child{{text-align:right;font-weight:800;color:{MUT};white-space:nowrap}}
.stack tr.tot td{{border-bottom:none;font-weight:900;font-size:17px;color:{F};padding-top:14px}}
.price{{text-align:center;margin:8px 0 4px 0}}
.price .was{{text-decoration:line-through;color:{MUT};font-size:22px;margin-right:12px}}
.price .now{{font-family:Georgia,serif;font-size:46px;font-weight:900;color:{F}}}
.guarantee{{background:{PL};border:2px solid {SG};border-radius:16px;padding:22px;margin:22px 0}}
.guarantee h3{{margin-top:0;color:{F}}}
.faq-q{{font-weight:800;color:{F};margin:18px 0 4px 0;font-size:16.5px}}
.faq-a{{margin-bottom:6px}}
.stats{{display:flex;gap:10px;text-align:center;margin:18px 0}}
.stats div{{flex:1;background:#fff;border:2px solid {PL};border-radius:14px;padding:14px 6px}}
.stats .n{{font-family:Georgia,serif;font-size:26px;font-weight:900;color:{F}}}
.stats .l{{font-size:10.5px;letter-spacing:1.2px;font-weight:800;color:{MUT};text-transform:uppercase}}
.otobar{{background:{CL};color:#fff;text-align:center;font-size:13px;font-weight:900;
 letter-spacing:1.5px;padding:9px;text-transform:uppercase}}
.prog{{text-align:center;font-size:13px;font-weight:700;color:{MUT};padding:12px 0;border-bottom:2px solid {PL}}}
.prog b{{color:{F}}}
.confirm{{text-align:center;font-size:14.5px;color:{F2};font-weight:700;margin:14px 0 0 0}}
.decline{{display:block;text-align:center;color:{MUT};font-size:14px;margin:4px 0 22px 0}}
.cardg{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0}}
.cardg div{{background:#fff;border:2px solid {PL};border-radius:14px;padding:14px}}
.cardg b{{color:{F};display:block;margin-bottom:4px;font-size:15px}}
.cardg p{{font-size:13.5px;margin:0;color:{MUT}}}
footer{{background:{INK};color:#A6A199;font-size:12.5px;line-height:1.7;padding:34px 20px;margin-top:48px}}
footer .wrap{{max-width:680px}}
footer a{{color:{SG};text-decoration:none;margin-right:14px}}
.steps li{{margin-bottom:14px}}
.steps b{{color:{F}}}
@media(max-width:520px){{.cardg{{grid-template-columns:1fr}}.stats{{flex-wrap:wrap}}.stats div{{min-width:44%}}}}
"""

DISCLAIMER = """This site and its products provide educational information about widely used,
evidence-based dog-training practices (desensitization and counterconditioning). They are not
veterinary or behaviorist advice, and no outcome is promised or implied &#8212; every dog is
different. If your dog has a bite history, targets children, or shows sudden behavior change,
consult a credentialed professional (DACVB, CAAB, or certified trainer) and your veterinarian.
This site is not part of, or endorsed by, Facebook&#8482;, Instagram&#8482;, or Meta Platforms,
Inc. Results referenced describe the structure of the method, not guaranteed outcomes."""

def doc(title, body, bar=None, desc=""):
    barhtml = f'<div class="bar">{bar}</div>' if bar else ""
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title><style>{CSS}</style></head>
<body>{barhtml}{body}
<footer><div class="wrap">
<p><b style="color:#FAF7F0;letter-spacing:3px;">CALMWALK</b> &#183; The Green Zone Method&#8482;</p>
<p>{DISCLAIMER}</p>
<p><a href="/terms">Terms</a><a href="/privacy">Privacy</a><a href="/refund">Refund Policy</a>
<a href="/disclaimer">Full Disclaimer</a><a href="mailto:{{{{SUPPORT_EMAIL}}}}">Support</a></p>
<p>&#169; CalmWalk 2026. All rights reserved.</p>
</div></footer></body></html>"""

LOGO = '<div class="logo">CALM<span>WALK</span></div>'

# ----------------------------------------------------------------- P1 SALES
def sales():
    fasc = "".join(f"<li>{x}</li>" for x in [
        "<b>The Food Test (page 18):</b> one treat and ten seconds tells you the exact distance your dog can work at today &#8212; no more guessing, no more hoping",
        "<b>The line where every dog on earth stops taking treats (page 9)</b> &#8212; once you see it, you'll know your dog was never 'too stubborn for treats'",
        "<b>Why &ldquo;socialize him more&rdquo; made it worse (page 8)</b> &#8212; the Exposure Trap, and the sentence that replaces it",
        "<b>The five loading signals (page 20):</b> your dog announces an explosion 3&#8211;10 seconds early &#8212; the first signal is the mouth, and you'll never un-see it",
        "<b>The Emergency U-Turn (page 24)</b> that turns ambushes into non-events &#8212; drilled in 10 reps a day on an empty street",
        "<b>What to throw at an incoming off-leash dog (page 55)</b> &#8212; it buys you 10&#8211;30 seconds, and it's already in your pouch",
        "<b>The Recovery Script (page 56):</b> the exact 10-second response after a blow-up, plus the 48-hour rule that stops one bad walk from costing a week",
        "<b>The 3-for-3 ladder (page 28):</b> three clean reps buy one car-length closer &#8212; a progression rule that keeps working for the life of the dog",
        "<b>How to screen any dog trainer in 5 minutes (page 65)</b> &#8212; the phrase that instantly exposes the ones who'll make it worse",
        "<b>The A&#8211;Z troubleshooting codex (pages 60&#8211;61):</b> twenty symptoms, alphabetized, each with the fix and its page number",
    ])
    body = f"""
{LOGO}
<div class="wrap">
  <div class="kicker">The Green Zone Method&#8482; &#183; for reactive dogs &#183; 2026</div>
  <h1>Your dog isn't broken. Everyone just told you to stand in the wrong place.</h1>
  <p class="sub">The 21-Day Calm Walks Plan is a measured, day-by-day system for walking a
  lunging, barking, leash-reactive dog &#8212; built on one number you can count on any street.</p>

  <div class="xstrip">
    <div><span>&#10005;</span>No prong, shock, or &ldquo;dominance&rdquo; anything</div>
    <div><span>&#10005;</span>No 118-video course to binge before you start</div>
    <div><span>&#10005;</span>No waiting six weeks for a $150/hour appointment</div>
    <div><span>&#10005;</span>No pretending your dog just needs &ldquo;more exposure&rdquo;</div>
  </div>

  <img class="img" src="{{{{IMG:hero}}}}" alt="The 21-Day Calm Walks Plan workbook">
  <!-- VSL SLOT (hidden until a video exists)
  <div class="vsl"><video controls poster=""><source src="" type="video/mp4"></video></div>
  -->

  <a class="cta" href="{{{{URL:CHECKOUT}}}}">GET THE PLAN &#8212; $27
  <small>Instant download &#183; 30-day keep-the-book guarantee</small></a>
  <div class="micro">One-time payment. No subscription. Yours forever.</div>

  <h2>If you walk your dog at 5am to avoid everyone&hellip; read this twice.</h2>
  <p>You know every house on the street with a dog behind the fence. You cross the road,
  U-turn, duck between parked cars &#8212; anything to avoid the chaos. You've stood there,
  arm yanked, while your sweet, couch-perfect dog screamed at a labradoodle, and felt the
  whole street's eyes on you.</p>
  <p>And you've tried. The treats that work brilliantly until the moment they don't. The
  YouTube videos. The group class that politely suggested &ldquo;private sessions.&rdquo;
  Maybe the trainer at $150 an hour who handed you a worksheet and a follow-up quote
  that looked like a car repair.</p>
  <p><b>Here's what nobody drew on paper for you:</b> a dog over his threshold physically
  can't eat, can't listen, can't learn. Fear beats food &#8212; every time, in every dog.
  All the things you tried weren't wrong. They were used <i>on the wrong side of a line
  nobody showed you how to find.</i></p>

  <h3>This is for you if</h3>
  <ul class="ckl">
    <li>Your dog is calm at home but becomes a different animal on the leash</li>
    <li>You've started planning walks around avoiding other dogs (hours, routes, holidays)</li>
    <li>Treats &ldquo;don't work&rdquo; the moment another dog appears</li>
    <li>You've spent real money &#8212; classes, gear, a session or two &#8212; and nothing stuck</li>
    <li>You don't need your dog to make friends. You need boring walks.</li>
  </ul>

  <h2>The method: three moves, one number, 21 days</h2>
  <p>The Green Zone Method&#8482; is structured desensitization and counterconditioning &#8212;
  the same evidence-based mechanics every credentialed behavior professional uses &#8212;
  rebuilt as a measured, day-by-day paper system you run in 16 minutes a day.</p>

  <div class="phase"><div class="n">01</div><div><b class="t">MAP &#8212; find your dog's number.</b>
  Every dog has a distance where he can see a trigger and still think and eat. You'll find
  yours in days, measured in parked cars &#8212; a ruler that exists on every street. This
  single number explains every failure you've ever had on a walk.</div></div>
  <div class="phase"><div class="n">02</div><div><b class="t">ANCHOR &#8212; install the new reflex.</b>
  Inside the Green Zone, your dog learns a new default: see the trigger &#8594; look back at you
  &#8594; get paid. Plus the Emergency U-Turn, drilled until it works at a trot, for the days
  the street cheats.</div></div>
  <div class="phase"><div class="n">03</div><div><b class="t">SHRINK &#8212; close the distance on a rule.</b>
  Three clean reps buy one car-length closer. One bad moment refunds two. No vibes, no
  guesswork &#8212; a ladder you can climb for the life of the dog, logged on paper where a
  bad day can't lie to you.</div></div>

  <img class="img" src="{{{{IMG:mockup-trio}}}}" alt="The Calm Walks system in print">
  <img class="img" src="{{{{IMG:inthewild}}}}" alt="The plan in use: day card and treat pouch by the door">

  <h2>Inside the 75-page plan</h2>
  <ul class="ckl fasc">{fasc}</ul>

  <div class="box">
    <h3 style="margin-top:0">Who this is NOT for</h3>
    <ul class="xl">
      <li>Dogs with a bite history that broke skin, or hard staring at children &#8212; that
      deserves an in-person credentialed professional, not a book (page 3 tells you exactly
      who to call and what their letters should be)</li>
      <li>Anyone shopping for an overnight personality transplant &#8212; this is a 21-day
      measured plan with worksheets, not a magic word</li>
      <li>People who want their dog to love the dog park &#8212; the goal here is calm
      indifference: boring, drama-free walks</li>
    </ul>
  </div>

  <!-- TESTIMONIAL SLOT 1 -->
  <!-- TESTIMONIAL SLOT 2 -->
  <!-- TESTIMONIAL SLOT 3 -->

  <h2>Everything you get today</h2>
  <table class="stack">
    <tr><td><b>The 21-Day Calm Walks Plan</b> &#8212; the 75-page designed workbook: diagnosis,
    the method, 21 day-pages with exact reps and pass/fail gates, maintenance</td><td>$47</td></tr>
    <tr><td><b>BONUS &#183; The Off-Leash Dog Protocol</b> &#8212; the feed-throw-voice-exit drill for
    the nightmare scenario (p. 55)</td><td>$17</td></tr>
    <tr><td><b>BONUS &#183; The Recovery Script</b> &#8212; the 10-second response + 48-hour reset
    after any blow-up (p. 56)</td><td>$9</td></tr>
    <tr><td><b>BONUS &#183; The Troubleshooting Codex</b> &#8212; 20 symptoms A&#8211;Z with fixes
    (pp. 60&#8211;61)</td><td>$17</td></tr>
    <tr><td><b>BONUS &#183; The 6-Sheet Log System</b> &#8212; baseline, triggers, routes, daily log,
    ladder tracker, week review (pp. 66&#8211;71)</td><td>$17</td></tr>
    <tr><td><b>BONUS &#183; The One-Page Field Summary</b> &#8212; the whole method on one printable
    page (p. 72)</td><td>$9</td></tr>
    <tr class="tot"><td>Total value</td><td>$116</td></tr>
  </table>
  <div class="price"><span class="was">$116</span><span class="now">$27</span></div>
  <a class="cta" href="{{{{URL:CHECKOUT}}}}">GET INSTANT ACCESS &#8212; $27
  <small>Download in 2 minutes &#183; works on phone, tablet, or printed</small></a>

  <div class="guarantee">
    <h3>&#128737; The 30-day keep-the-book guarantee</h3>
    <p>Run the first week &#8212; the measuring week. If you don't know more about your dog
    in 7 days than the last year of guessing taught you, email us within 30 days and we
    refund the $27, no questions, no return-the-PDF charade. The book stays yours.</p>
  </div>

  <h2>Questions, answered straight</h2>
  <div class="faq-q">Will this work on MY dog &#8212; fearful? frustrated-friendly? a rescue? an adolescent?</div>
  <div class="faq-a">The method is the same for fear-reactivity and frustration-reactivity (the
  &ldquo;he just wants to say hi&rdquo; screamers) &#8212; the plan flags where the two types differ.
  Age, breed, and backstory change the starting number, not the mechanics. Adolescents (6&#8211;18
  months) get their own regression notes.</div>
  <div class="faq-q">I've already tried treats and &ldquo;look at that.&rdquo; How is this different?</div>
  <div class="faq-a">The parts were never the problem &#8212; the dosage system was missing. This
  plan adds the measured distance, the pass/fail rule, and the progression ladder. Pills work;
  fistfuls of powder don't.</div>
  <div class="faq-q">How much time per day, honestly?</div>
  <div class="faq-a">Sixteen minutes: a 3-minute sniff in, 10 minutes of work, 3 minutes out.
  Plus two minutes of logging while the kettle's on. Days 5, 12, and 17 are deliberately easy.</div>
  <div class="faq-q">Is it videos? An app? A login?</div>
  <div class="faq-a">It's a designed 75-page PDF workbook &#8212; instant download, yours forever,
  built to be printed. On the sidewalk, paper beats screens: nothing to unlock with treat-greasy
  thumbs.</div>
  <div class="faq-q">Is this &ldquo;positive-only&rdquo;? Do I need special equipment?</div>
  <div class="faq-a">It uses no corrections &#8212; not for ideology, but plumbing: the method needs
  your dog's warning signals intact and triggers predicting good things. Gear list is page 26:
  a 6-ft leash, a front-clip harness, a treat pouch. About $40 if you own none of it.</div>
  <div class="faq-q">My dog has bitten someone. Should I buy this?</div>
  <div class="faq-a">Not as your main plan. Bite history needs an in-person credentialed
  professional &#8212; page 3 and page 65 tell you exactly how to find a good one. The book pairs
  well with that work and will make you their best-prepared client.</div>
  <div class="faq-q">What if it doesn't work for us?</div>
  <div class="faq-a">Thirty days, full refund, keep the book. The risk is ours; the worksheets
  are yours either way.</div>

  <h2 style="text-align:center">The door is open. Decide.</h2>
  <p class="sub">Tomorrow morning you can walk out the door with a plan in your pocket
  instead of a hope &#8212; knowing exactly what to measure, what to pay, and what to do when
  it goes sideways.</p>
  <a class="cta" href="{{{{URL:CHECKOUT}}}}">START THE 21 DAYS &#8212; $27
  <small>Instant access &#183; 30-day keep-the-book guarantee</small></a>
</div>"""
    return doc("The 21-Day Calm Walks Plan &#8212; The Green Zone Method&#8482;", body,
        bar="<b>LAUNCH PRICING:</b> $27 while our testimonial wall is still empty &#8212; the price rises when the reviews land.",
        desc="A measured 21-day plan for leash-reactive dogs: find your dog's threshold distance, install a new reflex, and shrink it on a strict rule.")

# ----------------------------------------------------------------- P2 CHECKOUT
def checkout():
    body = f"""
{LOGO}
<div class="wrap">
  <div class="kicker">&#128274; Secure checkout</div>
  <h1>You're 30 seconds from everything inside</h1>
  <p class="sub">Complete your order below &#8212; the download link arrives by email the
  moment payment clears.</p>

  <div class="box" style="padding:10px 10px 16px 10px">
    <!-- GHL ORDER FORM HERE -->
    <div style="text-align:center;color:{MUT};padding:60px 10px;border:2px dashed {PL};border-radius:12px;">
      [ GHL order-form element is inserted here in the funnel builder &#8212; FE product $27 ]</div>
  </div>
  <div class="micro">&#128274; 256-bit SSL encrypted &#183; Stripe-secured payment &#183; we never see your card number</div>

  <h3>What's included</h3>
  <ul class="ckl">
    <li>The 21-Day Calm Walks Plan &#8212; 75-page designed workbook (instant PDF)</li>
    <li>All five bonuses: Off-Leash Protocol, Recovery Script, Troubleshooting Codex,
    6-Sheet Log System, Field Summary</li>
    <li>30-day keep-the-book guarantee</li>
  </ul>
  <div class="price"><span class="was">$116 value</span><span class="now">$27</span></div>

  <h3>Right after you click</h3>
  <ol class="steps" style="margin-left:20px">
    <li><b>1. Instant email.</b> Your download link lands in your inbox within 60 seconds
    (subject: &ldquo;[Your Calm Walks Plan] &#8212; download inside&rdquo;).</li>
    <li><b>2. Tonight: read Part I.</b> Nine short pages on why everything failed. It will
    feel like someone finally drew the map.</li>
    <li><b>3. Tomorrow: Day 1.</b> A 20-minute scout walk. No training yet &#8212; just the
    first measurements. The plan does the thinking.</li>
  </ol>

  <div class="guarantee">
    <h3>&#128737; The 30-day keep-the-book guarantee</h3>
    <p>If the first week doesn't teach you more than the last year of guessing, one email
    refunds your $27 &#8212; and the book stays yours.</p>
  </div>
  <div class="micro">Questions? <a href="mailto:{{{{SUPPORT_EMAIL}}}}" style="color:{F2}">{{{{SUPPORT_EMAIL}}}}</a> &#8212; a human reads every message.</div>
</div>"""
    return doc("Secure Checkout &#8212; The 21-Day Calm Walks Plan", body,
        bar="<b>LAUNCH PRICING</b> &#183; one-time $27 &#183; no subscription",
        desc="Secure checkout for The 21-Day Calm Walks Plan.")

# ----------------------------------------------------------------- P3 UPSELL 1
def upsell1():
    body = f"""
<div class="otobar">One-time offer &#183; please don't refresh or close this page</div>
<div class="prog">&#10003; <b>Order confirmed</b> &nbsp;&#8594;&nbsp; <b>2. Your upgrade</b> &nbsp;&#8594;&nbsp; 3. Downloads</div>
{LOGO}
<div class="wrap">
  <a class="cta" href="{{{{URL:U1_ACCEPT}}}}">YES &#8212; ADD THE TOOLKIT FOR $97
  <small>One click &#183; uses the card you just entered &#183; instant download</small></a>
  <p class="confirm">&#10003; Your Calm Walks Plan is confirmed &#8212; before you head to your
  downloads, one question:</p>

  <div class="kicker">The Calm Walks Toolkit</div>
  <h1>Want the whole plan pre-built &#8212; so you never open the book on the sidewalk?</h1>
  <p class="sub">The book teaches the method. The Toolkit means each morning you grab ONE
  card and walk: today's goal, the three moves, the pass check, and the log line &#8212;
  already on it.</p>

  <div class="stats">
    <div><div class="n">21</div><div class="l">carry-one-card walk days</div></div>
    <div><div class="n">8</div><div class="l">cut-out pocket cards</div></div>
    <div><div class="n">0</div><div class="l">decisions before any walk</div></div>
  </div>

  <img class="img" src="{{{{IMG:toolkit-stack}}}}" alt="The Calm Walks Toolkit card stack">

  <ul class="ckl">
    <li><b>21 full-page Day Cards</b> &#8212; the entire plan, one card per walk, pocket-sized thinking</li>
    <li><b>The 3-poster set</b> &#8212; the Zone Map for the fridge, the emergency Red Poster for the leash hook, the Signals poster for the family</li>
    <li><b>8 cut-out pocket cards</b> &#8212; Food Test, Loop, U-Turn, Recovery, Ladder, Session, Signals, and what to say to humans</li>
    <li><b>7 walk-log sheets + both planners</b> &#8212; every page the method asks you to fill, pre-built</li>
  </ul>

  <a class="cta" href="{{{{URL:U1_ACCEPT}}}}">YES &#8212; ADD THE TOOLKIT FOR $97
  <small>One click &#183; no re-entering card details</small></a>
  <a class="decline" href="{{{{URL:U1_DECLINE}}}}">No thanks &#8212; I'd rather copy the worksheets and build my own cards by hand</a>

  <h2>Why owners add this</h2>
  <div class="cardg">
    <div><b>The 6am problem</b><p>Nobody re-reads a chapter before dawn. A card in the jacket
    pocket means the plan happens even when your brain hasn't booted.</p></div>
    <div><b>The family problem</b><p>Partners and dog-sitters won't read a 75-page book. They
    will follow a card and a fridge poster. Now the method survives delegation.</p></div>
    <div><b>The chaos problem</b><p>Mid-ambush is no time for an index. The Red Poster and
    pocket cards put the scripts where your hands already are.</p></div>
  </div>

  <h3>How it works</h3>
  <ol class="steps" style="margin-left:20px">
    <li><b>1.</b> Click YES &#8212; it's added to your order with one click.</li>
    <li><b>2.</b> Print this week's cards (any home printer, grayscale is fine).</li>
    <li><b>3.</b> Tomorrow: grab Card 1, pouch, leash. The book stays on the shelf.</li>
  </ol>

  <table class="stack">
    <tr><td>21 Day Cards (the plan, pre-built)</td><td>$67</td></tr>
    <tr><td>Poster set &#215;3</td><td>$27</td></tr>
    <tr><td>8 pocket cards + 7 logs + 2 planners</td><td>$37</td></tr>
    <tr class="tot"><td>Total value</td><td>$131</td></tr>
  </table>
  <div class="price"><span class="was">$131</span><span class="now">$97</span></div>

  <p class="sub"><b>This page is the only place the Toolkit exists at one click.</b> It's
  available later only at full list price, with a separate checkout &#8212; this screen is
  the shortcut.</p>
  <a class="cta" href="{{{{URL:U1_ACCEPT}}}}">YES &#8212; ADD THE TOOLKIT FOR $97
  <small>30-day guarantee covers this too</small></a>
  <a class="decline" href="{{{{URL:U1_DECLINE}}}}">No thanks &#8212; take me to my downloads</a>
</div>"""
    return doc("One-Time Offer &#8212; The Calm Walks Toolkit", body,
        desc="Add the done-for-you Calm Walks Toolkit to your order with one click.")

# ----------------------------------------------------------------- P4 DOWNSELL
def downsell():
    body = f"""
<div class="otobar">Wait &#8212; one more option &#183; one time only</div>
<div class="prog">&#10003; <b>Order confirmed</b> &nbsp;&#8594;&nbsp; <b>2. Your upgrade</b> &nbsp;&#8594;&nbsp; 3. Downloads</div>
{LOGO}
<div class="wrap">
  <a class="cta cta-g" href="{{{{URL:DS_ACCEPT}}}}">FINE &#8212; I'LL TAKE IT AT HALF PRICE: $47
  <small>One click &#183; same Toolkit, every page of it</small></a>

  <div class="kicker">Same Toolkit &#183; one-time courtesy price</div>
  <h1>Same Toolkit. <span style="color:{CL}">Half price.</span></h1>
  <p class="sub">No tricks and no &ldquo;lite&rdquo; version: the identical 36-page Toolkit
  from the last page &#8212; all 21 day cards, all 3 posters, all 8 pocket cards, every log
  &#8212; at $47 instead of $97.</p>

  <div class="cardg">
    <div><b>21 Day Cards</b><p>the whole plan, one card per walk</p></div>
    <div><b>3 Posters</b><p>fridge zone map &#183; leash-hook emergencies &#183; family signals</p></div>
    <div><b>8 Pocket Cards</b><p>the scripts, wallet-sized, cut and go</p></div>
    <div><b>7 Logs + 2 Planners</b><p>every sheet the method asks for</p></div>
  </div>

  <div class="box">
    <p style="margin:0"><b>Why the discount, honestly:</b> you said no at full price, and
    that's fair. But the data on plans like this is blunt &#8212; the printed-card owners
    follow through at much higher rates than the good-intentions owners. I'd rather you
    have the cards and finish the plan than save me the margin. One-time means one-time:
    this price doesn't exist after this page.</p>
  </div>

  <div class="price"><span class="was">$97</span><span class="now">$47</span></div>
  <a class="cta cta-g" href="{{{{URL:DS_ACCEPT}}}}">ADD THE TOOLKIT &#8212; $47
  <small>One click &#183; instant download &#183; same guarantee</small></a>
  <a class="decline" href="{{{{URL:DS_DECLINE}}}}">No thanks, I'll pass forever &#8212; on to the next step</a>
</div>"""
    return doc("One More Option &#8212; The Toolkit at Half Price", body,
        desc="The Calm Walks Toolkit, one-time half-price offer.")

# ----------------------------------------------------------------- P5 UPSELL 2
def upsell2():
    body = f"""
<div class="otobar">Final upgrade &#183; step 2 of 2 &#183; please don't close this page</div>
<div class="prog">&#10003; <b>Order confirmed</b> &nbsp;&#8594;&nbsp; &#10003; Upgrade &nbsp;&#8594;&nbsp; <b>Final step</b></div>
{LOGO}
<div class="wrap">
  <a class="cta" href="{{{{URL:U2_ACCEPT}}}}">YES &#8212; ADD THE HARD CASES MANUAL FOR $47
  <small>One click &#183; instant download</small></a>

  <div class="kicker">The Hard Cases Manual</div>
  <h1>The Plan handles the walk. THIS handles everything that tries to break it.</h1>
  <p class="sub">Nine situations where the normal rules bend &#8212; each with the full
  four-page treatment: the physics, the setup, the three-phase protocol, the pitfalls.</p>

  <div class="xstrip">
    <div><span>&#10005;</span>Not a repeat of the Plan &#8212; zero overlapping pages</div>
    <div><span>&#10005;</span>Not theory &#8212; protocols with rep counts and pass gates</div>
    <div><span>&#10005;</span>Not for &ldquo;someday&rdquo; &#8212; triage page tells you which case to run first</div>
  </div>

  <div class="stats">
    <div><div class="n">9</div><div class="l">hard cases, scripted</div></div>
    <div><div class="n">36</div><div class="l">protocol pages</div></div>
    <div><div class="n">4</div><div class="l">pages per case, same shape</div></div>
  </div>

  <img class="img" src="{{{{IMG:manual-mock}}}}" alt="The Hard Cases Manual">

  <h2>The nine cases</h2>
  <div class="cardg">
    <div><b>01 &#183; The Off-Leash Charge</b><p>the fire drill: feed, throw, voice, exit &#8212; rehearsed to reflex</p></div>
    <div><b>02 &#183; Hallways &amp; Elevators</b><p>reactivity where distance is rationed: timetables, thresholds, the skip-the-car rule</p></div>
    <div><b>03 &#183; The Vet Visit</b><p>spend the least bucket possible, then pre-pay the 48-hour invoice</p></div>
    <div><b>04 &#183; Night Walks</b><p>ambush-proofing: surcharges, corners, light &#8212; and the road back to daylight</p></div>
    <div><b>05 &#183; The Multi-Dog Household</b><p>solo season, the audience drill, and the gated re-merger</p></div>
    <div><b>06 &#183; Fence &amp; Window Barkers</b><p>shut down the 8-hour-a-day explosion gym (highest ROI in the system)</p></div>
    <div><b>07 &#183; Car Reactivity</b><p>loading, riding, and window explosions &#8212; the glass is your ladder</p></div>
    <div><b>08 &#183; Doorbell &amp; Visitors</b><p>rewire the bell, gate the entry, brief the humans</p></div>
    <div><b>09 &#183; The Regression Week</b><p>the calm investigation that replaces the panic &#8212; read it before you need it</p></div>
  </div>

  <h2>Why this pairs with the Plan</h2>
  <ol class="steps" style="margin-left:20px">
    <li><b>1. The Plan builds the skill; the Manual protects it.</b> One unmanaged fence-war or
    botched vet week can tax a month of ladder work &#8212; these are the leaks, plugged.</li>
    <li><b>2. It's the difference between knowing the method and owning it anywhere.</b>
    Apartments, cars, night shifts, second dogs &#8212; your life doesn't pause for training plans.</li>
    <li><b>3. Case 9 alone pays for it.</b> Every dog regresses eventually. Owners with a
    script run a one-week reset; owners without one quit.</li>
  </ol>

  <div class="faq-q">Do I need it on day 1?</div>
  <div class="faq-a">You need it the day the street cheats &#8212; which tends not to book an
  appointment. Most buyers run one case in week one (usually 06 or 02) and shelve the rest
  until needed.</div>
  <div class="faq-q">Is it covered by the same guarantee?</div>
  <div class="faq-a">Same 30 days, same keep-the-book deal.</div>
  <div class="faq-q">Will there be another chance at this price?</div>
  <div class="faq-a">This one-click screen is the launch arrangement; later it's list price
  with its own checkout.</div>

  <div class="price"><span class="was">$67 list</span><span class="now">$47</span></div>
  <a class="cta" href="{{{{URL:U2_ACCEPT}}}}">YES &#8212; ADD THE HARD CASES MANUAL FOR $47
  <small>One click &#183; finishes your system</small></a>
  <a class="decline" href="{{{{URL:U2_DECLINE}}}}">No thanks &#8212; take me to my downloads</a>
</div>"""
    return doc("Final Upgrade &#8212; The Hard Cases Manual", body,
        desc="Nine hard situations, fully scripted: the certainty layer for the Green Zone Method.")

# ----------------------------------------------------------------- P6 THANK YOU
def thankyou():
    body = f"""
{LOGO}
<div class="wrap">
  <div style="text-align:center;margin-top:10px">
    <span style="background:{F2};color:#fff;border-radius:20px;padding:8px 22px;font-weight:900;
    font-size:14px;letter-spacing:1px">&#10003; PAYMENT CONFIRMED</span>
  </div>
  <h1>You're 30 seconds from being inside</h1>
  <p class="sub">Your downloads are on their way to your inbox right now.</p>

  <div class="box">
    <h3 style="margin-top:0">&#128231; Find your delivery email</h3>
    <p>Search your inbox for: <b>&ldquo;[Your Calm Walks Plan] &#8212; download inside&rdquo;</b></p>
    <p style="margin-bottom:0" class="micro" >Nothing after 5 minutes? Check spam/promotions, then email
    <a href="mailto:{{{{SUPPORT_EMAIL}}}}" style="color:{F2}">{{{{SUPPORT_EMAIL}}}}</a> and a human will
    re-send it fast. (If you added the Toolkit or the Manual, each arrives in its own email.)</p>
  </div>

  <h2>Here's exactly what happens now</h2>
  <ol class="steps" style="margin-left:20px">
    <li><b>1. Tonight (15 minutes):</b> read pages 7&#8211;15 &#8212; Part I, &ldquo;Why Everything
    Failed.&rdquo; It's the diagnosis. Everything finally makes sense in nine pages.</li>
    <li><b>2. Tomorrow morning:</b> Day 1 &#8212; the scout walk. Your normal route, a notes app,
    zero training. The plan starts with measuring, so it cannot start with failing.</li>
    <li><b>3. This week:</b> find your dog's number (it's the whole of week 1). Sixteen
    minutes a day.</li>
    <li><b>4. Print what helps:</b> the worksheets (pages 66&#8211;71) &#8212; or your Toolkit cards
    if you grabbed them.</li>
  </ol>

  <div class="guarantee">
    <h3>One promise to hold onto</h3>
    <p>Week one feels almost too easy &#8212; that's by design. A measured problem stops being
    a monster. By Sunday you'll have a number in pen, and a number is something you can
    shrink. See you on the ladder.</p>
  </div>
  <div class="micro">Support: <a href="mailto:{{{{SUPPORT_EMAIL}}}}" style="color:{F2}">{{{{SUPPORT_EMAIL}}}}</a>
  &#183; answered by a human, usually same-day.</div>
</div>"""
    return doc("You're In &#8212; CalmWalk", body,
        desc="Order confirmed: your Calm Walks Plan downloads are on the way.")

PAGES = {
    "p1-sales.html": sales, "p2-checkout.html": checkout, "p3-upsell1.html": upsell1,
    "p4-downsell.html": downsell, "p5-upsell2.html": upsell2, "p6-thankyou.html": thankyou,
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in PAGES.items():
        with open(os.path.join(here, name), "w") as f:
            f.write(fn())
        print("wrote", name)
