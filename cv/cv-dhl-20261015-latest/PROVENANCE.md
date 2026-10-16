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

## Second pass, same day

- Address changed to 34 West 128th St, New York, NY 10027 in the CV and the two-pager footer.
- Columbia line is now "2026" with the thesis title hyperlinked to github.com/dhardestylewis/thesis; the thesis entry in publications carries the Columbia Academic Commons DOI 10.7916/1swr-4871 (OpenAlex, published 2026-06-10).
- Worldcastr blurb is the canonical overview with the leading "Worldcastr is building a" clause dropped so it fits two lines; each Worldcastr bullet was cut to two rendered lines in the CV. The 12.6% four-year MdAE keeps its NYC qualifier.
- A two-page variant exists at `resume/2-page/without-cover-letter/resume-dhl-20261015-latest/`: the 2026-07-26 Anthropic Fellows two-pager with the same Worldcastr entry, SPC as Member Jun. to Sep. 2026, the new address and email, and the thesis DOI. Title line "Research Engineer" and the Core Expertise and Technologies blocks are carried unchanged.
- Google Scholar and OpenAlex check: OpenAlex lists nine works under both author records; all are on the CV except a 2017 Springer chapter, "Big Data Analytics and Customs Throughput: The Case of Jamaica" (doi 10.1007/978-3-319-56538-5_52), which is likely a misattribution and was not added. Peer comparison in `artifacts/peer-cv-comparison-20261015.md`.

## Third pass, same day: edits against the comparables bar

Sources: `artifacts/comparison-theirs-vs-mine-20261015.md` and the Worldcastr preprint claims ledger of 2026-10-13 (rows A3, A4, B1, B2, B4, C1, C2, C11, C14).

- Worldcastr entry now leads with the named model and ledger-sourced scale: FMTSFlow on a 388M-row panel, 16 jurisdictions, 4 countries, 32 targets, one checkpoint per information cutoff 2019 to 2023; then the pre-registered benchmark (59.8% county win rate vs 18 sources on 3,134 counties; 54.9% tract vs 30 agencies, 44 vintages; held-flat and GBM baselines; information-matched 2025 test under way); then the archive and release package (131 sources, 3,065 files, 27 vintages; preprint, HF dataset, GitHub scorer, model card, pending approval). The diffusion forecaster, architecture and serving bullets follow. The two-pager carries four of the six for space.
- The LLM chat engine moved to Key Projects in the full CV and was dropped from the two-pager.
- TACC Frontera line reworded from "1M-node-scale jobs" to "system-scale, million-task jobs on Frontera (then a top-5 supercomputer, about 450K cores)"; the true node-hour figure is a TODO for Daniel.
- The Gil farewell-address bullet was removed; the Bagnold bullet now states the specific contribution (the inundation-mapping research presented to NOAA, which is on the Presentations list).
- PoliBOM "Directed development" became "Advised on", matching the Technical Advisor title. "The first ... model of NIMBYism" became "to our knowledge, the first".
- The thesis methods line links the repo. The full CV's Technology Skills block was replaced with an itemized stack (modeling, causal inference, LLM applications, data, geospatial, HPC and infrastructure naming Frontera, Stampede2, Lonestar).
- The two-pager dropped the SPC customer-discovery bullet to stay at two pages.

## Fourth pass, same day: cross-target results replace the housing-only headline

Daniel's call: the 7.0% one-year error and the Zillow comparison described the Homecastr-era parcel-value model scored alone, and are out of date now that FMTSFlow scores housing alongside the other targets. The Worldcastr entry now reports the cross-target standing from the evidence scoreboard (2026-10-07) and the claims ledger: beats official projections in 6 of 10 pooled target-level comparisons and ties the rest; county population 59.8% vs 18 sources; tract 54.9% vs 30 agencies with the per-target split (households 60.1%, housing 52.5%, population 48.0%); the gradient-boosted lag baseline still leads at tract; the information-matched 2025 test is under way. Housing appears as one target among the 32 in the registry and one of the three scored today. Homecastr is kept as the first product with its architecture named and its serving volume, with no accuracy figure. The former TODO item on the Zillow basis is marked superseded.

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
