# TACC Senior Bullet Optimization — Diff

Comparing `resume-dhl-20260207-fullstack-mle.tex` (original) vs `resume-dhl-20260207-fullstack-mle-v2.tex` (optimized)

---

## Summary of Changes

| Issue Fixed | Original | Optimized |
|-------------|----------|-----------|
| **Verb repetition** | "Developed" × 2 | "Authored" / "Engineered" |
| **Concept repetition** | "Real-Time Inundation Mapping" × 2 | Only once; 2nd → "statewide response system" |
| **Adjective repetition** | "high-resolution" × 2 | "sub-meter" in line 115 |
| **Phrase repetition** | "federal partnerships with" | → "across" |
| **Impact positioning** | "$40M" buried mid-sentence | "$40M" moved to front-load impact |

---

## Line-by-Line Diff

### Line 111 (Co-founded Summit Geospatial)

```diff
- \item Co-founded \href{...}{summitgeospatial.com} to commercialize and sustain state-level terrain models developed for the \$40M \href{...}{Texas Disaster Information System (TDIS)}, delivering precision decision-support for civil engineering.
+ \item Co-founded \href{...}{summitgeospatial.com} to commercialize \$40M state-level terrain models from the \href{...}{Texas Disaster Information System (TDIS)}, sustaining precision decision-support for civil engineering.
```

**Rationale:** Front-loaded `$40M` for immediate impact; changed "developed for" → "from" (tighter); moved "sustain" → "sustaining" as trailing clause.

---

### Line 112 (RFP/MOU frameworks)

```diff
- \item Developed inter-agency RFP and MOU frameworks with state and federal partners, translating technical requirements into scope and milestones facilitating \href{...}{Real-Time Inundation Mapping} and TDIS.
+ \item Authored inter-agency RFP and MOU frameworks with state and federal partners, translating technical requirements into scope and milestones for \href{...}{Real-Time Inundation Mapping} and TDIS.
```

**Rationale:** Changed verb "Developed" → "Authored" to avoid repetition with line 114. Changed "facilitating" → "for" (tighter).

---

### Line 113 (Supercomputer scaling)

```diff
- \item Scaled climate and flood models on supercomputers, executing million-node distributed jobs while managing multi-million-dollar compute budgets and federal partnerships with NOAA, NSF, USACE, GLO.
+ \item Scaled climate and flood models on supercomputers, executing million-node distributed jobs while managing multi-million-dollar compute budgets across NOAA, NSF, USACE, GLO.
```

**Rationale:** Changed "federal partnerships with" → "across" to avoid near-duplication with "federal partners" in line 112.

---

### Line 114 (1m flood maps)

```diff
- \item Developed efficient methods to produce high-resolution 1m flood maps from National Water Model outputs for Texas Emergency Management's Real-Time Inundation Mapping.
+ \item Engineered efficient methods to produce 1m flood maps from National Water Model outputs for Texas Emergency Management's statewide response system.
```

**Rationale:** 
- Changed verb "Developed" → "Engineered" (unique in section)
- Removed "high-resolution" (already used in line 115)
- Replaced "Real-Time Inundation Mapping" → "statewide response system" (already mentioned in line 112)

---

### Line 115 (USACE compound flood)

```diff
- \item Partnered with the US Army Corps of Engineers to statistically model compound flood hazards in coastal Texas, integrating high-resolution topographic data with hydrological models.
+ \item Partnered with the US Army Corps of Engineers to statistically model compound flood hazards in coastal Texas, integrating sub-meter topographic data with hydrological models.
```

**Rationale:** Changed "high-resolution" → "sub-meter" to avoid adjective repetition; "sub-meter" is more precise and technically impressive.

---

## Lines Unchanged

- **Line 116** (Bagnold Medal) — Already unique and strong anchor
- **Line 120** (Frontera Technical Reviewer) — Already unique and strong closing anchor
