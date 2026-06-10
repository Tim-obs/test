#!/usr/bin/env python3
"""Render pipeline: HTML -> wkhtmltopdf -> per-page PNG -> contact sheets."""
import os, subprocess, sys, glob

BUILD = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BUILD, "out")

def render(name, html, qa_dpi=60, sheets=True):
    os.makedirs(OUT, exist_ok=True)
    html_path = os.path.join(OUT, f"{name}.html")
    pdf_path = os.path.join(OUT, f"{name}.pdf")
    with open(html_path, "w") as f:
        f.write(html)
    subprocess.run([
        "wkhtmltopdf", "-q", "--enable-local-file-access",
        "--page-width", "8.5in", "--page-height", "11in",
        "-T", "0", "-B", "0", "-L", "0", "-R", "0",
        "--disable-smart-shrinking", "--dpi", "96",
        html_path, pdf_path], check=True)
    qa_dir = os.path.join(OUT, f"{name}-qa")
    os.makedirs(qa_dir, exist_ok=True)
    for f_ in glob.glob(os.path.join(qa_dir, "*.png")):
        os.remove(f_)
    subprocess.run(["pdftoppm", "-png", "-r", str(qa_dpi), pdf_path,
                    os.path.join(qa_dir, "p")], check=True)
    pages = sorted(glob.glob(os.path.join(qa_dir, "p-*.png")))
    sheet_paths = []
    if sheets:
        chunk = 12
        for i in range(0, len(pages), chunk):
            sp = os.path.join(OUT, f"{name}-sheet{i // chunk + 1:02d}.png")
            subprocess.run(["montage", *pages[i:i + chunk], "-tile", "4x3",
                            "-geometry", "+6+6", "-background", "#444",
                            "-label", "%f", sp], check=True)
            sheet_paths.append(sp)
    n = len(pages)
    print(f"RENDERED {name}: {n} pages -> {pdf_path}")
    for s in sheet_paths:
        print(f"  sheet: {s}")
    return n, pdf_path, sheet_paths

if __name__ == "__main__":
    mod = sys.argv[1]
    import importlib
    sys.path.insert(0, BUILD)
    m = importlib.import_module(mod)
    render(m.NAME, m.build())
