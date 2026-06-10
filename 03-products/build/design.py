# CalmWalk design system — shared CSS, components, SVG illustration library.
# Pages are fixed 816x1056px (US Letter @96dpi). Layout uses tables/inline-block
# only — wkhtmltopdf's Qt WebKit has unreliable flexbox.

PALETTE = dict(
    ink="#26241F", forest="#1B4332", forest2="#2D6A4F", sage="#74A892",
    pale="#DCE8DF", cream="#FAF7F0", paper="#FFFFFF", amber="#E8A13C",
    clay="#C45B4C", gold="#E5C45C", line="#D8D2C4", mut="#6B675C",
)

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#888; font-family:'Lato','Open Sans',sans-serif; color:%(ink)s; }
.page { width:816px; height:1056px; background:%(cream)s; position:relative;
        page-break-after:always; overflow:hidden; }
.pad { padding:64px 72px 96px 72px; }

/* footer chrome */
.chrome { position:absolute; left:0; right:0; bottom:0; height:54px; }
.chrome .rule { position:absolute; left:72px; right:72px; top:0; border-top:2px solid %(forest)s; }
.chrome .brand { position:absolute; left:72px; top:12px; font-size:10px; letter-spacing:2.5px;
                 font-weight:bold; color:%(forest)s; }
.chrome .mid { position:absolute; left:0; right:0; top:12px; text-align:center; font-size:10px;
               letter-spacing:2px; color:%(mut)s; }
.chrome .pno { position:absolute; right:72px; top:8px; font-size:12px; font-weight:bold;
               color:%(cream)s; background:%(forest)s; padding:3px 10px; border-radius:10px; }

/* part tab on page edge */
.ptab { position:absolute; right:0; top:120px; width:34px; padding:12px 0;
        color:%(cream)s; text-align:center; border-radius:8px 0 0 8px; }
.ptab span { display:block; font-family:'Roboto Slab',serif; font-size:15px; font-weight:bold; }

/* type */
.kicker { font-size:11px; letter-spacing:3px; font-weight:bold; color:%(amber)s;
          text-transform:uppercase; margin-bottom:10px; }
h1 { font-family:'Roboto Slab',serif; font-size:34px; line-height:1.15; color:%(forest)s;
     margin-bottom:18px; }
h2 { font-family:'Roboto Slab',serif; font-size:21px; line-height:1.25; color:%(forest)s;
     margin:22px 0 10px 0; }
h3 { font-size:14px; letter-spacing:1.5px; text-transform:uppercase; color:%(forest2)s;
     margin:18px 0 8px 0; }
p, li { font-size:14.5px; line-height:1.62; }
p { margin-bottom:12px; }
ul, ol { margin:0 0 12px 22px; }
li { margin-bottom:6px; }
b, strong { color:%(forest)s; }
.small { font-size:11.5px; color:%(mut)s; line-height:1.5; }
.lead { font-size:17px; line-height:1.6; color:%(ink)s; }

/* drop cap */
.dropcap:first-letter { font-family:'Roboto Slab',serif; font-size:58px; float:left;
  line-height:0.9; padding:4px 10px 0 0; color:%(amber)s; font-weight:bold; }

/* callouts */
.co { border-radius:10px; padding:16px 18px 12px 18px; margin:14px 0; }
.co .cohead { font-size:11px; font-weight:bold; letter-spacing:2px; margin-bottom:6px; }
.co p, .co li { font-size:13.5px; }
.co-note { background:%(pale)s; border-left:6px solid %(sage)s; }
.co-note .cohead { color:%(forest2)s; }
.co-warn { background:#F6E3DE; border-left:6px solid %(clay)s; }
.co-warn .cohead { color:%(clay)s; }
.co-key  { background:#F8EDD8; border-left:6px solid %(amber)s; }
.co-key .cohead { color:#A66A14; }

/* drill / rep block */
.drill { border:2px solid %(forest)s; border-radius:12px; margin:14px 0; background:%(paper)s; }
.drill .dhead { background:%(forest)s; color:%(cream)s; padding:9px 16px; font-size:13px;
                font-weight:bold; letter-spacing:1.5px; border-radius:9px 9px 0 0; }
.drill .dhead .reps { float:right; background:%(amber)s; color:%(ink)s; border-radius:9px;
                      padding:1px 10px; font-size:11.5px; letter-spacing:1px; }
.drill .dbody { padding:12px 16px 8px 16px; }
.drill .dbody ol, .drill .dbody ul { margin-left:20px; }
.drill .dbody li { font-size:13.5px; margin-bottom:5px; }

/* pass/fail */
.pf { width:100%%; border-collapse:separate; border-spacing:10px 0; margin:12px -10px; }
.pf td { width:50%%; vertical-align:top; border-radius:10px; padding:12px 14px; }
.pf .pass { background:%(pale)s; border:2px solid %(sage)s; }
.pf .fail { background:#F6E3DE; border:2px solid %(clay)s; }
.pf .pfh { font-size:12px; font-weight:bold; letter-spacing:2px; margin-bottom:6px; }
.pf .pass .pfh { color:%(forest2)s; } .pf .fail .pfh { color:%(clay)s; }
.pf li { font-size:13px; margin-bottom:4px; }
.pf ul { margin-left:18px; margin-bottom:2px; }

/* fix-it block */
.fixit { background:%(ink)s; color:%(cream)s; border-radius:10px; padding:13px 16px; margin:13px 0; }
.fixit .fh { color:%(gold)s; font-size:11px; font-weight:bold; letter-spacing:2px; margin-bottom:5px; }
.fixit p { font-size:13px; color:%(cream)s; margin-bottom:5px; }

/* worksheets */
.wline { border-bottom:1.6px solid %(mut)s; height:30px; margin:8px 0; }
.wlabel { font-size:11px; letter-spacing:1.5px; font-weight:bold; color:%(mut)s;
          text-transform:uppercase; margin-top:10px; }
.wbox { border:1.6px solid %(mut)s; border-radius:8px; min-height:64px; margin:8px 0; background:%(paper)s; }
.wgrid { width:100%%; border-collapse:collapse; margin:10px 0; background:%(paper)s; }
.wgrid th { background:%(forest)s; color:%(cream)s; font-size:11px; letter-spacing:1px;
            padding:8px 8px; text-align:left; }
.wgrid td { border:1px solid %(line)s; height:34px; font-size:12.5px; padding:4px 8px; }

/* stat row */
.stats { width:100%%; border-collapse:separate; border-spacing:10px 0; margin:14px -10px; }
.stats td { background:%(paper)s; border:2px solid %(pale)s; border-radius:12px;
            text-align:center; padding:14px 8px 10px 8px; width:33%%; }
.stats .n { font-family:'Roboto Slab',serif; font-size:30px; font-weight:bold; color:%(forest)s; }
.stats .l { font-size:10.5px; letter-spacing:1.5px; text-transform:uppercase; color:%(mut)s; margin-top:3px; }

/* pull quote */
.pull { border-left:5px solid %(amber)s; padding:6px 0 6px 18px; margin:16px 0;
        font-family:'Roboto Slab',serif; font-size:18px; line-height:1.45; color:%(forest)s; }
.pull .att { display:block; font-family:'Lato',sans-serif; font-size:11px; letter-spacing:1.5px;
             color:%(mut)s; margin-top:6px; text-transform:uppercase; }

/* tables */
.tbl { width:100%%; border-collapse:collapse; margin:12px 0; background:%(paper)s; }
.tbl th { background:%(forest)s; color:%(cream)s; font-size:12px; letter-spacing:1px;
          padding:9px 10px; text-align:left; }
.tbl td { border:1px solid %(line)s; padding:8px 10px; font-size:13px; line-height:1.45;
          vertical-align:top; }
.tbl tr:nth-child(even) td { background:%(cream)s; }

/* check / cross lists */
.cklist, .xlist { list-style:none; margin-left:0; }
.cklist li, .xlist li { padding-left:30px; position:relative; margin-bottom:8px; }
.cklist li:before { content:"\\2713"; position:absolute; left:0; top:-1px; font-weight:bold;
  color:%(paper)s; background:%(forest2)s; border-radius:50%%; width:20px; height:20px;
  text-align:center; line-height:20px; font-size:12px; }
.xlist li:before { content:"\\2715"; position:absolute; left:0; top:-1px; font-weight:bold;
  color:%(paper)s; background:%(clay)s; border-radius:50%%; width:20px; height:20px;
  text-align:center; line-height:20px; font-size:12px; }

/* day card header */
.daybar { background:%(forest)s; border-radius:12px; color:%(cream)s; padding:14px 18px; margin-bottom:14px; }
.daybar table { width:100%%; border-collapse:collapse; }
.daybar .dnum { font-family:'Roboto Slab',serif; font-size:30px; font-weight:bold; color:%(gold)s;
                white-space:nowrap; padding-right:16px; }
.daybar .dphase { font-size:10px; letter-spacing:2px; color:%(sage)s; text-transform:uppercase; }
.daybar .dgoal { font-size:15.5px; font-weight:bold; line-height:1.35; }

/* two-col helper (tables) */
.cols { width:100%%; border-collapse:separate; border-spacing:14px 0; margin:0 -14px; }
.cols td { vertical-align:top; width:50%%; }

/* TOC */
.tocrow { font-size:14px; margin-bottom:9px; position:relative; }
.tocrow .t { background:%(cream)s; padding-right:6px; position:relative; z-index:2; }
.tocrow .pn { float:right; background:%(cream)s; padding-left:6px; position:relative; z-index:2;
              font-weight:bold; color:%(forest)s; }
.tocrow .dots { position:absolute; left:0; right:0; top:11px; border-bottom:2px dotted %(line)s; }
.tocpart { font-family:'Roboto Slab',serif; font-size:16px; color:%(forest)s; font-weight:bold;
           margin:16px 0 8px 0; padding-bottom:4px; border-bottom:2px solid %(forest)s; }
.tocpart .pn { float:right; }

/* part divider */
.divider { background:%(forest)s; color:%(cream)s; }
.divider .dvpad { padding:110px 84px; }
.divider .dvnum { font-family:'Roboto Slab',serif; font-size:120px; color:%(amber)s;
                  font-weight:bold; line-height:1; }
.divider .dvkick { font-size:13px; letter-spacing:4px; color:%(sage)s; text-transform:uppercase;
                   margin:10px 0 6px 0; }
.divider h1 { color:%(cream)s; font-size:44px; margin-bottom:22px; }
.divider p { color:%(pale)s; font-size:16px; }
.divider .dvlist { margin-top:30px; border-top:2px solid %(forest2)s; padding-top:18px; }
.divider .dvlist li { color:%(pale)s; font-size:14.5px; margin-bottom:9px; list-style:none; }
.divider .dvlist li:before { content:"\\2192  "; color:%(amber)s; font-weight:bold; }

/* glossary */
.gitem { margin-bottom:13px; }
.gitem .gterm { font-weight:bold; color:%(forest)s; font-size:14.5px; }
.gitem p { font-size:13px; margin-bottom:0; }

/* misc */
.center { text-align:center; }
.figwrap { text-align:center; margin:12px 0; }
.figcap { font-size:11px; color:%(mut)s; letter-spacing:1px; text-transform:uppercase; margin-top:6px; }
.badge { display:inline-block; background:%(amber)s; color:%(ink)s; border-radius:10px;
         padding:2px 12px; font-size:11px; font-weight:bold; letter-spacing:1.5px; }
.rule-amber { border:none; border-top:3px solid %(amber)s; width:64px; margin:14px 0; }
""" % PALETTE


# ---------------------------------------------------------------- components
def esc(t):
    return t  # content is authored HTML; no escaping layer needed

def page(body, pno=None, part=None, partcolor=None, cls="", chrome=True,
         brand="THE GREEN ZONE METHOD", mid="CALMWALK"):
    tab = ""
    if part:
        tab = f'<div class="ptab" style="background:{partcolor or PALETTE["sage"]}"><span>{part}</span></div>'
    ch = ""
    if chrome:
        pn = f'<div class="pno">{pno}</div>' if pno else ""
        ch = (f'<div class="chrome"><div class="rule"></div><div class="brand">{brand}</div>'
              f'<div class="mid">{mid}</div>{pn}</div>')
    return f'<div class="page {cls}">{body}{tab}{ch}</div>'

def pad(inner):  return f'<div class="pad">{inner}</div>'
def kicker(t):   return f'<div class="kicker">{t}</div>'
def h1(t):       return f'<h1>{t}</h1>'
def h2(t):       return f'<h2>{t}</h2>'
def h3(t):       return f'<h3>{t}</h3>'
def p(t, cls=""):return f'<p class="{cls}">{t}</p>'
def lead(t):     return f'<p class="lead">{t}</p>'
def dropcap(t):  return f'<p class="dropcap">{t}</p>'
def small(t):    return f'<p class="small">{t}</p>'

def callout(kind, head, body):
    return f'<div class="co co-{kind}"><div class="cohead">{head}</div>{body}</div>'

def drill(name, reps, body):
    return (f'<div class="drill"><div class="dhead">{name}'
            f'<span class="reps">{reps}</span></div><div class="dbody">{body}</div></div>')

def passfail(pass_items, fail_items, pass_head="PASS — MOVE ON WHEN", fail_head="STOP — BACK UP WHEN"):
    pi = "".join(f"<li>{i}</li>" for i in pass_items)
    fi = "".join(f"<li>{i}</li>" for i in fail_items)
    return (f'<table class="pf"><tr><td class="pass"><div class="pfh">&#10003; {pass_head}</div>'
            f'<ul>{pi}</ul></td><td class="fail"><div class="pfh">&#10005; {fail_head}</div>'
            f'<ul>{fi}</ul></td></tr></table>')

def fixit(body, head="IF IT GOES WRONG"):
    return f'<div class="fixit"><div class="fh">&#9889; {head}</div>{body}</div>'

def stats(items):  # [(num, label), ...]
    tds = "".join(f'<td><div class="n">{n}</div><div class="l">{l}</div></td>' for n, l in items)
    return f'<table class="stats"><tr>{tds}</tr></table>'

def pull(q, att=""):
    a = f'<span class="att">{att}</span>' if att else ""
    return f'<div class="pull">&ldquo;{q}&rdquo;{a}</div>'

def table(headers, rows, cls="tbl"):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><tr>{th}</tr>{trs}</table>'

def cklist(items): return '<ul class="cklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def xlist(items):  return '<ul class="xlist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def wline(label=None, n=1):
    out = f'<div class="wlabel">{label}</div>' if label else ""
    out += '<div class="wline"></div>' * n
    return out

def wbox(label, h=64):
    return f'<div class="wlabel">{label}</div><div class="wbox" style="min-height:{h}px"></div>'

def wgrid(headers, nrows, widths=None):
    th = ""
    for i, hd in enumerate(headers):
        w = f' style="width:{widths[i]}"' if widths else ""
        th += f"<th{w}>{hd}</th>"
    rows = ("<tr>" + "<td></td>" * len(headers) + "</tr>") * nrows
    return f'<table class="wgrid"><tr>{th}</tr>{rows}</table>'

def daybar(day, phase, goal):
    return (f'<div class="daybar"><table><tr><td class="dnum">DAY {day}</td>'
            f'<td><div class="dphase">{phase}</div><div class="dgoal">{goal}</div></td></tr></table></div>')

def cols(left, right):
    return f'<table class="cols"><tr><td>{left}</td><td>{right}</td></tr></table>'

def fig(svg, cap=None):
    c = f'<div class="figcap">{cap}</div>' if cap else ""
    return f'<div class="figwrap">{svg}{c}</div>'

def divider(num, kick, title, blurb, items, color=None):
    lis = "".join(f"<li>{i}</li>" for i in items)
    body = (f'<div class="dvpad"><div class="dvnum">{num}</div><div class="dvkick">{kick}</div>'
            f'<h1>{title}</h1><p>{blurb}</p><ul class="dvlist">{lis}</ul></div>')
    return page(body, cls="divider", chrome=False)

def tocrow(t, pn):
    return f'<div class="tocrow"><span class="t">{t}</span><span class="pn">{pn}</span><div class="dots"></div></div>'

def tocpart(t, pn):
    return f'<div class="tocpart">{t}<span class="pn">{pn}</span></div>'

def gitem(term, definition):
    return f'<div class="gitem"><span class="gterm">{term}</span> — {definition}</div>'


# ------------------------------------------------------------ SVG library
F, F2, SG, PL, CR, AM, CL, GD, INK, MUT = (PALETTE[k] for k in
    ("forest", "forest2", "sage", "pale", "cream", "amber", "clay", "gold", "ink", "mut"))

def _dog(x, y, s=1.0, color=F, flip=False):
    """Simple geometric side-view dog silhouette."""
    t = f"translate({x},{y}) scale({-s if flip else s},{s})"
    return (f'<g transform="{t}"><ellipse cx="0" cy="0" rx="26" ry="13" fill="{color}"/>'
            f'<circle cx="24" cy="-12" r="9" fill="{color}"/>'
            f'<polygon points="20,-19 24,-28 28,-19" fill="{color}"/>'
            f'<polygon points="29,-20 34,-28 36,-18" fill="{color}"/>'
            f'<rect x="-18" y="8" width="5" height="14" rx="2" fill="{color}"/>'
            f'<rect x="-6" y="8" width="5" height="14" rx="2" fill="{color}"/>'
            f'<rect x="8" y="8" width="5" height="14" rx="2" fill="{color}"/>'
            f'<rect x="16" y="8" width="5" height="14" rx="2" fill="{color}"/>'
            f'<path d="M -24,-4 Q -38,-14 -34,-24" stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round"/></g>')

def _person(x, y, s=1.0, color=INK):
    t = f"translate({x},{y}) scale({s})"
    return (f'<g transform="{t}"><circle cx="0" cy="-46" r="9" fill="{color}"/>'
            f'<rect x="-7" y="-36" width="14" height="30" rx="6" fill="{color}"/>'
            f'<rect x="-7" y="-8" width="5" height="22" rx="2" fill="{color}"/>'
            f'<rect x="2" y="-8" width="5" height="22" rx="2" fill="{color}"/></g>')

def svg_zone_map(w=560, h=400):
    """Signature visual: overhead zones around a trigger."""
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 400" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="400" rx="14" fill="#EFEAE0"/>
<rect x="0" y="168" width="560" height="64" fill="#D8D2C4"/>
<line x1="10" y1="200" x2="550" y2="200" stroke="#FFF" stroke-width="3" stroke-dasharray="18 14"/>
<circle cx="455" cy="200" r="150" fill="{CL}" fill-opacity="0.22"/>
<circle cx="455" cy="200" r="245" fill="{GD}" fill-opacity="0.25"/>
<circle cx="455" cy="200" r="150" fill="none" stroke="{CL}" stroke-width="3"/>
<circle cx="455" cy="200" r="245" fill="none" stroke="{GD}" stroke-width="3" stroke-dasharray="10 8"/>
<rect x="8" y="8" width="206" height="384" rx="12" fill="{F2}" fill-opacity="0.18"/>
<rect x="8" y="8" width="206" height="384" rx="12" fill="none" stroke="{F2}" stroke-width="3"/>
{_dog(455, 196, 1.15, CL, flip=True)}
{_dog(96, 250, 1.1, F)}
{_person(150, 262, 1.05)}
<line x1="122" y1="244" x2="143" y2="232" stroke="{INK}" stroke-width="3"/>
<rect x="30" y="28" width="150" height="30" rx="15" fill="{F2}"/>
<text x="105" y="48" font-family="Lato" font-size="15" font-weight="bold" fill="#FFF" text-anchor="middle">GREEN ZONE</text>
<rect x="236" y="28" width="158" height="30" rx="15" fill="{GD}"/>
<text x="315" y="48" font-family="Lato" font-size="15" font-weight="bold" fill="{INK}" text-anchor="middle">YELLOW ZONE</text>
<rect x="412" y="28" width="120" height="30" rx="15" fill="{CL}"/>
<text x="472" y="48" font-family="Lato" font-size="15" font-weight="bold" fill="#FFF" text-anchor="middle">RED ZONE</text>
<text x="105" y="320" font-family="Lato" font-size="13" font-weight="bold" fill="{F}" text-anchor="middle">CAN THINK &#183; CAN EAT</text>
<text x="105" y="338" font-family="Lato" font-size="13" font-weight="bold" fill="{F}" text-anchor="middle">CAN LEARN</text>
<text x="315" y="320" font-family="Lato" font-size="13" font-weight="bold" fill="#8a6d1c" text-anchor="middle">STIFF &#183; LOCKED ON</text>
<text x="315" y="338" font-family="Lato" font-size="13" font-weight="bold" fill="#8a6d1c" text-anchor="middle">EATS SLOWLY</text>
<text x="472" y="320" font-family="Lato" font-size="13" font-weight="bold" fill="{CL}" text-anchor="middle">EXPLOSION &#183; NO FOOD</text>
<text x="472" y="338" font-family="Lato" font-size="13" font-weight="bold" fill="{CL}" text-anchor="middle">NO LEARNING</text>
<text x="276" y="385" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">EVERY DOG HAS A NUMBER. YOUR ONLY JOB IS TO FIND IT &#8212; THEN SHRINK IT.</text>
</svg>'''

def svg_engage_loop(w=460, h=300):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg">
<rect width="460" height="300" rx="14" fill="#EFEAE0"/>
<circle cx="230" cy="150" r="92" fill="none" stroke="{SG}" stroke-width="4" stroke-dasharray="12 9"/>
<polygon points="230,49 218,67 242,67" fill="{SG}"/>
<polygon points="230,251 218,233 242,233" fill="{SG}"/>
<rect x="150" y="14" width="160" height="44" rx="10" fill="{F}"/>
<text x="230" y="33" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">1. DOG SEES TRIGGER</text>
<text x="230" y="50" font-family="Lato" font-size="11" fill="{PL}" text-anchor="middle">(you say nothing)</text>
<rect x="334" y="128" width="116" height="44" rx="10" fill="{F2}"/>
<text x="392" y="147" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">2. DOG LOOKS</text>
<text x="392" y="164" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">BACK AT YOU</text>
<rect x="150" y="242" width="160" height="44" rx="10" fill="{AM}"/>
<text x="230" y="261" font-family="Lato" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">3. MARK &#8212; "YES!"</text>
<text x="230" y="278" font-family="Lato" font-size="11" fill="{INK}" text-anchor="middle">the instant the head turns</text>
<rect x="10" y="128" width="116" height="44" rx="10" fill="{F}"/>
<text x="68" y="147" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">4. PAY AT</text>
<text x="68" y="164" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">YOUR KNEE</text>
<text x="230" y="142" font-family="Roboto Slab" font-size="17" font-weight="bold" fill="{F}" text-anchor="middle">THE LOOP</text>
<text x="230" y="163" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">one rep &#8776; 5 seconds</text>
</svg>'''

def svg_uturn(w=460, h=270):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 460 270" xmlns="http://www.w3.org/2000/svg">
<rect width="460" height="270" rx="14" fill="#EFEAE0"/>
<rect x="0" y="105" width="460" height="60" fill="#D8D2C4"/>
<line x1="8" y1="135" x2="452" y2="135" stroke="#FFF" stroke-width="3" stroke-dasharray="16 12"/>
{_dog(392, 130, 1.0, CL, flip=True)}
<path d="M 290,135 L 200,135 Q 160,135 160,175 Q 160,215 200,215 L 300,215"
  stroke="{F2}" stroke-width="7" fill="none" stroke-linecap="round"/>
<polygon points="300,201 300,229 326,215" fill="{F2}"/>
{_dog(250, 110, 0.9, F)}
{_person(296, 122, 0.95)}
<rect x="22" y="18" width="190" height="56" rx="10" fill="{F}"/>
<text x="117" y="40" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">"THIS WAY!" &#8212; happy voice,</text>
<text x="117" y="58" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">turn YOUR body first</text>
<text x="160" y="250" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">cross, arc, or reverse &#8212; any direction that adds distance</text>
<rect x="330" y="30" width="108" height="26" rx="13" fill="{CL}"/>
<text x="384" y="48" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">SURPRISE DOG</text>
</svg>'''

def svg_carlength(w=620, h=170):
    cars = "".join(
        f'<g transform="translate({60 + i * 88},96)"><rect x="0" y="0" width="64" height="22" rx="8" fill="{F2 if i < 3 else (GD if i < 5 else CL)}"/>'
        f'<circle cx="14" cy="24" r="7" fill="{INK}"/><circle cx="50" cy="24" r="7" fill="{INK}"/>'
        f'<text x="32" y="-8" font-family="Lato" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">{i+1}</text></g>'
        for i in range(6))
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 620 170" xmlns="http://www.w3.org/2000/svg">
<rect width="620" height="170" rx="14" fill="#EFEAE0"/>
<text x="310" y="32" font-family="Roboto Slab" font-size="16" font-weight="bold" fill="{F}" text-anchor="middle">MEASURE IN PARKED CARS, NOT FEET</text>
<text x="310" y="52" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">one parked car &#8776; 15 ft &#8212; you can count cars on any street, mid-walk, under stress</text>
{cars}
<text x="310" y="158" font-family="Lato" font-size="12" font-weight="bold" fill="{F}" text-anchor="middle">"Cooper's number is 5 cars" beats "Cooper's threshold is 75 feet"</text>
</svg>'''

def svg_body_language(w=520, h=330):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg">
<rect width="520" height="330" rx="14" fill="#EFEAE0"/>
{_dog(250, 195, 2.6, F)}
<line x1="312" y1="125" x2="398" y2="68" stroke="{AM}" stroke-width="2.5"/>
<circle cx="312" cy="125" r="5" fill="{AM}"/>
<text x="404" y="62" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">EARS: pinned flat or</text>
<text x="404" y="78" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">locked hard forward</text>
<line x1="318" y1="168" x2="402" y2="168" stroke="{AM}" stroke-width="2.5"/>
<circle cx="318" cy="168" r="5" fill="{AM}"/>
<text x="408" y="164" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">MOUTH: closes shut.</text>
<text x="408" y="180" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">Panting stops = alarm</text>
<line x1="160" y1="172" x2="84" y2="110" stroke="{AM}" stroke-width="2.5"/>
<circle cx="160" cy="172" r="5" fill="{AM}"/>
<text x="20" y="88" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">TAIL: high + stiff +</text>
<text x="20" y="104" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">slow wag = loading</text>
<line x1="218" y1="230" x2="130" y2="280" stroke="{AM}" stroke-width="2.5"/>
<circle cx="218" cy="230" r="5" fill="{AM}"/>
<text x="36" y="296" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">WEIGHT: shifts forward,</text>
<text x="36" y="312" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">front legs braced</text>
<line x1="330" y1="225" x2="404" y2="268" stroke="{AM}" stroke-width="2.5"/>
<circle cx="330" cy="225" r="5" fill="{AM}"/>
<text x="352" y="288" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">BODY: freeze. The 2-second</text>
<text x="352" y="304" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">statue before the bark</text>
<rect x="150" y="14" width="220" height="28" rx="14" fill="{F}"/>
<text x="260" y="33" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">THE 5 LOADING SIGNALS</text>
</svg>'''

def svg_stress_bucket(w=470, h=320):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 470 320" xmlns="http://www.w3.org/2000/svg">
<rect width="470" height="320" rx="14" fill="#EFEAE0"/>
<path d="M 150,90 L 170,260 L 290,260 L 310,90 Z" fill="{PL}" stroke="{F}" stroke-width="4"/>
<path d="M 162,170 L 173,255 L 287,255 L 298,170 Z" fill="{SG}"/>
<line x1="156" y1="130" x2="304" y2="130" stroke="{CL}" stroke-width="3" stroke-dasharray="8 6"/>
<text x="318" y="135" font-family="Lato" font-size="12" font-weight="bold" fill="{CL}">OVERFLOW =</text>
<text x="318" y="151" font-family="Lato" font-size="12" font-weight="bold" fill="{CL}">THE EXPLOSION</text>
<g font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">
<text x="38" y="60">skipped breakfast</text><text x="150" y="40">trash truck</text>
<text x="262" y="40">dog behind fence</text><text x="392" y="60">doorbell</text>
</g>
<line x1="80" y1="66" x2="180" y2="100" stroke="{MUT}" stroke-width="2"/>
<line x1="185" y1="46" x2="215" y2="86" stroke="{MUT}" stroke-width="2"/>
<line x1="300" y1="46" x2="262" y2="86" stroke="{MUT}" stroke-width="2"/>
<line x1="400" y1="66" x2="288" y2="100" stroke="{MUT}" stroke-width="2"/>
<path d="M 290,260 Q 310,290 350,292" stroke="{F2}" stroke-width="5" fill="none"/>
<text x="358" y="297" font-family="Lato" font-size="12.5" font-weight="bold" fill="{F2}">THE DRAIN:</text>
<text x="358" y="312" font-family="Lato" font-size="11.5" fill="{F2}">sleep, sniffing, rest days</text>
<text x="230" y="300" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">the bucket drains slowly &#8212;</text>
<text x="120" y="300" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">up to 48&#8211;72 hours</text>
<rect x="135" y="8" width="200" height="26" rx="13" fill="{F}"/>
<text x="235" y="26" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">TRIGGER STACKING</text>
</svg>'''

def svg_three_for_three(w=560, h=210):
    checks = "".join(
        f'<g transform="translate({120 + i * 80},92)"><circle r="26" fill="{F2}"/>'
        f'<text y="9" font-family="Lato" font-size="26" font-weight="bold" fill="#FFF" text-anchor="middle">&#10003;</text>'
        f'<text y="48" font-family="Lato" font-size="11.5" font-weight="bold" fill="{INK}" text-anchor="middle">CLEAN REP {i+1}</text></g>'
        for i in range(3))
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="210" rx="14" fill="#EFEAE0"/>
<text x="280" y="36" font-family="Roboto Slab" font-size="17" font-weight="bold" fill="{F}" text-anchor="middle">THE 3-FOR-3 RULE</text>
{checks}
<line x1="370" y1="92" x2="430" y2="92" stroke="{AM}" stroke-width="6"/>
<polygon points="430,78 430,106 456,92" fill="{AM}"/>
<g transform="translate(498,92)"><circle r="30" fill="{F}"/>
<text y="-2" font-family="Lato" font-size="12" font-weight="bold" fill="{GD}" text-anchor="middle">&#8722;1 CAR</text>
<text y="14" font-family="Lato" font-size="10.5" fill="#FFF" text-anchor="middle">closer</text></g>
<text x="280" y="186" font-family="Lato" font-size="12.5" fill="{MUT}" text-anchor="middle">3 clean loops at this distance &#8212; on different triggers &#8212; before you earn one car-length. Miss one? Stay.</text>
</svg>'''

def svg_leash_J(w=520, h=240):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg">
<rect width="520" height="240" rx="14" fill="#EFEAE0"/>
<rect x="18" y="16" width="230" height="208" rx="12" fill="#F6E3DE"/>
<rect x="272" y="16" width="230" height="208" rx="12" fill="{PL}"/>
{_person(80, 150, 1.1)}{_dog(190, 140, 0.95, CL)}
<line x1="87" y1="118" x2="166" y2="132" stroke="{CL}" stroke-width="4"/>
<text x="133" y="206" font-family="Lato" font-size="13" font-weight="bold" fill="{CL}" text-anchor="middle">TIGHT LINE = pressure,</text>
<text x="133" y="222" font-family="Lato" font-size="13" font-weight="bold" fill="{CL}" text-anchor="middle">frustration, opposition reflex</text>
{_person(334, 150, 1.1)}{_dog(444, 140, 0.95, F)}
<path d="M 341,118 Q 380,175 420,135" stroke="{F2}" stroke-width="4" fill="none"/>
<text x="387" y="206" font-family="Lato" font-size="13" font-weight="bold" fill="{F2}" text-anchor="middle">LOOSE "J" = slack absorbs</text>
<text x="387" y="222" font-family="Lato" font-size="13" font-weight="bold" fill="{F2}" text-anchor="middle">startle; dog can choose calm</text>
<rect x="92" y="28" width="84" height="24" rx="12" fill="{CL}"/>
<text x="134" y="45" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">&#10005; WRONG</text>
<rect x="348" y="28" width="84" height="24" rx="12" fill="{F2}"/>
<text x="390" y="45" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">&#10003; RIGHT</text>
</svg>'''

def svg_decision_flow(w=560, h=380):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 380" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="380" rx="14" fill="#EFEAE0"/>
<rect x="190" y="18" width="180" height="40" rx="10" fill="{F}"/>
<text x="280" y="43" font-family="Lato" font-size="14" font-weight="bold" fill="#FFF" text-anchor="middle">YOU SPOT A TRIGGER</text>
<line x1="280" y1="58" x2="280" y2="86" stroke="{INK}" stroke-width="3"/>
<polygon points="272,84 288,84 280,96" fill="{INK}"/>
<polygon points="280,98 400,140 280,182 160,140" fill="{GD}"/>
<text x="280" y="135" font-family="Lato" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">Is the dog still</text>
<text x="280" y="152" font-family="Lato" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">in the Green Zone?</text>
<line x1="160" y1="140" x2="92" y2="140" stroke="{INK}" stroke-width="3"/>
<polygon points="94,132 94,148 82,140" fill="{INK}"/>
<text x="126" y="128" font-family="Lato" font-size="12" font-weight="bold" fill="{F2}">YES</text>
<rect x="14" y="170" width="156" height="64" rx="10" fill="{F2}"/>
<text x="92" y="196" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">WORK THE LOOP</text>
<text x="92" y="214" font-family="Lato" font-size="11.5" fill="{PL}" text-anchor="middle">see &#8594; look back &#8594; yes &#8594; pay</text>
<line x1="400" y1="140" x2="468" y2="140" stroke="{INK}" stroke-width="3"/>
<polygon points="466,132 466,148 478,140" fill="{INK}"/>
<text x="424" y="128" font-family="Lato" font-size="12" font-weight="bold" fill="{CL}">NO</text>
<rect x="396" y="170" width="150" height="64" rx="10" fill="{AM}"/>
<text x="471" y="196" font-family="Lato" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">EMERGENCY U-TURN</text>
<text x="471" y="214" font-family="Lato" font-size="11.5" fill="{INK}" text-anchor="middle">add distance FIRST, fast</text>
<line x1="471" y1="234" x2="471" y2="262" stroke="{INK}" stroke-width="3"/>
<polygon points="463,260 479,260 471,272" fill="{INK}"/>
<rect x="396" y="274" width="150" height="56" rx="10" fill="{F}"/>
<text x="471" y="297" font-family="Lato" font-size="12.5" font-weight="bold" fill="#FFF" text-anchor="middle">re-enter Green Zone,</text>
<text x="471" y="314" font-family="Lato" font-size="12.5" font-weight="bold" fill="#FFF" text-anchor="middle">THEN work the loop</text>
<rect x="14" y="274" width="156" height="56" rx="10" fill="{PL}" stroke="{F2}" stroke-width="2"/>
<text x="92" y="297" font-family="Lato" font-size="12.5" font-weight="bold" fill="{F}" text-anchor="middle">explosion anyway?</text>
<text x="92" y="314" font-family="Lato" font-size="12.5" font-weight="bold" fill="{F}" text-anchor="middle">&#8594; Recovery Script, p.62</text>
<line x1="92" y1="234" x2="92" y2="272" stroke="{INK}" stroke-width="3" stroke-dasharray="7 6"/>
</svg>'''

def svg_method_phases(w=560, h=230):
    boxes = [
        ("01", "MAP", "find your dog's number", F),
        ("02", "ANCHOR", "install the loop + U-turn", F2),
        ("03", "SHRINK", "close in, one car at a time", AM),
    ]
    out = ""
    for i, (n, t, d, c) in enumerate(boxes):
        x = 20 + i * 184
        tcol = INK if c == AM else "#FFF"
        scol = INK if c == AM else PL
        out += (f'<g transform="translate({x},60)"><rect width="160" height="120" rx="14" fill="{c}"/>'
                f'<text x="18" y="40" font-family="Roboto Slab" font-size="30" font-weight="bold" fill="{GD if c != AM else "#7A4F0E"}">{n}</text>'
                f'<text x="18" y="72" font-family="Lato" font-size="20" font-weight="bold" fill="{tcol}">{t}</text>'
                f'<text x="18" y="96" font-family="Lato" font-size="11.5" fill="{scol}">{d}</text></g>')
        if i < 2:
            out += (f'<polygon points="{x+162},120 {x+162},100 {x+182},110" fill="{INK}"/>')
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="230" rx="14" fill="#EFEAE0"/>
<text x="280" y="38" font-family="Roboto Slab" font-size="17" font-weight="bold" fill="{F}" text-anchor="middle">THE GREEN ZONE METHOD &#8212; THREE PHASES, 21 DAYS</text>
{out}
<text x="280" y="212" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">Days 1&#8211;5: Map &#183; Days 6&#8211;12: Anchor &#183; Days 13&#8211;21: Shrink</text>
</svg>'''

def svg_food_test(w=560, h=200):
    items = [
        ("EATS INSTANTLY", "soft + fast grab", F2, "GREEN"),
        ("EATS SLOWLY", "hard mouth, distracted", "#B89A2E", "YELLOW"),
        ("WON'T EAT", "head locked on trigger", CL, "RED"),
    ]
    out = ""
    for i, (t, d, c, z) in enumerate(items):
        x = 22 + i * 180
        out += (f'<g transform="translate({x},52)"><rect width="156" height="104" rx="12" fill="#FFF" stroke="{c}" stroke-width="3"/>'
                f'<circle cx="32" cy="34" r="16" fill="{c}"/>'
                f'<text x="32" y="40" font-family="Lato" font-size="15" font-weight="bold" fill="#FFF" text-anchor="middle">{i+1}</text>'
                f'<text x="58" y="32" font-family="Lato" font-size="12.5" font-weight="bold" fill="{INK}">{t}</text>'
                f'<text x="58" y="48" font-family="Lato" font-size="10.5" fill="{MUT}">{d}</text>'
                f'<rect x="16" y="66" width="124" height="24" rx="12" fill="{c}"/>'
                f'<text x="78" y="83" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">= {z} ZONE</text></g>')
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="200" rx="14" fill="#EFEAE0"/>
<text x="280" y="34" font-family="Roboto Slab" font-size="16" font-weight="bold" fill="{F}" text-anchor="middle">THE FOOD TEST &#8212; YOUR DOG'S MOUTH IS THE GAUGE</text>
{out}
<text x="280" y="184" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">offer one pea-sized treat at the moment the dog notices a trigger &#8212; the answer IS the zone</text>
</svg>'''

def svg_route_map(w=560, h=340):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 340" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="340" rx="14" fill="#EFEAE0"/>
<g fill="#D8D2C4">
<rect x="0" y="80" width="560" height="36"/><rect x="0" y="210" width="560" height="36"/>
<rect x="120" y="0" width="34" height="340"/><rect x="320" y="0" width="34" height="340"/>
</g>
<path d="M 40,300 L 40,228 L 137,228 L 137,98 L 337,98 L 337,228 L 470,228"
 stroke="{F2}" stroke-width="6" fill="none" stroke-dasharray="14 9" stroke-linecap="round"/>
<circle cx="40" cy="300" r="14" fill="{F}"/>
<text x="40" y="305" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">A</text>
<circle cx="470" cy="228" r="14" fill="{AM}"/>
<text x="470" y="233" font-family="Lato" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">B</text>
<g transform="translate(210,40)"><rect x="-12" y="-12" width="24" height="24" rx="5" fill="{CL}"/>
<text y="6" font-family="Lato" font-size="15" font-weight="bold" fill="#FFF" text-anchor="middle">!</text></g>
<text x="240" y="46" font-family="Lato" font-size="11.5" font-weight="bold" fill="{CL}">yard with fence dog &#8212; avoid</text>
<g transform="translate(430,60)"><rect x="-12" y="-12" width="24" height="24" rx="5" fill="{CL}"/>
<text y="6" font-family="Lato" font-size="15" font-weight="bold" fill="#FFF" text-anchor="middle">!</text></g>
<text x="380" y="36" font-family="Lato" font-size="11.5" font-weight="bold" fill="{CL}">dog-park corner</text>
<g transform="translate(80,160)"><circle r="12" fill="{F2}"/><text y="5" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">E</text></g>
<text x="20" y="138" font-family="Lato" font-size="11.5" font-weight="bold" fill="{F2}">escape: alley gap</text>
<g transform="translate(395,260)"><circle r="12" fill="{F2}"/><text y="5" font-family="Lato" font-size="13" font-weight="bold" fill="#FFF" text-anchor="middle">E</text></g>
<text x="350" y="290" font-family="Lato" font-size="11.5" font-weight="bold" fill="{F2}">escape: church lot</text>
<rect x="155" y="306" width="250" height="24" rx="12" fill="{F}"/>
<text x="280" y="323" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">PLAN THE ROUTE LIKE A HEIST</text>
</svg>'''

def svg_recovery_curve(w=560, h=240):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="240" rx="14" fill="#EFEAE0"/>
<line x1="60" y1="190" x2="520" y2="190" stroke="{INK}" stroke-width="2.5"/>
<line x1="60" y1="190" x2="60" y2="36" stroke="{INK}" stroke-width="2.5"/>
<path d="M 60,168 L 120,166 L 138,60 Q 150,44 162,68 Q 220,140 300,158 Q 400,172 520,166"
 stroke="{CL}" stroke-width="5" fill="none"/>
<line x1="60" y1="150" x2="520" y2="150" stroke="{F2}" stroke-width="3" stroke-dasharray="9 7"/>
<text x="66" y="142" font-family="Lato" font-size="11.5" font-weight="bold" fill="{F2}">baseline (can learn below this line)</text>
<circle cx="138" cy="60" r="7" fill="{CL}"/>
<text x="152" y="52" font-family="Lato" font-size="12" font-weight="bold" fill="{CL}">the explosion</text>
<text x="290" y="214" font-family="Lato" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">stress chemistry takes 24&#8211;72 HOURS to drain &#8212; not minutes</text>
<text x="40" y="120" font-family="Lato" font-size="11" fill="{MUT}" transform="rotate(-90 40 120)">AROUSAL</text>
<text x="160" y="186" font-family="Lato" font-size="10.5" fill="{MUT}">hour 0</text>
<text x="300" y="186" font-family="Lato" font-size="10.5" fill="{MUT}">day 1</text>
<text x="470" y="186" font-family="Lato" font-size="10.5" fill="{MUT}">day 2&#8211;3</text>
<rect x="330" y="52 " width="190" height="58" rx="10" fill="{F}"/>
<text x="425" y="76" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">after a blow-up: 48-hour</text>
<text x="425" y="94" font-family="Lato" font-size="12" font-weight="bold" fill="#FFF" text-anchor="middle">quiet protocol (p. 63)</text>
</svg>'''

def svg_treat_magnet(w=460, h=250):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 460 250" xmlns="http://www.w3.org/2000/svg">
<rect width="460" height="250" rx="14" fill="#EFEAE0"/>
{_person(150, 170, 1.5)}
{_dog(280, 168, 1.25, F)}
<circle cx="163" cy="120" r="10" fill="{AM}"/>
<text x="185" y="112" font-family="Lato" font-size="12" font-weight="bold" fill="{INK}">1. hand at your CHEST between reps</text>
<circle cx="160" cy="158" r="10" fill="{AM}"/>
<text x="185" y="155" font-family="Lato" font-size="12" font-weight="bold" fill="{INK}">2. deliver at the SEAM of your pants</text>
<circle cx="218" cy="196" r="10" fill="{AM}"/>
<text x="240" y="220" font-family="Lato" font-size="12" font-weight="bold" fill="{INK}">3. pay AT THE KNEE &#8212; dog turns fully away</text>
<text x="230" y="36" font-family="Roboto Slab" font-size="15" font-weight="bold" fill="{F}" text-anchor="middle">TREAT DELIVERY = STEERING</text>
<text x="230" y="56" font-family="Lato" font-size="11.5" fill="{MUT}" text-anchor="middle">where the food appears decides where the dog's eyes go next</text>
</svg>'''

def svg_session_clock(w=460, h=220):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 460 220" xmlns="http://www.w3.org/2000/svg">
<rect width="460" height="220" rx="14" fill="#EFEAE0"/>
<rect x="24" y="60" width="120" height="110" rx="12" fill="{F2}"/>
<text x="84" y="100" font-family="Roboto Slab" font-size="26" font-weight="bold" fill="#FFF" text-anchor="middle">3 min</text>
<text x="84" y="124" font-family="Lato" font-size="11.5" fill="{PL}" text-anchor="middle">sniff + settle</text>
<text x="84" y="140" font-family="Lato" font-size="11.5" fill="{PL}" text-anchor="middle">(decompress in)</text>
<rect x="170" y="48" width="120" height="122" rx="12" fill="{F}"/>
<text x="230" y="92" font-family="Roboto Slab" font-size="26" font-weight="bold" fill="{GD}" text-anchor="middle">10 min</text>
<text x="230" y="116" font-family="Lato" font-size="11.5" fill="{PL}" text-anchor="middle">the work:</text>
<text x="230" y="132" font-family="Lato" font-size="11.5" fill="{PL}" text-anchor="middle">loops in the zone</text>
<rect x="316" y="60" width="120" height="110" rx="12" fill="{AM}"/>
<text x="376" y="100" font-family="Roboto Slab" font-size="26" font-weight="bold" fill="{INK}" text-anchor="middle">3 min</text>
<text x="376" y="124" font-family="Lato" font-size="11.5" fill="{INK}" text-anchor="middle">sniff walk out</text>
<text x="376" y="140" font-family="Lato" font-size="11.5" fill="{INK}" text-anchor="middle">(end on grass)</text>
<text x="230" y="32" font-family="Roboto Slab" font-size="15" font-weight="bold" fill="{F}" text-anchor="middle">A SESSION IS 16 MINUTES. THAT'S THE WHOLE JOB.</text>
<text x="230" y="198" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">short and clean beats long and messy &#8212; every single time</text>
</svg>'''

def svg_progress_wave(w=560, h=220):
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg">
<rect width="560" height="220" rx="14" fill="#EFEAE0"/>
<line x1="50" y1="180" x2="530" y2="180" stroke="{INK}" stroke-width="2.5"/>
<path d="M 50,150 Q 90,120 110,140 Q 140,165 170,118 Q 200,88 225,128 Q 250,158 285,96 Q 310,70 340,108 Q 370,140 410,76 Q 440,52 480,70 Q 510,80 530,58"
 stroke="{F2}" stroke-width="5" fill="none"/>
<line x1="50" y1="150" x2="530" y2="58" stroke="{AM}" stroke-width="3" stroke-dasharray="10 8"/>
<circle cx="170" cy="118" r="6" fill="{F2}"/><circle cx="225" cy="128" r="6" fill="{CL}"/>
<text x="238" y="146" font-family="Lato" font-size="11.5" font-weight="bold" fill="{CL}">a bad day</text>
<text x="300" y="36" font-family="Roboto Slab" font-size="15" font-weight="bold" fill="{F}" text-anchor="middle">PROGRESS IS A WAVE, NOT A STAIRCASE</text>
<text x="290" y="206" font-family="Lato" font-size="12" fill="{MUT}" text-anchor="middle">judge the WEEK's average distance, never the day &#8212; that's what the logs are for</text>
</svg>'''


SVG_LIBRARY = {
    "zone_map": svg_zone_map, "engage_loop": svg_engage_loop, "uturn": svg_uturn,
    "carlength": svg_carlength, "body_language": svg_body_language,
    "stress_bucket": svg_stress_bucket, "three_for_three": svg_three_for_three,
    "leash_J": svg_leash_J, "decision_flow": svg_decision_flow,
    "method_phases": svg_method_phases, "food_test": svg_food_test,
    "route_map": svg_route_map, "recovery_curve": svg_recovery_curve,
    "treat_magnet": svg_treat_magnet, "session_clock": svg_session_clock,
    "progress_wave": svg_progress_wave,
}


def html_doc(pages_html, title="CalmWalk"):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}</style></head><body>{"".join(pages_html)}</body></html>')
