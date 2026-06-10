"""U1 — The Calm Walks Toolkit: 21 DFY daily walk cards, posters, pocket cards, logs."""
from design import *

NAME = "CalmWalk-Toolkit"
BRAND = "THE CALM WALKS TOOLKIT"
AM, F, F2, SG, PL, CR, CL, GD, INK, MUT = (PALETTE[k] for k in
    ("amber", "forest", "forest2", "sage", "pale", "cream", "clay", "gold", "ink", "mut"))

def tpage(body, pno=None, tab=None, tabcolor=None):
    return page(body, pno=pno, part=tab, partcolor=tabcolor, brand=BRAND)

# ---- 21 day cards: distilled card-speak versions of the FE plan
DAYS = [
 (1, "MAP", "Scout walk. Change nothing.", "Normal route, quiet hour. You are a surveyor today.",
  ["Note every NOTICE: what / how many cars / what his mouth did",
   "Handle triggers your old way &#8212; just write each one down after",
   "Home: fill the Trigger Inventory; circle the most common trigger"],
  "3+ sightings logged", "Blow-up = data. Log the distance, add 3 cars: that's tomorrow's start line."),
 (2, "MAP", "Food Test day. Get the provisional number.", "Quiet hour. 100 pea-size soft treats. Long-range sightings.",
  ["At each sighting: ONE treat at the nose. Say nothing",
   "Instant grab &#8594; next test 2 cars closer. Slow/refused &#8594; 2 cars farther",
   "Smallest instant-grab distance = the provisional number. Write it in pen"],
  "A number on paper, 3+ tests, 2+ triggers", "Refuses everywhere? Bucket's full: quiet walk now, retest tomorrow."),
 (3, "MAP", "Confirm it: 3 greens in a row.", "Same hour, same route. Today the number becomes official.",
  ["Food test at yesterday's number on 3 different sightings",
   "3 instant grabs at the same count = CONFIRMED. Any yellow: +2 cars, restart count",
   "Watch for his first loading signal (mouth!) and note his tell"],
  "Number circled in pen + his tell named", "Numbers bouncing? Dogs and people are different trigger classes &#8212; confirm the worst class."),
 (4, "MAP", "Build the heist map.", "Kitchen table first, then one rehearsal walk of Route A.",
  ["Mark every trigger house / pinch / dog-park corner in red on the Route Planner",
   "Route A passes sight-lines AT or BEYOND the number; mark escapes with E",
   "Route B = the bunker (near-zero sightings). Walk Route A once; fix the map where it lies"],
  "Two routes drawn, escapes marked", "Ambushed mid-rehearsal? Better now than next week. Add the red box, re-route tonight."),
 (5, "MAP", "Quiet Day: sniffari.", "Boring green space, longest leash, zero agenda. This IS the work.",
  ["20 minutes; the nose drives, you steer nothing",
   "Fewer than ten words total",
   "Tonight: re-read the marker + Loop pages (FE pp. 21&#8211;24)"],
  "15+ nose-down minutes, no training", "Pacing/scanning instead of sniffing = very full bucket. Repeat tomorrow; shift the plan a day."),
 (6, "MAP", "Charge the marker.", "Kitchen, post-breakfast. Then an easy J-walk on Route B.",
  ["&ldquo;YES&rdquo; &#8594; ONE-second pause &#8594; treat at the knee. 20 reps &#215; 2 sets",
   "Rep 15 check: say YES while he looks away &#8212; head should whip around",
   "Route B, 12 min: practice the loose J only (two hands, gather don't winch)"],
  "Head-whip on YES; J held 80% of the walk", "Staring at your pouch hand? The hand is moving too early. Word, count one-banana, THEN reach."),
 (7, "MAP", "First Loops &#8212; easy mode. Close week 1.", "Route A at the number +2 cars. It should feel like a card trick.",
  ["Re-measure (1 food test). Then: let him notice &#8594; WAIT &#8594; head-flick back &#8594; YES &#8594; pay at knee",
   "6&#8211;8 loops max across 2&#8211;3 sightings; quit on a win",
   "Home: Week Review &#8212; number, routes, marker: MAP complete"],
  "4+ loops with the flick inside 5 seconds", "Can't look away from the trigger? You're tight even at +2. Add 2 more. Easy mode has no floor."),
 (8, "ANCHOR", "Loops at the real number. Static triggers.", "Route A, quiet hour. Training wheels off.",
  ["60-sec re-measure first. Yellow? Work at +2 today &#8212; zero shame",
   "8&#8211;12 loops on stationary triggers; pay every flick at the knee",
   "Jackpot (5 treats) any look-back from a trigger that stares back"],
  "8+ clean loops, latency shrinking", "Mid-session collapse = something stacked. U-turn out, sniff 3 min, end early on any win."),
 (9, "ANCHOR", "Loops vs MOVING triggers.", "Position so triggers cross LATERALLY at distance. Head-on stays banned.",
  ["Re-measure on a mover (often static number +2). Work there",
   "Loop as always; movers slow the flick &#8212; pay slow ones, jackpot fast ones",
   "A mover turning toward you = ambush, not a rep: U-turn, reset, resume"],
  "6+ mover loops, zero red moments", "Locked-on sniper stare = too close for motion. +2 cars and retry. Screamers: 4&#8211;5 loops, leave early."),
 (10, "ANCHOR", "U-turn drill: ten peacetime reps.", "Route B. Today trains YOUR feet, not his feelings.",
  ["&ldquo;THIS WAY!&rdquo; (free-pizza voice) &#8594; YOUR body turns first &#8594; pay on the move",
   "10 reps: 180s, left arcs, right arcs, two at a trot",
   "Last 2: full fake-ambush sequence ending in a 3-treat grass scatter"],
  "By rep 7 he wheels on the CUE, leash loose", "Planted dog? Lure reps 1&#8211;3 with the treat at his nose, fade by rep 5."),
 (11, "ANCHOR", "Mix it all: loops + U-turns + the finder.", "Route A. Real walks are judgment calls; today you drill the judgment.",
  ["Read zones aloud (quietly): green = loop, yellow edge = U-turn NOW (it counts as a rep)",
   "Pinched pass? FINDER: scatter 3 treats in grass at the widest arc, let him hoover through it",
   "Cap at 14 actions; end on a loop if the street allows"],
  "3+ correct zone calls; 1 mid-loop U-turn", "&ldquo;One more loop&rdquo; into yellow is how day-11s die. The early exit is the advanced move."),
 (12, "ANCHOR", "Quiet Day II + gear audit.", "Sniffari rules. After 4 working days, the drain is the assignment.",
  ["20 min, nose drives, &lt;10 words",
   "Tonight: check pouch seams, harness fit (two fingers), leash clip",
   "Skim the FE emergency pages (54&#8211;59) once &#8212; load the scripts before you need them"],
  "15+ nose-down minutes, gear checked", "Feels like losing momentum? Rest days are where gains consolidate. Champions take the rest day."),
 (13, "ANCHOR", "The two-trigger session.", "Route A, slightly busier window. The skill: the SECOND sighting.",
  ["Set 1: re-measure, 5&#8211;6 loops, end clean",
   "Re-measure AGAIN before set 2 &#8212; expect +1 to +2 surcharge. Honor it",
   "Set 2 at the fatter distance: 4&#8211;5 loops, end early, 5-min sniff out"],
  "Both sets green; set 2 wider ON PURPOSE", "Set 1 blew up? Today becomes a Quiet Day from that second. One bad set costs a day, never the plan."),
 (14, "ANCHOR", "Re-measure ceremony.", "Original quiet hour &#8212; day-3 conditions, on purpose.",
  ["Formal day-3 protocol: descending food tests, 3 greens to confirm. No loops first",
   "Write the new number NEXT TO day-3's. Most: 1&#8211;3 cars tighter. Flat is fine too",
   "Victory lap: 6 easy loops at the new number; jackpot the best one. Week Review"],
  "New number in pen; loops feel routine", "Number UP? Almost always bucket/weather/hidden stressor. Re-run in 2 days before concluding anything."),
 (15, "SHRINK", "The ladder: earn your first car.", "Route A. Rung 1 = yesterday's number.",
  ["3 CLEAN loops (instant eat, &lt;3-sec flick, soft mouth) across 2+ sightings = bell rings",
   "Step ONE car closer &#8594; food test &#8594; green? New rung. Work it",
   "2 rungs = strong day. 3 = ceiling. Log the ending rung"],
  "1 earned car with 3-for-3 receipts", "Red on a new rung? Refund 2 cars instantly, finish wide, note what differed. The ladder forgives; it bills."),
 (16, "SHRINK", "Ladder II: movers on the rungs.", "Manufactured-traffic spot ok. Clean now includes motion.",
  ["Re-measure on a mover; that's rung 1 (often +1&#8211;2 over yesterday)",
   "3 clean MOVER loops = 1 car. Statics between sets as palate cleansers",
   "Head-on traffic: still banned. Cross early, arc wide, no apology"],
  "1 mover-car earned, statics stayed boring", "Barking trigger collapses the rung? Loud dogs are their own class &#8212; separate number, separate ladder."),
 (17, "SHRINK", "Banked-win day. Deposit on purpose.", "Route A at the ladder rung +2. It should feel almost silly.",
  ["8 boringly perfect loops across 2&#8211;3 sightings",
   "Jackpot the single best flick like he returned a lost wallet",
   "Quit at 14 minutes. No ladder thoughts today"],
  "8 easy loops + 1 party + early quit", "Even +2 reads yellow? The bucket is talking. Convert to a full Quiet Day, shift the week by one."),
 (18, "SHRINK", "New location: pay the transfer tax.", "Somewhere he barely knows. Numbers reset fatter here &#8212; planned.",
  ["Full re-measure from generously far: expect +2 to +4 cars. That's the tax, not a relapse",
   "Easy loops at the local number until smooth, then ladder ONE rung",
   "Log the home/away gap &#8212; watch it close over the next month"],
  "Away-number measured + 6 clean loops", "Unworkable chaos? Work from beside your parked car &#8212; cars are portable Green Zones &#8212; or leave. Scouting failures are cheap."),
 (19, "SHRINK", "Ambush rehearsal: drill the nightmare.", "Pick a blind corner in advance (hedge, parked van). Empty, every time.",
  ["Normal loops first, wherever the ladder stands",
   "3 rehearsals at the corner AS IF a dog were there: exhale &#8594; &ldquo;THIS WAY!&rdquo; &#8594; turn &#8594; pay moving &#8594; scatter at 2 cars",
   "Make the third rehearsal at a jog"],
  "3 crisp sequences, party-toned under pressure", "Voice goes flat because &ldquo;nothing's there&rdquo;? YOUR voice-under-load is the skill. He can't tell what you're rehearsing."),
 (20, "SHRINK", "The parallel walk.", "Park path with one-way dog traffic. Following reads as pack drift, not threat.",
  ["Fall in BEHIND a calm leashed dog at rung +1, matching pace",
   "Pay every glance-and-back; JACKPOT if he forgets the dog and just walks",
   "3&#8211;4 minutes, peel off on an arc BEFORE it degrades. 1&#8211;2 follows total"],
  "3+ soft-bodied minutes of following", "Following turns into stiff stalking? Too close for this dog: +2 cars or pick a slower target."),
 (21, "SHRINK", "Graduation: the normal walk.", "Route A at a NORMAL hour &#8212; the time you used to avoid. Full kit.",
  ["Walk like a person walking a dog: loops where offered, U-turns where owed, finder if pinched",
   "Mid-walk: one formal food test at the best rung &#8212; the book's final number",
   "Home: final Week Review + the 3-sentence letter to future-you"],
  "Route done at human hours, number logged", "A clean U-turn on the graduation walk is a PASS, not an asterisk. The system is installed; huskies still exist."),
]

PHASECOLORS = {"MAP": F2, "ANCHOR": AM, "SHRINK": F}

def day_card(d):
    n, phase, goal, setup, steps, passline, fixline = d
    pc = PHASECOLORS[phase]
    steps_html = "".join(
        f'<table style="width:100%;border-collapse:collapse;margin-bottom:10px;"><tr>'
        f'<td style="width:46px;vertical-align:top;">'
        f'<div style="background:{pc};color:#FFF;border-radius:50%;width:34px;height:34px;'
        f'text-align:center;line-height:34px;font-size:17px;font-weight:bold;">{i+1}</div></td>'
        f'<td style="font-size:15.5px;line-height:1.5;vertical-align:middle;">{s}</td></tr></table>'
        for i, s in enumerate(steps))
    body = f'''
<div class="pad">
  <div style="background:{F};border-radius:14px;color:{CR};padding:18px 22px;margin-bottom:14px;">
    <table style="width:100%;border-collapse:collapse;"><tr>
      <td style="font-family:'Roboto Slab',serif;font-size:44px;font-weight:bold;color:{GD};white-space:nowrap;padding-right:18px;">DAY {n}</td>
      <td><div style="font-size:11px;letter-spacing:2.5px;color:{SG};">WEEK {(n - 1) // 7 + 1} &#183; {phase} PHASE</div>
      <div style="font-size:18px;font-weight:bold;line-height:1.3;">{goal}</div></td>
      <td style="text-align:right;vertical-align:top;">
        <span style="background:{pc};color:#FFF;border-radius:10px;padding:3px 12px;font-size:11px;font-weight:bold;letter-spacing:1px;">CARD {n}/21</span></td>
    </tr></table>
  </div>
  <div style="font-size:13.5px;color:{MUT};margin-bottom:14px;"><b style="color:{F};">SETUP &#8212;</b> {setup}</div>
  {h3("THE THREE THINGS")}
  {steps_html}
  <table style="width:100%;border-collapse:separate;border-spacing:0 0;margin-top:6px;"><tr>
    <td style="width:49%;background:{PL};border:2px solid {SG};border-radius:10px;padding:10px 14px;vertical-align:top;">
      <div style="font-size:11px;font-weight:bold;letter-spacing:2px;color:{F2};">&#10003; TODAY PASSES WHEN</div>
      <div style="font-size:13.5px;margin-top:4px;">{passline}</div></td>
    <td style="width:2%;"></td>
    <td style="background:{INK};border-radius:10px;padding:10px 14px;vertical-align:top;">
      <div style="font-size:11px;font-weight:bold;letter-spacing:2px;color:{GD};">&#9889; IF IT GOES WRONG</div>
      <div style="font-size:13px;margin-top:4px;color:{CR};">{fixline}</div></td>
  </tr></table>
  <div style="margin-top:16px;">
    <table style="width:100%;border-collapse:collapse;">
      <tr><td style="width:33%;font-size:11px;letter-spacing:1.5px;color:{MUT};font-weight:bold;">TODAY'S NUMBER (CARS)<div style="border-bottom:1.6px solid {MUT};height:26px;"></div></td>
      <td style="width:4%;"></td>
      <td style="width:30%;font-size:11px;letter-spacing:1.5px;color:{MUT};font-weight:bold;">CLEAN REPS<div style="border-bottom:1.6px solid {MUT};height:26px;"></div></td>
      <td style="width:4%;"></td>
      <td style="font-size:11px;letter-spacing:1.5px;color:{MUT};font-weight:bold;">MOUTH SCORE (I / S / R)<div style="border-bottom:1.6px solid {MUT};height:26px;"></div></td></tr>
    </table>
  </div>
  <div style="margin-top:18px;">
    <div style="font-size:11px;letter-spacing:1.5px;color:{MUT};font-weight:bold;">WHAT HAPPENED (ONE HONEST SENTENCE) &#183; AND ONE GOOD MOMENT TO KEEP</div>
    {('<div style="border-bottom:1.6px solid ' + MUT + ';height:34px;"></div>') * 3}
  </div>
  <div style="position:absolute;left:72px;right:72px;bottom:74px;border-top:2px dashed {MUT};padding-top:10px;font-size:11px;color:{MUT};letter-spacing:1px;text-align:center;">
    CARRY THIS CARD, NOT THE BOOK &#183; FULL DETAIL: PLAN PAGE FOR DAY {n} &#183; EMERGENCIES: RED POSTER<br/>
    THE GREEN ZONE METHOD&#8482; &#183; MAP &#183; ANCHOR &#183; SHRINK</div>
</div>'''
    return body

def cover():
    stack = "".join(
        f'<div style="position:absolute;left:{84 + i * 14}px;top:{430 + i * 12}px;width:430px;height:270px;'
        f'background:{["#FFFFFF", "#F2EDE2", "#EAE4D6"][i % 3]};border:2px solid {PALETTE["line"]};border-radius:14px;"></div>'
        for i in range(2, -1, -1))
    card = f'''
<div style="position:absolute;left:84px;top:430px;width:430px;height:270px;background:#FFF;
     border:2px solid {PALETTE['line']};border-radius:14px;padding:22px;">
  <table style="border-collapse:collapse;"><tr>
    <td style="font-family:'Roboto Slab',serif;font-size:34px;font-weight:bold;color:{GD};padding-right:14px;">DAY 8</td>
    <td><div style="font-size:9px;letter-spacing:2px;color:{SG};">WEEK 2 &#183; ANCHOR PHASE</div>
    <div style="font-size:14px;font-weight:bold;color:{INK};">Loops at the real number.</div></td></tr></table>
  <div style="margin-top:14px;">{"".join(f'<div style="margin-bottom:8px;"><span style="background:{AM};color:#FFF;border-radius:50%;display:inline-block;width:22px;height:22px;text-align:center;line-height:22px;font-size:12px;font-weight:bold;">{k}</span><span style="font-size:12px;color:{INK};">&nbsp; {t}</span></div>' for k, t in [(1, "60-sec re-measure first"), (2, "8&#8211;12 loops, pay at the knee"), (3, "Jackpot the brave look-backs")])}</div>
</div>'''
    body = f'''
<div style="background:{F};width:816px;height:1056px;position:relative;">
  <div style="padding:90px 84px 0 84px;">
    <div style="font-size:13px;letter-spacing:5px;color:{GD};font-weight:bold;">CALMWALK &#183; COMPANION TO THE GREEN ZONE METHOD&#8482;</div>
    <div style="border-top:3px solid {AM};width:72px;margin:24px 0;"></div>
    <div style="font-family:'Roboto Slab',serif;font-size:62px;line-height:1.08;color:{CR};font-weight:bold;">The Calm Walks<br/>Toolkit</div>
    <div style="font-size:19px;line-height:1.6;color:{PL};max-width:560px;margin-top:22px;">
      The plan, pre-built: 21 carry-one-card walk days, the poster set, cut-out pocket cards,
      and every log the method needs. Zero teaching. Grab today's card and go.</div>
    <div style="margin-top:30px;"><span style="background:{AM};color:{INK};border-radius:14px;padding:7px 18px;
      font-size:13px;font-weight:bold;letter-spacing:2px;">SKIP THE BUILD &#183; WALK THE PLAN</span></div>
  </div>
  {stack}{card}
  <div style="position:absolute;bottom:30px;left:0;right:0;text-align:center;font-size:11px;letter-spacing:3px;color:{PL};">
    21 DAY CARDS &#183; 3 POSTERS &#183; 8 POCKET CARDS &#183; 7 LOG SHEETS &#183; PLANNERS</div>
</div>'''
    return page(body, chrome=False)

def how_to():
    b = pad(
        kicker("HOW THIS TOOLKIT WORKS")
        + h1("Print. Cut. Clip. Walk.")
        + lead("This is the done-for-you layer of the Green Zone Method. Nothing here teaches; "
               "everything here deploys.")
        + table(["Piece", "What you do with it", "Pages"],
            [["<b>21 Day Cards</b>", "print the week, carry ONE card per walk &#8212; goal, three moves, "
              "pass check, and the log strip, all on the card", "3&#8211;23"],
             ["<b>Poster set</b>", "the Zone Map on the fridge; the Red Poster (emergencies) by the leash "
              "hook; the Signals poster wherever the family will actually look", "24&#8211;26"],
             ["<b>Pocket cards</b>", "cut the 8 wallet cards; laminate if you're fancy; one lives in the "
              "treat pouch forever", "27"],
             ["<b>Daily logs</b>", "one row per walk, two minutes, kettle on; 7 sheets cover the plan", "28&#8211;34"],
             ["<b>Planners</b>", "route map + trigger inventory, toolkit-sized", "35&#8211;36"]])
        + callout("key", "&#9733; THE WHOLE POINT",
            p("On the sidewalk, a book is a liability &#8212; pages flap, dogs lunge, coffee spills. "
              "A single card in a jacket pocket is the difference between knowing the plan and "
              "<b>running</b> it. Print this once and the next three weeks require zero decisions "
              "before any walk."))
        + h3("PRINT SETTINGS")
        + p("US Letter, portrait, 100% scale (no &ldquo;fit to page&rdquo;), color if you can. "
            "Cards work fine in grayscale; the posters earn their color. Re-print freely &#8212; "
            "it's your copy.", "small")
    )
    return tpage(b, pno=2)

def poster_zone():
    b = f'''<div style="padding:50px 60px 90px 60px;">
  {kicker("POSTER 01 &#183; THE FRIDGE ONE")}
  <div style="font-family:'Roboto Slab',serif;font-size:40px;font-weight:bold;color:{F};margin-bottom:16px;">The Zone Map</div>
  {fig(svg_zone_map(680, 486))}
  <table style="width:100%;border-collapse:separate;border-spacing:8px 0;margin-top:16px;">
    <tr>
    <td style="width:33%;background:{F2};border-radius:12px;color:#FFF;padding:14px;text-align:center;">
      <div style="font-size:15px;font-weight:bold;letter-spacing:1px;">GREEN</div>
      <div style="font-size:13px;margin-top:4px;">eats instantly &#8594; WORK THE LOOP</div></td>
    <td style="width:33%;background:{GD};border-radius:12px;color:{INK};padding:14px;text-align:center;">
      <div style="font-size:15px;font-weight:bold;letter-spacing:1px;">YELLOW</div>
      <div style="font-size:13px;margin-top:4px;">mouth closes &#8594; LEAVE, CALMLY</div></td>
    <td style="background:{CL};border-radius:12px;color:#FFF;padding:14px;text-align:center;">
      <div style="font-size:15px;font-weight:bold;letter-spacing:1px;">RED</div>
      <div style="font-size:13px;margin-top:4px;">explosion &#8594; OUT FAST + 48H QUIET</div></td>
    </tr></table>
  <div style="text-align:center;margin-top:18px;font-size:14px;color:{MUT};">
    Every dog has a number. Find it. Work inside it. Shrink it on the rule. &#8212; THE GREEN ZONE METHOD&#8482;</div>
</div>'''
    return tpage(b, pno=24, tab="POSTER", tabcolor=F2)

def poster_red():
    def block(n, title, lines, color):
        lis = "".join(f'<div style="font-size:14px;line-height:1.5;margin-bottom:5px;color:#FFF;">&#8226; {l}</div>' for l in lines)
        return (f'<td style="width:49%;background:{color};border-radius:14px;padding:18px;vertical-align:top;">'
                f'<div style="font-size:12px;letter-spacing:2px;color:{GD};font-weight:bold;">{n}</div>'
                f'<div style="font-size:19px;font-weight:bold;color:#FFF;margin:4px 0 10px 0;">{title}</div>{lis}</td>')
    b = f'''<div style="padding:50px 60px 90px 60px;">
  {kicker("POSTER 02 &#183; THE LEASH-HOOK ONE &#183; EMERGENCIES")}
  <div style="font-family:'Roboto Slab',serif;font-size:40px;font-weight:bold;color:{CL};margin-bottom:18px;">When It Goes Wrong</div>
  <table style="width:100%;border-collapse:separate;border-spacing:8px;">
    <tr>{block("AMBUSH &#183; TRIGGER TOO CLOSE", "THE U-TURN",
        ["One exhale", "&ldquo;THIS WAY!&rdquo; &#8212; free-pizza voice", "YOUR body turns first &#8594; GO",
         "Pay at the knee, on the move", "At 2+ cars: scatter 3 treats in grass"], F)}
    {block("LOOSE DOG INBOUND", "FEED &#183; THROW &#183; VOICE &#183; EXIT",
        ["Fistful at YOUR dog's nose, arc away", "Throw a fistful AT the loose dog's face",
         "Deep voice: &ldquo;SIT! GO HOME!&rdquo;", "Barrier between dogs (car, hedge, gate)",
         "About to make contact? Drop the leash"], CL)}</tr>
    <tr>{block("IT ALREADY BLEW UP", "THE RECOVERY SCRIPT",
        ["Move first &#8212; silence, brisk feet", "No scolding, no soothing monologue",
         "Scatter-finder once clear", "Home the calm way; done for today", "Tomorrow: Quiet Day. The echo is real"], INK)}
    {block("EVERY SINGLE WALK", "THE THREE LAWS",
        ["Distance first. Always", "Never train red &#8212; red means exit",
         "End on a win, one rep early", "Re-measure before you work", "Sniffing drains the bucket"], F2)}</tr>
  </table>
  <div style="text-align:center;margin-top:14px;font-size:13px;color:{MUT};">
    Print me. Tape me where the leash lives. Heart rate 140 is no time to remember things.</div>
</div>'''
    return tpage(b, pno=25, tab="POSTER", tabcolor=CL)

def poster_signals():
    b = f'''<div style="padding:50px 60px 90px 60px;">
  {kicker("POSTER 03 &#183; THE FAMILY BRIEFING")}
  <div style="font-family:'Roboto Slab',serif;font-size:40px;font-weight:bold;color:{F};margin-bottom:14px;">The Five Loading Signals</div>
  {fig(svg_body_language(640, 406))}
  <table style="width:100%;border-collapse:collapse;margin-top:12px;">
    <tr><td style="background:{F};color:#FFF;border-radius:12px;padding:14px 18px;font-size:15px;line-height:1.6;">
    <b style="color:{GD};">THE SEQUENCE:</b> mouth closes &#8594; ears lock &#8594; freeze &#8594; weight forward &#8594; launch.
    The window is 3&#8211;10 seconds. <b style="color:{GD};">House rule: mouth closes = we move.</b>
    Don't wait for confirmation from the other four.</td></tr></table>
  <div style="text-align:center;margin-top:14px;font-size:13px;color:{MUT};">
    Everyone who ever holds this leash reads this poster first. &ldquo;He's in training&rdquo; is a complete sentence.</div>
</div>'''
    return tpage(b, pno=26, tab="POSTER", tabcolor=SG)

def pocket_cards():
    def pcard(title, color, lines, dark=False):
        tcol = "#FFF"
        lcol = CR if dark else "#FFF"
        lis = "".join(f'<div style="font-size:10.5px;line-height:1.45;margin-bottom:3px;color:{lcol};">&#8226; {l}</div>' for l in lines)
        return (f'<td style="width:50%;border:2px dashed {MUT};padding:12px 14px;vertical-align:top;background:{color};">'
                f'<div style="font-size:8px;letter-spacing:2px;color:{GD};font-weight:bold;">CALMWALK POCKET CARD</div>'
                f'<div style="font-size:15px;font-weight:bold;color:{tcol};margin:3px 0 7px 0;">{title}</div>{lis}</td>')
    rows = [
        [pcard("THE FOOD TEST", F2, ["ONE pea treat at the nose. Say nothing",
            "Instant grab = GREEN: work here", "Slow / hard mouth = YELLOW: +2 cars",
            "Refused = RED: leave, retest farther", "The smallest green count = the number"]),
         pcard("THE LOOP", F, ["Green Zone only. Loose leash. WAIT",
            "He notices the trigger &#8212; stay silent", "Head flicks back &#8594; &ldquo;YES!&rdquo;",
            "Pay at the knee (he turns fully away)", "8&#8211;12 reps. Quit on a win"])],
        [pcard("THE U-TURN", CL, ["&ldquo;THIS WAY!&rdquo; &#8212; happy, loud",
            "YOUR body turns first; leash stays loose", "Pay at the knee while moving",
            "10 steps before you think again", "Then: scatter 3 treats, breathe"]),
         pcard("THE RECOVERY SCRIPT", INK, ["Move. Silence. Brisk feet",
            "No scolding. No baby talk", "Clear of sight-line: grass scatter",
            "Straight home, calm route", "48h quiet protocol starts NOW"], dark=True)],
        [pcard("THE LADDER (3-FOR-3)", F2, ["3 clean loops at this rung, 2+ sightings",
            "= step ONE car closer (test first!)", "1 red moment = refund 2 cars",
            "2 rungs/day strong; 3 = ceiling", "Earn. Never borrow"]),
         pcard("THE SESSION SANDWICH", F, ["3 min sniff in (drain the bucket)",
            "60-sec re-measure: work at TODAY'S number", "10 min work: loops / ladder",
            "3 min sniff out (end soft)", "Log it: 2 min, kettle on"])],
        [pcard("LOADING SIGNALS", CL, ["Mouth closes &#8212; FIRST ALARM",
            "Ears pin or lock forward", "Tail high + stiff + slow wag",
            "Freeze (1&#8211;2 sec statue)", "Weight forward &#8594; launch. MOVE AT #1"]),
         pcard("WHAT TO SAY TO HUMANS", INK, ["&ldquo;He's in training&rdquo; (complete sentence)",
            "&ldquo;Please don't let your dog greet&rdquo;", "&ldquo;Can you give us the sidewalk? Thanks!&rdquo;",
            "To advice-givers: &ldquo;vet's orders&rdquo;", "You owe nobody a seminar. Walk on"], dark=True)],
    ]
    trs = "".join(f"<tr>{a}{b}</tr>" for a, b in rows)
    b = f'''<div style="padding:44px 60px 90px 60px;">
  {kicker("CUT-OUT SHEET &#183; SCISSORS ALONG THE DASHES")}
  <div style="font-family:'Roboto Slab',serif;font-size:30px;font-weight:bold;color:{F};margin-bottom:12px;">Eight Pocket Cards</div>
  <table style="width:100%;border-collapse:separate;border-spacing:8px;">{trs}</table>
</div>'''
    return tpage(b, pno=27, tab="CUT", tabcolor=AM)

def log_page(i):
    days = f"DAYS {i * 3 + 1}&#8211;{min(i * 3 + 3, 21)}" if i < 7 else "SPARE"
    blocks = ""
    for j in range(3):
        d = i * 3 + j + 1
        if d > 21:
            label = "SPARE DAY ___"
        else:
            label = f"DAY {d}"
        blocks += f'''
  <div style="border:2px solid {PALETTE['line']};border-radius:12px;padding:12px 16px;margin-bottom:14px;background:#FFF;">
    <table style="width:100%;border-collapse:collapse;"><tr>
      <td style="font-family:'Roboto Slab',serif;font-size:19px;font-weight:bold;color:{F};width:90px;">{label}</td>
      <td style="font-size:10.5px;color:{MUT};letter-spacing:1px;">DATE ______ &#183; ROUTE ___ &#183; WEATHER ______ &#183; BUCKET (1&#8211;5) ___</td></tr></table>
    <table style="width:100%;border-collapse:collapse;margin-top:8px;">
      <tr>
        <td style="width:25%;font-size:10px;letter-spacing:1px;color:{MUT};font-weight:bold;">WORKING DISTANCE (CARS)<div style="border-bottom:1.4px solid {MUT};height:22px;"></div></td>
        <td style="width:4%;"></td>
        <td style="width:21%;font-size:10px;letter-spacing:1px;color:{MUT};font-weight:bold;">CLEAN / TOTAL LOOPS<div style="border-bottom:1.4px solid {MUT};height:22px;"></div></td>
        <td style="width:4%;"></td>
        <td style="width:15%;font-size:10px;letter-spacing:1px;color:{MUT};font-weight:bold;">U-TURNS<div style="border-bottom:1.4px solid {MUT};height:22px;"></div></td>
        <td style="width:4%;"></td>
        <td style="font-size:10px;letter-spacing:1px;color:{MUT};font-weight:bold;">MOUTH SCORES (I/S/R)<div style="border-bottom:1.4px solid {MUT};height:22px;"></div></td>
      </tr></table>
    <div style="font-size:10px;letter-spacing:1px;color:{MUT};font-weight:bold;margin-top:8px;">WHAT HAPPENED (ONE HONEST SENTENCE)</div>
    <div style="border-bottom:1.4px solid {MUT};height:24px;"></div>
    <div style="border-bottom:1.4px solid {MUT};height:24px;"></div>
  </div>'''
    b = pad(
        kicker(f"DAILY LOG &#183; SHEET {i+1} OF 7 &#183; {days}")
        + h1("Walk Log")
        + blocks
        + small("Clean loop = instant eat + flick-back under ~3 seconds + soft mouth. "
                "Bucket 1 = spa day, 5 = construction crew next door. The trend out-argues the despair."))
    return tpage(b, pno=28 + i, tab="LOG", tabcolor=MUT)

def planner_route():
    b = pad(
        kicker("PLANNER &#183; TOOLKIT EDITION")
        + h1("Route Planner")
        + p("Red boxes = trigger houses. E = escapes. Route A passes sight-lines at or beyond the "
            "number; Route B is the bunker.", "small")
        + wbox("ROUTE A &#8212; TRAINING ROUTE", 300)
        + wbox("ROUTE B &#8212; BAIL-OUT ROUTE", 230)
        + cols(wline("Pinch points to respect", 2), wline("Loose-dog houses / gate-open days", 2))
    )
    return tpage(b, pno=35, tab="PLAN", tabcolor=F2)

def planner_triggers():
    b = pad(
        kicker("PLANNER &#183; TOOLKIT EDITION")
        + h1("Trigger Inventory")
        + p("One row per trigger CLASS (dogs, kids, bikes&hellip;), not per individual. Update forever.", "small")
        + wgrid(["Trigger class", "Worst version", "Calm at (cars)", "Loads at (cars)", "Notes"],
                12, ["22%", "26%", "14%", "14%", "24%"])
        + callout("note", "&#9998; READ IT BACK",
            p("Train the most COMMON class first, not the scariest. Rare-but-nuclear gets a route "
              "answer until the everyday stuff is boring."))
    )
    return tpage(b, pno=36, tab="PLAN", tabcolor=F2)

def build():
    pages_html = [cover(), how_to()]
    for i, d in enumerate(DAYS):
        pages_html.append(tpage(day_card(d), pno=3 + i, tab=f"D{d[0]}",
                                tabcolor=PHASECOLORS[d[1]]))
    pages_html += [poster_zone(), poster_red(), poster_signals(), pocket_cards()]
    pages_html += [log_page(i) for i in range(7)]
    pages_html += [planner_route(), planner_triggers()]
    return html_doc(pages_html, "The Calm Walks Toolkit")
