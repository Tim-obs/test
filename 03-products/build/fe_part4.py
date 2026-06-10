"""FE Part IV — When It Goes Wrong (emergencies & troubleshooting)."""
from design import *
from fe_front import PARTCOLORS

P, C = "IV", PARTCOLORS["IV"]

def _pg(body, toc=None):
    return {"html": body, "part": f"PART {P}", "color": C, "toc": toc}

def pages():
    out = []

    out.append({"raw_divider": ("04", "PART FOUR", "When It Goes Wrong",
        "The street does not read training books. These are the scripts for the moments that used "
        "to end in tears &#8212; written to be remembered at heart rate 140.",
        ["The one-glance decision flowchart", "The off-leash dog", "The Recovery Script (the 10 seconds after)",
         "&ldquo;My dog won't take food&rdquo;", "Regression weeks", "Apartments, elevators, and cities",
         "The troubleshooting table"]),
        "toc_part": "PART IV &#8212; WHEN IT GOES WRONG"})

    out.append(_pg(pad(
        kicker("THE ONE-GLANCE ANSWER")
        + h1("The decision flowchart")
        + p("Every walk decision in this book compresses into one picture. When in doubt, this is the "
            "whole method's law, enforceable at a glance:")
        + fig(svg_decision_flow(), "FIG. 15 &#8212; LAMINATE THIS IN YOUR HEAD")
        + callout("key", "&#9733; THE THREE-SECOND VERSION",
            p("<b>Green &#8594; work. Yellow &#8594; leave. Red &#8594; leave faster, then forgive everyone involved, "
              "including yourself.</b> There is no fourth option, and there is nothing a reactive dog can "
              "do on a sidewalk that this triage doesn't cover."))
        + p("Print-sized copies of this chart and the zone map live in the Calm Walks Toolkit as "
            "pocket cards; a hand-drawn version on an index card works exactly as well. What matters "
            "is that the triage happens in your spine, not your memory &#8212; which is why day 19 made "
            "you rehearse it.")
    ), toc="The decision flowchart"))

    out.append(_pg(pad(
        kicker("EMERGENCY &#183; CODE RED")
        + h1("The off-leash dog")
        + p("The nightmare scenario, and the one place this book adds tools beyond the U-turn, because "
            "distance stops being fully yours to control. Priorities, in order: <b>your body between "
            "dogs &#8594; food on the ground &#8594; voice &#8594; exit.</b>")
        + drill("PROTOCOL &#183; LOOSE DOG INBOUND", "MEMORIZE",
            "<ol><li><b>Feed YOUR dog's face first</b> &#8212; literally a fistful at his nose &#8212; while you "
            "turn and angle away on an arc. A chewing mouth can't scream, and the arc reads as non-confrontation to the incoming dog.</li>"
            "<li><b>Throw a fistful of treats AT the loose dog's face.</b> Most pet dogs brake for a "
            "food scatter. You just bought 10&#8211;30 seconds. Use them to put a parked car, hedge, or gate between dogs.</li>"
            "<li><b>Voice:</b> a sharp, deep &ldquo;SIT! GO HOME!&rdquo; stops a surprising number of "
            "neighborhood wanderers. Command voice, not panic voice.</li>"
            "<li><b>If contact is about to happen:</b> drop the leash. Two tangled dogs hurt each other "
            "less than two tangled dogs and a rope and a falling human. It feels wrong; the data says do it.</li></ol>")
        + callout("warn", "&#9888; AFTERWARD &#8212; EVEN IF &ldquo;NOTHING HAPPENED&rdquo;",
            p("A close pass from a loose dog fills the bucket to the brim. Walk straight home the "
              "calm way, run the Recovery Script (next page), and write the incident on the log with "
              "the location &#8212; loose-dog houses get a permanent red box on the route map."))
        + small("Carry spray cheese or a sealed bag of real meat on every walk in loose-dog country. "
                "Also genuinely useful: knowing which neighbors leave gates open on trash day. Scouts win.")
    ), toc="The off-leash dog"))

    out.append(_pg(pad(
        kicker("EMERGENCY &#183; AFTERMATH")
        + h1("The Recovery Script: the ten seconds after, and the 48 hours after that")
        + p("There WILL be explosions during this plan. The difference between a blip and a spiral is "
            "entirely in what happens next. Two clocks start the moment the barking starts:")
        + h3("CLOCK ONE &#8212; THE FIRST 10 SECONDS")
        + cklist([
            "<b>Move first, feel later.</b> U-turn or arc until the trigger is gone from his sight-line. "
            "Don't stop to apologize to anyone mid-extraction; wave, go.",
            "<b>Say nothing to the dog.</b> No &ldquo;NO,&rdquo; no soothing monologue either &#8212; both pay "
            "attention into the explosion. Neutral silence, brisk feet.",
            "<b>At 2+ cars of separation: scatter a treat-finder in grass.</b> Sniffing is the off-ramp. "
            "If he can eat the scatter, the worst is already draining.",
        ])
        + h3("CLOCK TWO &#8212; THE NEXT 48 HOURS")
        + cklist([
            "<b>Today:</b> shortest legal route home; no more training; evening enrichment indoors "
            "(stuffed Kong, find-it game, lick mat &#8212; chewing and licking are drain valves too).",
            "<b>Tomorrow:</b> Quiet Day (day-5 rules). Route B or skip the walk entirely for yard games. "
            "The echo (p. 12) is real chemistry; honor it.",
            "<b>Day after:</b> re-measure before working. Expect +1 to +2 cars temporarily. Take the "
            "surcharge without editorializing; it refunds itself within days.",
        ])
        + fixit(p("And the third clock, the human one: one bad walk does not erase a week of clean reps "
                  "&#8212; the wave chart on p. 14 is in this book twice for a reason. Log it, laugh if you "
                  "can, kettle on, tomorrow's easy."), head="THE OWNER'S RECOVERY")
    ), toc="The Recovery Script"))

    out.append(_pg(pad(
        kicker("DIAGNOSTICS")
        + h1("&ldquo;My dog won't take food&rdquo; &#8212; the full checklist")
        + p("Food refusal is information, never defiance. Run this list top to bottom; the fix is "
            "almost always in the first three rows.")
        + table(["Check", "The tell", "The fix"],
            [["<b>Distance</b> (90% of cases)", "eats fine at home; refuses near triggers",
              "you're past the line; add cars until the mouth works &#8212; that IS the food test doing its job"],
             ["<b>Bucket</b>", "refuses even at huge distances, scanning, won't settle",
              "stacked day or the 48h echo; Quiet Day now, retest tomorrow"],
             ["<b>Pay grade</b>", "takes chicken at 6 cars but ignores kibble at 6 cars",
              "your currency is too weak for the venue; outside work = cheese/hot dog/real meat, always"],
             ["<b>Stomach</b>", "fed dinner 20 minutes before the session",
              "train before meals, not after; a full dog is a low-motivation dog"],
             ["<b>Heat / weather</b>", "refuses on warm afternoons, fine at dawn",
              "panting and eating compete; work the cool ends of the day in summer"],
             ["<b>Pain</b> (see the vet)", "new refusal + new reluctance to walk, jump, or be touched",
              "sudden behavior change is medical until proven otherwise &#8212; safety page rules apply"]])
        + callout("note", "&#9998; THE NON-FOOD DOG (RARE, REAL)",
            p("A small minority of dogs genuinely work better for a tug toy or sniffy praise-party. "
              "The Loop runs identically: see &#8594; flick &#8594; YES &#8594; ten seconds of the good thing. "
              "Currency is negotiable; the mechanism is not."))
    ), toc="&ldquo;My dog won't take food&rdquo;"))

    out.append(_pg(pad(
        kicker("THE LONG GAME")
        + h1("Regression weeks: when the number climbs back up")
        + p("Somewhere &#8212; week 4, week 7, after the holidays &#8212; the number will climb for several "
            "days and your stomach will drop. Before you decide the method &ldquo;stopped working,&rdquo; "
            "know that regression waves have a short, boring list of causes:")
        + cklist([
            "<b>An incident you discounted</b> &#8212; the fence-fight through the gate &ldquo;that wasn't a "
            "big deal.&rdquo; It was. Echo math (p. 12).",
            "<b>Adolescence</b> &#8212; dogs 6&#8211;18 months re-negotiate everything twice; waves are bigger "
            "and pass.",
            "<b>Season shifts</b> &#8212; the street population doubles in May; the dog didn't relapse, "
            "the test got harder.",
            "<b>Pain or illness</b> &#8212; always on the list; re-read the safety page if the wave comes "
            "with any physical change.",
            "<b>Nothing at all</b> &#8212; some waves are just waves. P. 14. Still true.",
        ])
        + drill("PROTOCOL &#183; THE REGRESSION RESET", "ONE WEEK",
            "<ol><li>Two Quiet Days back to back. Full drain.</li>"
            "<li>Re-measure formally (day-3 protocol). Accept the new number in writing without commentary.</li>"
            "<li>Run THREE days of week-2-style anchor work at the new number &#8212; easy loops, "
            "no laddering. Rebuild the floor.</li>"
            "<li>Resume the ladder (3-for-3, day-15 rules). Most dogs re-earn the lost cars in "
            "one-third the original time &#8212; the wiring is still there; you're dusting it, not rebuilding it.</li></ol>")
        + pull("You are never back at square one. The reps don't un-happen.", "part one, still true in week seven")
    ), toc="Regression weeks"))

    out.append(_pg(pad(
        kicker("GEOMETRY PROBLEMS")
        + h1("Apartments, elevators, and cities: when distance is rationed")
        + p("The method assumes you can add cars. Hallways, elevators, and stairwells ration distance "
            "brutally &#8212; so city work leans harder on timing, barriers, and scheduling:")
        + cklist([
            "<b>Own the schedule:</b> 10 minutes earlier than building rush beats 10 cars of distance. "
            "Learn the building's dog timetable in week 1 (it's astonishingly consistent).",
            "<b>The doorway pause:</b> never exit blind. Crack the lobby/apartment/elevator door, "
            "scan, THEN commit. Three seconds of scouting prevents most hallway ambushes.",
            "<b>Stairwells are your tunnel network:</b> two flights of stairs = a city block of "
            "separation. Yes, even with groceries.",
            "<b>The elevator script:</b> dog in the rear corner, you between dog and door, finder "
            "scatter on the floor if anyone boards. Skip a car rather than share with another dog &#8212; "
            "always, forever, no exceptions.",
            "<b>Courtyards and parking garages at off-hours</b> are your Green Zone laboratories &#8212; "
            "big, boring, predictable. Map two before day 8.",
        ])
        + callout("key", "&#9733; THE CITY REFRAME",
            p("Urban reactive-dog work is 70% logistics, 30% training &#8212; and the training works "
              "exactly the same once logistics buy you the distance. You're not doing it on hard mode; "
              "you're doing it on planning mode. (Nine fully-scripted hard scenarios &#8212; elevators "
              "included &#8212; get the four-page treatment each in the Hard Cases Manual.)"))
    ), toc="Apartments &amp; cities"))

    out.append(_pg(pad(
        kicker("REFERENCE")
        + h1("Troubleshooting, A&#8211;M")
        + table(["Symptom", "Likely cause", "Page / fix"],
            [["Barks at trigger AFTER it passes", "relief bark &#8212; tension exiting", "normal; lengthen the sniff-out; fades by week 3"],
             ["Can't look AT the trigger (avoids)", "too close; avoidance is yellow", "add 2 cars until he can observe calmly"],
             ["Can't look AWAY from trigger", "too close, or mover too hot", "add 2 cars; movers get their own number (day 16)"],
             ["Eats but explodes anyway, no warning", "you're missing the loading signals", "re-study p. 20; film one session &#8212; the tells are there"],
             ["Fine with dogs, explodes at SOME people", "specific-feature trigger (hats, carts, kids)", "each feature class gets its own number; ladder separately"],
             ["Great on walks, fence-fights at home", "different behavior system (territory)", "block the sight-line (film on windows); Hard Cases #6"],
             ["Husband/wife gets explosions, you don't", "handler mechanics differ (leash, breath, timing)", "have them read p. 25; film both; compare J-shapes"],
             ["Ignores YES outdoors", "marker under-charged for the venue", "re-run day 6 in the yard, then driveway, then street"],
             ["Lunges at bikes/cars/skateboards only", "motion-trigger (chase wiring, not fear)", "same plan; expect faster ladders but stricter mover rules"],
             ["Marker works, won't flick back at all", "trigger too interesting; distance too short", "the flick is bought with cars, not patience: +2"]])
        + small("Continued on the next page.")
    ), toc="Troubleshooting table"))

    out.append(_pg(pad(
        kicker("REFERENCE")
        + h1("Troubleshooting, N&#8211;Z")
        + table(["Symptom", "Likely cause", "Page / fix"],
            [["Number stuck 2+ weeks despite clean reps", "rehearsal leaking somewhere (yard? window? daycare?)", "audit the whole week for un-logged red moments; they tax the ladder invisibly"],
             ["Perfect at training spots, awful on real walks", "sessions too staged; transfer not bought", "more day-18s: three new venues in two weeks, tax paid at each"],
             ["Pulls TOWARD dogs, screams when blocked", "frustration-type (p. 7)", "identical plan; day-9 note; expect stickier loops, faster food tests"],
             ["Quiet Days make him MORE wired", "sniffari venue too stimulating", "duller field, longer line, or swap to indoor find-it games"],
             ["Refuses to leave the house at all", "walk itself has gone red (leash predicts panic)", "10 doorstep meals over 3 days, then driveway loops; rebuild from the porch out"],
             ["Walks fine at dawn, explodes at 5pm", "not time &#8212; density; 5pm streets are full", "that's a fatter number at rush hour, not a relapse; measure per-hour"],
             ["Whines constantly in the Green Zone", "anticipation overflow (common in frustration types)", "longer pauses between reps; pay calm stillness once per set"],
             ["You feel scared of the next walk", "human nervous system keeping score honestly", "shrink tomorrow to a 5-minute driveway session; wins rebuild handlers too"],
             ["&ldquo;Tried everything, nothing works&rdquo;", "usually: working in yellow, paying in kibble, no log", "the brutal audit: re-read pp. 18&#8211;26, restart at day 2 by the book"],
             ["It's working and I'm scared to believe it", "three weeks of receipts beat a feeling", "believe the log; keep climbing; Part V is next"]])
        + callout("note", "&#9998; NOT ON THIS LIST?",
            p("If the problem involves contact, blood, children, or your own safety: safety page rules, "
              "credentialed professional, this week. For everything else: when in doubt, add distance "
              "and re-measure. It is almost embarrassing how often that's the whole answer."))
    ), toc=None))

    return out
