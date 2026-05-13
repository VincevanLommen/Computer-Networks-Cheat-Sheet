"""
Script om automatisch een cheat sheet PDF te maken van alle .md bestanden in deze folder.

Gebruik:
    pip install markdown xhtml2pdf
    python generate_pdf.py

Output: cheat_sheet.pdf
"""

import glob
import os
import markdown
from xhtml2pdf import pisa

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "cheat_sheet.pdf")

# Volgorde van bestanden (pas aan indien gewenst)
FILE_ORDER = [
    "readme.md",
    "OSI model.md",
    "Cisco cheat sheet.md",
    "Protocollen cheat sheet.md",
    "Security.md",
    "Wireless concepts.md",
    "Wireshark.md",
    "good to know.md",
    "extra uitleg comandos.md",
    "voorbeeldexamen raf.md",
]

CSS = """
@page {
    size: A4;
    margin: 1.5cm;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10px;
    line-height: 1.4;
    color: #222;
}
h1 {
    color: #1a5276;
    border-bottom: 2px solid #1a5276;
    padding-bottom: 4px;
    page-break-before: always;
    font-size: 18px;
}
h1:first-child {
    page-break-before: avoid;
}
h2 {
    color: #2471a3;
    font-size: 14px;
    margin-top: 12px;
}
h3 {
    color: #2e86c1;
    font-size: 12px;
}
code {
    background-color: #f4f4f4;
    padding: 1px 4px;
    font-family: "Courier New", Courier, monospace;
    font-size: 9px;
}
pre {
    background-color: #f4f4f4;
    padding: 8px;
    border: 1px solid #ddd;
    font-family: "Courier New", Courier, monospace;
    font-size: 9px;
    overflow: hidden;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 8px 0;
}
th, td {
    border: 1px solid #ccc;
    padding: 4px 6px;
    font-size: 9px;
    text-align: left;
}
th {
    background-color: #eaf2f8;
}
blockquote {
    border-left: 3px solid #2471a3;
    margin-left: 0;
    padding-left: 10px;
    color: #555;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 12px 0;
}
"""


def collect_md_files():
    """Verzamel alle .md bestanden in de juiste volgorde."""
    ordered = []
    remaining = set()

    # Vind alle .md bestanden (exclusief dit script)
    for f in glob.glob(os.path.join(SCRIPT_DIR, "*.md")):
        remaining.add(os.path.basename(f))

    # Voeg eerst de bestanden in FILE_ORDER toe
    for name in FILE_ORDER:
        if name in remaining:
            ordered.append(name)
            remaining.remove(name)

    # Voeg eventuele overgebleven bestanden toe
    for name in sorted(remaining):
        ordered.append(name)

    return ordered


def md_to_html(md_files):
    """Lees alle markdown bestanden en converteer naar één HTML string."""
    md_extensions = ["tables", "fenced_code", "codehilite", "toc", "nl2br"]
    sections = []

    for filename in md_files:
        filepath = os.path.join(SCRIPT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        html = markdown.markdown(content, extensions=md_extensions)
        sections.append(f'<!-- {filename} -->\n{html}')

    body = "\n<hr/>\n".join(sections)

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


def html_to_pdf(html_string, output_path):
    """Converteer HTML naar PDF."""
    with open(output_path, "wb") as f:
        status = pisa.CreatePDF(html_string, dest=f)
    return not status.err


def main():
    md_files = collect_md_files()
    print(f"Gevonden bestanden ({len(md_files)}):")
    for f in md_files:
        print(f"  - {f}")

    print("\nConverteren naar HTML...")
    html = md_to_html(md_files)

    print(f"PDF genereren: {OUTPUT_FILE}")
    success = html_to_pdf(html, OUTPUT_FILE)

    if success:
        size_kb = os.path.getsize(OUTPUT_FILE) / 1024
        print(f"\nKlaar! PDF aangemaakt: {OUTPUT_FILE} ({size_kb:.1f} KB)")
    else:
        print("\nFout bij het genereren van de PDF.")
        exit(1)


if __name__ == "__main__":
    main()
