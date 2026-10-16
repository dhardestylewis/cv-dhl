# CVs

This directory contains all CV versions, organized chronologically with the most recent marked as `-latest`.

## Current CVs

- **cv-dhl-20261015-latest** - Current CV (October 2026). Full-length CV built from the 2026-07-26 two-page resume plus the November 2025 CV, with role dates reconciled to the 2026-10-15 LinkedIn export. See its `PROVENANCE.md`.
- **cv-dhl-20251117-latest** - Historical November 2025 CV
- **cv-dhl-20231231** - December 2023 version
- **cv-dhl-20230831** - August 2023 version
- **cv-dhl-20230801** - August 2023 early version

## Files

Each CV folder contains:
- Main `.tex` source file
- Compiled `.pdf` output
- Supporting files (`.log`, `.aux`, etc.)
- `moderncvcolorblack.sty` (where applicable)

## Compilation

```bash
cd cv-dhl-YYYYMMDD/
pdflatex cv-dhl-YYYYMMDD.tex
```
