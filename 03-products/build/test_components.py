"""Component test: exercise every design-system component + all SVGs before content."""
from design import *

NAME = "component-test"

def build():
    pages = []
    b = pad(
        kicker("COMPONENT TEST &#183; TYPOGRAPHY + BLOCKS")
        + h1("Every text component on one page")
        + lead("This is the lead paragraph style. It runs a little larger so openers breathe.")
        + dropcap("This paragraph tests the drop cap. The first letter floats large and amber, "
                  "and the following lines wrap around it the way a chapter opener should. "
                  "Body text is Lato at 14.5px with relaxed leading for long reading sessions.")
        + h2("A Roboto Slab section heading")
        + h3("An uppercase sub-heading")
        + callout("note", "&#9998; NOTE", p("A note callout with sage border."))
        + callout("warn", "&#9888; CAREFUL", p("A warning callout with clay border."))
        + callout("key", "&#9733; KEY IDEA", p("A key-idea callout with amber border."))
        + pull("Progress is a wave, not a staircase.", "The Green Zone Method")
        + stats([("5", "CARS TODAY"), ("3&#215;", "CLEAN REPS"), ("16", "MINUTES")])
        + small("Small print: educational use only; not veterinary advice.")
    )
    pages.append(page(b, pno=1, part="PART I", partcolor=PALETTE["sage"]))

    b = pad(
        h1("Blocks: drills, pass/fail, fix-it, lists, tables")
        + drill("DRILL &#183; THE FOOD TEST", "5 REPS",
                "<ol><li>Stand at your start distance. Wait for the dog to notice the trigger.</li>"
                "<li>Offer one pea-sized treat at the nose.</li>"
                "<li>Score the mouth: instant / slow / refused.</li></ol>")
        + passfail(["Dog eats instantly on 3 straight reps", "Loose leash the whole time"],
                   ["Dog refuses food twice", "Any bark, lunge, or freeze"])
        + fixit(p("Dog explodes mid-rep? U-turn, add two cars of distance, breathe, restart at the easier line."))
        + cklist(["A checklist item", "Another good thing"])
        + xlist(["A thing this is NOT", "Another myth"])
        + table(["Symptom", "Meaning", "Do"],
                [["Won't eat", "Over threshold", "Add distance"],
                 ["Eats slowly", "Yellow zone", "Hold or add 1 car"]])
        + daybar(7, "PHASE 2 &#183; ANCHOR", "Install the loop on moving triggers at 6 cars")
    )
    pages.append(page(b, pno=2, part="PART II", partcolor=PALETTE["amber"]))

    b = pad(
        h1("Worksheet components")
        + wline("Dog's name", 1) + wline("Today's trigger + distance", 2)
        + wbox("Sketch your route (mark escapes with E)", 90)
        + wgrid(["Rep", "Trigger", "Cars", "Mouth score", "Clean?"], 5,
                ["8%", "32%", "14%", "26%", "20%"])
        + h2("TOC styles")
        + tocpart("PART I &#8212; WHY EVERYTHING FAILED", "9")
        + tocrow("The advice that made it worse", "10")
        + tocrow("Fear beats food: the line nobody drew", "12")
        + gitem("Threshold", "the distance at which your dog can notice a trigger and still think.")
        + '<span class="badge">BONUS</span>'
    )
    pages.append(page(b, pno=3, part="WORKSHEETS", partcolor=PALETTE["forest2"]))

    for i, (key, fn) in enumerate(SVG_LIBRARY.items()):
        if i % 2 == 0:
            cur = pad(h1(f"SVG check {i // 2 + 1}"))
        cur += fig(fn(), key)
        if i % 2 == 1 or i == len(SVG_LIBRARY) - 1:
            pages.append(page(cur, pno=4 + i // 2))

    pages.append(divider("01", "PART ONE", "Why Everything Failed",
                         "Not you. The advice. Here is the mechanism under every failed fix.",
                         ["The Exposure Trap", "Fear beats food", "Trigger stacking"]))
    return html_doc(pages, "Component Test")
