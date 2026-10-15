# Change ledger: July 18 data-engineer resume to July 26 Anthropic Fellows resume

## Comparison basis

- Branch: `codex/anthropic-fellows-20260726`
- Baseline: `resume/2-page/without-cover-letter/resume-dhl-20260718-data-engineer/resume-dhl-20260718-data-engineer.tex`
- Target: `resume/2-page/without-cover-letter/resume-dhl-20260726-anthropic-fellows/resume-dhl-20260726-anthropic-fellows.tex`
- Highlighted review: `resume/2-page/without-cover-letter/resume-dhl-20260726-anthropic-fellows/resume-dhl-20260726-anthropic-fellows-HIGHLIGHTED-REVIEW.pdf`
- Final source difference: 6 removed lines and 6 added lines. Every other TeX line is identical.

The highlighted review PDF places yellow markers over all six final replacement locations. The clean target PDF remains the submission copy.

## Complete edit list

### 1. Title, line 50

Baseline: `Data Engineer`

Target: `Research Engineer`

Reason: Match the research role while retaining the engineering identity.

### 2. Professional summary, line 69

Baseline: `Specializing in automated validation frameworks and scalable distributed infrastructure. Delivered consumer pricing and statewide resiliency platforms across geospatial & time-series workloads.`

Target: `Specializing in causal inference, automated validation, and scalable distributed infrastructure. Delivered forecasting, financial modeling, and statewide resiliency platforms across geospatial & time-series workloads.`

Reason: Surface causal inference and economic modeling without changing the resume structure.

### 3. Homecastr description, line 98

Baseline: `Consumer AI forecasting platform serving 66K+ unique visitors and 4.3M weekly API requests.`

Target: `Built-environment foundation model using 50M+ parcel observations and serving roughly 14M production requests weekly.`

Reason: Use the current company framing and current production scale.

### 4. PoliBOM bullet, line 109

Baseline: The final clause used a vague process label for the former manual work.

Target: `replacing manual trade-compliance analysis with predictable multi-step reasoning.`

Reason: Name the concrete analysis being replaced.

### 5. Summit Geospatial description, line 115

Baseline: The description ended with a vague process label.

Target: `High-resolution elevation data and web delivery for engineering and hazard analysis.`

Reason: Name the concrete analytical use.

### 6. TACC scale bullet, line 125

Baseline: `Scaled climate and flood models on supercomputers, executing 800,000-node distributed jobs while managing $1M+ compute budgets and federal partnerships with NOAA, NSF, USACE, GLO.`

Target: `Scaled climate and flood models through 1M-node-scale jobs on Frontera, a top-5 most powerful supercomputer in the world; managed $1M+ compute budgets and NOAA, NSF, USACE, and GLO partnerships.`

Reason: Use the current preferred compute-scale phrasing and identify Frontera explicitly.

## Direct source comparison

From the CV repository root:

```powershell
git diff --no-index -- resume/2-page/without-cover-letter/resume-dhl-20260718-data-engineer/resume-dhl-20260718-data-engineer.tex resume/2-page/without-cover-letter/resume-dhl-20260726-anthropic-fellows/resume-dhl-20260726-anthropic-fellows.tex
```

An experimental addition of Stijn van Nieuwerburgh to the thesis job title was fully reverted. It is not present in the final source difference because that context belongs in the application reference field.
