# CV and Resume Repository

This repository contains Daniel Hardesty Lewis's CVs and resumes, organized by document type, page count, and cover letter status.

## Structure

```
cv-dhl.git/
├── cv/                          # Curriculum Vitae
├── resume/                      # Resumes
│   ├── 1-page/                  # 1-page resumes
│   │   ├── with-cover-letter/
│   │   └── without-cover-letter/
│   ├── 2-page/                 # 2-page resumes
│   │   ├── with-cover-letter/
│   │   └── without-cover-letter/
│   └── 2plus-page/             # 2+ page resumes
│       ├── with-cover-letter/
│       └── without-cover-letter/
├── _archive/                   # Archived/legacy contents
├── artifacts/                  # Saved profile and supporting artifacts
├── dhardestylewis/             # GitHub profile README submodule
├── GUIDELINES.md               # Project guidelines
├── TODO.md                     # Current tasks
└── TODO-COMPLETED.md           # Completed tasks archive
```

## Naming Schema

- **CVs**: `cv-dhl-YYYYMMDD[-latest]`
- **Resumes**: `resume-dhl-YYYYMMDD-[descriptor]`
- Use hyphens (`-`), not underscores (`_`), except in legacy descriptors like `columbia_assistantship`

## Current versions (read first)

- Full CV: `cv/cv-dhl-20261015-latest` (8 pages). Two-pager: `resume/2-page/without-cover-letter/resume-dhl-20261015-latest`. Both built 2026-10-15; provenance and reconciliation decisions in `cv/cv-dhl-20261015-latest/PROVENANCE.md`.
- Comparables and the bar: `artifacts/comparables-ladder-20261015.md` (who evaluates Daniel, up to DeepMind), `artifacts/comparables/` (40 pulled profiles, four tiers, plus `writing/` with 77 sources on what makes a strong profile), `artifacts/comparison-theirs-vs-mine-20261015.md` (14-dimension comparison, role bars, bullet audit, ranked gaps).
- Open work: the P1 block at the top of `TODO.md`, dated 2026-10-15. Items needing Daniel are marked Owner: Daniel.

## Current CVs

- `cv-dhl-20261015-latest` - Current CV: 2026-07-26 resume content on the 2026-10-15 LinkedIn dates (see its `PROVENANCE.md`)
- `cv-dhl-20251117-latest` - Historical November 2025 CV source and PDF
- `cv-dhl-20231231` - December 2023 version
- `cv-dhl-20230831` - August 2023 version
- `cv-dhl-20230801` - August 2023 early version

## Current Resumes

See [resume/README.md](resume/README.md) for the full directory of targeted resumes.

- `resume-dhl-20261015-latest` - Current two-page résumé (October 2026): the July 2026 two-pager with roles reconciled to the 2026-10-15 LinkedIn export
- `resume-dhl-20260726-anthropic-fellows` - July 2026 targeted résumé (Anthropic Fellows)
- `_BASE_resume-dhl-latest` - Base/template version

## Recovered Historical Documents

Distinct CV and résumé artifacts recovered from the Jobsearch and PhD Applications directories are recorded in [IMPORT-20261015.md](IMPORT-20261015.md). They retain the established document-type, page-count, and cover-letter hierarchy.

## Saved LinkedIn Profile Exports

Ten verified local LinkedIn profile exports are kept in [`artifacts/`](artifacts/), ordered by the PDF-embedded Eastern timestamp and numbered `v01` through `v10`. See [artifacts/README.md](artifacts/README.md) for provenance, hashes, and source mapping.

## Documentation

See `GUIDELINES.md` for project-wide guidelines and best practices.
