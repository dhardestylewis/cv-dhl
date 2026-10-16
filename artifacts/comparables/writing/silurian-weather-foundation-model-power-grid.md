---
author: "Silurian AI with Hydro-Quebec"
org: "Silurian"
url: "https://arxiv.org/html/2509.25268v1"
date: "2025-09-28"
fetch_date: "2026-10-15"
connects_to: "Gupta, Shankar (Silurian)"
why_it_matters: "Fine-tuning a 1.5B weather foundation model on utility asset data; shows how domain-specific evaluation against operator needs is reported."
---

# A Weather Foundation Model for the Power Grid

###### Abstract

Weather foundation models (WFMs) have recently set new benchmarks in global forecast skill, yet their concrete value for the weather-sensitive infrastructure that powers modern society remains largely unexplored. In this study, we fine-tune Silurian AI’s 1.5B-parameter WFM, Generative Forecasting Transformer (GFT), on a rich archive of Hydro-Québec asset observations - including transmission-line weather stations, wind-farm met-mast streams, and icing sensors - to deliver hyper-local, asset-level forecasts for five grid-critical variables: surface temperature, precipitation, hub-height wind speed, wind-turbine icing risk, and rime-ice accretion on overhead conductors. Across 6–72 h lead times, the tailored model surpasses state-of-the-art NWP benchmarks, trimming temperature mean absolute error (MAE) by , total-precipitation MAE by , and lowering wind speed MAE by . Most importantly, it attains an average precision score of 0.72 for day-ahead rime-ice detection, a capability absent from existing operational systems, which affords several hours of actionable warning for potentially catastrophic outage events. These results show that WFMs, when post-trained with small amounts of high-fidelity utility data, can serve as a practical foundation for next-generation grid-resilience intelligence.

A Weather Foundation Model for the Power Grid

Cristian Bodnar1,
Raphaël Rousseau-Rizzi2,
Nikhil Shankar1, James Merleau2,
  
Stylianos Flampouris1, Guillem Candille2, Slavica Antic2,
  
François Miralles2,
Jayesh K. Gupta∗,1

1Silurian AI          2Hydro-Québec

∗corresponding author: jayesh@silurian.ai

## 1 Introduction

Modern electricity networks are becoming markedly more weather sensitive. Rapid penetration of wind and solar introduces variability that is tightly coupled to mesoscale meteorology, while ageing transmission and distribution grids face mounting exposure to storms, icing, and heatwaves. Grid operators must now balance supply and demand in real time in ever more reactive way, safeguard assets against extreme events, and plan maintenance in a climate where “once-in-a-century” conditions recur with unsettling frequency. At the same time, the decarbonization of the economy increases social vulnerability to power outages, enhancing the need for reliability. Traditional numerical weather prediction (NWP) feeds remain indispensable, yet their spatial granularity (often 3 km) limits their usefulness for hyper-local, asset-level decisions such as dynamic line rating (IEEE Power and Energy Society, 2013), de-icing crew dispatch, or curtailment of turbine fleets in icing conditions.

Addressing these granular, asset-level challenges requires a new forecasting paradigm, one offered by recent advances in the world of large scale machine learning. The foundation-model paradigm of pretraining large transformers on petabyte-scale data, followed by fine-tuning for downstream tasks, has found great success across a variety of disciplines (Bommasani et al., 2021; Brown et al., 2020; OpenAI, 2023; Radford et al., 2021; Kirillov et al., 2023; Jumper et al., 2021; Rives et al., 2021; Wang et al., 2023). Weather foundation models (WFMs) apply this paradigm to the task of atmospheric prediction, leveraging vast reanalysis, satellite, and other climate data archives. By learning flow-consistent latent representations across lead times and scales, WFMs have surpassed operational NWP in global skill metrics while offering quick inference on commodity GPUs. Crucially, their parameter sharing and attention mechanisms allow regional adaptation with orders-of-magnitude fewer labelled samples than would be required to train a model from scratch.

While the AI weather models now match or surpass traditional operational NWP models for conventional forecasting tasks at broad, continent-spanning scales Bodnar et al. (2025); Chantry et al. (2025); Lam et al. (2023); Bi et al. (2023); Pathak et al. (2022); Chen et al. (2023), this work demonstrates a pivotal new capability brought about by WFM’s regional adaptation capabilities: forecast products tailored to user needs: both flexibly and rapidly. This is a difficult endeavor using existing NWP models. This makes WFM technology invaluable for utility companies since the grid isn’t much impacted by “averaged” and generic weather variables, but rather by the ways the weather interact with assets right here, right now: on this ridge, over these wind turbines, along this particular stretch of transmission line. More precisely, grid operation requires forecasts that can meet three challenging requirements at once:

* •

  Hyper-locality: The forecast is sensitive enough to capture kilometer-scale pecularities like terrain, land-use, and other environmental factors in the vicinity.
* •

  Specificity: Highly task-specific variables such as thermal ratings, renewable output, and icing risk can be forecast.
* •

  Actionability: The forecast is timely, clear and expressed in terms that facilitate real-time decision making by grid operators (e.g., probability to exceed a critical threshold along with information on the false alarm rate).

WFMs are uniquely suited to meet these challenges, yet their potential remains largely untapped. This is not due to a failure of the technology, but rather a gap in awareness and a lack of established pathways for integrating their highly specific data into grid operations. This work aims to bridge this gap, showcasing how WFM technology can empower operators and build a more resilient energy infrastructure.

To illustrate WFM capabilities for the grid, in this paper we adapt Silurian’s 1.5-billion-parameter WFM, Generative Forecasting Transformer (GFT) to Hydro-Québec’s asset network, producing hyper-local hourly forecasts for five grid-critical variables: surface temperature, accumulated precipitation, hub-height wind speed, wind-turbine icing risk, and rime-ice accretion on overhead conductors. Against state-of-the-art NWP baselines over 1–72 h horizons, the fine-tuned model

1. 1.

   Lowers temperature MAE by 15%,
2. 2.

   Reduces total-precipitation MAE by 35%,
3. 3.

   Reduces wind speed MAE by 15%, and
4. 4.

   Achieves an unprecedented 0.72 average precision for day-ahead rime-ice detection, providing several additional hours of warning compared to existing process.

These gains translate into tangible operational benefits: earlier de-icing interventions, more reliable dynamic line ratings, and improved renewable dispatch (see Section A.3). The study thus demonstrates that WFMs, when enriched with utility-grade observations, can become a cornerstone of next-generation grid-resilience intelligence.

## 2 A Weather FM for the Grid

##### Weather Foundation Models.

Recent foundation-model efforts such as ClimaX (Nguyen et al., 2023) and Aurora (Bodnar et al., 2025) have established that a single transformer-based backbone, pre-trained on heterogeneous climate data archives, can surpass global numerical weather prediction (NWP) skill. They also demonstrate how these models can be efficiently adapted for a wide variety of tasks in this space, ranging from wave modeling and air-pollution forecasting to regional downscaling. An overview of our WFM setup for grid applications is shown in Figure 1. In this work, we show how Silurian’s foundation model, the Generative Forecasting Transformer (GFT), inheriting the same principles, can be adapted for a variety of energy infrastructure use cases that demand hyperlocal spatial detail and complex weather risk assessments.

##### Architecture Overview.

The model follows the general encoder–backbone–decoder paradigm (Figure 1). The encoder ingests operational weather inputs such as gridded and sparse observations and maps them into a latent representation. The backbone consists of a large transformer that acts as a neural simulator of the latent representation. Finally, the decoder translates the evolved latent representations into physical predictions. The GFT decoder contains two modules: a “dense” decoder and a “sparse” hyperlocal decoder. The dense decoder produces gridded outputs on a predefined coordinate grid, while the sparse decoder produces forecasts at a specific set of query latitude–longitude locations.

##### Pretraining and Post-training.

The model is pretrained on a petabyte-scale dataset consisting of a mix of public and private data, with dense/gridded observations forming the bulk of this dataset. The general recipe is similar to the approach given in Bodnar et al. (2025). After pretraining on this large dataset, we post-train the model on a much smaller set of hyperlocal observations from sensors across the Hydro-Québec grid infrastructure.

##### Post-training versus post-processing.

Utilities typically adapt fixed NWP guidance with Model Output Statistics, ensemble calibration, or site-specific regressors that operate one variable and one location at a time. Because the upstream flow solution never changes, these post-processing pipelines struggle to maintain multivariate consistency, cannot introduce new targets absent from the NWP feed, and scale poorly as the asset portfolio grows. Our post-training updates the core WFM weights so that a single backbone jointly forecasts temperature, wind, precipitation, and icing. The shared latent state enforces cross-variable coherence, enables the model to learn novel heads such as rime-ice probability directly from observations, and eliminates the need to maintain dozens of bespoke statistical correctors.

##### Hydro-Québec post-training setup.

At inference time, the encoder ingests ECMWF-IFS analysis fields (ECMWF, 2021) and the sparse Hydro-Québec asset observations collected at the cycle issue time. The decoder is trained to produce five operational targets in one forward pass: 2 m temperature, hourly precipitation, hub-height wind speed, wind-farm icing probability, and rime-ice probability on transmission lines. We fine-tune on 2016–2023 observations and hold out January 2024–March 2025 for evaluation, balancing regression losses for the continuous variables with probabilistic classification losses for the icing heads. Unless noted otherwise, utility streams provide supervision only; they are not assimilated online.

## 3 Hyperlocal forecasting for grid operations

To demonstrate the flexibility of the foundation-model paradigm, we post-train GFT into GFT-HQ, on three important environmental tasks that have a significant impact on grid operations: (1) rime-ice forecasting for transmission lines, (2) wind-farm wind and icing forecasting, and (3) temperature and precipitation forecasting.

Figure 2 illustrates Hydro-Québec’s existing high-voltage network and corridors under study for future expansion, compiled from public planning materials and reports (Hydro-Québec, 2023a; Hydro-Québec, 2023b; Hydro-Québec, 2024; Hydro-Québec, 2025). These large-scale buildouts and prospective wind additions motivate asset-level forecasts that are fast, location-specific, and actionable.

There are two ways hyperlocal WFM forecast products can improve grid operations. The first is to improve the skill of forecast products already in use within the utility, while retaining a similar format and role in existing operational processes. This is the case for the temperature, precipitation, and wind forecasts in the present study. The second is to meet an operational need that is not currently addressed by existing structured process in the utility, as is the case for ahead-of-time transmission-line and wind-farm rime-ice forecasts. The effort required to integrate each product–and the benefits to the utility–differ considerably between these two types. Contributions of the first type are relatively easy to integrate into the value chain, and their benefit is determined by the improvement over available forecast products. Contributions of the second type are harder to integrate because, by definition, they require the creation of new activities within the company. The potential benefit of WFMs is much greater here, as it also comes from a qualitative change to the value chain - such as being able to pre-emptively deploy an operational team to de-ice lines ahead of the start of an event.

##### Evaluation protocol.

Continuous targets (temperature, wind, precipitation) are scored with mean absolute error (MAE) and reported as fractional skill relative to ECMWF-IFS (ECMWF, 2021). Rare-event targets (icing) are assessed with precision, recall, F1, and average precision (PR-AUC), with lift computed against the relevant base rates: 3.7% for transmission-line rime ice and 13% for wind-farm icing. To reflect operational decision windows, we aggregate hourly probabilities into a 24 h “any icing” probability alongside the hour-by-hour scores. ROC-AUC is provided for completeness but we emphasize PR metrics because they better reflect the cost of false dispatches in low-base-rate regimes.

### 3.1 Rime ice forecasting for transmission lines

Rime ice is formed when super-cooled water droplets freeze instantly upon contact with a sub-zero surface. It accumulates rapidly under fog, low-level cloud, and mountainous or coastal weather systems and poses a persistent reliability threat to overhead transmission lines. The ice accretion alters both the geometric and electrical characteristics of conductors: it increases effective diameter and surface roughness, thereby magnifying wind drag, modifying corona onset voltage, and adding eccentric mechanical loading. These translate into elevated risk of conductor clashing, flashovers, structural member fatigue, and ultimately line outages.

Despite the many operational headaches it causes, utilities lack reliable forecasting systems for rime ice. The gap traces chiefly to numerical weather prediction models: their kilometre-scale grids smooth out the shallow fog banks and ridge-top cloud filaments where rime forms, and their bulk microphysics schemes convert supercooled droplets to ice far too quickly, systematically erasing the liquid-water signal that drives accretion. With neither high-resolution physics nor a corridor-wide network of icing masts to assimilate or validate supercooled liquid water, model output remains both biased and unverifiable, leaving operators without a trustworthy baseline on which to build operational alerts.

##### Data

For this task, we post-train GFT on hourly data collected from 14 high-elevation Sygivre rime-ice stations from Hydro-Québec’s 40-station network; each measures ice-accretion cycles plus standard meteorological variables. See Section A.2 for details.

We convert the cumulative ice-accretion counts into a binary variable indicating the presence of rime ice within the last hour. In the resulting data, rime-ice events represent just of total hours, underscoring the rarity of this phenomenon and the challenge it poses for any AI-based detection system. We train on 2016-2023 and validate on January 2024 to May 2025.

##### Operational decision model

Dispatching de-icing crews carries a fixed cost , while a missed icing event incurs a loss that can be partially avoided if action succeeds with effectiveness . Using a standard cost–loss analysis, we trigger action whenever the forecast probability exceeds

|  |
| --- |
| (1) |

For windowed “any icing in the next 24 h” alerts we map hourly probabilities to and apply the same rule, with hysteresis and watch/dispatch tiers to avoid thrashing in operations. This framing connects forecast quality directly to avoided outage risk and underpins the value analysis in Section A.3.

##### Baselines

In addition to climatology, we compare against an ERA5-derived Makkonen index that interpolates reanalysis temperature, dewpoint, winds, and liquid-water content to each site and evaluates a physical icing proxy (Hersbach et al., 2020). Because this proxy is generated from retrospective reanalysis rather than a true forecast, it serves as a strong physics-based reference rather than an operational baseline.

##### Results

Pinpointing the exact hour of icing is difficult, and hourly skill reflects this: GFT-HQ’s F1 scores are typically in the 0.40–0.45 range during the first 24 h; see Appendix Figure 14(a). Because operations often act on multi-hour windows, we also evaluate a 6-hour “any icing in window” target, which smooths timing errors and yields higher, more stable skill across lead times; see Appendix Figure 14(b). In both settings, GFT-HQ provides the best performance and is comparable to or better than the ERA5-derived Makkonen reference out to 72 h. As can be seen in Figure 3, GFT-HQ also detects the approximate icing period well. For instance, when forecasting whether any icing will occur over the next 24 h at the 14 locations of interest, GFT-HQ attains average precision AP ( lift over base rate), outperforming an ERA5-derived Makkonen index (AP ; lift) and climatology (AP ; lift). Note that Makkonen† is computed from ERA5 reanalysis fields (see Section A.1.4; ERA5 described in Hersbach et al., 2020), so it is closer to observations than to a true forecast; we include it as a strong physics-based reference rather than an operational baseline. GFT-HQ exceeds this reference by relative AP (0.72 vs 0.53). Across 14 sites, station-level F1 scores are consistently higher for GFT-HQ, indicating improvements at the median and in the worst-case stations, not just at a few outliers.

##### Case study

Beyond aggregate skill, the finetuned model captured individual high-impact episodes that posed particular challenges for Hydro-Québec’s operations. A prime example is the collapse of a transmission line from the Romaine hydro centre around November 19, 2024 due to rime ice (Gerbet, 2024). Figure 4 compares two nearby Sygivre stations (ERIC\_C and MONTAG\_C) separated by only 11 km using a Hovmöller-style view: rows are successive 6-hourly forecast initializations, columns are valid hours, colours show the forecast probability of 1-h rime ice, and the black strip below indicates the observed binary icing. At ERIC\_C, a coherent high-probability swath is already present by 16 Nov and persists across cycles, peaking on 18–19 Nov when the longest observed episode occurs; subsequent bursts on 20–24 Nov are also captured. At MONTAG\_C, icing was shorter and more intermittent, and the model response is correspondingly weaker - probabilities remain low most of the time with brief increases around 16–19 Nov. Despite their proximity, these stations exhibit markedly different behaviour, underscoring sharp micro-scale variability along the corridor; nevertheless the corridor-scale risk around 18–19 Nov was visible 1–3 days in advance, providing actionable lead time for grid operations.

##### Initialization and inputs

Unless otherwise stated, the case-study forecasts are produced by 6-hourly GFT-HQ cycles (issue times 00, 06, 12, 18 UTC). For each cycle, the encoder is conditioned on dense ECMWF-IFS Analysis fields (ECMWF, 2021) (0 h analyses) at the issue time - including multi-level temperature, humidity, and winds; surface pressure and near-surface fields; cloud liquid-water proxies; static orography and land–sea mask; and time encodings. These fields provide the initial conditions from which the backbone evolves the latent state forward in time. Hydro-Québec asset streams (Sygivre icing stations and wind-farm masts) are used for post-training supervision; unless explicitly noted, they are not assimilated at runtime during inference. The traces in Figure 4 therefore reflect differences solely from the changing synoptic initial state between successive 6-hourly initializations.

### 3.2 Wind-farm wind speed and ice forecasting

For utilities reliable forecasts of turbine-level icing and hub-height wind speed are mission-critical because they dictate how much variable generation will actually reach the grid, how much spinning reserve must be scheduled, and whether transmission lines risk overloads or voltage excursions when production suddenly collapses. An unexpected icing episode can slash a wind-plant’s output by tens of megawatts within minutes, while excessive winds force cut-out shutdowns; both events create sharp ramps that the utility must offset with fast-responding thermal units, battery assets, or market purchases, often at premium prices. Day-ahead and intraday visibility into these weather-driven outages therefore underpins accurate load-generation balancing, congestion management, and reliable commitment of ancillary services, ultimately lowering imbalance penalties and safeguarding system stability.

##### Data

As the grid operator, Hydro-Québec does not have direct measurements of icing on wind-turbine blades. Instead, this label is inferred from substantial power-production declines observed at a wind farm given the measured wind speed and direction. The wind speed measurements come from met masts placed next to the wind farms such that potential wake effects are negligible. As before, we fine-tune the model on data from 2016–2023 and test on data from January 2024 to January 2025.

We use 65 meteorological masts near wind farms across Québec (10-minute data, multiple heights) and infer hourly wind-farm icing from production losses relative to potential output given the meteorological conditions. See Section A.2 for details.

##### Results

Across the held-out period , the finetuned model (GFT-HQ) delivers strong and geographically consistent skill on both the drivers (hub-height wind) and the impact target (wind-farm icing).

Icing risk At a base rate of 13%, GFT-HQ attains AP (lift over random), for detecting whether any icing will occur in the next 24 h, exceeding both Climatology (AP ) and an ERA5-derived Makkonen index (AP ). Evaluated strictly at 24 h lead time, GFT-HQ again leads (AP = 0.73) versus Climatology (AP=), and Makkonen (AP ). Corresponding ROC performance is high as well (AUC = 0.93 vs 0.86–0.87 (Climatology) and 0.59–0.71 (Makkonen) in the two setups). Note. The Makkonen curve is computed from ERA5 reanalysis (see Section A.1.4) and is included as a strong physics-based reference, not an operational forecast baseline. Performance here is often worse than Climatology partially because icing is not directly measured at wind-farms, rather inferred from loss in power production and could include other factors as well.

Wind-speed skill Finetuning materially reduces hub-height wind MAE across 0–72 h relative to untuned GFT and ECMWF-IFS, with the majority of sites showing lower error than IFS at each lead time. Gains persist and are most pronounced during evening hours (18–23 EST/EDT), which are operationally critical for peak load.

Lead-time averages remain high. Icing F1 stays above 0.6 through 60 h and ROC-AUC remains above 0.9 (plots in Section A.5.2) - while the diurnal slices in Figure 8 illustrate how GFT-HQ damps the errors compared to both baselines. Seasonal panels are provided in Section A.5.2; the evening/night margins are the largest, aligning with Hydro-Québec’s highest-risk periods.

Performance under high-icing conditions. As can be seen in Figure 6, conditioned on hours flagged as high icing risk, GFT-HQ keeps the wind-speed accuracy edge and is the only model with consistently non-zero skill for turbine cut-out events (m/s). Its CSI shows frequent high-skill episodes, whereas both GFT and ECMWF-IFS are near zero.

##### Case study

To illustrate how the system presents actionable guidance to operators, Figure 9 shows a mid-winter icing episode at a representative Hydro-Québec wind farm (site code “AVA”). The Hovmöller-style plot stacks successive 6-hourly forecasts by initialization time (y-axis) against their valid hours (x-axis); colours denote the GFT-HQ probability of 1-h turbine icing, while the black strip beneath marks the observed binary icing derived from production losses. A coherent high-probability swath emerges and stabilizes 2–3 days before the prolonged mid-to-late January event, and shorter early-month bursts are also indicated. The cross-cycle persistence of this signal provides dependable early warning for curtailment planning and reserve scheduling.

### 3.3 Temperature and precipitation forecasting

Accurate temperature and precipitation forecasts sit at the heart of utility planning because they govern every major balance-sheet variable: demand, supply, and asset risk. Temperature is the dominant driver of electric load - hot spells boost air-conditioning demand, cold snaps spike heating and resistive losses - so even a 1 °C error can translate into hundreds of megawatts of forecasting miss and costly imbalance charges. Precipitation matters just as much: rain, snow, or ice determine hydro-reservoir inflows, solar panel soiling, wind-turbine icing shutdowns, and outage probabilities from lightning or tree-fall. By anticipating these weather-dependent swings, a utility can commit generation and reserves economically, schedule maintenance when both load and storm risk are low, pre-stage crews and mobile transformers ahead of severe weather, and optimise fuel and emissions strategies. In short, precise temperature and precipitation outlooks convert meteorological uncertainty into actionable lead time, protecting reliability while trimming operating costs.

##### Spatial footprint of gains.

Station-wise skill patterns (Section A.5.3) show that post-training amplifies rather than redistributes the model’s strengths: GFT-HQ inherits the spatial structure of the untuned GFT but pushes most stations into the positive-skill regime by 24–48 h. Figure 10 highlights the expanded positive-skill footprint for both temperature and precipitation. The broad coverage means load-forecast errors decline system-wide instead of concentrating at a few sites, and precipitation improvements propagate across the river basins that drive Hydro-Québec’s reservoir operations. Diurnal and seasonal breakouts in Figure 11 (additional panels in Section A.5.3) confirm that the gains hold during evening peaks and the extreme winter months that dominate risk planning.

##### Data

We use hourly observations from federal/provincial networks and RMCQ (534 temperature stations and 241 automatically validated precipitation stations, each with years of data). We fine-tune the model on data from 2016-2023 and test on data from January 2024 to March 2025. See Section A.2 for details.

##### Results

Figure 11 shows that GFT-HQ is consistently the lowest-error model for temperature forecasts across the entire 0–5-day horizon. Errors grow with lead time for all models, but the finetuned GFT-HQ model maintains a clear MAE gap to both GFT and ECMWF-IFS at every lead. The improvement is broadly distributed across sites: the fraction of stations with lower error than IFS rises from roughly a majority at short leads to by days 4-5. Gains are operationally aligned with HQ priorities: they are largest during evening peak hours (18-23 EST/EDT), and they persist through the anomalously hot 2024 summer, indicating robustness under regime shifts. In practical terms, trimming even a few-tenths of a degree in MAE at these horizons materially reduces load-forecast error and the reserve over-commit or imbalance penalties that follow.

Figure 12 shows that GFT-HQ has the lowest MAE for precipitation forecasts at every lead from 0–5 days ( better than GFT, better than ECMWF-IFS). The improvement is broadly distributed across sites: the fraction of stations beating IFS climbs to for day-ahead forecasts. Operationally, even a few-tenths of a tenth of a millimeter per hour compounds into meaningful 24-h accumulation error reductions, tightening day-ahead hydro-inflow and storm staffing plans.

## 4 Conclusion

Weather foundation models can materially improve weather intelligence for grid operations when post-trained on high-fidelity utility data. By adapting a pre-trained transformer based weather foundation model to Hydro-Québec assets, we produced hyper-local forecasts that outperformed strong NWP baselines on standard weather variables (temperature, precipitation, and wind). For rare but operationally critical hazards like rime ice, the model provides a new capability: reliable, hours-ahead alerts with usable precision-recall trade-offs. These gains translate into earlier and better-targeted interventions (e.g., de-icing; see Section A.3), more reliable renewable dispatch, and improved situational awareness at the asset level.

Looking ahead, we see three priorities for deployment: (i) decision-driven evaluation with utility-calibrated cost-loss parameters and crew constraints; (ii) tighter coupling with grid models (e.g., dynamic line ratings and outage risk) to convert forecast probabilities into asset risk; and (iii) continuous post-training and recalibration as new sensors come online. Beyond Québec, the same approach is directly transferable to other regions (Silurian AI, 2025) and infrastructure owners, requiring only modest amounts of local data to adapt the model.

#### Acknowledgments

We wish to thank Ana Poenariu, Guillem Candille, Alexis Trottier-Paquet, Alexandre Vidal, Pierre-Olivier Caron-Perigny, Sara-Ann Piscopo, Solutions Mesonet, Eric Morissette, Melanie Otis, Daniel Beland, Jean-Sebastien Ducharme-Aubé for their support.

## References


[Excerpt truncated at the line cap; see url for the remainder.]
