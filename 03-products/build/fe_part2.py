"""FE Part II — The Green Zone Method (the three moves)."""
from design import *
from fe_front import PARTCOLORS

P, C = "II", PARTCOLORS["II"]

def _pg(body, toc=None):
    return {"html": body, "part": f"PART {P}", "color": C, "toc": toc}

def pages():
    out = []

    out.append({"raw_divider": ("02", "PART TWO", "The Green Zone Method",
        "Three moves. That's the entire method. Map the zone, anchor a new habit inside it, "
        "then shrink it on a strict rule.",
        ["Phase 1 &#8212; MAP: the Food Test and your dog's number",
         "Reading the five loading signals",
         "Phase 2 &#8212; ANCHOR: the marker, the Loop, the U-turn",
         "Phase 3 &#8212; SHRINK: the 3-for-3 ladder",
         "Leash mechanics, gear, and the 16-minute session"]),
        "toc_part": "PART II &#8212; THE GREEN ZONE METHOD"})

    out.append(_pg(pad(
        kicker("THE METHOD AT A GLANCE")
        + h1("Three phases. One number. Twenty-one days.")
        + fig(svg_method_phases(), "FIG. 5 &#8212; THE WHOLE METHOD ON ONE CARD")
        + p("<b>MAP (days 1&#8211;5).</b> You find your dog's number: the distance, counted in parked "
            "cars, where he can see a trigger and still eat. No training yet. Just measurement, "
            "five days of easy wins, and a baseline on paper.")
        + p("<b>ANCHOR (days 6&#8211;12).</b> Inside the Green Zone you install one new reflex: "
            "<i>see the trigger &#8594; look back at you &#8594; get paid.</i> You also drill the Emergency "
            "U-Turn until it's muscle memory &#8212; yours, not just his.")
        + p("<b>SHRINK (days 13&#8211;21).</b> You close the distance one car-length at a time, and you "
            "only earn a car when you've banked three clean reps at the current one. By day 21 the "
            "ladder is yours for life: it keeps shrinking the number long after this book.")
        + callout("key", "&#9733; WHY IT WORKS WHEN THE FRAGMENTS DIDN'T",
            p("You may recognize the parts &#8212; you tried treats, you tried &ldquo;look at that.&rdquo; "
              "The parts were never the problem. The missing piece was the <b>dosage system</b>: "
              "a measured distance, a pass/fail rule, and a progression ladder. "
              "Pills work; fistfuls of powder don't. This is the pill."))
    ), toc="The method at a glance"))

    out.append(_pg(pad(
        kicker("PHASE 1 &#183; MAP")
        + h1("The Food Test: your dog's mouth is the gauge")
        + p("You cannot see threshold. You can see eating. They track each other so tightly that "
            "for our purposes they are the same thing &#8212; which turns your treat pouch into a "
            "measuring instrument.")
        + fig(svg_food_test(), "FIG. 6 &#8212; ONE TREAT, THREE POSSIBLE ANSWERS, ZERO GUESSWORK")
        + drill("DRILL &#183; THE FOOD TEST", "5 REPS / SESSION",
            "<ol><li>Spot a trigger your dog has noticed (ears up, head turned toward it). Stand still. Loose leash.</li>"
            "<li>Reach down and offer ONE pea-sized soft treat right at his nose. Say nothing.</li>"
            "<li>Score the mouth: <b>instant soft grab = GREEN. Slow, hard, distracted grab = YELLOW. "
            "Refusal or can't look away = RED.</b></li>"
            "<li>If yellow or red: add distance (cross, arc, retreat) and test again.</li>"
            "<li>Write the green distance down. That number is the whole point.</li></ol>")
        + callout("warn", "&#9888; THE TEST IS NOT A BRIBE",
            p("You are not trying to get him to eat. You are reading what his mouth already says. "
              "Shoving treats at a red-zone dog teaches him treats predict scary things. One offer, "
              "one read, then move."))
    ), toc="Phase 1 &#8212; the Food Test"))

    out.append(_pg(pad(
        kicker("PHASE 1 &#183; MAP")
        + h1("Count cars, not feet. Find the number.")
        + fig(svg_carlength(), "FIG. 7 &#8212; THE STREET IS ALREADY A RULER")
        + p("Feet are useless mid-walk &#8212; nobody can eyeball 75 feet with a barking dog on the line. "
            "Parked cars are everywhere, always the same size (about 15 feet with the gap), and "
            "countable under stress. So this book measures everything in cars.")
        + p("<b>Your dog's number</b> is the smallest count of cars at which the Food Test comes back "
            "green <b>three times in a row</b>. A typical starting number for a city-stressed reactive "
            "dog is 4&#8211;8 cars; some start at half a block. The number is not a grade. "
            "It is a starting line, and big numbers shrink on the same schedule as small ones.")
        + stats([("3&#215;", "GREEN TESTS = CONFIRMED"), ("4&#8211;8", "TYPICAL STARTING CARS"), ("&#8722;1", "CAR PER EARNED RUNG")])
        + callout("key", "&#9733; THE NUMBER MOVES &#8212; MEASURE DAILY",
            p("Remember the bucket (page 11). The number you confirmed Monday can be two cars longer "
              "on Tuesday after a noisy morning. <b>Every session in this plan begins with a 60-second "
              "re-measure</b>, and the day's work happens at TODAY'S number. The plan never asks "
              "&ldquo;where should he be by now?&rdquo; &#8212; only &ldquo;where is he today?&rdquo;"))
        + small("Suburban streets without parked cars: use driveways (&#8776;1 car each), sidewalk squares "
                "(&#8776;5ft &#8212; 3 squares to a car), or utility poles (&#8776;8 cars apart). Pick one ruler and keep it.")
    ), toc="Count cars: find the number"))

    out.append(_pg(pad(
        kicker("PHASE 1 &#183; MAP")
        + h1("The five loading signals: read the explosion before it ships")
        + fig(svg_body_language(), "FIG. 8 &#8212; THE BODY ANNOUNCES THE BARK 3&#8211;10 SECONDS EARLY")
        + p("Between green and explosion there is a loading sequence, and it is astonishingly "
            "consistent: <b>mouth closes &#8594; ears lock &#8594; body freezes &#8594; weight shifts forward "
            "&#8594; launch.</b> Most dogs broadcast it for three to ten full seconds. "
            "That window is where every save in this book happens.")
        + table(["Signal", "What you'll see", "What it means"],
            [["Mouth", "panting stops, lips close", "first alarm &#8212; the most reliable early signal"],
             ["Ears", "pinned flat or locked hard forward", "attention has narrowed to the trigger"],
             ["Tail", "high, stiff, slow metronome wag", "arousal climbing (a wag is NOT happiness)"],
             ["Weight", "chest drops, front legs brace", "body is preparing to lunge"],
             ["Freeze", "total statue, 1&#8211;2 seconds", "final boarding call &#8212; act NOW or it ships"]])
        + callout("key", "&#9733; YOUR NEW REFLEX",
            p("Mouth closes = you move. Don't wait to confirm with the other four. The closed mouth "
              "is yellow zone by definition, and yellow has exactly one job: add distance. "
              "Catch it at the mouth and your dog may never rehearse another full explosion."))
    ), toc="The five loading signals"))

    out.append(_pg(pad(
        kicker("PHASE 2 &#183; ANCHOR")
        + h1("The marker word: a camera shutter for good decisions")
        + p("Before the Loop, you need one tool: a <b>marker</b> &#8212; a single short word that means "
            "&ldquo;THAT exact thing you just did earned the food.&rdquo; We'll use <b>&ldquo;YES.&rdquo;</b> "
            "Said bright and clipped, it photographs the half-second of behavior you want more of, "
            "so the dog knows precisely what got paid.")
        + drill("DRILL &#183; CHARGING THE MARKER (KITCHEN, DAY 6)", "20 REPS &#215; 2",
            "<ol><li>Dog mildly interested, no triggers, TV off. Say <b>&ldquo;YES&rdquo;</b> once &#8212; bright, short.</li>"
            "<li>THEN reach for a treat and deliver at your knee. The order is sacred: word first, "
            "<i>then</i> the hand moves. The word predicts the hand &#8212; not the reverse.</li>"
            "<li>One-second pause between reps. Twenty reps, twice today. Done.</li></ol>")
        + passfail(
            ["Dog's head whips toward you on &ldquo;YES&rdquo; before your hand moves (test on rep 15+)",
             "Works in the yard, not just the kitchen"],
            ["Dog stares at your treat hand or pouch the whole time &#8212; your hand is moving too early",
             "Word is long, soft, or chatty (&ldquo;yesss good boooy&rdquo;) &#8212; keep it to one clipped syllable"])
        + callout("note", "&#9998; WHY NOT A CLICKER?",
            p("A clicker is excellent and your hands are full. Leash, pouch, poop bags, coffee &#8212; "
              "you need a marker that can't be dropped. Your voice is always loaded."))
    ), toc="Phase 2 &#8212; the marker word"))

    out.append(_pg(pad(
        kicker("PHASE 2 &#183; ANCHOR")
        + h1("The Loop: see it &#8594; look back &#8594; YES &#8594; paid")
        + fig(svg_engage_loop(391, 255), "FIG. 9 &#8212; ONE REP &#8776; 5 SECONDS, AND IT REWIRES THE TRIGGER")
        + p("This is the engine of the method: in the Green Zone your dog can look at a trigger "
            "<i>and think at the same time</i> &#8212; so we let him look, and we pay the look-away. "
            "Enough loops, and the sight of a dog stops meaning alarm and starts meaning easy money.")
        + drill("DRILL &#183; THE LOOP", "8&#8211;12 REPS / SESSION",
            "<ol><li>Set up in the Green Zone at today's number. Loose leash. Mouth open? Good.</li>"
            "<li><b>Let him notice the trigger. Say nothing.</b> This is the hard part. Wait.</li>"
            "<li>The instant his head turns back toward you &#8212; even a flick &#8212; <b>&ldquo;YES!&rdquo;</b> and pay at your knee.</li>"
            "<li>He'll look at the trigger again. Perfect. That's rep two. Same deal.</li>"
            "<li>After 8&#8211;12 reps or 90 seconds, walk away on a high note.</li>"
            "<li><b>Never cue it</b> &#8212; no &ldquo;look at me,&rdquo; no kissy noises, no name. The dog "
            "must <b>choose</b> the look-back; a choice becomes a habit.</li></ol>")
        + passfail(
            ["Look-backs are getting FASTER across the session", "Mouth stays soft; he eats instantly every rep"],
            ["He can't look away from the trigger at all &#8212; you're 1&#8211;2 cars too close. Back up, restart",
             "He won't look AT the trigger (avoidance) &#8212; also too close. Distance fixes both directions"])
    ), toc="The Loop (engage&#8211;disengage)"))

    out.append(_pg(pad(
        kicker("PHASE 2 &#183; ANCHOR")
        + h1("Treat delivery is steering")
        + fig(svg_treat_magnet(), "FIG. 10 &#8212; WHERE THE FOOD APPEARS DECIDES WHERE THE EYES GO NEXT")
        + p("Amateurs think the treat is the payment. Pros know the treat is also the <b>steering "
            "wheel</b>: where the food shows up controls where the dog's head, eyes, and feet point "
            "for the next three seconds. Three rules:")
        + cklist([
            "<b>Park the hand.</b> Between reps your treat hand lives flat on your chest. A hovering "
            "hand becomes the cue, and the dog watches the hand instead of making the choice.",
            "<b>Pay at the seam.</b> Deliver every treat at the side seam of your pants, at your knee. "
            "The dog must turn fully AWAY from the trigger to collect &#8212; you're paying for the "
            "look-back and buying body rotation for free.",
            "<b>Drop a finder.</b> When you need 3 extra seconds (trigger passing close), scatter "
            "2&#8211;3 treats in the grass at your feet. A sniffing dog is a self-calming dog with "
            "his eyes off the problem. This is the &ldquo;magnet,&rdquo; and it's legal anytime.",
        ])
        + callout("note", "&#9998; PAY SCALE",
            p("Green-zone routine rep: one pea-sized treat. Hard rep (trigger surprised you both and "
              "he STILL chose the look-back): jackpot &#8212; five treats, one at a time, party voice. "
              "Pay the hard ones like you mean it; dogs audit."))
    ), toc="Treat delivery is steering"))

    out.append(_pg(pad(
        kicker("PHASE 2 &#183; ANCHOR")
        + h1("The Emergency U-Turn: your get-out-of-red-free card")
        + fig(svg_uturn(), "FIG. 11 &#8212; TURN YOUR BODY FIRST; THE DOG FOLLOWS THE MOTION")
        + p("Sometimes the street ambushes you: a husky materializes from a driveway two cars away. "
            "No zone to work in &#8212; you need OUT. The U-turn must be drilled in peacetime "
            "until it's a reflex for both species, because mid-ambush nobody can think.")
        + drill("DRILL &#183; U-TURN (NO TRIGGERS PRESENT)", "10 REPS / DAY, DAYS 8&#8211;12",
            "<ol><li>Mid-walk, calm street: say <b>&ldquo;THIS WAY!&rdquo;</b> &#8212; bright, happy, like you "
            "just spotted free pizza behind you.</li>"
            "<li><b>Turn your own body 180&#176; and GO.</b> Don't pull the leash &#8212; the leash stays loose; "
            "your movement is the cue. Dogs follow momentum.</li>"
            "<li>As he wheels with you: &ldquo;YES,&rdquo; pay at the knee ON THE MOVE, keep walking 10 steps.</li>"
            "<li>Vary it: left turns, right arcs, jog-aways. Direction doesn't matter. Speed + cheer do.</li></ol>")
        + passfail(
            ["Dog whips around with you on &ldquo;THIS WAY&rdquo; before the leash could ever tighten",
             "Works at a trot, in both directions, on day 12"],
            ["You're hauling him around by the neck &#8212; you turned before he heard the cue. Cue, THEN turn",
             "Your voice sounds like an apology. The cue must sound like good news or it reads as your alarm"])
        + callout("key", "&#9733; PANIC PROTOCOL", p("Real ambush: <b>cue &#8594; turn &#8594; move &#8594; "
            "scatter a treat-finder once you're 2+ cars out.</b> Never stand and hold a screaming dog "
            "to &ldquo;wait it out.&rdquo; Distance first. Always distance first."))
    ), toc="The Emergency U-Turn"))

    out.append(_pg(pad(
        kicker("MECHANICS")
        + h1("The loose J: leash mechanics that don't light the fuse")
        + fig(svg_leash_J(), "FIG. 12 &#8212; THE SHAPE OF THE LEASH IS THE MOOD OF THE WALK")
        + p("Dogs have an <b>opposition reflex</b>: pressure on the neck or chest triggers an automatic "
            "push the other way. A tight line doesn't restrain arousal &#8212; it feeds it, and it "
            "broadcasts YOUR nerves down the rope like a telegraph. The fix is a shape: "
            "the leash should hang in a soft <b>J</b> between you.")
        + cklist([
            "<b>Two hands, thumb in the handle,</b> leash crossing your body. Elbows soft. "
            "A startle gets absorbed by your arms before it ever reaches the clip.",
            "<b>Shorten by gathering, not by winching.</b> If a trigger appears, take up slack "
            "smoothly so the J survives at a shorter length. The dog should never feel the adjustment.",
            "<b>Your breath is gear too.</b> One slow exhale when you spot a trigger before you do "
            "anything else. It steadies your hands, your voice, and &#8212; down the telegraph &#8212; your dog.",
        ])
        + callout("warn", "&#9888; IF HE'S ALREADY PULLING",
            p("Stop walking. Stand like a post (boring, not angry). The instant the leash softens "
              "even an inch: &ldquo;YES,&rdquo; pay at the knee, walk on. Three days of this and the J "
              "starts maintaining itself. Pulling only works if pulling works."))
    ), toc="Leash mechanics: the loose J"))

    out.append(_pg(pad(
        kicker("LOGISTICS")
        + h1("Gear, fuel, and the 16-minute session")
        + table(["Get this", "Skip this", "Why"],
            [["6-ft flat leash", "retractable anything", "retractables teach pulling, can't make a J, and fail at the worst moments"],
             ["front-clip harness (Y-front)", "prong / slip / e-collar", "we need the alarm system intact and triggers predicting good news (p. 13)"],
             ["silicone treat pouch on your belt", "treats in a coat pocket", "2 seconds of fumbling is the whole loading window (p. 20)"],
             ["100 pea-size soft treats per session", "kibble, biscuits", "this is brain surgery on a budget; pay in real currency &#8212; cheese, hot dog, chicken"]])
        + fig(svg_session_clock(), "FIG. 13 &#8212; A SESSION IS 16 MINUTES, BOOKENDED BY SNIFFING")
        + p("Every training day in Part III is this same sandwich: <b>3 minutes</b> of sniffy walking "
            "to drain the bucket on the way in &#8212; <b>10 minutes</b> of work (loops, tests, ladder reps) "
            "&#8212; <b>3 minutes</b> of sniffy walking out so the session ends in a soft place. "
            "Sniffing isn't the boring part of the walk; it's the drain valve (p. 11) and it's load-bearing.")
        + callout("key", "&#9733; SHORT BEATS LONG. EVERY TIME.",
            p("Ten focused minutes banks 8&#8211;12 clean reps. Forty heroic minutes fills the bucket, "
              "invites an ambush, and usually ends the streak. When in doubt, quit early on a win. "
              "The plan is 21 days long precisely so that no single day has to be big."))
    ), toc="Gear + the 16-minute session"))

    return out
