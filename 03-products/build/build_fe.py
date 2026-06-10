"""Assemble the FE book: auto page numbers + computed TOC."""
from design import *
import fe_front, fe_part1, fe_part2, fe_part3, fe_part4, fe_part5

NAME = "CalmWalk-The-21-Day-Calm-Walks-Plan"

def build():
    entries = (fe_front.pages() + fe_part1.pages() + fe_part2.pages()
               + fe_part3.pages() + fe_part4.pages() + fe_part5.pages())

    # pass 1: numbering + TOC collection
    toc_items = []          # (kind, title, pno, part_index)
    part_idx = -1
    for i, e in enumerate(entries):
        e["pno"] = i + 1
        if "raw_divider" in e:
            part_idx += 1
            toc_items.append(("part", e["toc_part"], e["pno"], part_idx))
        elif e.get("toc"):
            toc_items.append(("row", e["toc"], e["pno"], part_idx))

    def toc_page(items, first):
        body = kicker("THE 21-DAY CALM WALKS PLAN") if first else kicker("CONTENTS, CONTINUED")
        body += h1("Contents") if first else h1("&nbsp;")
        for kind, title, pno, _ in items:
            body += tocpart(title, pno) if kind == "part" else tocrow(title, pno)
        if not first:
            body += callout("note", "&#9998; HOW TO READ THIS BOOK",
                p("Tonight: Part I. Tomorrow: Part II. Then one day-page per day. "
                  "Parts IV and V are reference &#8212; read them when the street sends homework."))
        return body

    slot1 = [t for t in toc_items if t[3] <= 1]   # parts I–II
    slot2 = [t for t in toc_items if t[3] >= 2]   # parts III–V

    html_pages = []
    for e in entries:
        if "raw" in e:
            html_pages.append(e["raw"])
        elif "tocslot" in e:
            body = pad(toc_page(slot1 if e["tocslot"] == 1 else slot2, e["tocslot"] == 1))
            html_pages.append(page(body, pno=e["pno"]))
        elif "raw_divider" in e:
            html_pages.append(divider(*e["raw_divider"]))
        else:
            html_pages.append(page(e["html"], pno=e["pno"], part=e.get("part"),
                                   partcolor=e.get("color")))
    return html_doc(html_pages, "The 21-Day Calm Walks Plan")
