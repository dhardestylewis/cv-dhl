---
author: "NVIDIA Earth-2 team"
org: "NVIDIA"
url: "https://developer.nvidia.com/blog/forecasting-the-weather-beyond-two-weeks-using-nvidia-earth-2/"
date: "2025-07-11"
fetch_date: "2026-10-15"
connects_to: "Kashinath, Pathak, Harrington, Pritchard (NVIDIA Earth-2)"
why_it_matters: "Practitioner-oriented technical blog: tooling, validation utilities, and reproducible recipes."
---

Data Science

English日本語中文

# Forecasting the Weather Beyond Two Weeks Using NVIDIA Earth-2

Jul 11, 2025

By Ram Cherukuri, Peter Harrington, Mike Pritchard and Niall Robinson

Discuss (0)

* L
* T
* F
* R
* E

## AI-Generated Summary

* The Earth-2 platform provides a performant, scalable stack of tools for weather experts to evaluate and validate AI models and for AI/ML experts to develop, customize, and scale them.
* Earth2Studio now includes a subseasonal-to-seasonal forecasting capability demonstrated with the Deep Learning Earth System Model (DLESyM), a parsimonious deep-learning model that couples a multi-layer atmosphere AI model to a separate ocean AI model predicting sea surface temperature evolution.
* DLESyM uses a U-Net architecture with modified padding to support the HEALPix grid at approximately 1 degree resolution and has demonstrated realistic ability to asymptote to expected climatological error rates on multi-month timescales.
* Earth2Studio provides a new S2S recipe supporting multi-GPU distributed inference and parallel I/O for generating large ensemble forecasts from HENS FourCastNet V2 (SFNO) and DLESyM, enabling domain experts to understand and validate model skill.
* Efficient inference and scoring of large S2S ensemble forecasts is now possible, with DLESyM ensemble forecasts across an entire year running and scoring in less than two hours on eight GPUs, and DLESyM showing competitive skill with ECMWF IFS in weeks three through five.

### Next Steps

* Explore the Deterministic seasonal forecasting with DLESyM example to begin generating forecasts.
* Review the Ensemble forecasting with HENS – FourCastNet V2(SFNO) recipe for probabilistic subseasonal forecasting.
* Try the S2S Ensembles with DLESyM or HENS recipe to run and score large ensemble forecasts.

Powered by NVIDIA Nemotron. AI-generated content may summarize information incompletely. Verify important information. Learn more

Being able to predict extreme weather events is essential as such conditions become more common and destructive. Subseasonal climate forecasting - predicting weather two or more weeks in the future - underpins proactive decision making and risk management across sectors that are sensitive to weather fluctuations.

It can help farmers better choose which crops to grow and manage their water resources in drought-prone regions. Power companies can balance energy supply and demand, while fisheries can protect themselves from marine heatwaves. And governments can prepare for natural disasters and public-health threats, such as pre-provisioning mobile firefighting and heat risk mitigation infrastructure in regions where the subseasonal outlook is worse.

Using AI models to forecast weather and climate has gained significant steam in research over the past two years, and is now gaining traction in operational settings. The NVIDIA Earth-2 platform has been supporting both the scientific and enterprise communities by providing a performant and scalable stack of tools. It benefits everyone from weather experts who want to evaluate and validate the skill of models, to AI/ML experts trying to develop, customize, and scale the models for various use cases and datasets.

In this post, we will provide an overview of the utilities offered by the Earth-2 platform for weather domain experts to develop and validate large ensembles for probabilistic subseasonal forecasts - all at much lower compute costs than traditional non-ML techniques.

## Subseasonal forecasting with AI

One of the key advantages of AI weather models is the ability to run much larger operational ensembles than what is feasible with traditional methods at compute costs that are orders of magnitude less. Researchers at the University of California, Berkeley demonstrated earlier this year an effective way to generate well-calibrated, multi-thousand-member ensembles (“Huge Ensemble,” or HENS) using the Bred Vector/Multi Checkpoint (BVMC) methodology. Enterprises like JBA and AXA are using this HENS approach with a FourCastNet V2 (SFNO) model for hindcasting in insurance applications.

The latest release of Earth2Studio has introduced a new subseasonal-to-seasonal (S2S) forecasting capability demonstrated in the context of the Deep Learning Earth System Model (DLESyM). This is a parsimonious deep-learning model that couples a multi-layer atmosphere AI model to a separate ocean AI model that predicts sea surface temperature evolution.

The model architecture is a U-Net with padding operations modified to support using the HEALPix grid with approximately 1 degree in resolution. Since it is based on local stencils that do not use position embeddings, this architecture has the potential to generalize. The model has demonstrated realistic ability to asymptote to expected climatological error rates on multi-month timescales, and researchers at the University of Washington have shown it has the capacity for remarkable autoregressive stability on climate-scale simulations.

In the following code snippet, you can see the ease of using the model to generate subseasonal forecasts. The full implementation is available in Earth2Studio here.

```
# Prepare model, data source, and I/O backend
package = DLESyMLatLon.load_default_package()
model = DLESyMLatLon.load_model(package).to(device)
data = ARCO()
io = KVBackend()

# 60-day forecast, initialized in June 2021
ic_date = np.datetime64("2021-06-15")
n_steps = 16

# Prepare coordinates for forecast outputs
input_coords = model.input_coords()
output_coords = model.output_coords(input_coords)
inp_lead_time = input_coords["lead_time"]
out_lead_times = [
    output_coords["lead_time"] + output_coords["lead_time"][-1] * i
    for i in range(n_steps)
]
output_coords["lead_time"] = np.concatenate([inp_lead_time, *out_lead_times])

# Run forecast
io = run.deterministic(
    [ic_date], n_steps, model, data, io, output_coords=output_coords
)
```

## Probabilistic forecasting with ensembles

S2S forecasts are, however, inherently probabilistic, not deterministic. They do not predict the exact weather on a specific day months in advance but rather provide the likelihood of seasonal conditions deviating from the norm. These forecasts are commonly expressed in terms of probabilities for terciles: the likelihood of the upcoming season being in the upper third (above normal), middle third (near normal), or lower third (below normal) of the historical climate distribution for variables like temperature or precipitation.

Prior to the availability of this new model, enterprises have extended the HENS approach with the FourCastNet V2 (SFNO) model to do S2S forecasting. And researchers at the University of California, Irvine have shown it is as skillful as the ECMWF forecast system for Madden-Julian Oscillation (MJO) predictability; the MJO is a leading source of S2S predictability in the atmosphere.

Now, Earth2Studio provides a new S2S recipe for users interested in trying HENS-SFNO, DLESyM, or other models to make S2S predictions. Reflecting the need for larger ensembles and longer forecast timescales, the recipe supports multi-GPU distributed inference, along with parallel I/O to efficiently save forecast data as it is generated. It also permits saving only a subset of the forecast outputs if storage space is a constraint. To streamline the usage of this recipe, much like the HENS recipe in Earth2Studio, complex aspects of running the ensembles are already taken care of. Controlling the behavior amounts to specifying a configuration:

```
# DLESyM ensemble with 16 total checkpoint combinations
nperturbed: 4
ncheckpoints: 16
batch_size: 4
defaults:
    - forecast_model: dlesym
    - perturbation: gaussian
```

With this new recipe, domain experts can now generate large ensemble forecasts from HENS FourCastNet V2 (SFNO) and DLESyM to understand and validate the skill of these models. For instance, you can explore how prediction uncertainty is driven by perturbations to initial conditions or alternate model checkpoint weights. This allows you to generate a skillful, calibrated ensemble of subseasonal forecasts. This forms the  basis from which you can explore additional strategies for optimal AI forecast calibration on S2S timescales.

As a demonstrative example, the recipe can be used to generate S2S forecasts for the 2021 Pacific Northwest heatwave, which are shown in Figure 1. This unprecedented event was remarkable in the intensity and duration of extreme heat, and difficult to predict on S2S timescales, according to the 2021 Western North American Heatwave and Its Subseasonal Predictions paper published in Geophysical Research Letters. While no model captures both the location and intensity of the heatwave perfectly, we can see that all models began predicting some level of warm anomaly in North America as far as three weeks in advance, with accuracy varying between HENS-SFNO, IFS ENS, and DLESyM.

*Figure 1. Sample comparison of weekly-averaged S2S forecasts between (counterclockwise from top left) IFS ENS (11 hindcast members, downloaded ECMWF API), SFNO-HENS, and DLESyM for the 2021 Pacific Northwest heatwave, alongside the corresponding ERA5 data in week three of the forecasts. All models predict some level of warm anomaly in North America, but with this long of a lead time, it is difficult to capture both the exact location and intensity of such extreme heat.*

## What’s next?

Accelerating the adoption of AI for S2S forecasting requires more robust evaluation of such models and their capabilities by domain experts. Providing open source libraries reduces barriers to entry on the skills needed on the AI front. It also provides feedback on the future development of models to the AI/ML research community.

The AI Weather Quest competition from the European Centre for Medium-Range Weather Forecasting (ECMWF) aims to accelerate community participation in advancing S2S forecasting. While engineers at NVIDIA gear up to participate in it (alongside researchers at the University of Washington), we are working on composability of Earth-2 tools with those provided by ECMWF for the Weather Quest competition to enable the community to participate. This should allow for faster iterations in evaluating models using ECMWF’s AI-WQ-package directly with forecast data generated in Earth2Studio, along with the ability to train custom models in PhysicsNeMo. These are the same tools used by NVIDIA research teams, and we hope sharing these will enable other researchers to rapidly iterate on their ideas.

```
# Score an earth2studio-generated forecast using ECMWF AI-WQ routines
for var in aiwq_variables:
    fcst_data, fcst_coords = load_forecast_for_aiwq(io_backend, ic, var)
    rpss_wk3, rpss_wk4 = compute_aiwq_rpss(fcst_data, fcst_coords, var)
    write_aiwq_scores(score_io_dict, rpss_wk3, rpss_wk4, var)
```

In general, efficient inference and scoring of large S2S ensemble forecasts is an essential part of the scientific process. Assessing models properly requires scoring many forecasts to determine their skill. To accelerate this resource-intensive process, Earth2Studio can now run and score large S2S ensembles efficiently. For example, DLESyM ensemble forecasts using multiple atmosphere and ocean models across an entire year can be run and scored in less than two hours on eight GPUs.

See Figure 2 for an example of these scoring results, which also demonstrate that the DLESyM model has S2S skill that is competitive with ECMWF IFS in weeks three through five, a strong physics baseline. We are releasing these general scoring capabilities along with AI Weather Quest-specific ones in the S2S recipe in Earth2Studio. This provides practitioners with a variety of means to assess the performance of models they are interested in trying.

*Figure 2. Fair CRPS z500 scores of weekly-averaged S2S forecasts evaluated across 2018 for the IFS ENS and DLESyM models. DLESyM is competitive with IFS in general, but lags behind in skill in the earlier weeks due to reduced model spread.*

## Key takeaways

S2S forecasting is essential to a wide array of climate sensitive sectors. This post discussed the key new functionality in Earth2Studio to enable enterprises to evaluate and validate pretrained atmosphere-ocean coupled AI prediction models like DLESyM to generate ensemble forecasts.

Here are resources to get started:

Learn more about the Earth-2 platform from these GTC sessions. These resources provide more insights on how enterprises are using AI for generating large ensemble forecasts:

Discuss (0)

## Tags

## About the Authors

**About Ram Cherukuri**
  
Ram Cherukuri is a senior product manager for PhysicsNeMo, the Physics-ML platform for AI in science and engineering . He is also the product manager for DLA software, working with embedded AI developers and was part of the CUDA product management team. Prior to NVIDIA, Ram was a product manager at MathWorks for code generation and verification products for embedded software development, working with automotive and aero-def customers. He holds a master’s degree in aerospace engineering from Purdue University and a bachelor’s degree in the same discipline from IIT Bombay.

**About Peter Harrington**
  
Peter Harrington is a senior scientific software engineer for Earth-2 at NVIDIA, specializing in machine learning for weather and climate forecasting. His interests include scalable AI model training, applied AI in the physical sciences, and their intersection with HPC and GPU-based computing. Before NVIDIA, Peter worked at Lawrence Berkeley National Laboratory on scientific AI and HPC research. He holds a master’s degree in scientific computing & applied mathematics from UC Santa Cruz.

**About Mike Pritchard**
  
Mike Pritchard is the director of climate simulation research for NVIDIA Research, where he works on Earth-2. He leads a team of researchers who are exploring the potential of AI to advance weather and climate simulation. Mike previously served as a professor of Earth system sciences at the University of California, Irvine, where he led a research lab studying climate dynamics and next-generation atmospheric simulation algorithms starting in 2013.

**About Niall Robinson**
  
Niall Robinson is the developer relationship manager for Earth-2, NVIDIA’s platform for weather and climate. He collaborates with partners to develop innovative new solutions using Earth-2. Before NVIDIA, Niall worked at the U.K. Met Office, applying emerging technologies to solve problems. He started his career as a climate scientist working in decadal forecasting and air-quality science. He has a Ph.D. in atmospheric science from Manchester University.
