"""FE Part I — Why Everything Failed (diagnosis)."""
from design import *
from fe_front import PARTCOLORS

P, C = "I", PARTCOLORS["I"]

def _pg(body, toc=None):
    return {"html": body, "part": f"PART {P}", "color": C, "toc": toc}

def pages():
    out = []

    out.append({"raw_divider": ("01", "PART ONE", "Why Everything Failed",
        "Not you &#8212; the advice. Every fix you tried failed for the same mechanical reason. "
        "Once you see it, you can't unsee it.",
        ["What reactivity is (and what it isn't)", "The Exposure Trap",
         "Fear beats food: where the line is", "Trigger stacking and the 48-hour echo",
         "Why corrections load the bomb", "Why progress comes in waves"]),
        "toc_part": "PART I &#8212; WHY EVERYTHING FAILED"})

    out.append(_pg(pad(
        kicker("THE DIAGNOSIS")
        + h1("Your dog is not giving you a hard time. Your dog is having a hard time.")
        + dropcap("At home he is perfect. On the leash he becomes a different dog: locked eyes, "
                  "hackles, that explosion of barking that makes the whole street turn around. "
                  "Here is the first fact that changes everything: <b>that explosion is not "
                  "disobedience.</b> It is panic with a leash attached.")
        + p("Reactivity is a <b>big emotional response to a normal thing</b> &#8212; usually another dog, "
            "sometimes people, bikes, or trucks. Under the noise it is almost always one of two feelings:")
        + table(["The driver", "What it looks like", "What the dog is &ldquo;saying&rdquo;"],
            [["<b>Fear</b>", "barking while backing up, hiding behind you after, hackles, tucked tail between bursts",
              "&ldquo;Stay away from me. I'm scary, I promise!&rdquo;"],
             ["<b>Frustration</b>", "pulling TOWARD the trigger, whining, spinning, friendly off-leash with the same dogs",
              "&ldquo;Let me GET THERE and I can't and I'm losing my mind.&rdquo;"]])
        + p("Both run on the same wiring: the alarm system fires <b>before the thinking brain gets a vote.</b> "
            "That matters because you cannot reason, command, or correct a brain whose thinking part "
            "is offline. Every fix that failed, failed right there.")
        + callout("note", "&#9998; WHAT IT IS NOT",
            p("It is not dominance. It is not your dog &ldquo;protecting&rdquo; you. It is not because you "
              "&ldquo;let him on the couch.&rdquo; Forty years of behavior science retired those ideas; "
              "the people who repeat them just haven't gotten the memo."))
        + pull("He's not doing this on purpose to embarrass you. He's overwhelmed.", "every good trainer, eventually")
    ), toc="Your dog is not giving you a hard time"))

    out.append(_pg(pad(
        kicker("THE VILLAIN")
        + h1("The Exposure Trap: why &ldquo;socialize him more&rdquo; made it worse")
        + p("It is the most common advice in the world, and it is free, and it is confident, and for "
            "a reactive dog it is exactly backwards: <i>&ldquo;He just needs more exposure. Take him "
            "around more dogs. He'll get used to it.&rdquo;</i>")
        + p("Behavior science has a name for what that actually does: <b>flooding</b> &#8212; holding an "
            "animal inside its own alarm until the alarm burns out. Sometimes flooding produces a dog "
            "who stops barking. It almost never produces a dog who stops <i>fearing</i> &#8212; it produces "
            "a dog who stops <i>warning</i>. And most of the time it doesn't even do that. It does this instead:")
        + cklist([
            "Every close-range encounter fires the full alarm. The brain practices the explosion <b>like a rep at the gym.</b>",
            "What gets practiced gets stronger. Ten explosions a week is a training program &#8212; for explosions.",
            "The dog learns the leash predicts panic. Now the walk itself is loaded before you see a single dog.",
        ])
        + callout("key", "&#9733; THE SENTENCE THAT REPLACES THE BAD ADVICE",
            p("Reactive dogs do not get used to triggers by getting <b>closer</b>. They get used to "
              "triggers by winning easy reps <b>farther away</b> &#8212; at a distance where the alarm "
              "never fires at all. Distance first. Always distance first."))
        + p("So if you have spent months walking him &ldquo;past it&rdquo; while he screams, and he has "
            "gotten worse &#8212; nothing is wrong with your dog. The plan was upside down. "
            "You were running a strength program for the exact muscle you wanted to shrink.")
        + fixit(p("Guilt check: you did what everyone told you to do. The advice failed you; "
                  "you did not fail the dog. Now we do it the right way up."), head="READ THIS IF YOU FEEL AWFUL")
    ), toc="The Exposure Trap (&ldquo;socialize him more&rdquo;)"))

    out.append(_pg(pad(
        kicker("THE LINE NOBODY DREW")
        + h1("Fear beats food &#8212; every time, in every dog")
        + dropcap("You carried treats. Good treats. And in the moment that mattered, your dog &#8212; "
                  "a dog who would sell you to a stranger for cheese &#8212; turned his head away and screamed. "
                  "Here is the mechanism, because once you know it, you'll never blame him again.")
        + p("When the alarm system fires hard enough, the body shuts down digestion and gets ready to "
            "fight or run. A dog over that line <b>physically can't take food</b>, the same way you "
            "couldn't enjoy a sandwich while a fire alarm screams in your ear. "
            "The treat didn't fail. The treat was offered <b>on the wrong side of a line</b> "
            "nobody ever drew for you.")
        + stats([("EATS FAST", "UNDER THE LINE &#183; CAN LEARN"),
                 ("EATS SLOW", "AT THE LINE &#183; BARELY COPING"),
                 ("WON'T EAT", "OVER THE LINE &#183; ALARM ONLY")])
        + p("Trainers call the line <b>threshold</b>. Every dog has one, and it is measured in "
            "<b>distance</b>: how far away a trigger can be while your dog still thinks, sniffs, "
            "and eats. Close enough, and every dog on earth goes over. Far enough, and every dog "
            "on earth can cope. Your dog's line is just closer than you wish &#8212; for now.")
        + callout("key", "&#9733; WHY THIS IS THE WHOLE GAME",
            p("Learning only happens under the line. Treats only work under the line. Cues only work "
              "under the line. So the first job of this entire plan is not to train your dog at all &#8212; "
              "it is to <b>find your dog's line and refuse to cross it.</b> That is Phase 1, "
              "and it starts on page 18."))
        + pull("When your dog is in the middle of an explosive reaction, treats and baby talk just don't cut it.", "every reactive-dog owner, before learning about the line")
    ), toc="Fear beats food: where the line is"))

    out.append(_pg(pad(
        kicker("THE MAP")
        + h1("The three zones")
        + p("Draw the line, then add a buffer, and you get the map this whole method is named for. "
            "Around every trigger there are three zones:")
        + fig(svg_zone_map(), "FIG. 1 &#8212; THE ZONE MAP: the signature picture of this method")
        + cklist([
            "<b>Green Zone</b> &#8212; far enough that your dog can notice the trigger and still think, eat, "
            "and check in with you. <b>All training in this book happens here and only here.</b>",
            "<b>Yellow Zone</b> &#8212; the warning band: stiff body, slow mouth, hard stare. No learning here, "
            "only coping. Your job in yellow is one thing: get out, calmly, fast.",
            "<b>Red Zone</b> &#8212; over the line. The explosion, or the silent freeze before it. Nothing useful "
            "ever happens in red. Not training, not &ldquo;lessons,&rdquo; not corrections. Only rehearsal of the panic.",
        ])
        + callout("note", "&#9998; THE SHIFT",
            p("Stop thinking &ldquo;how do I stop the barking?&rdquo; Start thinking &ldquo;what zone are we "
              "in right now?&rdquo; The barking is just what red sounds like. Manage the zone "
              "and the barking manages itself."))
    ), toc="The three zones"))

    out.append(_pg(pad(
        kicker("WHY GOOD DAYS LIE")
        + h1("Trigger stacking: the bucket your dog carries")
        + p("Monday he walked past the corgi at four houses' distance, no problem. Tuesday the same corgi "
            "at the same distance blew him sky-high. Owners read that as random &#8212; or worse, as proof "
            "the training &ldquo;isn't working.&rdquo; It is neither. It is arithmetic.")
        + fig(svg_stress_bucket(), "FIG. 2 &#8212; EVERY STRESS DRIP STAYS IN THE BUCKET FOR HOURS")
        + p("Stress chemistry is a bucket, not a light switch. The trash truck at 7am, the doorbell at "
            "noon, the fence dog two blocks back &#8212; each one adds water, and the bucket drains "
            "<b>slowly</b>. An explosion happens when one more drip hits an already-full bucket. "
            "Tuesday's corgi wasn't scarier; Tuesday's bucket was fuller.")
        + callout("key", "&#9733; TWO PRACTICAL CONSEQUENCES",
            "<ul><li><b>Your dog's number moves day to day.</b> The plan teaches you to measure the bucket "
            "every session (it takes 60 seconds) and work at TODAY'S distance, not Monday's.</li>"
            "<li><b>After a blow-up, the bucket is brim-full for up to 48&#8211;72 hours.</b> "
            "Pushing training the next morning is training a full bucket. The plan builds in "
            "quiet days &#8212; they are not days off, they are the drain.</li></ul>")
    ), toc="Trigger stacking: the bucket"))

    out.append(_pg(pad(
        kicker("THE 48-HOUR ECHO")
        + h1("One bad moment costs three days. Spend accordingly.")
        + fig(svg_recovery_curve(), "FIG. 3 &#8212; AROUSAL AFTER AN EXPLOSION DRAINS IN DAYS, NOT MINUTES")
        + p("This chart is the most expensive thing in the book, because it prices every decision "
            "you'll make on a walk. After a full explosion, your dog's baseline chemistry stays "
            "high for one to three days. During the echo: shorter fuse, closer line, worse decisions &#8212; "
            "from a brain that is still half-listening to last Tuesday's alarm.")
        + p("Now run the math on &ldquo;pushing through&rdquo;:")
        + table(["Choice on today's walk", "What it buys", "What it costs"],
            [["Squeeze past the trigger at 2 cars (&ldquo;he has to learn&rdquo;)",
              "you got where you were going 90 seconds sooner",
              "an explosion rep + a 48&#8211;72h echo + every session in it compromised"],
             ["U-turn and take the boring route at 8 cars",
              "a quiet rep of &ldquo;triggers mean nothing happens&rdquo;",
              "90 seconds"]])
        + callout("key", "&#9733; THE TRADE",
            p("An explosion is never one bad moment &#8212; it is a three-day tax on everything you're "
              "building. The U-turn always wins the math. <b>Avoiding a blow-up is not losing. "
              "It is the highest-value move you own.</b>"))
    ), toc="The 48-hour echo"))

    out.append(_pg(pad(
        kicker("THE HARD CONVERSATION")
        + h1("Why corrections quiet the bark and load the bomb")
        + p("Leash pops, prong pressure, the shouted &ldquo;NO!&rdquo;, the can of pennies &#8212; "
            "they often &ldquo;work&rdquo; in the worst possible way: the noise stops, "
            "and the feeling underneath gets worse. Here's the sequence, mechanically:")
        + cklist([
            "The dog's alarm fires at another dog. The dog barks &#8212; the warning system, the steam valve.",
            "The correction lands. The dog learns: <b>barking near other dogs causes pain or fright.</b>",
            "The bark goes quiet. The fear does not. You now have a dog who feels the same alarm "
            "and has been taught not to show it.",
        ])
        + p("That is how you build the most dangerous dog on the street: one who skips the warning. "
            "Trainers have a saying about punishing growls and barks &#8212; <b>you're not defusing the bomb, "
            "you're cutting the wire to the warning light.</b>")
        + callout("warn", "&#9888; ALSO &#8212; THE PAIRING PROBLEM",
            p("Corrections delivered while the dog stares at a trigger get <b>paired with the trigger</b>. "
              "From the dog's side: &ldquo;every time a husky appears, my neck gets popped &#8212; "
              "huskies are even worse than I thought.&rdquo; You can suppress behavior and grow "
              "the emotion that drives it at the same time. Many a board-and-train graduate comes "
              "home quieter and more dangerous."))
        + p("This plan uses no corrections &#8212; not because of ideology, but because of plumbing: "
            "we need the warning system intact, and we need triggers to start predicting good news. "
            "Both are load-bearing.")
    ), toc="Why corrections load the bomb"))

    out.append(_pg(pad(
        kicker("THE SHAPE OF PROGRESS")
        + h1("Progress is a wave. Bad days are in the plan.")
        + fig(svg_progress_wave(), "FIG. 4 &#8212; JUDGE THE WEEK, NEVER THE DAY")
        + p("Here is the sentence that has sunk more reactive-dog owners than any other: "
            "<i>&ldquo;We were doing so well, and then today he exploded, and we're back to square one.&rdquo;</i> "
            "You have felt it &#8212; the good days alternating with bad days that sink you right back "
            "to the bottom. So let's kill it properly:")
        + cklist([
            "<b>You are never back at square one.</b> The reps your dog banked don't un-happen because Tuesday's bucket was full.",
            "<b>The wave shape is what real progress looks like</b> in every behavior plan ever logged. A straight line up means someone isn't logging the bad days.",
            "<b>The trend is the truth, and the trend lives on paper.</b> That is why this plan logs distance in numbers every day &#8212; so on a bad Thursday you can look at three weeks of falling numbers and let the data out-argue your despair.",
        ])
        + callout("key", "&#9733; THE ONLY QUESTION THAT MATTERS EACH WEEK",
            p("Not &ldquo;was today good?&rdquo; but <b>&ldquo;is this week's average distance smaller than "
              "last week's?&rdquo;</b> If yes &#8212; and you follow the plan, it usually is &#8212; you are winning, "
              "whatever today felt like."))
        + pull("Good days alternating with bad days that sink me right back to the bottom.", "what it feels like without a log")
    ), toc="Progress is a wave"))

    out.append(_pg(pad(
        kicker("SETTING THE CONTRACT")
        + h1("What this method is &#8212; and what it is not")
        + cols(
            h3("THIS PLAN IS") + cklist([
                "A <b>measured system</b>: one number (distance), one rule (stay green), one ladder (shrink it).",
                "16 minutes a day, on your normal streets, starting tomorrow morning.",
                "The same mechanics &#8212; desensitization + counterconditioning &#8212; used by every credentialed behavior professional.",
                "Built for fear AND frustration reactivity; the moves are the same, the timelines differ.",
                "On paper, so a bad week can't gaslight you.",
            ]),
            h3("THIS PLAN IS NOT") + xlist([
                "A personality change. A watchful dog stays watchful; we're retiring the panic, not the dog.",
                "A straight line. Waves (page 14). Plan on them.",
                "A promise of dog-park life. The goal is boring walks, not best friends.",
                "A replacement for a professional when the safety page says get one.",
                "Finished at day 21. Day 21 is when the new habit starts paying compound interest (Part V).",
            ]))
        + callout("note", "&#9998; AND ONE QUIET REFRAME BEFORE THE METHOD",
            p("Through all of it, remember what the 5am walks and the crossed streets actually were: "
              "<b>love, doing its best with bad information.</b> You never needed more grit. "
              "You needed the line, the loop, and the ladder. They're on the next page."))
    ), toc="What this is / what this is not"))

    return out
