# cv-dhl-20261015 provenance

Built 2026-10-15. Every line in this CV traces to one of three sources. Nothing was written from LinkedIn wording alone.

| Section | Source | What changed |
| --- | --- | --- |
| Skeleton, publications, presentations, posters, academic and professional projects, review committees, students mentored, coursework, affiliations, extracurriculars, languages | `cv/cv-dhl-20251117-latest/cv_dhl_20251117.tex` (latest full CV) | Unchanged except `\Needspace` guards before section headings so no heading is orphaned at a page foot. |
| Professional experience bullets, research entries, teaching wording, Key Projects, TACC bullets | `resume/2-page/without-cover-letter/resume-dhl-20260726-anthropic-fellows/resume-dhl-20260726-anthropic-fellows.tex` (latest two-page resume, 2026-07-26) | Carried over in full. Bold emphasis dropped to match CV style. |
| Role names, start and end dates for Worldcastr, South Park Commons, Summit Geospatial; Columbia degree years | `artifacts/linkedin-profile-v10-20261015-174244.pdf` (latest saved LinkedIn export) | Worldcastr, Founder, Dec. 2025 to Present. South Park Commons, Member, Jun. 2026 to Sep. 2026. Summit Geospatial, Nov. 2023 to Aug. 2025. Columbia M.S. 2024 to 2026. |

## Reconciliation decisions

These are the items the public LinkedIn profile forces a reader to reconcile, and how this CV resolves each.

1. **Current company.** The July resume leads with Homecastr (Sep. 2025 to Present); LinkedIn v10 leads with Worldcastr (Dec. 2025 to Present) and omits Homecastr. The CV leads with Worldcastr on the LinkedIn dates and keeps every Homecastr technical bullet under it, naming Homecastr as the first product. No separate Homecastr entry, so no third Homecastr start date is asserted.
2. **Summit end date.** LinkedIn v08 to v10 end Summit in Aug. 2025. The CV uses Aug. 2025 and drops the "now targeting licensing to AI labs" line that described a live venture.
3. **South Park Commons.** LinkedIn lists Member, Jun. to Sep. 2026. The July resume says Entrepreneur-in-Residence, Jun. 2026 to Present. The CV uses the LinkedIn title and end date and keeps the resume's two bullets.
4. **PoliBOM.** Absent from LinkedIn v10. Kept on the July resume's terms (Technical Advisor, Oct. 2024 to Sep. 2025) because it is an ended role and a CV is the more complete record. Omission on LinkedIn is not a contradiction.
5. **UT Austin teaching.** Jan. 2018 to Dec. 2020 continuous, matching LinkedIn v07 to v10 and every resume. Older exports (v01 to v06) show two terms; see `artifacts/tech-holding-provenance-audit.md`.
6. **Columbia degree.** LinkedIn shows 2024 to 2026; the July resume lists the thesis as 2026 and no longer says "expected". The CV uses 2024 to 2026 with the thesis title.
7. **Sep. to Nov. 2025.** Left unannotated. No explanation belongs in the CV.

## Assumptions to overturn

- Homecastr is presented as Worldcastr's first product rather than as a separate company. If Homecastr should stand as its own dated entry, the latest resume's dates are Sep. 2025 to Present.
- The 14M weekly production requests figure is the July resume's, carried unchanged.
- The Columbia M.S. is treated as conferred in 2026. If it is still pending, restore "expected".
- Contact email is daniel@worldcastr.com, the current primary mailbox.

## Build

```bash
cd cv/cv-dhl-20261015-latest
pdflatex -interaction=nonstopmode cv-dhl-20261015.tex
pdflatex -interaction=nonstopmode cv-dhl-20261015.tex
```

Output: 8 pages. Verified rendered on 2026-10-15; every page break falls on a section or entry boundary.
