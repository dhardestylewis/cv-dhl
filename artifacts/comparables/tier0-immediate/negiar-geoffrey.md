---
name: Geoffrey Négiar
title: Co-founder and CEO
org: The Forecasting Company (YC S24, Paris)
tier: 0 (immediate; PROTECTED org per outreach rules, research only, no contact)
urls fetched:
  - https://www.theforecastingcompany.com/company/
  - https://www.theforecastingcompany.com/
  - https://www.theforecastingcompany.com/blog/t0-gamma/
  - https://vivatech.com/speakers/geoffrey-negiar-the-forecasting-company-ac89d3ea-5f5b-f111-8fcb-6045bd954326
  - https://www.thegeniuslist.com/interview/geoffrey-negiar/
  - https://www.ycombinator.com/companies/the-forecasting-company/jobs
  - https://arxiv.org/abs/2609.24559
  - search result only (not fetched): scholar.google.ca citations uDo9RIEAAAAJ (Google Scholar is rate-limited; LinkedIn not fetched by policy)
fetch date: 2026-10-15
why comparable: Closest peer on the exact axis Daniel is screened on: a founder who ships an open-weights forecasting foundation model on public data and is benchmarked in public (GIFT-Eval, fev-bench, TIME). Energy (grid load, ERCOT prices) is a named use case. He is the person most likely to read Daniel's backtestable-forecast claims critically.
---

# Profile (company page, VivaTech bio, interview)

Company bio (theforecastingcompany.com/company): "Forecasting systems at Amazon and Bloomberg; ML research at Google Brain. PhD, UC Berkeley (BAIR)."

VivaTech speaker bio: cofounder and CEO of The Forecasting Company (YC S24). The company builds foundation models for time-series data and systems for temporal data, to improve planning for large organizations. Previously built forecasting systems at Amazon.com, Bloomberg LP and Shift Technology; machine learning research at Google Brain. PhD UC Berkeley BAIR; MS Ecole Normale Superieure; engineering degree Ecole polytechnique. Martial arts for 25+ years.

Interview (The Genius List, undated, written while he was a PhD student): PhD advisor Laurent El Ghaoui, research on robust optimization for ML under data uncertainty; MVA master's at ENS Paris-Saclay; Ecole polytechnique (ingenieur polytechnicien); interned at Bloomberg LP, Shift Technology, SumUp Analytics, Google Research; member of the French Armament Corps. Stated early interest in urban planning (public transport, walkable cities) as a driver toward applied ML.

# Roles (dates only where a source gave them)
- Co-founder and CEO, The Forecasting Company, 2024 to present (YC S24; Paris; 7 employees per YC page)
- Forecasting systems: Amazon.com, Bloomberg LP, Shift Technology (dates not fetched; UNVERIFIED)
- ML research: Google Brain / Google Research (internship during PhD)
- PhD EECS UC Berkeley (BAIR), 2017 to 2023 (from search snippet of his profile; not fetched)

# Named artifacts
- t0 family of open-weights time-series foundation models (Apache 2.0 per his post snippet): t0-alpha (102M params), t0-beta (256M), t0-gamma (released 2026-10-13).
- Tech report: "t_0: A Time-Series Foundation Model for Forecasting with Context", arXiv 2609.24559, submitted 2026-09-21, first author Lucas Meyer plus 7 others (39 pages). Pretraining: curated public data plus synthetic generator families with covariate-to-target dependencies. Conditions on target history, past covariates and known-future covariates; alternating attention along time and across variates; quantile outputs.
- Reported results: GIFT-Eval t0-beta CRPS 0.4738, MASE 0.6865; fev-bench t0-beta skill 46.7. t0-gamma (company blog, 2026-10-13): fev-bench skill 49.42 and 91.6% win rate, GIFT-Eval CRPS 0.4520 / MASE 0.6608, TIME CRPS 0.5340 / MASE 0.6370, first among single zero-shot TSFMs at release. These are the company's own claims; the blog notes agents and fine-tuned systems excluded.
- Independent evaluation cited in the report: Macrocosm, hourly ERCOT prices over 29 months, both t0 models cut MAE of the lagged-price baseline by 38%.
- Open-source library tfc-t0 (PyPI), Retrocast API (backtest and forecast your own series, "up to 200,000 forecasts a second").
- Talk: VivaTech, "Forecast anything, with world context, in seconds: Announcing t_0, an open-weights foundation model for time-series" (Future of Industries Arena, June 18; year not stated on page).
- Customers/users named on site: Engie, Netflix, Shake Shack, MIT, OpenAI ("playing with t0").

# Skills and tools evidenced
Time-series foundation models, probabilistic forecasting (CRPS, quantile), benchmark-driven release (GIFT-Eval, fev-bench, TIME), robust optimization, production forecasting at Amazon and Bloomberg, Hugging Face and PyPI releases.

# Hiring signal
YC job: Founding Machine Learning Engineer, Paris, EUR 80k to 130k, 0.5% to 2.0% equity, 3+ years. Company page asks for people who "have gone unusually deep somewhere": built ambitious systems, excellent research, widely used tools.

# Notes for Daniel
- Protected organization: do not contact. This file is research only.
- Compare: Daniel's claim set (backtestable against published forecasts, real public data) maps onto TFC's public-leaderboard posture; expect questions on leakage and benchmark hygiene.
