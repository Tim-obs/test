"""FE Part III — the 21-day plan: rules page, 3 week overviews, 21 day pages."""
from design import *
from fe_front import PARTCOLORS

P, C = "III", PARTCOLORS["III"]

def _pg(body, toc=None):
    return {"html": body, "part": f"PART {P}", "color": C, "toc": toc}

def day_page(n, phase, goal, setup, drill_name, reps, steps, pass_items, fail_items, fix, note=None):
    b = pad(
        daybar(n, phase, goal)
        + h3("TODAY'S SETUP")
        + p(setup)
        + drill(drill_name, reps, "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>")
        + passfail(pass_items, fail_items)
        + fixit(p(fix))
        + (callout("note", "&#9998; NOTE", p(note)) if note else "")
    )
    return _pg(b)

def pages():
    out = []

    out.append({"raw_divider": ("03", "PART THREE", "The 21-Day Plan",
        "One page per day. Sixteen minutes per session. Every day has a goal, exact reps, "
        "a pass check, and a fix for when the street doesn't cooperate.",
        ["Week 1 &#8212; MAP: find the number (days 1&#8211;7)",
         "Week 2 &#8212; ANCHOR: install the Loop and the U-turn (days 8&#8211;14)",
         "Week 3 &#8212; SHRINK: the 3-for-3 ladder (days 15&#8211;21)"]),
        "toc_part": "PART III &#8212; THE 21-DAY PLAN"})

    out.append(_pg(pad(
        kicker("RULES OF ENGAGEMENT")
        + h1("How the plan works")
        + cklist([
            "<b>Every session is the 16-minute sandwich</b> (p. 26): 3 sniffy minutes in, 10 working minutes, 3 sniffy minutes out.",
            "<b>Every session starts with a 60-second re-measure.</b> One food test at yesterday's number. Green? Work there. Yellow? Add 2 cars and work THERE. The plan flexes; the rule doesn't.",
            "<b>Log every session</b> on the Daily Walk Log (p. 69). Two minutes, in the kitchen, while the kettle's on. The log is what makes bad days survivable (p. 14).",
            "<b>Blow-up happens anyway?</b> Run the Recovery Script (p. 56) and make tomorrow a Quiet Day (like day 5). The plan pauses; it never breaks. 21 days is a floor, not a deadline.",
        ])
        + fig(svg_three_for_three(), "FIG. 14 &#8212; THE LADDER RULE YOU'LL USE FROM DAY 15 FOREVER")
        + callout("key", "&#9733; THE THREE LAWS, ONE LAST TIME",
            "<ul><li><b>Distance first.</b> When anything is unclear, add cars.</li>"
            "<li><b>Never train red.</b> A red moment is an exit cue, not a teaching moment.</li>"
            "<li><b>End on a win.</b> Quit one rep early, every day, forever.</li></ul>")
        + small("Frustration-type dogs (the &ldquo;he just wants to SAY HI&rdquo; screamers): the plan is identical. "
                "Expect faster food-test greens but stickier loops in week 2 &#8212; your day-9 note covers it.")
    ), toc="Rules of engagement"))

    # ---------------- WEEK 1
    out.append(_pg(pad(
        kicker("DAYS 1&#8211;7")
        + h1("Week 1 &#8212; MAP: find the number")
        + p("This week contains no training and cannot fail. You are a surveyor: by Sunday you will "
            "know your dog's number, his top three triggers, his loading signals, and the two routes "
            "you'll run for the rest of the plan. Most owners report the dread easing THIS week &#8212; "
            "not because the dog changed, but because a measured problem feels nothing like a mystery.")
        + table(["Day", "Job", "Minutes"],
            [["1", "Scout walk: log triggers, distances, reactions. Change nothing.", "20"],
             ["2", "Food Test day: first provisional number", "16"],
             ["3", "Confirm the number: 3-green rule across trigger types", "16"],
             ["4", "Trigger inventory + plan two routes with escape hatches", "20 + map"],
             ["5", "Quiet Day: sniffari. Drain the bucket. Read Part II again.", "20"],
             ["6", "Charge the marker (kitchen) + easy J-walk", "10 + 12"],
             ["7", "First Loops at number +2 (easy mode) + week review", "16"]])
        + callout("note", "&#9998; SET THE SCENE",
            p("Walk at your usual avoidance hours this week &#8212; the 5am routine is, for once, perfect: "
              "you'll meet triggers at long, workable distances. The plan will walk you back toward "
              "normal hours in week 3."))
    ), toc="Week 1 overview &#8212; MAP"))

    out.append(day_page(1, "WEEK 1 &#183; MAP", "Scout the territory. Change nothing yet.",
        "Your normal route at your normal quiet hour. Phone in pocket for notes, treats in pouch "
        "(for the J, not for tests yet). This walk is pure reconnaissance.",
        "MISSION &#183; THE SCOUT WALK", "1 WALK",
        ["Walk the usual route. Every time your dog NOTICES anything (head turn, ear lock), note three "
         "things: <b>what</b> it was, <b>how many cars</b> away, <b>what his mouth did</b>.",
         "If he loads up (p. 20), do what you'd normally do &#8212; cross, turn, retreat. Just write it down after.",
         "Back home: transfer everything to the Trigger Inventory (p. 67). Five minutes.",
         "Circle the trigger that appeared most. That's your training partner for the next 20 days."],
        ["You came home with 3+ logged sightings (even &ldquo;a cat, 2 cars, froze&rdquo; counts)",
         "You can name the distance of the closest calm moment"],
        ["You trained, tested, or &ldquo;just tried one thing&rdquo; &#8212; not yet; data first",
         "Zero sightings logged &#8212; route too sterile; tomorrow use the medium route, not the bunker route"],
        "Explosion on the scout walk? Fine &#8212; it's data. Log the distance it happened at, add 3 cars to "
        "it, and that's tomorrow's starting line. The scout walk cannot fail; it can only inform.",
        note="Tonight, on paper, finish this sentence from memory: &ldquo;My dog's mouth closes when ___ "
             "is about ___ cars away.&rdquo; If you can't, tomorrow will tell you."))

    out.append(day_page(2, "WEEK 1 &#183; MAP", "Run the Food Test. Get a provisional number.",
        "Quiet hour, the route where you logged the most sightings. Pouch loaded with 100 pea-size "
        "softs. You need 3&#8211;5 trigger sightings at LONG range; park yourself where dogs pass at a distance "
        "(across a park, a wide street) if your route can't supply them.",
        "DRILL &#183; FOOD TEST (p. 18)", "5 TESTS",
        ["First sighting: stop at a distance that feels embarrassingly safe. Count the cars.",
         "Offer ONE treat at the nose. Say nothing. Score the mouth: instant / slow / refused.",
         "Instant grab? Take 2 cars off and test the next sighting closer. Slow? Add 2 and test farther.",
         "After 3&#8211;5 tests, you'll have bracketed it: the smallest cars-count with an instant grab. "
         "Write it on the Baseline sheet (p. 66) in pen.",
         "Sniff-walk home. Done. Resist the urge to &ldquo;just do a little training.&rdquo;"],
        ["You wrote down a number (whatever it is &#8212; 4, 9, 15: all fine)",
         "At least 3 tests scored, on 2+ different triggers"],
        ["Only one sighting all walk &#8212; re-run tomorrow at a busier window (10 min earlier is often enough)",
         "He refused food even at half a block &#8212; bucket's full today (p. 11): quiet day now, retest tomorrow"],
        "If a trigger ambushed you inside the test distance: U-turn (your old instinct is fine for now), "
        "get out, and re-run the test at +4 cars once your own heart rate settles. Adrenaline reads as red on both ends of the leash.")
    )

    out.append(day_page(3, "WEEK 1 &#183; MAP", "Confirm the number: three greens, different triggers.",
        "Same hour, same route as day 2. Today turns the provisional number into a confirmed one "
        "&#8212; and your eyes start learning the loading signals chart (p. 20).",
        "DRILL &#183; THE 3-GREEN CONFIRMATION", "3&#8211;6 TESTS",
        ["Set up at yesterday's number on the first sighting. Food test. Green?",
         "Repeat on the next two sightings &#8212; ideally a different dog, a person, a bike. "
         "<b>Three instant grabs in a row at the same count = number confirmed.</b>",
         "Any yellow or red: add 2 cars, and the 3-count starts over at the new distance.",
         "Between tests, watch his body against the chart on p. 20. Find his order &#8212; most dogs "
         "lead with the mouth, some lead with the tail. Note his tell on the Baseline sheet.",
         "Sniffy walk out. Log it."],
        ["One number, three greens, two-plus trigger types: <b>circled in pen</b>",
         "You spotted his first loading signal at least once today and moved BEFORE the bark"],
        ["Numbers bouncing wildly between tests (4, then 11, then 6) &#8212; you're measuring different "
         "trigger intensities; log dog-triggers separately from people-triggers and confirm the worst one",
         "You crept closer &ldquo;to see what he can really do&rdquo; &#8212; that's the Exposure Trap wearing your shoes (p. 8)"],
        "A blow-up during confirmation costs nothing but ink: write the distance, add 3 cars, work there. "
        "The number isn't a test you pass; it's a fact you record.")
    )

    out.append(day_page(4, "WEEK 1 &#183; MAP", "Build the trigger map and plan two routes.",
        "Half the session is at the kitchen table with the Route Planner (p. 68). The walk itself "
        "is a dress rehearsal of your new A-route.",
        "MISSION &#183; THE HEIST PLAN", "1 MAP + 1 WALK",
        ["From the Trigger Inventory, mark your block map: every fence-dog yard, the dog-park corner, "
         "the retriever who's always loose at 6pm. Red boxes, like the diagram on p. 68.",
         "Draw <b>Route A (training route)</b>: passes trigger sight-lines at or beyond your number. "
         "Mark every escape hatch &#8212; alleys, driveways, church lots &#8212; with an E.",
         "Draw <b>Route B (bail-out route)</b>: near-zero sightings, for full-bucket days. Every plan needs a bunker.",
         "Walk Route A once at the quiet hour. Count cars at every sight-line as you pass. Adjust the map where reality disagrees."],
        ["Two routes on paper with escapes marked &#8212; you could hand the map to a dog-sitter",
         "Route A delivered 2+ sightings at workable distance on the rehearsal"],
        ["Route A is trigger-free &#8212; that's a Route B; training needs material. Re-draw it one street braver",
         "An unfixable pinch point (the hallway, the only exit) &#8212; don't fight geometry; that's a Hard Case "
         "and there's a whole manual for those"],
        "If today's rehearsal ambushed you at a pinch you didn't predict: excellent &#8212; better the map "
        "fails on a rehearsal than on a training day. Add the red box and re-route tonight.")
    )

    out.append(day_page(5, "WEEK 1 &#183; MAP", "Quiet Day: drain the bucket. (This is a real assignment.)",
        "A sniffari: 20 minutes, the most boring green space you know, longest leash you own (or a "
        "20-ft line), zero agenda. The dog picks the direction; you hold the clock.",
        "MISSION &#183; THE SNIFFARI", "20 MIN",
        ["Let him sniff ANYTHING for as long as he wants. Sniffing meters stress down &#8212; it's the "
         "drain on the bucket diagram (p. 11), and it's measurable in heart-rate studies.",
         "No cues, no tests, no phone. Your only job: keep the J in the leash and go where the nose goes.",
         "Tonight: re-read pages 21&#8211;24 (marker + Loop). Tomorrow you start building.",
         "Optional but powerful: note how he sleeps this evening compared to a normal day."],
        ["Your dog spent 15+ of 20 minutes with his nose down",
         "You said fewer than ten words the whole walk"],
        ["You &ldquo;snuck in a few reps&rdquo; &#8212; the rest IS the work today; a drained bucket buys "
         "all of next week's wins",
         "He paced and scanned instead of sniffing &#8212; bucket's very full; do tomorrow as a second "
         "Quiet Day and start the marker on day 7. The plan flexes; the rule doesn't."],
        "Rain ruining it? A 15-minute indoor &ldquo;find it&rdquo; game (scatter kibble around two rooms, "
        "narrate nothing) drains the same pipe.")
    )

    out.append(day_page(6, "WEEK 1 &#183; MAP", "Charge the marker. Ten kitchen minutes that pay for years.",
        "Kitchen, post-breakfast, dog mildly bored. Then a separate, easy J-practice walk on Route B. "
        "Today wires the word that makes every future rep legible.",
        "DRILL &#183; CHARGING THE MARKER (p. 21)", "20 REPS &#215; 2",
        ["Say <b>&ldquo;YES&rdquo;</b> &#8212; one bright syllable. THEN the hand moves to the pouch, "
         "treat at your knee. Word first, hand second. Twenty reps. Coffee break. Twenty more.",
         "Rep 15 check: say YES while he's looking away. Head whip = the word is charging.",
         "Walk Route B for 12 minutes practicing only the loose J (p. 25): two hands, gather don't winch, "
         "one exhale at anything interesting.",
         "Log both. Tomorrow the word goes outside."],
        ["Head-whip on YES from across the kitchen by the second set",
         "One full Route B circuit with the J intact 80% of the way"],
        ["He stares at your pouch hand &#8212; your hand is moving before (or with) the word; exaggerate the "
         "one-second gap: say it, count &ldquo;one-banana,&rdquo; then reach",
         "Family members freelancing other words (&ldquo;good boy!&rdquo; &ldquo;yes yes YES&rdquo;) &#8212; "
         "one marker, one meaning; brief the household tonight"],
        "Multi-dog home? Charge each dog separately behind a closed door. Markers are per-dog wiring, "
        "and an audience of jealous colleagues ruins the signal.")
    )

    out.append(day_page(7, "WEEK 1 &#183; MAP", "First Loops &#8212; in easy mode. Then close the week's books.",
        "Route A, quiet hour, at your confirmed number <b>plus two cars</b>. Easy mode is deliberate: "
        "the first Loops should be so far from threshold they feel like a card trick.",
        "DRILL &#183; THE LOOP, EASY MODE (p. 22)", "6&#8211;8 REPS",
        ["Re-measure: one food test at number+2. Green (it should be, out here)? Work here.",
         "First sighting: let him notice. <b>Say nothing. Wait.</b> Watch his head like a hawk.",
         "The flick back toward you &#8212; &ldquo;YES!&rdquo; &#8212; pay at the knee. That's one. Expect 5&#8211;20 "
         "seconds of staring before the first flick; the second comes faster. They always do.",
         "6&#8211;8 loops or 90 seconds per sighting, then stroll on. Two or three sightings is a full day.",
         "Home: Week Review (p. 71). Write the week's number trend and one sentence to yourself."],
        ["At least 4 loops where the look-back came inside 5 seconds",
         "Week Review filled: number confirmed, routes drawn, marker charged &#8212; MAP complete"],
        ["He stares at the trigger and can't flick back &#8212; even at +2 you're tight; add 2 more cars; "
         "easy mode has no floor",
         "He ignores the trigger entirely and mugs your pouch &#8212; too FAR (yes, that's a thing); "
         "drop 2 cars so the trigger exists"],
        "If week 1 took you ten days instead of seven, you are exactly on schedule. The calendar serves "
        "the dog, never the reverse.",
        note="MAP phase complete. You now know more, in numbers, about your dog's behavior than most "
             "owners ever learn. Week 2 builds the reflex on top of it."))

    # ---------------- WEEK 2
    out.append(_pg(pad(
        kicker("DAYS 8&#8211;14")
        + h1("Week 2 &#8212; ANCHOR: install the reflex")
        + p("The number stops being a fact and starts being a workshop. This week the Loop becomes "
            "your dog's default answer to a trigger, the U-turn becomes <i>your</i> default answer to "
            "an ambush, and both get tested against movement &#8212; the hard part. By day 14 you'll "
            "re-measure and watch the number itself start to drop.")
        + table(["Day", "Job", "Minutes"],
            [["8", "Loops at the number, static triggers", "16"],
             ["9", "Loops vs MOVING triggers (the real exam)", "16"],
             ["10", "U-turn drill day: ten peacetime reps", "16"],
             ["11", "Loops + U-turns mixed; the treat-scatter finder", "16"],
             ["12", "Quiet Day II. Non-negotiable.", "20"],
             ["13", "The two-trigger session (bucket-aware work)", "16"],
             ["14", "Re-measure ceremony + week review", "16"]])
        + callout("warn", "&#9888; THE WEEK-2 TRAP",
            p("Day 8 or 9 usually delivers a session so good you'll be tempted to skip ahead &#8212; "
              "&ldquo;he's fixed, let's walk past the dog park!&rdquo; That impulse has un-fixed more dogs "
              "than any husky ever did. The ladder (day 15) is how we get closer. Not yet."))
    ), toc="Week 2 overview &#8212; ANCHOR"))

    out.append(day_page(8, "WEEK 2 &#183; ANCHOR", "Loops at the real number. Static triggers.",
        "Route A at the quiet hour. Today drops the +2 training wheels: you work AT the confirmed "
        "number, on triggers that hold mostly still &#8212; a dog sniffing a tree across the field, "
        "a person waiting at the bus stop.",
        "DRILL &#183; THE LOOP AT THE NUMBER", "8&#8211;12 REPS",
        ["60-second re-measure (one food test). Green at the number? Begin. Yellow? +2 cars, begin there, zero shame.",
         "Work sightings exactly as day 7: notice &#8594; wait &#8594; flick &#8594; YES &#8594; knee. "
         "The only change is the shorter distance &#8212; expect the first look-back to take longer again. Normal.",
         "Pay scale (p. 23): routine reps one treat; any look-back from a trigger that's STARING BACK, jackpot five.",
         "Cap it: 12 loops or three sightings, sniff out, log the rep count and today's working distance."],
        ["8+ clean loops; look-back latency shrinking across the session",
         "You caught at least one mouth-close and added distance BEFORE he loaded past yellow"],
        ["Two refusals on the re-measure &#8212; today is a +2 day or a Quiet Day; the bucket outranks the calendar",
         "Loops work on dog-triggers but not people-triggers (or vice versa) &#8212; separate numbers, remember; "
         "work each trigger class at ITS distance"],
        "Mid-session collapse (was looping, suddenly can't): something stacked &#8212; a second trigger, a "
        "noise you missed. Don't push through the fog: U-turn out, sniff 3 minutes, end early on any easy win.")
    )

    out.append(day_page(9, "WEEK 2 &#183; ANCHOR", "Loops against moving triggers.",
        "Same place, same number &#8212; but today you pick triggers in MOTION: the lateral dog walking "
        "across your field of view at distance. Movement yanks the alarm harder; expect the work to feel "
        "like day 7 again. That's not regression, that's the syllabus.",
        "DRILL &#183; LOOPS VS MOTION", "8&#8211;12 REPS",
        ["Re-measure on a moving trigger if you can get one early. Moving-number is often the static "
         "number +2. Work at whatever today says.",
         "Position yourself so the trigger crosses your view <b>laterally</b> &#8212; never approaching head-on. "
         "Lateral motion is a 4/10 problem; head-on is a 9/10 and lives in week 3.",
         "Loop as always. The flick-backs will be slower against motion. Pay the slow ones too; "
         "jackpot the fast ones.",
         "If a mover turns and comes TOWARD you: that's an ambush, not a rep. U-turn, reset at distance, resume."],
        ["6+ loops against movers, even if the distances were fatter than yesterday",
         "Zero red moments &#8212; every approach answered with distance, not hope"],
        ["He locks on and tracks the mover like a sniper &#8212; too close for motion; +2 and retry",
         "Frustration screamers (the &ldquo;LET ME SAY HI&rdquo; type): if loops melt into whining, shorten "
         "to 4&#8211;5 loops per sighting and leave while he still has half his mind"],
        "No movers showing up? Manufacture one: park 8+ cars from a trailhead or a vet's parking lot "
        "and let the world deliver lateral traffic on schedule.")
    )

    out.append(day_page(10, "WEEK 2 &#183; ANCHOR", "U-turn day: drill the escape until it's boring.",
        "Route B (yes, the boring one) &#8212; today is about YOUR feet, not his feelings. Ten peacetime "
        "U-turns, spaced through a normal walk, zero triggers required.",
        "DRILL &#183; THE EMERGENCY U-TURN (p. 24)", "10 REPS",
        ["Mid-stride, no trigger anywhere: <b>&ldquo;THIS WAY!&rdquo;</b> &#8212; party voice &#8212; turn your "
         "body 180&#176;, GO. Leash stays loose; your momentum is the cue.",
         "As he wheels with you: YES, pay at the knee while still moving. Ten steps, resume the stroll.",
         "Mix the menu: full 180s, left arcs, right arcs, a 5-step jog-away. Two of the ten at a real trot.",
         "Last two reps: have someone (or a parked car) ahead as a pretend &ldquo;threat&rdquo; and rehearse "
         "the full sequence: exhale &#8594; cue &#8594; turn &#8594; pay &#8594; scatter a 3-treat finder at 2 cars out."],
        ["By rep 7, he's wheeling on the CUE &#8212; before your body finishes turning",
         "You can do it at a trot without the leash tightening"],
        ["You're towing him through the turn &#8212; cue is landing AFTER your turn; say it a full beat first",
         "Your &ldquo;THIS WAY&rdquo; sounds like a fire alarm &#8212; it must sound like free pizza; "
         "rehearse the tone without the dog (yes, really, in the shower)"],
        "He plants and won't turn on rep 1? Lure the first three: cue, show the treat at his nose, "
        "turn, pay after three steps. Fade the lure by rep 5. Reflex first, pride later.")
    )

    out.append(day_page(11, "WEEK 2 &#183; ANCHOR", "Mix it: loops, U-turns, and the finder, all in one session.",
        "Route A, quiet hour. Real sessions aren't drills in a row; they're judgment calls. Today you "
        "practice the judgment: zone says loop, yellow says U-turn, tight pass says finder.",
        "DRILL &#183; THE FULL TOOLKIT", "10&#8211;14 REPS MIXED",
        ["Re-measure. Then walk Route A reading zones out loud (quietly): &ldquo;green&hellip; green&hellip; "
         "yellow.&rdquo; Saying it sharpens it.",
         "Green-zone sighting &#8594; work 4&#8211;6 loops.",
         "Mouth closes / yellow edge &#8594; <b>U-turn immediately</b>, even mid-loop. Exiting yellow on cue "
         "IS a rep &#8212; log it as one.",
         "Unavoidable closer pass (sidewalk narrows)? <b>Finder:</b> scatter 3 treats in the grass at "
         "your feet at the widest available arc; let him hoover while it passes; YES and stroll on.",
         "Cap at 14 total actions. End on a loop, not an escape, if the street allows."],
        ["You made 3+ zone calls correctly (the log will tell you &#8212; latency and mouth scores don't lie)",
         "At least one mid-loop U-turn taken without hesitation"],
        ["You finished loops &ldquo;just one more&rdquo; into yellow &#8212; greed is the enemy of the anchor; "
         "the early exit is the advanced move",
         "Finder turns into floor-vacuuming the whole walk &#8212; it's an emergency tool, max 2 per session"],
        "If everything melted today &#8212; calls wrong, loops slow &#8212; check the bucket first (what happened "
        "at home this morning?) before blaming the method. Full bucket = quiet day, retry tomorrow.")
    )

    out.append(day_page(12, "WEEK 2 &#183; ANCHOR", "Quiet Day II. The bucket drain is part of the machine.",
        "Sniffari, 20 minutes, boring green space, long line. After four working days, today is "
        "maintenance on the only hardware you can't buy: his baseline.",
        "MISSION &#183; SNIFFARI II", "20 MIN",
        ["Same rules as day 5: nose drives, you steer nothing, fewer than ten words.",
         "Watch for the difference a week makes: many dogs sniff DEEPER and check in MORE on the "
         "second sniffari. Note it if you see it.",
         "Gear audit tonight: pouch seams, harness fit (two fingers under every strap), leash clip "
         "spring. Week 3 works closer; equipment failures get expensive closer.",
         "Skim pages 54Skim pages 53&#8211;58#8211;59 (the emergency scripts) once. You want them loaded before you need them."],
        ["15+ nose-down minutes; you resisted all temptation to train",
         "Gear checked, emergency pages skimmed"],
        ["&ldquo;He did so well this week, we did a few loops&rdquo; &#8212; the drain day drains; "
         "that's its entire job",
         "He scanned more than sniffed &#8212; if this is two sniffaris in a row, your neighborhood baseline "
         "may be too loud; next quiet day, drive 5 minutes to somewhere genuinely dull"],
        "Quiet days feel like &ldquo;losing momentum&rdquo; to motivated owners. Re-read p. 12: the echo "
        "math says rest days are where the gains consolidate. Champions take the rest day.")
    )

    out.append(day_page(13, "WEEK 2 &#183; ANCHOR", "The two-trigger session: work the bucket on purpose.",
        "Route A at a slightly busier window (15&#8211;30 min later than usual). Today's skill is SEQUENCING: "
        "handling a second sighting while the first is still draining.",
        "DRILL &#183; BACK-TO-BACK SIGHTINGS", "2 SETS",
        ["Re-measure. Work the first sighting normally: 5&#8211;6 loops, end clean.",
         "<b>Before the second sighting, re-measure again.</b> After sighting one, today's number is "
         "temporarily +1 to +2. Honor the surcharge: set up the second set FATTER than the first.",
         "Work sighting two at the surcharged distance: 4&#8211;5 loops, end early, sniff out long (5 minutes).",
         "That's it. Two sets is the whole day. The lesson is the surcharge, not the volume."],
        ["Both sets green; second set run at a wider distance ON PURPOSE",
         "He could still eat instantly at the end of set two"],
        ["You ran set two at set-one's distance because set one went great &#8212; that's exactly how "
         "day-13s end in barking; the surcharge is the syllabus",
         "No second sighting appeared &#8212; fine; bank set one and take the win; sequencing reappears day 19"],
        "Set one ends in a blow-up? Today becomes a Quiet Day from that second forward (sniff home the "
        "long way), and tomorrow's re-measure decides everything. One bad set costs a day, never the plan.")
    )

    out.append(day_page(14, "WEEK 2 &#183; ANCHOR", "Re-measure ceremony: watch the number move.",
        "Route A, the original quiet hour &#8212; the same conditions as day 3, on purpose. Today is the "
        "first read on the only metric that matters.",
        "DRILL &#183; THE FORMAL RE-MEASURE", "3&#8211;5 TESTS + REVIEW",
        ["Run the exact day-3 protocol: food tests at descending distances, 3 instant-greens in a row "
         "to confirm. No loops first &#8212; clean instrument, clean read.",
         "Compare to the day-3 number in pen on the Baseline sheet. Most dogs who followed the week: "
         "<b>1&#8211;3 cars tighter.</b> Some hold flat &#8212; flat with two weeks of calm walks is still a win.",
         "Then a victory lap: 6 easy loops at the NEW number (or old one if flat), jackpot the best one.",
         "Home: Week Review (p. 71). Fill the trend line. Read what you wrote to yourself on day 7."],
        ["A confirmed number written next to day-3's; ANY direction logged honestly",
         "Loops at today's number felt routine &#8212; the anchor is set"],
        ["Number went UP &#8212; almost always bucket, weather, or a hidden stressor (construction next door?); "
         "re-run in two days before concluding anything",
         "You skipped the ceremony because &ldquo;you can feel it's better&rdquo; &#8212; feelings said "
         "&ldquo;back to square one&rdquo; on day 9; only the pen tells the truth"],
        "Whatever the number says: ANCHOR phase is complete &#8212; reflex installed, escape drilled, "
        "bucket respected. Week 3 is where the map starts shrinking.",
        note="Half the plan is behind you. If you've blown a day or three: normal. The streak that "
             "matters is measured in weeks."))

    # ---------------- WEEK 3
    out.append(_pg(pad(
        kicker("DAYS 15&#8211;21")
        + h1("Week 3 &#8212; SHRINK: climb down the ladder")
        + p("Now the payoff structure: the 3-for-3 ladder turns distance into a game you can win on "
            "purpose. Three clean loops at the rung &#8594; earn one car &#8594; repeat. You'll also take the "
            "show to a new location, rehearse an ambush on purpose, and finish with a graduation walk "
            "at normal human hours.")
        + table(["Day", "Job", "Minutes"],
            [["15", "The ladder, first descent", "16"],
             ["16", "Ladder II: movers on the rungs", "16"],
             ["17", "Banked-win day: easy session at +2 (insurance, by design)", "16"],
             ["18", "New location: the generalization tax", "16"],
             ["19", "Ladder + a rehearsed ambush", "16"],
             ["20", "The parallel walk (following a calm dog)", "16"],
             ["21", "Graduation walk + final measure + what's next", "25"]])
        + callout("key", "&#9733; LADDER LAW",
            p("You can only EARN distance; you can never take it on credit. Three clean loops &#8212; "
              "instant food, fast flick-backs, soft mouth &#8212; at the current rung, across at least two "
              "sightings, buys exactly one car. A single red moment refunds two. The ladder is slower "
              "than your ambition and faster than anything else you've tried."))
    ), toc="Week 3 overview &#8212; SHRINK"))

    out.append(day_page(15, "WEEK 3 &#183; SHRINK", "First descent: earn your first car.",
        "Route A, quiet hour. The ladder starts at yesterday's confirmed number. Today you earn "
        "(maybe) one car. That's not a small day; that's the mechanism working in daylight.",
        "DRILL &#183; THE 3-FOR-3 LADDER (p. 28)", "2&#8211;3 RUNGS MAX",
        ["Re-measure at the number. Green? This is rung one.",
         "Work loops at the rung. Count CLEAN ones only: instant eat, flick-back under ~3 seconds, "
         "mouth soft. Three clean &#8212; across 2+ sightings &#8212; rings the bell.",
         "<b>Step ONE car closer.</b> Re-test with a food test. Green? New rung; work it.",
         "Two rungs is a strong day; three is the ceiling even if he's flawless. End mid-rung if "
         "the clock says so &#8212; rungs don't expire overnight.",
         "Log the rung you ended on; that's tomorrow's start."],
        ["You banked at least one earned car with the 3-for-3 receipts in the log",
         "Every step closer was preceded by a green food test, no exceptions"],
        ["You took two cars at once because three loops felt easy &#8212; one rung per bell; the ladder's "
         "pace IS its power",
         "Stuck at rung one all session &#8212; fine and normal on day one of laddering; a no-progress green "
         "day still banks reps"],
        "Red moment on a new rung? Refund two cars immediately, finish the session at the wider rung, "
        "and note what was different (mover? head-on? second trigger?). The ladder forgives; it just bills.")
    )

    out.append(day_page(16, "WEEK 3 &#183; SHRINK", "Ladder II: put movers on the rungs.",
        "Route A or your manufactured-traffic spot (day 9). Same ladder, harder material: today's "
        "clean-rep standard includes triggers in motion.",
        "DRILL &#183; LADDER VS MOTION", "2 RUNGS MAX",
        ["Re-measure on a mover. Your moving-number may sit +1 to +2 above yesterday's rung &#8212; "
         "that's today's rung one.",
         "Ladder exactly as day 15, movers only: 3 clean loops on lateral movers = 1 car.",
         "Keep statics in play as palate cleansers between mover sets &#8212; easy wins hold the mood up.",
         "Head-on traffic remains off-syllabus until day 19's rehearsal. Cross early, arc wide, no apology."],
        ["One earned car against movers (or honest receipts showing why not today)",
         "Palate-cleanser statics stayed boringly green throughout"],
        ["Mover rungs collapse the moment the trigger barks back &#8212; loud triggers are a different "
         "trigger class; give them their own number and ladder them separately",
         "You chased a fast mover to keep it in range &#8212; never close distance ON a trigger; "
         "let traffic come to the zone"],
        "Windy/garbage-truck/chaos day reading as red everywhere? Swap today and tomorrow: take the "
        "banked-win day now, run movers tomorrow. The plan's order bends; the rules don't.")
    )

    out.append(day_page(17, "WEEK 3 &#183; SHRINK", "Banked-win day: deposit confidence on purpose.",
        "Route A at the number <b>plus two</b> &#8212; yes, wider than your newest rung. A deliberately "
        "easy day placed exactly where most plans collapse: right after two days of pushing.",
        "DRILL &#183; EASY LOOPS + ONE PARTY", "8 LOOPS",
        ["Re-measure, add two cars to wherever the ladder stands. Work THERE. It should feel almost "
         "silly. That's the assignment.",
         "8 loops across 2&#8211;3 sightings. Jackpot the single best flick-back of the day like he "
         "just returned a lost wallet.",
         "Five-minute sniff out. Done in 14 minutes. Resist all ladder thoughts.",
         "Tonight: read Part V's first page (p. 63) &#8212; the maintenance pattern starts making sense now."],
        ["Eight boringly perfect loops; one jackpot party; an early quit",
         "He ended the session looking at you like the pouch owes him money &#8212; that's the emotional "
         "balance we're banking"],
        ["You &ldquo;tested&rdquo; the new rung just once at the end &#8212; the win stays banked only if "
         "it stays easy; greed audit, page 37, read it again",
         "It felt pointless &#8212; good; cheap deposits compound; this is the day that pays for day 19"],
        "If even +2 reads yellow today, the bucket is talking (busy weekend? visitors?). Convert to a "
        "full Quiet Day without guilt and shift the week by one. Floors, not deadlines.")
    )

    out.append(day_page(18, "WEEK 3 &#183; SHRINK", "New location: pay the generalization tax.",
        "A DIFFERENT neighborhood, park edge, or big-box parking lot &#8212; somewhere he's been rarely "
        "or never. Dogs don't transfer skills between contexts for free; today buys the transfer.",
        "DRILL &#183; THE TRAVELING LADDER", "RE-MAP + 1&#8211;2 RUNGS",
        ["Treat it like day 2: full re-measure from generously far. <b>Expect the number to be fatter "
         "here &#8212; often +2 to +4.</b> This is the tax, not a relapse.",
         "Run easy loops at the new local number until they're smooth (usually 5&#8211;10 minutes).",
         "If smooth, ladder ONE rung the normal way. Two max.",
         "Note the gap between home-number and away-number in the log &#8212; watch that gap close over "
         "the next month; it's your best long-term progress gauge."],
        ["A measured away-number on paper and at least 6 clean loops at it",
         "You predicted the tax instead of being ambushed by it (your week-1 self wouldn't have)"],
        ["&ldquo;He KNOWS this!&rdquo; frustration when the away-number is fat &#8212; he knows it on Route A; "
         "context is half the skill; the tax is mandatory and it shrinks every visit",
         "New place is unworkably hot (off-leash chaos) &#8212; leave; scouting failures are cheap; "
         "pick somewhere duller tomorrow"],
        "Couldn't find a workable distance anywhere on site? Work from inside or beside your parked car "
        "&#8212; doors open, dog on the seat, world at 10 cars. Cars are portable Green Zones.")
    )

    out.append(day_page(19, "WEEK 3 &#183; SHRINK", "The rehearsed ambush: practice the worst case on your terms.",
        "Route A, plus a spot you've chosen in advance with a real blind corner (hedge, parked van). "
        "Today you simulate the nightmare &#8212; on purpose, with you in full control of the geometry.",
        "DRILL &#183; AMBUSH REHEARSAL", "3 RUNS + NORMAL LOOPS",
        ["Normal session start: re-measure, one set of loops wherever the ladder stands.",
         "Now the rehearsal: approach your blind corner. One step before the sight-line opens, "
         "run the full panic protocol AS IF a dog were there: exhale &#8594; <b>&ldquo;THIS WAY!&rdquo;</b> "
         "&#8594; turn &#8594; pay on the move &#8594; finder scatter at 2 cars.",
         "Three rehearsal runs, spaced minutes apart. Make the third one at a jog.",
         "If a REAL ambush happens today: you've literally been practicing; run the script, then quit "
         "for the day on that win."],
        ["Three crisp full-sequence rehearsals; the cue came out party-toned under fake pressure",
         "Regular loops in the same session stayed green (rehearsals didn't leak stress into the work)"],
        ["Your fake &ldquo;THIS WAY&rdquo; is flat because &ldquo;he can tell there's nothing there&rdquo; &#8212; "
         "HE can't tell what you're rehearsing, but YOUR voice-under-load is the skill being built",
         "You rehearsed right next to a real fence-dog &ldquo;for realism&rdquo; &#8212; rehearsals are "
         "choreography, not stunts; empty corner, every time"],
        "This drill is what makes week-4-and-beyond ambushes survivable: when the husky finally does "
        "appear at two cars, your mouth will say the line before your brain finishes panicking. "
        "That's the entire point of rehearsal.")
    )

    out.append(day_page(20, "WEEK 3 &#183; SHRINK", "The parallel walk: motion, same direction, shared world.",
        "A park path or wide sidewalk where dog traffic flows one way. The easiest hard thing in dog "
        "training: FOLLOWING a calm dog at distance. Same-direction motion reads as 'pack drift', "
        "not confrontation.",
        "DRILL &#183; THE SHADOW WALK", "1&#8211;2 FOLLOWS",
        ["Spot a calm, leashed dog moving away from you. Fall in BEHIND at your current rung + 1.",
         "Walk parallel/behind, matching pace, loops as offered: every glance at the dog that flicks "
         "back to you &#8212; YES, knee.",
         "If he forgets the dog and just walks &#8212; jackpot THAT. Co-existing without working is the "
         "actual end-state of this whole book.",
         "3&#8211;4 minutes per follow, then peel off on an arc. One or two follows is the day."],
        ["3+ minutes of following with a soft body and at least a few self-interruptions",
         "You peeled off BEFORE it degraded (ending early is still the advanced move)"],
        ["Following tips into hunting &#8212; stiff tail-up stalk &#8212; you're too close for this dog; "
         "+2 cars or pick a slower target",
         "The target dog's owner keeps glancing back nervously &#8212; bigger gap; we don't train at "
         "other people's expense; 'he's in training' + wave covers the rest"],
        "No candidate dogs? Follow a jogger or a stroller at distance &#8212; the mechanics (sustained "
        "same-direction motion + voluntary check-ins) transfer fine. Targets are fuel, not the lesson.")
    )

    out.append(day_page(21, "WEEK 3 &#183; SHRINK", "Graduation: the normal walk, at normal hours, on the record.",
        "Route A at a NORMAL human hour &#8212; the time you used to avoid. Full kit, full hour of margin, "
        "and the Week Review open on the counter for when you get back.",
        "MISSION &#183; THE GRADUATION WALK", "25 MIN",
        ["Walk Route A like a person walking a dog: J-leash, zones read aloud quietly, loops where "
         "offered, U-turns where needed, finder if pinched. Use everything; force nothing.",
         "Mid-walk, run one formal food-test confirmation at your best current rung &#8212; the final "
         "number for the book's record.",
         "Home: final Week Review + the day-21 letter to yourself (p. 71): three sentences &#8212; what "
         "the number was on day 3, what it is now, what surprised you.",
         "Then read Part V (p. 63). Tomorrow starts the maintenance pattern: 3 short pattern walks + "
         "1 sniffari + ladder work twice a week."],
        ["Completed the route at normal hours using the toolkit, whatever the street threw at you",
         "Final number logged; it's smaller than day 3's, or you know exactly why not (and Part IV's "
         "regression script is already in hand)"],
        ["Perfect-walk expectations &#8212; graduation means the SYSTEM is installed, not that huskies "
         "stopped existing; a clean U-turn on the graduation walk is a pass, not an asterisk",
         "Skipping the letter &#8212; write it; week-6-you, mid-regression-wave, needs it more than "
         "today-you knows"],
        "However the number reads: you now run a measured system most owners &#8212; and frankly some "
        "trainers &#8212; never learn. Day 22 isn't the end of the plan. It's the first day the plan "
        "belongs to you.",
        note="GRADUATION. Part V takes it from here &#8212; ten minutes of reading on keeping, growing, "
             "and troubleshooting the skill for the life of the dog."))

    return out
