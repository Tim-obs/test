"""U2 — The Hard Cases Manual: 9 hard cases x 4-page treatment + triage + master plan."""
from design import *
from u2_cases_a import CASES_A
from u2_cases_b import CASES_B

NAME = "CalmWalk-Hard-Cases-Manual"
BRAND = "THE HARD CASES MANUAL"
CASES = CASES_A + CASES_B
F, F2, SG, PL, CR, AM, CL, GD, INK, MUT = (PALETTE[k] for k in
    ("forest", "forest2", "sage", "pale", "cream", "amber", "clay", "gold", "ink", "mut"))

def mpage(body, pno=None, tab=None, tabcolor=None):
    return page(body, pno=pno, part=tab, partcolor=tabcolor, brand=BRAND)

def case_band(c, sub):
    return f'''
<div style="background:{INK};border-radius:12px;color:{CR};padding:14px 20px;margin-bottom:16px;">
  <table style="width:100%;border-collapse:collapse;"><tr>
    <td style="font-family:'Roboto Slab',serif;font-size:30px;font-weight:bold;color:{GD};white-space:nowrap;padding-right:16px;">CASE 0{c["n"]}</td>
    <td><div style="font-size:18px;font-weight:bold;line-height:1.25;">{c["title"]}</div>
        <div style="font-size:11px;letter-spacing:2px;color:{SG};text-transform:uppercase;margin-top:2px;">{c["tag"]} &#183; {sub}</div></td>
  </tr></table>
</div>'''

def case_pages(c, start_pno):
    tabcol = [F, F2, CL, AM, MUT, SG, INK, "#8a6d1c", F][c["n"] - 1] if False else (F2 if c["n"] % 2 else CL)
    tab = f"C{c['n']}"
    pgs = []

    # A — why it breaks the rules
    body = pad(
        case_band(c, "PAGE 1 OF 4 &#183; THE PHYSICS")
        + kicker("WHY IT BREAKS THE NORMAL RULES")
        + "".join(p(t) for t in c["why"])
        + callout(*c["why_call"])
        + small("Four-page treatment: physics &#8594; setup &#8594; the 3-phase protocol &#8594; mistakes &amp; troubleshooting. "
                "Read all four before the first session; run them from page 3.")
    )
    pgs.append(mpage(body, pno=start_pno, tab=tab, tabcolor=tabcol))

    # B — setup checklist
    lines = "".join(wline(lbl, n) for lbl, n in c["setup_lines"])
    body = pad(
        case_band(c, "PAGE 2 OF 4 &#183; THE SETUP")
        + kicker("SETUP CHECKLIST &#8212; BEFORE THE FIRST SESSION")
        + p(c["setup_intro"])
        + cklist(c["setup_checks"])
        + lines
    )
    pgs.append(mpage(body, pno=start_pno + 1, tab=tab, tabcolor=tabcol))

    # C — protocol
    drills = ""
    for name, reps, steps in c["phases"]:
        drills += drill(name, reps, "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>")
    body = pad(
        case_band(c, "PAGE 3 OF 4 &#183; THE PROTOCOL")
        + kicker("THE THREE-PHASE PROTOCOL")
        + drills
    )
    pgs.append(mpage(body, pno=start_pno + 2, tab=tab, tabcolor=tabcol))

    # D — mistakes + troubleshooting + log strip
    body = pad(
        case_band(c, "PAGE 4 OF 4 &#183; THE PITFALLS")
        + kicker("THE CLASSIC MISTAKES")
        + xlist(c["mistakes"])
        + kicker("TROUBLESHOOTING")
        + table(["What's happening", "What it usually is", "What to do"], c["trouble"])
        + kicker("CASE LOG")
        + wgrid(["Date", "Phase", "What we ran", "Result (1&#8211;5)"], 2, ["14%", "14%", "52%", "20%"])
    )
    pgs.append(mpage(body, pno=start_pno + 3, tab=tab, tabcolor=tabcol))
    return pgs

def cover():
    cells = ""
    titles = [c["title"].replace("&amp;", "&#38;") for c in CASES]
    for i, t in enumerate(titles):
        cells += (f'<td style="width:33%;background:{"#22392E" if i % 2 else "#1F3429"};border:1px solid {F2};'
                  f'border-radius:10px;padding:12px 12px;vertical-align:top;">'
                  f'<div style="font-family:\'Roboto Slab\',serif;font-size:17px;font-weight:bold;color:{GD};">0{i+1}</div>'
                  f'<div style="font-size:12px;color:{PL};line-height:1.35;margin-top:2px;">{t}</div></td>')
        if i % 3 == 2:
            cells += '</tr><tr>'
    body = f'''
<div style="background:{F};width:816px;height:1056px;position:relative;">
  <div style="padding:88px 84px 0 84px;">
    <div style="font-size:13px;letter-spacing:5px;color:{GD};font-weight:bold;">CALMWALK &#183; COMPANION TO THE GREEN ZONE METHOD&#8482;</div>
    <div style="border-top:3px solid {CL};width:72px;margin:24px 0;"></div>
    <div style="font-family:'Roboto Slab',serif;font-size:62px;line-height:1.08;color:{CR};font-weight:bold;">The Hard Cases<br/>Manual</div>
    <div style="font-size:19px;line-height:1.6;color:{PL};max-width:580px;margin-top:22px;">
      The nine walks that break the normal rules &#8212; each with the full four-page treatment:
      why it breaks them, the setup, the three-phase protocol, and the mistakes that cost a week.</div>
    <div style="margin-top:26px;"><span style="background:{CL};color:#FFF;border-radius:14px;padding:7px 18px;
      font-size:13px;font-weight:bold;letter-spacing:2px;">MAKE IT STICK &#183; FOR WHEN THE STREET CHEATS</span></div>
    <table style="width:100%;border-collapse:separate;border-spacing:6px;margin-top:36px;"><tr>{cells}</tr></table>
  </div>
  <div style="position:absolute;bottom:28px;left:0;right:0;text-align:center;font-size:11px;letter-spacing:3px;color:{PL};">
    9 CASES &#183; 36 PROTOCOL PAGES &#183; TRIAGE &#183; MASTER PLAN</div>
</div>'''
    return page(body, chrome=False)

def read_first():
    b = pad(
        kicker("BEFORE THE FIRST CASE")
        + h1("How to use this manual")
        + lead("The 21-Day Plan handles the standard walk. This book handles everything that "
               "cheats &#8212; the situations where the normal rules bend, ration, or invert.")
        + cklist([
            "<b>This is a reference, not a curriculum.</b> Nobody runs nine cases at once. Triage "
            "(next page) picks your two; the rest wait on the shelf until the street assigns them.",
            "<b>Every case assumes the Method's vocabulary</b> &#8212; zones, the number, the Loop, the "
            "U-turn, the bucket, 3-for-3. If those words aren't reflexes yet, finish the main plan first.",
            "<b>Four pages, one shape, every time:</b> the physics (why your good tools misfire here) "
            "&#8594; the setup (won before the first session) &#8594; the protocol (three phases, exact reps) "
            "&#8594; the pitfalls (mistakes + troubleshooting + a log strip).",
            "<b>One case at a time, two weeks per case</b> is the honest pace. Most cases are 70% "
            "setup and scheduling; the protocols themselves are short.",
            "<b>The safety page still rules everything.</b> Bites, kids, or fear inside your own home: "
            "credentialed professional, this week, with your logs in hand.",
        ])
        + callout("key", "&#9733; THE THEME, IF YOU WANT IT IN ONE LINE",
            p("Every hard case is the same lesson wearing different weather: <b>when you can't add "
              "distance, add time, barriers, or schedule &#8212; and when you can't add any of those, "
              "leave and bill it to management, not to your dog.</b>"))
        + small("Educational material; not veterinary or behaviorist advice. &#169; CalmWalk.")
    )
    return mpage(b, pno=2)

def triage():
    rows = [
        ["Loose dogs keep materializing mid-walk", "01 &#183; The Off-Leash Charge", "scan habit + the throw, today"],
        ["We live in an apartment building", "02 &#183; Hallways &amp; Elevators", "recon week first; it's 80% timetable"],
        ["Vet (or groomer) visit coming up", "03 &#183; The Vet Visit", "book the quiet slot 3 days out"],
        ["Walks only fit before dawn / after dark", "04 &#183; Night Walks", "gear tonight, dusk-bridge tomorrow"],
        ["There's a second (or third) dog at home", "05 &#183; The Multi-Dog Household", "solo season starts now"],
        ["He patrols windows / fights the fence", "06 &#183; Fence &amp; Window", "hardware store today &#8212; highest ROI in the book"],
        ["The car ride is its own explosion", "07 &#183; Car Reactivity", "containment + ledger before any drills"],
        ["The doorbell detonates the house", "08 &#183; Doorbell &amp; Visitors", "bell station + gate this weekend"],
        ["The numbers are climbing and I'm scared", "09 &#183; The Regression Week", "two quiet days, then the audit"],
    ]
    b = pad(
        kicker("START HERE")
        + h1("Triage: which case, in which order")
        + table(["What's true at your house", "Run this case", "First move"], rows)
        + callout("note", "&#9998; PICKING WHEN SEVERAL ARE TRUE",
            p("Order by <b>frequency, not drama</b>: the case that fires daily (windows, hallways, "
              "the household) outranks the scary one that fires monthly. Daily cases drain the "
              "bucket that monthly cases then overflow &#8212; fix the drip before the lightning. "
              "Exception: anything with a safety dimension (Case 1 in loose-dog country) installs "
              "its Phase 1 immediately regardless of order &#8212; the scan habit costs nothing."))
        + small("Most households: Case 6 or 2 first (the daily rehearsal machines), then their "
                "situational case, with Case 9 read once now &#8212; before it's needed &#8212; like a fire exit.")
    )
    return mpage(b, pno=3)

def master_plan():
    b = pad(
        kicker("WORKSHEET &#183; THE MASTER PLAN")
        + h1("Your two cases, on paper")
        + wline("From triage &#8212; CASE A (the daily one)", 1)
        + wline("CASE A: setup items still missing (from its page 2)", 2)
        + wline("CASE A: phase 1 starts on (date)", 1)
        + wline("From triage &#8212; CASE B (the situational one)", 1)
        + wline("CASE B: setup items still missing", 2)
        + wline("CASE B: phase 1 starts on (date)", 1)
        + wgrid(["Week", "Case A phase", "Case B phase", "Main-plan maintenance (3 walks + sniffari?)", "Re-measure?"],
                4, ["10%", "22%", "22%", "32%", "14%"])
        + callout("key", "&#9733; THE LOAD RULE",
            p("Hard cases ride ON TOP of maintenance, never instead of it. If a week can't fit both, "
              "maintenance wins and the case waits &#8212; a drained bucket is the precondition for "
              "every protocol in this book."))
    )
    return mpage(b, pno=40, tab="PLAN", tabcolor=F2)

def closing():
    b = pad(
        kicker("THE LAST PAGE")
        + h1("The street will keep writing new exams")
        + dropcap("And that's fine, because you stopped studying for exams somewhere around the "
                  "middle of this book. You learned the physics instead: arousal is a budget, "
                  "distance has substitutes, rehearsal is destiny, and every chaos on four legs "
                  "yields to setup plus protocol plus an honest log.")
        + p("Somewhere in your neighborhood there's an owner mid-spiral &#8212; 5am walks, gear "
            "drawer of regrets, a dog they love and dread. You can't hand them a method on a "
            "sidewalk. But you can be the person whose dog passes them at four cars, boring as "
            "furniture, while you nod like it's nothing. It isn't nothing. It's engineering.")
        + p("Walk on.")
        + p("<b>&#8212; CalmWalk</b>")
        + '<hr class="rule-amber"/>'
        + small("The Hard Cases Manual &#183; companion to The Green Zone Method&#8482; &#183; &#169; CalmWalk. "
                "Educational material; not veterinary or behaviorist advice. Personal use only.")
    )
    return mpage(b, pno=41)

def build():
    pages_html = [cover(), read_first(), triage()]
    pno = 4
    for c in CASES:
        pages_html += case_pages(c, pno)
        pno += 4
    pages_html += [master_plan(), closing()]
    return html_doc(pages_html, "The Hard Cases Manual")
