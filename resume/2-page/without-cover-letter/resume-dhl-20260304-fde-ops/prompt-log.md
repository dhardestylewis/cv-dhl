# Prompt Log — Ramp FDE Ops Resume

## User Requests & Actions Taken

### Round 1: Initial tailoring
- **Request**: Tailor resume for Ramp FDE Ops role from `resume-dhl-20260217-priorlabs-cloud.tex`
- **Actions**: Created branch `resume-dhl-20260219-ramp-fde-ops`, copied base file, rewrote title/summary/Core Expertise/Technologies/experience bullets for FDE Ops framing. Compiled to 3 pages.

### Round 2: "3x founder" concern
- **Request**: "is 3x founder safe description considering none of these exited"
- **Action**: Changed to "repeat founder" — accurate and still signals founder experience (Ramp nice-to-have)

### Round 3: Detailed line-by-line feedback (15+ items)
- **Request**: Are customers described accurately?
  - **Action**: Teaching only claims Petrobras for ML Geosciences course; others are just grad courses. Changed "external enterprise engineers" → "Petrobras geoscientists and petroleum engineers"
- **Request**: "year-long competition" doesn't align with 2-month research intern dates
  - **Action**: Moved "year-long" to Data Scientist role (Feb 2018–Jul 2021) where dates support it
- **Request**: Dedup Petrobras between Data Scientist and Teaching
  - **Action**: Removed Petrobras bullet from Data Scientist (now only in Teaching)
- **Request**: Check old CV for lost relevant details
  - **Action**: Added "Managed relationships with NOAA, NSF, USACE, Texas GLO, USC, UT, A&M" from old CV
- **Request**: "checklists and milestones" — is this FDE language? trim by one word
  - **Action**: Changed to "launch checklists" — matches Ramp JD language exactly
- **Request**: Summit Geospatial — "documented repeatable workflows for client onboarding" doesn't reflect website
  - **Action**: Removed entirely (user confirmed fabricated)
- **Request**: "translating technical data specs into client-friendly documentation" — never did this
  - **Action**: Removed entirely
- **Request**: Parenthetical tech stacks lazy AI speak?
  - **Action**: Removed all parenthetical tech lists: `(Airflow, Elasticsearch, FastAPI, Supabase, Redis)`, `(React frontend, Python/FastAPI backend, Postgres)`, `(Python, React, SQL)` from summary
- **Request**: "AI & automation" line too long, spans two lines
  - **Action**: Shortened by removing "Airflow" (already in Infrastructure context) and "embeddings"
- **Request**: homecastr.com link redundant (already in title)
  - **Action**: Removed inline link
- **Request**: Save JD verbatim in folder
  - **Action**: Saved as `jd-ramp-fde-ops.txt`
- **Request**: Bold what JD cares about
  - **Action**: Audited bolding — now bolded: `scoped product requirements`, `automated data pipelines`, `scoped integration requirements`, `managed relationships`, `web distribution platform end-to-end`
- **Request**: multi-million-dollar — be specific or keep vague?
  - **Action**: Kept "multi-million-dollar" (matches CV phrasing, avoids false precision)

### Round 4: Final polish
- **Request**: Still seeing "3x founder" and "AI &automation" in PDF
  - **Action**: Confirmed `.tex` has "repeat founder"; "AI &automation" was PDF line-wrap artifact. Shortened line and recompiled fresh PDF.

## Outstanding / TODO
(none currently — awaiting user review of fresh PDF)

### Round 5: "AI & automation" label fix
- **Request**: "AI & automation" still spans two lines — is "automation" even a category engineers use?
- **Research**: Looked up FDE/ML engineer resume skill categories — industry standard is "AI/ML", not "AI & automation"
- **Action**: Changed label to "AI/ML". Added Airflow back since shorter label freed space. Recompiled.
