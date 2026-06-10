"""FE Part V — Keeping It (maintenance) + worksheets + summary + glossary + closing."""
from design import *
from fe_front import PARTCOLORS

P, C = "V", PARTCOLORS["V"]

def _pg(body, toc=None):
    return {"html": body, "part": f"PART {P}", "color": C, "toc": toc}

def _ws(body, toc=None):
    return {"html": body, "part": "WS", "color": PALETTE["forest"], "toc": toc}

def pages():
    out = []

    out.append({"raw_divider": ("05", "PART FIVE", "Keeping It",
        "Day 21 isn't a finish line; it's a handover. The system is yours now. Here is the "
        "maintenance pattern, the growth path, and the honest line where a book ends and a "
        "professional begins.",
        ["The weekly maintenance pattern", "Generalization: new streets, new triggers, higher bars",
         "When to call a professional (and how to pick one)"]),
        "toc_part": "PART V &#8212; KEEPING IT"})

    out.append(_pg(pad(
        kicker("AFTER DAY 21")
        + h1("The maintenance pattern: 90 minutes a week, forever-ish")
        + p("New wiring needs traffic or it fades &#8212; but maintenance traffic is light. The weekly "
            "pattern that keeps the number shrinking on its own:")
        + table(["Slot", "What", "Time"],
            [["&#215;3 / week", "<b>Pattern walks:</b> normal walks on known routes, loops wherever the "
              "street offers them, U-turns when owed. Training disguised as life.", "20 min each"],
             ["&#215;1 / week", "<b>Sniffari.</b> Non-negotiable, permanent. The drain stays plumbed.", "20 min"],
             ["&#215;2 / week", "<b>Ladder sessions:</b> real 3-for-3 work at the current rung &#8212; this is "
              "where the number keeps falling.", "16 min each"]])
        + callout("key", "&#9733; THE MAINTENANCE LAWS",
            "<ul><li><b>Re-measure monthly</b>, formally, day-3 protocol, in pen, same page of the log. "
            "Five minutes that catches drift while it's cheap to fix.</li>"
            "<li><b>Jackpots never retire.</b> The day the hard look-backs stop paying premium is the "
            "day the habit starts negotiating.</li>"
            "<li><b>One rehearsed ambush a month</b> (day-19 drill) keeps the U-turn in your spine.</li></ul>")
        + p("Most owners report the pattern stops feeling like training around week 6 &#8212; it's just "
            "how you walk this dog now. That's not you slacking; that's the system reaching its "
            "designed end-state: <b>invisible.</b>")
    ), toc="The maintenance pattern"))

    out.append(_pg(pad(
        kicker("RAISING THE BAR")
        + h1("Generalization: spending your gains")
        + p("The number on Route A is the prototype. The life you actually wanted back &#8212; patios, "
            "trails, visiting your sister and her terrible doodle &#8212; is bought by deliberately "
            "spending gains in new places. The rules of expansion:")
        + cklist([
            "<b>One new variable at a time.</b> New place OR new trigger class OR busier hour &#8212; never "
            "two at once. Each new variable starts at +2 to +4 cars (the tax, day 18) and shrinks fast.",
            "<b>Patios start at off-peak.</b> Tuesday 2pm caf&#233;, table at the edge, mat under him, "
            "finder scatters for passing dogs. Ten quiet minutes, leave wanting more. Three visits "
            "before you try a weekend.",
            "<b>Trails: long line + the same zones.</b> Blind curves are the hallway problem (p. 59) "
            "wearing hiking boots: doorway-pause every bend you can't see past.",
            "<b>Houseguests and other homes:</b> the doorbell and the threshold are different problems "
            "than the sidewalk (different system entirely &#8212; Hard Cases #8 scripts it). Don't "
            "freelance it with leash-method tools and conclude the method failed.",
            "<b>The doodle summit:</b> parallel walks (day 20) on neutral ground &#215;3 before any "
            "yard-sharing. Calm co-walking IS the relationship; greeting is optional, often forever, "
            "and that's a fine outcome.",
        ])
        + callout("note", "&#9998; THE GOAL, RESTATED HONESTLY",
            p("Some dogs end up with dog friends. Many end up gloriously, peacefully indifferent &#8212; "
              "they walk past the world like it's furniture. Indifference is not a consolation prize; "
              "it is the prize. The dream was always the boring walk."))
    ), toc="Generalization: spending your gains"))

    out.append(_pg(pad(
        kicker("THE HONEST LINE")
        + h1("When to call a professional &#8212; and how to pick a good one")
        + p("This book covers the fat middle of leash reactivity. These flags mean you've left the "
            "middle, and paying a good professional is the move (it's also what the author of any "
            "honest book would do):")
        + xlist([
            "Any bite that broke skin, ever &#8212; dog or human.",
            "Explosions whose TARGET is children, or hard silent staring at kids.",
            "The number won't confirm anywhere &#8212; red at every distance you can physically find.",
            "Reactivity is spreading: new trigger classes appearing monthly despite clean work.",
            "Home is not safe-feeling: guarding food/space/people against the household.",
            "Your own anxiety is now the ceiling &#8212; you can't breathe out, and he reads it (no shame; "
            "handlers have nervous systems too).",
        ])
        + h3("HOW TO PICK (THE 5-MINUTE SCREEN)")
        + cklist([
            "Titles that mean schooling: <b>DACVB</b> (veterinary behaviorist) &gt; <b>CAAB</b> &gt; "
            "<b>CPDT-KA / KPA-CTP / IAABC</b> (certified trainers). &ldquo;20 years with dogs&rdquo; is not a credential.",
            "Ask: &ldquo;How will we work with my dog around triggers?&rdquo; The right answer contains "
            "<b>under threshold / distance / counterconditioning</b>. The wrong answer contains "
            "<b>pack leader, dominance, correction, or &ldquo;he'll wear the e-collar for a few weeks.&rdquo;</b>",
            "A good one will ask YOU for data. Hand them your logs from this book &#8212; you'll be their "
            "favorite client of the year, and you'll skip three paid sessions of discovery.",
        ])
        + callout("note", "&#9998; THE MUZZLE PARAGRAPH (PROMISED ON THE SAFETY PAGE)",
            p("Basket muzzle intro, the kind way, ~1 week: night 1&#8211;2, muzzle on the floor = treats "
              "rain near it. Night 3&#8211;4, treats eaten THROUGH it (smear peanut butter inside; he "
              "pokes his own nose in; never push). Night 5&#8211;6, strap clipped for 10 seconds &#8594; "
              "treat &#8594; off; stretch to minutes. Day 7, first short walk. A dog who wears a muzzle "
              "like sunglasses gets a bigger life, not a smaller one."))
    ), toc="When to call a professional"))

    # ------------- worksheets
    out.append(_ws(pad(
        kicker("WORKSHEET 01")
        + h1("Baseline &amp; The Number")
        + wline("Dog &#183; age &#183; the trigger list, worst first", 2)
        + cols(
            wline("DAY 2 &#8212; provisional number (cars)", 1)
            + wline("DAY 3 &#8212; confirmed number (3 greens)", 1)
            + wline("His tell (first loading signal)", 1),
            wline("DAY 14 &#8212; re-measure", 1)
            + wline("DAY 21 &#8212; graduation number", 1)
            + wline("MONTHLY &#8212; date / number", 3))
        + wgrid(["Food test #", "Trigger", "Cars", "Mouth (instant/slow/refused)"], 6,
                ["14%", "34%", "14%", "38%"])
        + small("One sheet per dog. Photocopy or re-draw freely &#8212; this page is the spine of the whole plan.")
    ), toc="Worksheet: Baseline &amp; the Number"))

    out.append(_ws(pad(
        kicker("WORKSHEET 02")
        + h1("Trigger Inventory")
        + p("From the day-1 scout walk, then growing for the life of the dog. A trigger CLASS gets a "
            "row, not each individual dog.", "small")
        + wgrid(["Trigger class", "Worst version of it", "Calm at (cars)", "Loads at (cars)", "Notes"],
                10, ["22%", "26%", "14%", "14%", "24%"])
        + callout("note", "&#9998; HOW TO READ IT BACK",
            p("Your training partner is the class with the most sightings, not the scariest one. "
              "Rare-but-nuclear (the husky who lives two blocks over) gets a route answer, not a "
              "training answer, until the common stuff is boring."))
    ), toc="Worksheet: Trigger Inventory"))

    out.append(_ws(pad(
        kicker("WORKSHEET 03")
        + h1("Route Planner")
        + p("Draw your blocks. Red-box the trigger houses. Mark escapes with E. Route A passes "
            "sight-lines at or beyond the number; Route B is the bunker.", "small")
        + wbox("ROUTE A &#8212; training route", 270)
        + wbox("ROUTE B &#8212; bail-out route", 200)
        + cols(wline("Pinch points I cannot fix", 2), wline("Loose-dog houses (date last seen)", 2))
    ), toc="Worksheet: Route Planner"))

    out.append(_ws(pad(
        kicker("WORKSHEET 04")
        + h1("Daily Walk Log")
        + p("Two minutes, kettle on. The trend line on this page is the entire antidote to "
            "&ldquo;back to square one.&rdquo;", "small")
        + wgrid(["Day", "Route", "Working distance (cars)", "Loops (clean/total)", "U-turns", "Mouth score", "Bucket note"],
                12, ["8%", "10%", "20%", "16%", "10%", "14%", "22%"])
        + small("Bucket note = anything that filled it today: visitors, fireworks, vet, fence fight, skipped sniffari.")
    ), toc="Worksheet: Daily Walk Log"))

    out.append(_ws(pad(
        kicker("WORKSHEET 05")
        + h1("The 3-for-3 Ladder Tracker")
        + p("One row per rung. Three clean-rep boxes; the date column only fills when the bell rings. "
            "Red moment = cross out the rung below and re-enter it two rows later.", "small")
        + wgrid(["Rung (cars)", "Clean rep 1", "Clean rep 2", "Clean rep 3", "Earned on (date)", "Notes"],
                11, ["16%", "13%", "13%", "13%", "19%", "26%"])
        + callout("key", "&#9733; LADDER LAW, POCKET EDITION",
            p("Earn, never borrow. Three cleans across two-plus sightings = one car. "
              "One red = two cars refunded. The ladder is patient; that's why it works."))
    ), toc="Worksheet: 3-for-3 Tracker"))

    out.append(_ws(pad(
        kicker("WORKSHEET 06")
        + h1("Week Review")
        + cols(
            wline("Week # &#183; dates", 1)
            + wline("This week's average working distance", 1)
            + wline("Last week's average", 1)
            + wline("Best moment (be specific)", 2),
            wline("Worst moment + which script you ran", 2)
            + wline("Bucket events I didn't control", 1)
            + wline("Next week's single focus", 1)
            + wline("Note to future-me on a bad day", 2))
        + pull("Judge the week's average, never the day. The pen out-argues the despair.", "the whole point of this page")
        + small("Three copies needed for the plan (days 7, 14, 21); then monthly. Photocopy freely.")
    ), toc="Worksheet: Week Review"))

    out.append(_pg(pad(
        kicker("THE WHOLE BOOK, ONE PAGE")
        + h1("The Green Zone Method&#8482; &#8212; field summary")
        + fig(svg_method_phases())
        + cols(
            h3("THE LAWS") + cklist([
                "Distance first. Always.",
                "Never train red. Red = exit, not lesson.",
                "Measure, don't vibe: food test + car count.",
                "3 cleans buy 1 car. 1 red refunds 2.",
                "End on a win, one rep early.",
                "Sniffing drains the bucket. Schedule it.",
            ]),
            h3("THE MOVES") + cklist([
                "<b>Food Test:</b> one treat at the nose &#8594; instant / slow / refused = green / yellow / red.",
                "<b>The Loop:</b> sees trigger &#8594; flicks back &#8594; &ldquo;YES&rdquo; &#8594; pay at the knee.",
                "<b>U-Turn:</b> &ldquo;THIS WAY!&rdquo; party voice &#8594; your body turns first.",
                "<b>Finder:</b> 3 treats in the grass buys 10 seconds and a calmer brain.",
                "<b>Recovery:</b> move &#8594; silence &#8594; scatter &#8594; quiet 48h.",
            ]))
        + callout("key", "&#9733; AND THE SENTENCE THAT REPLACES ALL OF IT",
            p("<b>Find the distance where your dog can think, pay him for thinking there, and shrink "
              "that distance on a rule instead of a hope.</b>"))
    ), toc="Field summary (one page)"))

    gl1 = [
        ("The bucket", "the running total of stress chemistry; fills in drips, drains over 24&#8211;72 hours. Full bucket = shorter fuse (p. 11)."),
        ("Car-length", "this book's unit of distance: one parked car &#8776; 15 ft including the gap. Countable mid-crisis."),
        ("Counterconditioning", "changing the trigger's emotional meaning by pairing it, below threshold, with good things. Half the engine of this method."),
        ("Desensitization", "the other half: graduated exposure at intensities the dog can handle &#8212; the ladder, in science clothes."),
        ("Finder / scatter", "2&#8211;3 treats dropped in grass; sniffing occupies eyes + brain and self-soothes. Emergency tool, 2-per-session cap."),
        ("Flooding", "exposure OVER threshold &#8212; the Exposure Trap's real name. Teaches panic, occasionally teaches silence, never teaches calm (p. 8)."),
        ("Food test", "one treat at the nose at the moment of noticing: instant / slow / refused reads the zone exactly (p. 18)."),
        ("Frustration reactivity", "the &ldquo;let me SAY HI&rdquo; screamer: pulls toward, friendly off-leash. Same plan, day-9 footnote."),
        ("Generalization (and its tax)", "skills don't transfer to new contexts for free; every new venue starts +2&#8211;4 cars and shrinks fast (day 18)."),
        ("Green Zone", "distance at which the dog can notice a trigger and still think, eat, and choose. The only place training happens."),
        ("Jackpot", "five treats, one at a time, party voice &#8212; the premium rate for hard choices. Never retires."),
        ("Ladder / 3-for-3", "three clean loops at a rung, across 2+ sightings, earns one car closer; a red moment refunds two (day 15)."),
    ]
    gl2 = [
        ("Loading signals", "the broadcast before the bark: mouth closes &#8594; ears lock &#8594; freeze &#8594; weight forward &#8594; launch (p. 20)."),
        ("The Loop", "engage&#8211;disengage: dog looks at trigger, chooses to look back, marker, pay at the knee. The engine (p. 22)."),
        ("Management", "arranging the world so rehearsal can't happen (routes, hours, barriers). Not defeat &#8212; scaffolding."),
        ("Marker", "one clipped word (&ldquo;YES&rdquo;) that photographs the exact behavior being paid (p. 21)."),
        ("The number", "your dog's current confirmed Green Zone distance, in cars. The protagonist of this book."),
        ("Opposition reflex", "automatic push against leash pressure; why tight lines feed lunges (p. 25)."),
        ("Quiet Day / sniffari", "a dog-driven sniffing walk with no agenda; the bucket's drain valve, scheduled weekly forever."),
        ("Red Zone", "over threshold: explosion or pre-explosion freeze. Nothing is learnable here except the explosion itself."),
        ("Threshold", "the line where coping ends and the alarm takes over; measured in distance, read by the mouth (p. 9)."),
        ("Trigger", "anything that reliably starts the loading sequence. Logged by CLASS (dogs, kids, bikes), each with its own number."),
        ("Trigger stacking", "drips accumulating faster than the drain; why Tuesday's corgi exploded when Monday's didn't (p. 11)."),
        ("Yellow Zone", "the warning band: stiff, slow-mouthed, locked on. One legal move: leave."),
    ]
    out.append(_pg(pad(
        kicker("GLOSSARY &#183; A&#8211;L")
        + h1("Speak the method")
        + "".join(gitem(t, d) for t, d in gl1)
    ), toc="Glossary"))
    out.append(_pg(pad(
        kicker("GLOSSARY &#183; L&#8211;Z")
        + h1("Speak the method, continued")
        + "".join(gitem(t, d) for t, d in gl2)
        + callout("note", "&#9998; WHY THE VOCABULARY MATTERS",
            p("Words are handles. The owner who can say &ldquo;he went yellow at four cars, I U-turned "
              "and finder-ed&rdquo; can debug a walk in one sentence &#8212; and explain it to a partner, "
              "a dog-sitter, or a trainer in two."))
    ), toc=None))

    out.append(_pg(pad(
        kicker("THE LAST PAGE")
        + h1("A closing letter, from one 5am walker to another")
        + dropcap("Somewhere back in week one, you wrote a number on a worksheet, and the problem "
                  "stopped being a monster and started being a measurement. That was the whole trick. "
                  "Everything after it was just reps.")
        + p("Nobody else will ever fully get it &#8212; the engineering behind your boring walk. The "
            "neighbors see a person strolling past a labradoodle, nothing happening. They cannot see "
            "the map, the ladder, the four hundred logged loops, the U-turns drilled until they "
            "live in your spine. Nothing happening, it turns out, is a built thing. You built it.")
        + p("Your dog never needed to become a different dog. He needed the world held at a distance "
            "where he could think &#8212; and a human with a system instead of a hope. He has one now. "
            "Keep the sniffaris sacred, keep the jackpots flowing, re-measure monthly, and when the "
            "wave dips &#8212; it will &#8212; you know exactly which page to open.")
        + p("Go walk your dog. At whatever hour you like.")
        + p("<b>&#8212; CalmWalk</b>")
        + '<hr class="rule-amber"/>'
        + small("The Green Zone Method&#8482; &#183; The 21-Day Calm Walks Plan &#183; &#169; CalmWalk. "
                "Educational material; not veterinary or behaviorist advice. Personal use; please "
                "don't redistribute &#8212; it keeps the lights on and the worksheets coming.")
    ), toc="A closing letter"))

    return out
