---
author: "Jua"
org: "Jua"
url: "https://jua.ai/articles/2026-ai-weather-model-benchmarks/"
date: "2026-05-14"
fetch_date: "2026-10-15"
connects_to: "Gabler, Molinaro (Jua)"
why_it_matters: "Vendor-authored benchmark post; useful both as a model of presenting results and as a case where self-benchmarking needs scrutiny."
---

Written by: Olivier Lam, Physical AI Team, Jua.ai AG | Last updated: July 6, 2026

## Key Takeaways for Energy Trading Teams

* WeatherBench 2 measures global structural skill against ERA5, while StationBench measures point-level accuracy against more than 10,000 real surface stations that match how assets earn or lose money.
* EPT-2 leads the 2026 benchmarks, beating ECMWF HRES across all lead times from 0–240 hours on the four energy-critical surface variables and extending the advantage previously shown by EPT-1.5 on European wind and temperature.
* EPT-2e surpasses the 50-member ECMWF ENS mean on both RMSE and CRPS at virtually every lead time, becoming the first productised AI ensemble to outperform the long-standing probabilistic NWP gold standard.
* AI models such as Microsoft Aurora lack SSRD output entirely, which removes them from solar-generation benchmarks, while EPT-2 produces all four energy-critical variables natively at far lower inference cost.
* Energy traders can validate these results in seconds on Jua’s live benchmarking surface and book a demo to see EPT-2 head-to-head against their current provider.

Explore station benchmark results by variable, observed regime, forecast horizon, and country.

## WeatherBench 2 2026 Leaderboard for Energy Variables

The WeatherBench 2 leaderboard now shows EPT-2 as the strongest performer on energy-relevant surface variables. The benchmark tracks deterministic and probabilistic skill across global AI and numerical weather prediction (NWP) models. As of mid-2026, the leading entries on RMSE across upper-air and surface variables include EPT-2, Microsoft Aurora, ECMWF AIFS, and the NWP incumbent ECMWF HRES. EPT-2 outperforms ECMWF HRES on every lead time from 0 to 240 hours on the four energy-critical surface variables. Aurora, a research output from Microsoft's AI lab, loses to EPT-2 on 10 m wind, 100 m wind, and 2 m temperature across the full 0–240 hour range; Aurora has no SSRD output at all, which eliminates it from solar-generation benchmarks by default.

ECMWF AIFS, ECMWF's own machine-learned model, runs on the Jua platform alongside EPT-2 and the NWP incumbents, so energy teams can compare models in a single workspace. DeepMind GraphCast, a graph neural network model initialised on NOAA GFS data, is also available on the platform as a research-output reference. Neither Aurora nor GraphCast ships a productised ensemble equivalent, which limits their utility for probabilistic trading decisions.

Book a demo to compare EPT-2, AIFS, and your current provider side by side.

## StationBench Results on Real Energy Assets

StationBench evaluates EPT-2 against more than 10,000 real ground stations, with no post-processing or station fine-tuning applied. This methodology is deliberately conservative, because models that benefit from station-level calibration would score higher but the comparison would no longer be like-for-like. That stricter standard makes EPT-2's results more significant. On European wind and temperature, EPT-1.5 already outperformed GraphCast, FuXi, Pangu-Weather, and ECMWF HRES; EPT-2 extends that lead. The StationBench methodology is open-source, and the results are published in peer-reviewed technical reports on arXiv, giving meteorologists and procurement teams an auditable basis for evaluation rather than vendor-provided graphics.

Research outputs such as Aurora and GraphCast are not evaluated on StationBench with the same station coverage or energy-variable depth. AirCast-SR, a diffusion-based downscaling model, has demonstrated zero-shot generalisation to German StationBench stations, but it operates as a downscaling layer on top of GraphCast rather than as a standalone global forecast model. Energy teams that care about end-to-end forecast skill need to account for that distinction.

## Probabilistic Benchmarks for AI Weather Ensembles

Probabilistic skill for energy trading depends on CRPS (Continuous Ranked Probability Score, which rewards both accuracy and calibration of ensemble spread) and on ensemble RMSE. EPT-2e, Jua's ensemble variant, beats the 50-member ECMWF ENS mean on both RMSE and CRPS at virtually every lead time. ECMWF ENS has been the gold standard for probabilistic NWP for decades, so EPT-2e surpassing it on these metrics is the most operationally significant result in the 2025–2026 benchmark cycle.

ECMWF has responded to the AI challenge with its own machine-learned ensemble. ECMWF's AIFS-CRPS ensemble, trained with an almost-fair CRPS loss, outperforms the operational IFS ensemble on CRPS for the majority of upper-air variables at medium range. This is a meaningful result for the NWP community, but AIFS-CRPS is not yet a productised platform with an operational refresh schedule, an agent layer, or a benchmarking surface. It runs on the Jua platform as a reference model.

No AI peer, including Aurora, GraphCast, or AIFS in its current productised form, ships an ensemble that has been benchmarked against ECMWF ENS on CRPS at the variable depth and lead-time range that EPT-2e covers.

## Extreme-Event Accuracy for Energy P&L

Extreme-event accuracy determines whether a forecast model can be trusted during tail events that drive most energy trading P&L, such as price spikes during heat waves, wind droughts, or cold snaps. This benchmark category is where AI weather models have historically faced the most scrutiny. A 2024 Science Advances study found that GraphCast, Pangu-Weather, and FuXi systematically underestimated the frequency and intensity of record-breaking heat, cold, and wind events relative to ERA5, while ECMWF HRES produced record counts comparable to its own analysis. Forecast errors in those AI models increased nearly linearly with the magnitude of record exceedance, which compounds bias at the tails most relevant to energy risk.

More recent work shows that the picture is evolving. When AI weather models are evaluated with threshold-weighted potential CRPS on WeatherBench 2, FuXi, GraphCast, and Pangu-Weather can produce informative forecasts for extreme-event exceedances. The key qualifier is “potential” CRPS, which measures the upper bound of accuracy achievable with post-processing rather than the out-of-the-box operational skill. EPT-2's physics-constrained architecture, trained on observational data with conservation laws embedded at the representation level, is designed to reduce the systematic underestimation bias that earlier AI models exhibited on record-breaking events.

## Energy Weather Forecast Benchmarks at a Glance

The table below highlights a consistent pattern for energy teams: EPT-2 and EPT-2e outperform ECMWF HRES and ECMWF ENS across all four energy-critical variables, while key AI peers either lose on multiple variables or lack SSRD entirely. The table summarises deterministic RMSE and probabilistic CRPS performance for the four variables that drive energy P&L across the models most relevant to energy trading teams. EPT-2 and EPT-2e are productised platform models available through Jua for Energy. Aurora and GraphCast are research outputs available on the Jua platform as reference models. All numeric claims are sourced from the EPT-2 technical report and the EPT-1.5 technical report on arXiv.

Aurora's absence of any SSRD output creates a structural gap for solar-generation forecasting. A model that cannot produce surface solar radiation cannot serve as a primary forecast source for solar asset operators or solar-weighted power traders, regardless of its wind or temperature skill.

## Ensemble Skill for EPT-2e versus ECMWF ENS

EPT-2e beats the 50-member ECMWF ENS mean on RMSE and CRPS at virtually every lead time. ECMWF ENS has been the probabilistic gold standard for NWP for over two decades. This result is operationally significant, because energy traders who use ensemble spread to size positions, set stop-loss thresholds, or price weather derivatives now have a productised AI ensemble that outperforms the incumbent on the two metrics that matter most for probabilistic decision-making.

EPT-2e updates 4 times per day, with an ensemble horizon that extends to 60 days and covers the subseasonal range where gas storage and hydro-dispatch decisions are made. No AI peer, including Aurora, GraphCast, or AIFS in its current productised form, ships an ensemble with comparable benchmark documentation or operational refresh schedule.

Book a demo to see EPT-2e ensemble skill on your region and variables.

## Update Frequency and Inference Cost for Trading Use

EPT-2's cost and speed profile unlocks refresh rates that traditional NWP cannot match. Update frequency is a structural constraint in traditional NWP. A single ECMWF HRES simulation consumes approximately 8,400 kWh and costs €1,000–€20,000 to run on HPC infrastructure, which caps the operational schedule at 2–4 runs per day. EPT-2 runs on a single GPU in minutes, at approximately 0.25 kWh and $0.20–$15 per simulation, which is roughly four orders of magnitude cheaper at inference time. EPT-2 was trained on 8 × H100 GPUs over 10 days, while Microsoft Aurora required 32 × A100 GPUs over 18 days.

This cost asymmetry enables a fundamentally different operational cadence. EPT-2 RR (rapid refresh) updates up to 24 times per day. EPT-2 HRRR delivers the same hourly cadence at up to 5 km native resolution over Europe. A typical Jua run completes approximately 2.5 hours ahead of competing operational runs at the same cycle, which gives Jua for Energy customers access to the next forecast before the market re-prices on it. EPT-2 is also approximately 25% faster at inference than Microsoft Aurora.

## Benchmark Methodology for WeatherBench 2 and StationBench

All EPT-2 benchmark results cited in this article are drawn from the EPT-2 technical report (arXiv:2507.09703) and the EPT-1.5 technical report (arXiv:2410.15076). StationBench evaluation uses more than 10,000 real surface stations with no post-processing or station fine-tuning applied to any model. WeatherBench 2 evaluation uses ERA5 reanalysis as ground truth on a global grid. RMSE (root-mean-square error, lower is better) and CRPS (Continuous Ranked Probability Score, lower is better and rewards both accuracy and calibration) are the primary metrics. Lead time refers to the number of hours ahead of the forecast initialisation time. Ensemble mean RMSE and CRPS are computed against the same station and grid references as the deterministic models, which enables direct comparison between EPT-2e and ECMWF ENS.

Aurora and GraphCast are classified as research outputs throughout this article because neither ships a productised operational refresh schedule, a benchmarked ensemble, or a workflow layer equivalent to Jua for Energy. Both run on the Jua platform as reference models under a unified API schema.

## Run Your Own Benchmarks on Jua

The benchmark numbers above are reproducible on demand, and energy teams can verify them directly. Jua for Energy's live benchmarking surface puts more than 25 models on a single platform, including 10 proprietary AI models from the EPT family plus 15 third-party NWP and AI models such as ECMWF HRES, ECMWF ENS, ECMWF AIFS, NOAA GFS, Microsoft Aurora, and DeepMind GraphCast. Users select any region, any variable, and any time window, and a head-to-head accuracy comparison returns in seconds. Jua serves major utilities, commodity traders, and hedge funds across four continents, and the live benchmark is consistently the deal trigger, because meteorologists who were sceptical of vendor accuracy claims often become internal champions once they run the numbers themselves.

A 1 GW wind portfolio that gains four percentage points of forecast accuracy saves approximately €1.5 M per year under typical hedging and imbalance structures. A 1 GW solar portfolio at the same accuracy gain saves approximately €3 M per year. The benchmark takes about five minutes, and the economics scale linearly with portfolio size.

Run benchmarks on your own region using Jua's live platform.

## Frequently Asked Questions

### What is the difference between WeatherBench 2 and StationBench for energy applications?

WeatherBench 2 evaluates AI weather models against ERA5 reanalysis data on a global grid. ERA5 is a high-quality historical reconstruction of the atmosphere, but it is a smoothed gridded product rather than a direct observation. For energy applications, where forecast accuracy at a specific wind farm, solar plant, or load zone determines P&L, grid-level scores can overstate real-world performance. StationBench addresses this by scoring models directly against more than 10,000 real surface stations, with no post-processing or station fine-tuning applied to any model. The result is a stricter, more operationally relevant test. Energy traders, meteorologists at regulated utilities, and quant developers evaluating forecast providers should require StationBench scores on the energy-critical variables, including 10 m wind, 100 m wind, 2 m temperature, and surface solar radiation, before making procurement decisions. WeatherBench 2 remains valuable for assessing global structural skill and upper-air performance, while StationBench is the closer proxy for what a model will actually deliver at a physical asset.

### How does EPT-2e compare to ECMWF ENS for probabilistic energy trading?

EPT-2e is Jua's ensemble variant of the EPT-2 foundation model and outperforms ECMWF ENS on both RMSE and CRPS across the full lead-time range, as detailed in the benchmark sections above. ECMWF ENS has been the gold standard for probabilistic NWP for over two decades, so this result is the most operationally significant in the current benchmark cycle. For energy trading, probabilistic forecasts are used to size positions, set risk thresholds, price weather derivatives, and manage imbalance exposure. A model that outperforms ECMWF ENS on CRPS, the metric that rewards both accuracy and calibration of ensemble spread, gives traders a more reliable basis for those decisions. EPT-2e runs 4 times per day, with an ensemble horizon extending to 60 days, which covers the subseasonal range relevant to gas storage and hydro-dispatch planning. No AI peer currently ships a productised ensemble with comparable benchmark documentation or operational refresh schedule.

### Why does Aurora's lack of surface solar radiation output matter for energy benchmarks?

Surface solar radiation (SSRD) is the primary driver of solar power generation, which now represents a substantial and growing share of installed capacity across European and North American power markets. A model without SSRD output cannot serve as a primary forecast source for solar asset operators, solar-weighted power traders, or any team managing a mixed renewable portfolio where solar and wind interact in the residual load. Microsoft Aurora has no SSRD output. This gap eliminates Aurora from the benchmark comparison on one of the four energy-critical variables entirely, and it means any energy team relying on Aurora for solar forecasting must source that variable from a separate model, which reintroduces the pipeline fragmentation that a productised platform is designed to remove. EPT-2 produces SSRD natively and outperforms ECMWF HRES on this variable across the full 0–240 hour lead-time range.

### What does Jua mean when it describes EPT-2 as a foundation model rather than a weather model?

Jua is a foundation model and agent company. EPT, the Earth Physics Transformer, is a general spatiotemporal transformer foundation model that learns the governing physics of complex systems directly from observational data. The architecture is domain-agnostic, and what changes from one physical system to the next is the data and the fine-tune. The atmosphere is the first physical system EPT has been fine-tuned for, and energy trading is the first market where Athena, Jua's AI agent, has been instrumented. The relationship mirrors the one Anthropic has to Claude Code, a horizontal AI platform with a flagship vertical product. Describing EPT as a weather model would be like describing Anthropic as a coding company. For energy buyers, the practical implication is that they are not purchasing a point-solution weather feed; they are accessing the first applied product of a foundation-model and agent platform that will expand into other physical-economy domains. The same architecture that predicts atmospheric dynamics already predicts plasma behaviour inside a tokamak.

### How quickly can an energy team run a benchmark on their own region and variables?

The live benchmarking surface on the Jua platform returns a head-to-head accuracy comparison in seconds after a region and variable are selected. A full backtest against years of historical forecasts runs in approximately five minutes via Athena, Jua's AI agent. The platform puts more than 25 models on a single surface, including 10 proprietary AI models from the EPT family plus 15 third-party NWP and AI models such as ECMWF HRES, ECMWF ENS, ECMWF AIFS, NOAA GFS, Microsoft Aurora, and DeepMind GraphCast, all under a unified API schema. A meteorologist evaluating Jua for Energy during procurement can run the benchmark on the company's most stakes-relevant region and variable, compare EPT-2 against their current provider, and bring a defensible, peer-reviewed accuracy comparison to their trading desk and procurement team before the end of a single working session. The benchmark is available at athena.jua.ai without a sales call.
