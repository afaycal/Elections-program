"""Build iri_product_lookup.html from the IRI standards Excel file.

Usage:
    python build_lookup.py path/to/IRI_Standards_All.xlsx

The script reads the "All Standards" sheet (title row 1, headers row 2,
data from row 3), embeds every row as JSON into template.html and writes
iri_product_lookup.html next to this script. Re-run it whenever the Excel
file is updated.
"""
import datetime
import json
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
NCOLS = 25  # Customs HS Code .. Portal


def cell_text(value):
    if value is None:
        return ""
    if isinstance(value, datetime.datetime):
        return value.strftime("%d/%m/%Y")
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ws = openpyxl.load_workbook(sys.argv[1], read_only=True, data_only=True).worksheets[0]
    rows = []
    for row in ws.iter_rows(min_row=3, values_only=True):
        values = [cell_text(v) for v in list(row)[:NCOLS]]
        values += [""] * (NCOLS - len(values))
        if any(values):
            rows.append(values)

    template = (HERE / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
    html = template.replace("/*__IRI_DATA__*/[]", payload)
    out = HERE / "iri_product_lookup.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} with {len(rows)} standards")


if __name__ == "__main__":
    main()
