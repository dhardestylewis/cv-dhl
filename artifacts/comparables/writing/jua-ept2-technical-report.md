---
author: "Roberto Molinaro, Marvin Gabler et al."
org: "Jua"
url: "https://arxiv.org/html/2507.09703v1"
date: "2025-07-13"
fetch_date: "2026-10-15"
connects_to: "Gabler, Molinaro (Jua)"
why_it_matters: "Shows how a company names a model family, reports scale, and compares to ECMWF and AI baselines."
---

# EPT-2 Technical Report

###### Abstract

We present EPT-2, the latest iteration in our Earth Physics Transformer (EPT) family of foundation AI models for Earth system forecasting. EPT-2 delivers substantial improvements over its predecessor, EPT-1.5, and sets a new state of the art in predicting energy-relevant variables-including 10m and 100m wind speed, 2m temperature, and surface solar radiation-across the full 0–240h forecast horizon. It consistently outperforms leading AI weather models such as Microsoft Aurora, as well as the operational numerical forecast system IFS HRES from the European Centre for Medium-Range Weather Forecasts (ECMWF).

In parallel, we introduce a perturbation-based ensemble model of EPT-2 for probabilistic forecasting, called EPT-2e. Remarkably, EPT-2e significantly surpasses the ECMWF ENS mean-long considered the gold standard for medium- to long-range forecasting-while operating at a fraction of the computational cost. EPT models, as well as third-party forecasts, are accessible via the app.jua.ai platform.

## I Introduction

The foundation of numerical weather prediction was established by Vilhelm Bjerknes in the early 20th century. Bjerknes proposed that atmospheric processes could be represented by a set of mathematical equations. Specifically, the fundamental laws of physics governing fluid dynamics and thermodynamics. By numerically solving these equations, it became possible to predict future states of the atmosphere based on current observational data.

Today, numerical weather prediction models simulate the atmosphere by dividing it into a three-dimensional grid and calculating changes in atmospheric variables like temperature, pressure, wind speed, and humidity at each grid point over time. These models require immense computational power and are continually refined to include more complex processes, such as cloud formation, radiation, and interactions between the atmosphere and the Earth’s surface. Advanced data assimilation techniques incorporate real-time observational data from satellites, weather stations, and radar to enhance the accuracy of these models. Alongside, artificial intelligence and machine learning have been increasingly employed to optimize model parameters and improve predictive capabilities, marking a new era in weather forecasting.

Building upon these advancements, AI-based Earth system models have emerged that directly map raw observational data to predictions using end-to-end techniques. These models leverage deep learning to process vast datasets from satellites, radars, and sensors, capturing complex interactions among the atmosphere, oceans, land surfaces, and biosphere. By bypassing some traditional numerical methods, machine learning models aim to provide faster and more accurate forecasts.

Examples of such AI-driven systems include Aurora [1], a 1.3B-parameter transformer model trained on diverse datasets including ERA5, GFS, and IFS-HR, which currently sets the state of the art in global forecasting; GraphCast from Google [2], which introduced a GNN-based approach to model weather patterns; and AIFS [3], ECMWF’s AI model that improves GraphCast by incorporating a sliding-window transformer processor. Other notable models include Pangu-Weather [4], which uses 3D vision transformers; WeatherMesh-3 [5], which performs latent-space forecasting; and Aardvark weather [6], which improves ensemble reliability through learned distributional corrections.

Among the early efforts to operationalize these AI advances is Jua’s system. On March 1, 2023, Jua launched Vilhelm [7], the first global AI weather model capable of producing native hourly forecasts. One month later, it introduced a 1 km1 km global precipitation product [8], followed by EPT-1, which extended the model’s capabilities to include high-resolution solar radiation forecasts. This was followed in October 2024 by EPT-1.5 [9], demonstrating superior performance to prior AI models such as GraphCast, Pangu-Weather, and FuXi-Weather [10].

Building on these developments, this report presents the latest iteration of the Jua models-EPT-2 and its ensemble variant EPT-2e-and provides a comprehensive evaluation of their performance.

The key contributions of this work are:

* •

  We introduce EPT-2, a compute-efficient, dynamically conditioned weather model that delivers state-of-the-art performance on deterministic forecasts.
* •

  We present EPT-2e, an ensemble version of the model that considerably outperforms both Aurora and the ECMWF ENS across all key variables and lead times, achieving lower RMSE and CRPS throughout the full 0–240 h forecast range.
* •

  We highlight the operational advantages of the EPT-2 family, including 25% faster inference, flexible lead time handling, and broad variable support.

## II EPT-2: Model Architecture and Operational Setting

The core of EPT-2 is a predictive machine learning engine that maps sequences of past atmospheric states to future conditions. This approach mirrors the logic of traditional numerical weather prediction, but replaces hand-coded physical solvers with physical solvers learned from data.

This process can be more rigorously formalized by approximating the mapping:

which delineates the relationship between the current and previous states of the weather and the future state through a machine learning model. In this formulation, the model is denoted by , where:

The model is trained by minimizing the following objective function:

Here, denotes the number of weather variables, including temperature, wind velocity components, geopotential, etc., while and represent latitude and longitude, respectively. The weights are given by:

This formula adjusts the importance of each term based on latitude, compensating for the varying density of grid points across latitudes in most geographic coordinate systems.

### II-A Key Features

The key features of EPT-2 are outlined below:

* 1.

  Foundational Earth Systems Model: Like its predecessor EPT-1.5, EPT-2 is an AI model trained on diverse datasets.
* 2.

  Any Lead Time Forecasting: Unlike most current AI weather models that can only provide forecasts every six hours, EPT-2 offers predictions for any lead time , and generates native hourly forecasts in an operational setting.
* 3.

  Probabilistic Forecasting: EPT-2 supports uncertainty-aware forecasting through an operational perturbation-based ensemble model, referred to as EPT-2e. This extends the core model’s capabilities and supports more robust decision-making under uncertainty.

### II-B Operational Specifications

* •

  Spatial Resolution: EPT-2 operates at a spatial resolution of 0.083 degrees or roughly 9 x 9 km at the equator, providing highly detailed forecasts. A high-resolution variant of EPT-2 has also been developed and may be discussed in future work; for comparability, we solely discuss the 9 x 9 km variant in this paper.
* •

  Temporal Resolution: EPT-2 currently runs at a temporal resolution of 1 hour up to 20 days into the future.
* •

  Forecast Frequency: The model runs four times daily at 00:00, 06:00, 12:00, and 18:00 UTC. At each of these times, both an early version and a standard version are executed. The standard version becomes available with a typical 6-hour delay (like ECMWF IFS) but supports faster dissemination once initialized. The early version produces forecasts approximately 2.5 hours earlier11 1 https://www.jua.ai/. An enhanced high-refresh variant, designed for continuous, low-latency forecasting through direct assimilation of high-frequency observational data, is nearing public release and may be detailed in future work.

## III Benchmarks Details

In this section, we outline the evaluation process for the performance of the EPT and third-party models. The pipeline is based on the well-established WeatherBench [11].

### III-A Ground Truth Datasets

A fundamental aspect of evaluating model performance is the definition of a ground truth dataset. In the following, we describe three datasets commonly accepted in the weather community.

ERA5. ERA5 [12] is a state-of-the-art global atmospheric reanalysis dataset produced by the European Centre for Medium-Range Weather Forecasts (ECMWF). It is a gridded dataset and provides hourly estimates of a wide array of atmospheric, land, and oceanic variables from 1940 to the present, with a horizontal resolution of approximately 31 x 31 km at the equator (0.25 degrees).

IFS HRES IC. The ECMWF High-Resolution Forecast (HRES) initial conditions (ICs) are computed from the most recent observational data. The high-resolution initial conditions serve as the starting point for ECMWF’s weather forecasts, which operate at a horizontal resolution of about 9 x 9 km at the equator (0.1 degrees). Although these are not direct observations, ICs are widely used in the research community due to their complete spatial coverage, ease of alignment, and historical use in training or validation pipelines.

Weather Stations. We use the WeatherReal-ISD dataset [13], which aggregates global in-situ weather observations from over 14,000 stations as part of NOAA’s Integrated Surface Database (ISD). These stations include traditional public networks such as SYNOP and METAR, reporting standard surface weather variables such as 2m air temperature, 10m wind speed, surface pressure, humidity, and precipitation. The data undergo extensive quality control and station unification procedures, ensuring consistency across both time and geography. Figure 1 shows the global distribution of stations used. While spatially sparse and unevenly distributed, they offer a more neutral and fair ground truth for both AI and NWP models, free from the potential biases introduced when models are trained on datasets like ERA5. For this reason, station observations are widely regarded as a more faithful proxy for ground truth, and hence, serve as the primary evaluation target throughout this work. We emphasize that none of the models discussed in this work have been postprocessed or finetuned using weather station data, ensuring a fair comparison.

### III-B Models Evaluations

Models are evaluated through two different types of benchmarkings:

* 1.

  Grid Benchmarks: This approach compares the gridded model outputs with a gridded ground truth dataset, specifically IFS HRES IC.
* 2.

  Point Benchmarks: This approach compares the model output at a specific point with an actual observation from WeatherReal stations. The code used for running point benchmarks is available on GitHub at github.com/juaAI/stationbench.

Unless otherwise specified, all benchmark results are computed on a global scale.

### III-C Methodology

Next, we describe our benchmarking methodology more precisely.

Initial Conditions. To ensure comparability, EPT-2 is initialized using the same input data as the other models, providing a standardized baseline for evaluation. All models are initialized at 00:00 and 12:00 UTC on a uniform schedule throughout 2023.

Reference Forecast. As reference for deterministic evaluations, we choose the IFS HRES forecast produced by the European Centre for Medium-Range Weather Forecasts (ECMWF) [14], benchmarked against its initial conditions and weather stations. IFS HRES is currently considered to be the world’s most accurate numerical medium-range weather model.

In the probabilistic evaluations, we also report the performance of ECMWF ENS mean, which averages forecasts across all members of the ECMWF ensemble prediction system (ENS). The ensemble mean offers a deterministic approximation that benefits from the spread of the ensemble, often improving skill over individual members, on the long-range time horizon.

Evaluation Metrics. We focus on two primary evaluation metrics: Root Mean Square Error (RMSE) and Continuous Ranked Probability Score (CRPS), which together assess both deterministic and probabilistic forecast quality.

Root Mean Square Error (RMSE). RMSE measures the average magnitude of forecast errors and is widely used in meteorology for evaluating deterministic predictions:

|  |
| --- |
| (1) |

where is the predicted state (typically the deterministic forecast or the ensemble mean), is the corresponding ground truth, and are spatial weights (e.g., area-weighted). The spatial weighting is latitudes based for the grid benchmarks and for the point benchmarks.

Continuous Ranked Probability Score (CRPS). CRPS is a strictly proper scoring rule for probabilistic forecasts, measuring the difference between the predicted cumulative distribution function (CDF) and the step function at the observation. For ensemble forecasts, the CRPS can be decomposed into two terms:

|  |
| --- |
| (2) |

where are the predicted ensemble members. The first term measures accuracy (closeness to the observation), while the second captures ensemble spread (internal variability).

A well-calibrated ensemble should balance spread and skill: if the ensemble is overconfident (too narrow), CRPS will penalize forecast misses; if it’s too broad (underconfident), CRPS will penalize the lack of sharpness. Lower CRPS values indicate better overall probabilistic performance.

## IV Results

In this section, we compare the performance of the EPT-2 family against its predecessor EPT-1.5, as well as the current state-of-the-art weather model Aurora [1], across two distinct evaluation settings:

* •

  Deterministic Forecasting: Evaluating forecast skill based on unperturbed ICs as input.
* •

  Probabilistic Forecasting: Measuring the quality of uncertainty estimates and distributional outputs. Probabilistic forecasts for EPT-2e and Aurora are produced by introducing small perturbations to the ICs, with each perturbed state independently propagated through the model to generate the ensemble.

### IV-A Deterministic Forecasting Results

We evaluate the performance of EPT-2 and baselines models using RMSE computed over the full 0–240 h forecast range. Results are reported against both gridded (IC) and ground-based weather station observations. In addition to 10 m wind speed, 100 m wind speed, and 2 m temperature, we also include results for surface solar radiation accumulated over six hours. This metric is only reported for EPT-2 and EPT-1.5, as the publicly available Aurora model does not provide shortwave radiation output.

#### Evaluation against Initial Conditions.

When evaluated against reference ICs (Figures 2, 3, 4, 5), EPT-2 consistently outperforms EPT-1.5 across all lead times and variables, including 10 m wind speed, 100 m wind speed, 2 m air temperature, and surface solar radiation. For solar radiation, we use ERA5 as the reference, since SSRD is a diagnostic variable and not available in the HRES initial conditions.

Compared to Aurora, EPT-2 achieves consistently lower RMSE on 10 m wind speed across the entire 0–240 h forecast horizon. For 2 m temperature, EPT-2 outperforms Aurora up to 130 h, with a slight drop in relative performance at longer lead times.

EPT-2 also demonstrates substantial improvements over the HRES deterministic forecast beyond 12 h across all variables considered. Notably, for solar radiation, EPT-2 outperforms both EPT-1.5 and HRES consistently throughout the full 0–240 h range.

Additionally, Figures 12 and 14 show global snapshots of 2m temperature and 10m wind speed for EPT-2, Aurora and EPT-1.5 at 1, 2, and 10 days lead time, alongside the initial condition. EPT-2 delivers considerably sharper predictions at 10 days compared to Aurora, which produces visibly blurrier forecasts, and yet producing less accurate forecasts.

#### Evaluation against Weather Stations.

Next, we evaluate model performance against in-situ weather station observations. EPT-2 consistently outperforms EPT-1.5 on 10m wind speed across all lead times (Figure 7), confirming the improvements introduced in the latest version. For 2m air temperature (Figure 7), EPT-2 initially shows slightly higher RMSE than EPT-1.5 up to 100 hours, but the difference narrows and reverses around 120 hours, after which EPT-2 becomes more accurate.

Compared to Aurora, EPT-2 performs similarly for short-term 10m wind forecasts, but achieves lower RMSE beyond 6 days. On temperature, EPT-2 maintains an advantage over Aurora for almost the entire lead time range.

Across both variables and all lead times, all EPT variants outperform the HRES deterministic forecast, with the gap widening as lead time increases-highlighting the advantage of data-driven models in medium-range prediction.

Finally, to illustrate the EPT models’ capability for high-resolution temporal forecasting, Figures 13 and 15 show 4-day time series of temperature and wind speed at a Zurich location. These examples underscore the value of hourly predictions:

### IV-B Probabilistic Forecasting Results.

Next, we compare the ensemble performance of Aurora and EPT-2e using two complementary metrics: the root-mean-square error of the ensemble mean, and the continuous ranked probability score. This evaluation is conducted exclusively against weather station observations, as they offer the most direct and fair measure of real-world forecast accuracy. Both AI models use ensembles composed of 10 members.

Figures 9 and 9 present the RMSE of the ensemble mean for 2m air temperature and 10m wind speed across the 0–240h forecast horizon. EPT-2e clearly outperforms all other models, achieving the lowest RMSE at virtually every lead time. Most notably, it consistently outperforms the ECMWF ENS mean-widely regarded as the gold standard for medium- to long-range forecasting-despite using only 10 members versus HRES’s 50.

Figures 11 and 11 confirm these findings from a probabilistic standpoint. EPT-2e achieves the lowest CRPS across almost the entire forecast range for both variables, with particularly large gains beyond 48h, demonstrating its ability to provide sharper and more reliable uncertainty estimates.

This represents a significant step forward: a AI-based model not only matches, but in all the cases surpasses, the performance of a leading operational ensemble model-despite using far fewer members and requiring substantially lower computational cost.

### IV-C Comparison with Aurora

Finally, to provide a comprehensive view, we summarize key differences between EPT-2 and Aurora across training cost, inference speed, and modeling flexibility:

* •

  Forecast accuracy: EPT-2 consistently outperforms Aurora across variables and lead times.
* •

  Training efficiency: EPT-2 was pretrained on 8 H100 GPUs for 10 days, while Aurora required 32 A100 GPUs for 18 days. Despite using over 4 fewer GPUs and less total training time, EPT-2 achieves comparable or superior forecast skill across most variables and lead times. To better understand scaling behavior and performance trade-offs, we also conducted extensive large-scale experiments, training model variants with up to 10 billion parameters. Nevertheless, the EPT-2 version discussed in this paper remains dramatically more compute-efficient and cost-effective than other state-of-the-art models.

[Excerpt truncated at the line cap; see url for the remainder.]
