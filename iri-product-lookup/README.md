# IRI Product Lookup

`iri_product_lookup.html` is a single self-contained page: open it in any browser (double-click).

Type a product name (optionally the manufacturer) or an HS code. The page:

1. **Searches the web** (Wikipedia, no API key needed) to describe the product or company — e.g.
   "Duracell" → batteries — and uses that description to help match the list.
2. **Searches the IRI standards list** (577 standards embedded from `IRI_Standards_All.xlsx`) in the
   category, description, scope, examples and sector columns, or by HS code prefix.
3. Shows the **category, section, sector, HS code(s)**, and whether the product is **subject to a decree
   and standard** — with the decree number/date, restriction (NAJM code), applicable standards, and each
   standard's scope / out of scope / examples. Other possible categories are listed below.
   If nothing matches, it says the product was not found in the IRI list.

Results are keyword-based: "Possible match — please verify" means the match came only from the web
description, and an exclusion warning appears when your words occur in a standard's *Out of scope* text.
Google search links are provided to confirm HS codes and standards.

## Updating the data

- Permanent: `python build_lookup.py path/to/IRI_Standards_All.xlsx` (needs `openpyxl`) regenerates
  `iri_product_lookup.html` from `template.html`.
- Temporary: click **Load updated Excel…** in the page (same sheet layout: title row, header row, data).
