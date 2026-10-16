---
author: "Silurian"
org: "Silurian"
url: "https://silurian.ai/blog/gft-api-announce"
date: "2025-01-09"
fetch_date: "2026-10-15"
connects_to: "Jayesh Gupta, Nikhil Shankar (Silurian)"
why_it_matters: "Names the model (GFT), states 1.5B parameters, and packages access as an API; model naming plus scale statement."
---

## Earth API

What is it worth to know the weather forecast one day sooner? That’s not a hypothetical question, every decade weather forecasting systems improve enough to see a day further into the future, and so one way to get the answer is by checking back in 2036. That’s not what we’d recommend though. Instead, try out our Earth API today which serves state of the art forecasts powered by our physics foundation models.

Foundation models have been taking the world by storm. There are models for text, images, and even videos. At Silurian we built one to model the Earth. The Generative Forecasting Transformer (GFT) uses 1.5 billion parameters to simulate global weather conditions with unprecedented accuracy. We’re excited to share GFT via our API which features:

* **Global Forecasts**: Our API provides global coverage, whether at land or at sea.
* **Granular Time Horizons**: Know how the weather will change every hour.
* **SOTA Accuracy:** Check out our evaluations below!
* **Energy Ready:** Own wind farms or solar panels? We’ve got you covered with 100m winds and surface solar radiation (GHI).
* **More variables:** Predictions for more variables than any other AI model, including 100m winds, solar radiation, snowfall accumulation, precipitation type, and others.

Try out the Earth API in our playground or in your applications with our Python and Typescript SDKs!

## Evaluations

The weather is a complex and only partially observed physical process. This means that defining the ground truth to evaluate against can be uncertain. If rain falls in a forest and no rain gauge catches it, does it still contribute to your errors? The meteorological community has been grappling with this problem for decades and fortunately they have come up with good answers. We’ll be using 3 versions of ground truth from the community: weather station observations from Meteostat and analysis/re-analysis datasets from the ECMWF. The station observations capture precise meteorological conditions across a diverse set of locations. In contrast, the analysis and re-analysis datasets offer a more global yet less precise view of the historical meteorology. All evaluations are over the entire year 2023.

Throughout the evaluations we display *Skill Score (%)* by default. This is a measure of relative improvement as compared to a chosen baseline. For example, if model A has a skill score of 10% when compared against model B that means model A has 10% lower relative error than model B.

### Main weather variables

In our global evaluations, we compare GFT with HRES, the gold standard global numerical model for weather prediction, and GraphCast, a flagship AI model from Google DeepMind.

Variable

Metric

Region

Compare Against

Show Markers

GFT

HRES

GraphCast

At a regional level we also consider HRRR and ICON, the top regional models for the USA and Europe, respectively. GFT uniformly outperforms the global models (HRES and GraphCast) across all variables, while also eventually outperforming HRRR and ICON after the first few hours.

Variable

Metric

Region

Compare Against

Show Markers

GFT

HRRR

HRES

GraphCast

Variable

Metric

Region

Compare Against

Show Markers

GFT

HRES

GraphCast

ICON

### Renewable energy variables

Besides the standard weather variables, wind speeds at 100m altitude and solar radiation measurements (SSRD/GHI) are crucial for accurate renewable energy forecasting. Since these quantities are not predicted by publicly available AI models and are not included in the weather station observations, we compare GFT and HRES against two authoritative datasets: IFS analysis for wind data and ERA5 for solar radiation. GFT demonstrates superior performance compared to HRES forecasts for both metrics.

Variable

Metric

Region

Compare Against

Show Markers

GFT

HRES

Variable

Metric

Region

Compare Against

Show Markers

GFT

HRES

We are excited to see what our users will build with this API and welcome any requests for features!
