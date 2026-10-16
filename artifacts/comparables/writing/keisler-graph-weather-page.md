---
author: "Ryan Keisler"
org: "Brightband (then Descartes Labs lineage)"
url: "https://rkeisler.github.io/graph_weather"
date: "2022"
fetch_date: "2026-10-15"
connects_to: "Ryan Keisler (Brightband)"
why_it_matters: "A solo researcher's project page for a graph-network weather model that became a widely cited public artifact; shows a small page plus code and paper can count."
---

Forecasting Global Weather with Graph Neural Networks

In the second half of 2021 I worked on a project to forecast global weather (think NOAA's GFS or ECMWF's IFS) using a data-driven, machine learning approach. It works well, with forecast performance improving upon previous data-driven approaches and comparable to operational, full-resolution, physical models from GFS and ECMWF, at least when evaluated on 1-degree scales and when using reanalysis initial conditions. Please feel free to email me with any feedback.

The video below shows 5-day rollouts of ERA5 (left) and the ML model (right). Three separate rollouts are shown, and for each rollout we cycle through Q850, T850, U500, V500, W500, and Z500.

Video showing Hurricane Sandy

This video shows an 8-day rollout of Z1000 (geopotential height at 1000 hPa) for Hurricane Sandy. The original GFS forecast is shown on the left, the ERA5 reanalysis data is shown in the center, and the 8-day forecast from the ML model (with ERA5 initial conditions) is shown on the right.

6-hour model predictions

The image below shows an example of the 6-hour difference in geopotential height, temperature, and humidity in the ERA5 dataset (left column) and the prediction from the machine learning model (right column). The model is able to accurately predict 6-hour changes in these variables using only the initial state.

Model Architecture

The image below shows the model archicture. Using the current atmospheric state, the model evolves the state forward by 6 hours. The 3D atmospheric state is defined on a uniform latitude/longitude grid, with 78 channels per pixel (6 physical variables × 13 pressure levels = 78 channels). An Encoder GNN encodes onto latent features defined on a icosahedron grid, a Processor GNN performs additional processing of the latents, and a Decoder GNN maps back to the atmospheric state on a latitude/longitude grid.

Videos showing 1-year rollout

While this system was designed to forecast weather on ~5-day horizons, it is interesting to observe the model behavior over very long rollouts. The videos below shows a 1-year rollout, from 2020-01-01 to 2021-01-01. While the model remains numerically stable over 1460 steps, it does develop several unphysical properties: overly smooth predictions, location-specific anomalies, and a grid pattern corresponding to the icosahedron processing grid.
