---
author: "The Forecasting Company"
org: "The Forecasting Company"
url: "https://www.theforecastingcompany.com/blog/t0-beta/"
date: "2026-09-16"
fetch_date: "2026-10-15"
connects_to: "Negiar, Fainberg (TFC; protected organization, read-only research)"
why_it_matters: "How a forecasting startup names a model, states parameter count, and compares against TimesFM, Chronos-2, Toto."
---

**t0-beta is our new 256-million-parameter forecasting foundation model.** We built the t0 family of models to forecast from target history, related time series, and inputs known ahead of time. Now, with a place among the strongest zero-shot forecasters in our benchmark comparisons, we’re ready to take it further. We’re proud to share it.

Hugging Face ↗Tech report ↗

## A major step forward for the t0 family

GIFT-Eval and fev-bench are two major public benchmarks for time-series forecasting, testing models across diverse datasets and forecasting tasks. GIFT-Eval measures accuracy across domains and time horizons; fev-bench also tests forecasts using related series and covariates.

**t0-beta** ranks **third on GIFT-Eval and third on fev-bench** among the zero-shot checkpoints compared in our tech report. One checkpoint, across both benchmarks, with no task-specific retraining.

On GIFT-Eval, it reaches **0.4738 CRPS** and **0.6865 MASE**, improving on t0-alpha by 4.1% and 5.2%, respectively. On fev-bench, its **46.7% skill score** is 4.5 percentage points above t0-alpha. It also takes third place on the benchmark’s 42 tasks with covariates.

### GIFT-Eval

CRPS and MASE · lower is better

1. TimesFM-3.0Google331M parameters**CRPS 0.4557****MASE 0.6668**
2. Granite-PatchTST-FMIBM385M parameters**CRPS 0.4672****MASE 0.6846**
3. t0-betaThe Forecasting Company256M parameters**CRPS 0.4738****MASE 0.6865**
4. Toto-2.0-2.5BDatadog2.45B parameters**CRPS 0.4759****MASE 0.6956**
5. TiRex-2NXAI82.5M parameters**CRPS 0.4781****MASE 0.6973**
6. t0-alphaThe Forecasting Company102M parameters**CRPS 0.4941****MASE 0.7240**

Bars show CRPS. MASE scores appear alongside.

### fev-bench

Skill (%) · higher is better

1. TimesFM-3.0Google**48.7% skill**
2. Chronos-2Amazon**47.3% skill**
3. t0-betaThe Forecasting Company**46.7% skill**
4. TiRex-2NXAI**45.5% skill**
5. Toto-2.0-1BDatadog**44.4% skill**
6. Toto-2.0-2.5BDatadog**44.4% skill**
7. t0-alphaThe Forecasting Company**42.2% skill**

GIFT-Eval: leading five models and t0-alpha, ranked by CRPS. MASE is shown for the same models. Both scores are normalized to a seasonal-naive baseline across 97 configurations. fev-bench: leading five ranks, including the tie for fifth, plus t0-alpha; skill relative to seasonal naive across 100 tasks. CRPS evaluates probabilistic forecasts; MASE measures point-forecast error. Source: Tables 3–4 of our September 19, 2026 tech report. This comparison of time-series foundation models (TSFMs) uses zero-shot checkpoints and excludes ensembles, agents and fine-tuned systems.

That puts t0-beta just ahead of Toto-2.0-2.5B on GIFT-Eval, with roughly a tenth of the parameters. TimesFM-3.0 still leads both benchmarks in our comparison; on the separate TIME benchmark, t0-beta ranks fifth by CRPS. There is more to do. But this is a substantial step for t0 - and for what a compact forecasting model can deliver.

### Head to head on individual tasks

An aggregate score is only one view. On the official fev-bench results, **t0-beta beats Chronos-2 on 43 of 100 tasks**. On the 42 covariate-informed tasks, it beats Toto-2.0-2.5B on **29 tasks (69.0%)** and Toto-2.0-1B on **30 (71.4%)**. At 256M parameters, that makes t0-beta a compelling model to evaluate on your own data.

### How often does t0-beta win?

Share of tasks with lower forecast loss than each model

| Compared with | With covariates42 tasks | Without covariates58 tasks |
| --- | --- | --- |
| TimesFM-3Google | **28.6%**  -  12 of 42 tasks | **22.4%**  -  13 of 58 tasks |
| Chronos-2Amazon | **42.9%**  -  18 of 42 tasks | **43.1%**  -  25 of 58 tasks |
| Toto-2.0-2.5BDatadog | **69.0%**  -  29 of 42 tasks | **29.3%**  -  17 of 58 tasks |
| Toto-2.0-1BDatadog | **71.4%**  -  30 of 42 tasks | **32.8%**  -  19 of 58 tasks |
| TiRex-2NXAI | **54.8%**  -  23 of 42 tasks | **56.9%**  -  33 of 58 tasks |
| Toto-2.0-313mDatadog | **73.8%**  -  31 of 42 tasks | **34.5%**  -  20 of 58 tasks |
| TiRexNXAI | **78.6%**  -  33 of 42 tasks | **60.3%**  -  35 of 58 tasks |
| Seasonal NaiveBaseline | **100.0%**  -  42 of 42 tasks | **100.0%**  -  58 of 58 tasks |

Pairwise task win rates on fev-bench, retrieved September 20, 2026. A win means lower scaled quantile loss (SQL); ties count as half a win. Higher percentages favour t0-beta; 50% means an even split. These are distinct task subsets, not a covariate ablation. Calculated from the benchmark’s published per-task scores, including its missing-result and training-overlap adjustments. Seven forecasting models and a seasonal-naive baseline are shown; this is not the complete leaderboard.

These comparisons also show where there is room to improve: TimesFM-3 wins most head-to-head tasks against t0-beta, and the larger Toto models are stronger on the tasks without covariates. The two groups cover different task sets; they do not measure the effect of adding covariates to the same tasks.

## Forecasting ERCOT electricity prices with Macrocosm

Our collaboration with Macrocosm puts the t0 family to the test on a practical energy-market problem. Macrocosm, which builds simulation-driven world models for the US electric grid, conducted an independent evaluation and authored the ERCOT case study in our tech report.

The evaluation tested how well the models could forecast **hourly real-time (SCED) electricity prices across ERCOT’s four Texas load zones** for the next operating day. Macrocosm evaluated forecasts from January 2024 to May 2026, made at 09:00 Central Time on the preceding day. Each forecast used only information available at that cutoff, including 21 covariates covering load, renewable generation, outages and weather.

t0-beta achieved a mean absolute error of **$14.46/MWh**, versus $23.57 for a baseline that repeats the latest complete day’s hourly prices - about **39% lower**. Extreme price spikes remain difficult: its nominal 80% prediction interval covered 75% of observed prices. Macrocosm’s analysis shows both the peaks the model captured and the spikes it missed.

In Macrocosm’s trading backtest, t0-beta’s selected strategy generated **$14.94 million in simulated P&L**, with an annualized daily-dollar Sharpe ratio of **1.29**. An always-short control made $11.82 million without using forecasts. The backtest used a fixed 100 MW reference size per zone, without reinvestment or market impact; each model’s strategy was selected retrospectively over the evaluation period.

## Try t0 on your data

Recently, we’ve made the t0 family easier to try, run locally and use in production.

### Open-weights

The latest t0-beta weights are on Hugging Face. For local inference, the t0 family of models has first-party Python runtimes: `tfc-t0` for PyTorch and `tfc-t0-mlx` for MLX on Apple silicon.

### ONNX builds

We also publish portable t0-alpha ONNX builds on Hugging Face, with different precision and quantization options to suit model-size and memory requirements, including embedded and edge deployments. You can see these builds in action in Finish This Chart and t0.run, which runs 1,000 forecasts across multiple data sources in your browser using ONNX on WebGPU. Our browser inference post explains how we made t0-alpha portable enough to run in a tab.

### A descriptive API

For managed forecasting, our new API lets you describe your dataset once, then request forecasts and backtests across its series and aggregation levels. We walk through that workflow in Describe your data, don’t reshape it.

### Visual exploration

Retrocast gives you a visual workspace to explore forecasts and backtests on your own data.

### The automated forecaster

> We want teams to spend less time assembling forecasting pipelines and more time making decisions they can trust. Our vision is the automated forecaster: a system that prepares data, finds useful inputs, evaluates its forecasts and helps turn them into decisions, across millions of time series. The t0 family is the foundation we’re building that system on. With t0-beta, we’re taking another step towards it.

**For enterprise deployments, larger forecasting workloads, or help evaluating the t0 family on your own data, talk to us.** And if you like the sound of what we’re building, we’re hiring.

Hugging Face ↗Tech report ↗
