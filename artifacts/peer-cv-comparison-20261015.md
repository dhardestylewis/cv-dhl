# Peer CV comparison, 2026-10-15

Purpose: compare Daniel's skills and credentials against public CVs of people at and above his level at the places he should consider from where he stands now (spatiotemporal and earth-system foundation models, housing and energy forecasting, physical-world AI founders, frontier labs). Collected by a research subagent using only pages it fetched. LinkedIn was not used. Google Scholar returned HTTP 429, so two DeepMind pages (Rémi Lam, Chris Brown) are omitted except by title.

## Peers fetched

| # | Person, title, org | Page | Skills, tools, domains listed | Education |
|---|---|---|---|---|
| 1 | Ilan Price, Senior Research Scientist, Google DeepMind (GenCast) | https://ilanprice.github.io/ | Probabilistic weather forecasting; sparse and efficient deep nets; adversarial robustness; ICML/ICASSP first-author | DPhil Mathematics, Oxford |
| 2 | Cristian Bodnar, Founding Member, Prometheus; Silurian cofounder; ex-MSR Aurora co-lead | https://cbodnar.com/ | Earth-system foundation model (Aurora, Nature 2025); topological deep learning, GNNs, sheaf diffusion, neural ODEs; MSR, Twitter Cortex, Google Brain, Google X | PhD Cambridge, MSR PhD Fellowship |
| 3 | Jaideep Pathak, Senior Research Scientist, NVIDIA Earth-2 | https://www.alphaxiv.org/@jaideep-pathak | FourCastNet (AFNO), spherical Fourier neural operators; diffusion downscaling (CorrDiff), DiffObs; score-based and ETKF data assimilation; CRPS and lagged-ensemble benchmarking | PhD Physics, UMD; NERSC postdoc |
| 4 | Peter Harrington, Sr Scientific ML Software Engineer, NVIDIA Earth-2 (ex-NERSC) | https://cai.ieee.org/2023/peter-harrington/ | Deep learning on supercomputers; DL software stack benchmarking at NERSC; scaling FourCastNet | MS Scientific Computing, UCSC |
| 5 | Jayesh K. Gupta, Founder and CEO, Silurian AI (YC S24) | https://silurian.ai/about | ClimaX co-lead, Aurora co-author; generative forecasting transformer; energy-sector deployments | PhD CS, Stanford 2020 |
| 6 | Ryan Keisler, Cofounder and Chief Scientist, Brightband | https://rkeisler.github.io/ | Physics plus statistics plus ML on sensor data; solo GNN global weather paper, open-sourced; remote sensing; Chief Scientist, Descartes Labs | Cosmology PhD-track (degree not stated) |
| 7 | Daniel Rothenberg, Cofounder, Head of Data and Weather, Brightband | https://danielrothenberg.com/ | Python, Spark/dask/MPI, Prefect/Airflow/Argo, TensorFlow/PyTorch/JAX, CNN and Transformer models for remote sensing and weather, Cython/Numba, Julia, Fortran, C/C++/CUDA, Kubernetes/Helm, GEOS-Chem, CESM, WRF, GCP/AWS, NCAR/NERSC/ORNL supercomputers; Pangeo founder; Waymo Staff SWE; Tomorrow.io Chief Scientist | PhD Atmospheric Science, MIT; NSF GRFP |
| 8 | Prasanna Balaprakash, Cofounder and CEO, PrimaLabs; ex-Director of AI Programs, ORNL | https://pbalapra.github.io/ | Trillion-parameter training on Frontier (49,152 GPUs); ORBIT 113B ViT climate model (Gordon Bell finalist); DeepHyper AutoML; graph foundation models | PhD Engineering Sciences, ULB; DOE Early Career |
| 9 | Mike Pritchard, Director of Climate Simulation Research, NVIDIA; Assoc. Prof. UCI | https://sites.ps.uci.edu/pritchard/ | Global atmospheric simulation, HPC, ML emulation of convection; ClimSim (NeurIPS D&B outstanding paper); CorrDiff; causally-informed DL | Professor |
| 10 | Rahul Ramachandran, Senior Data Science Strategist, NASA MSFC (Prithvi) | https://www.alphaxiv.org/@rahul-ramachandran | Informatics and ML for massive geospatial data; Prithvi-EO-2.0 (temporal and location embeddings, GEO-Bench); TerraMind; satellite remote sensing | Not stated |
| 11 | Tung Nguyen, final-year PhD, UCLA (ClimaX, Stormer); interned NVIDIA Earth-2, DeepMind, MSR | https://tung-nd.github.io/ | Foundation models for weather and climate; transformer neural processes; ChaosBench; ICML/NeurIPS/ICLR papers, three best-paper awards | PhD CS, UCLA 2026 |
| 12 | Sheridan Grant, Applied Scientist, Zillow | https://sheridanlgrant.github.io/ | Causal inference and ML for housing economics (Zillow Offers underwriting); experimentation platform; energy-systems and carbon modeling (E3) | PhD Statistics, UW 2021 |
| 13 | Mimi Sun, Google Research (PDFM co-author) | https://research.google/people/mimisun/ | GNN location embeddings (PDFM) across 27 tasks; TimesFM coupling; differential privacy; Gemini-powered geospatial agent with benchmarks | Not stated |
| 14 | Dibya Ghosh, MTS pretraining, Anthropic; Mo Tiwari, MTS, OpenAI | https://dibyaghosh.com/about, https://motiwari.com/ | Ghosh: RL, optimization, goal-conditioned policies, Google Brain residency, NSF GRFP. Tiwari: adaptive sampling algorithms, security engineering lead, quant research | PhD CS Berkeley; PhD CS Stanford |

## Skills on three or more peer CVs that Daniel's documents do not list

Add only those he has actually used; otherwise treat as a learning list.

- Graph neural networks for spatial fields (Keisler, Bodnar, Sun; GraphCast and GenCast are graph-based)
- Neural operators (AFNO, SFNO) and Fourier-domain architectures (Pathak, Harrington, Pritchard)
- Transformer and ViT pretraining at scale, including masked autoencoding and location or time embeddings (Rothenberg, Balaprakash, Nguyen, Ramachandran)
- Atmospheric and climate model stack: ERA5, HLS, numerical weather prediction, data assimilation (Rothenberg, Pathak, Pritchard, Keisler)
- Ensemble verification vocabulary: CRPS, lagged ensembles, spectra (Pathak, Price, Pritchard, Nguyen)
- Satellite remote sensing and Earth observation (Keisler, Ramachandran, Rothenberg, Nguyen)
- Distributed training at thousands of GPUs: MPI, DeepSpeed, scaling studies (Rothenberg, Balaprakash, Harrington)
- JAX (Rothenberg; DeepMind models are JAX-native)

## Skills Daniel already has that these CVs also emphasize

Foreground these in the two-pager's Core Expertise and Technologies blocks.

- Diffusion models and score-based sampling (Pathak, Price, Pritchard)
- Supercomputer-scale HPC, CUDA, C++ (Harrington, Balaprakash, Rothenberg, Pathak)
- Calibration and uncertainty: PIT, coverage, sharpness (Price, Pathak, Nguyen)
- Causal inference (Grant, Pritchard, Pathak)
- Kubernetes, Airflow, Dask, Spark production stack (Rothenberg)
- Geospatial data engineering and PostGIS-style indexing (Ramachandran, Sun)
- LLM agents over geospatial tools (Sun, Nguyen)

## Credentials and signals they carry that Daniel lacks

- PhD on 10 of 14 pages
- First-author papers at ICML, NeurIPS, ICLR or Nature; or one high-citation solo arXiv (Keisler)
- Named open-source model or framework releases (FourCastNet, ClimaX, Prithvi-EO-2.0, DeepHyper, Pangeo)
- Public benchmark authorship (ClimSim, ChaosBench, GEO-Bench, lagged-ensemble CRPS)
- Fellowships and prizes (NSF GRFP, MSR PhD Fellowship, Amazon Fellowship, DOE Early Career, Gordon Bell finalist)
- Frontier-lab internships or residencies on 5 pages
- A founder already shipping to energy customers (Gupta; Keisler and Rothenberg)
- An itemized technical-skills section naming supercomputers and tools (Rothenberg); others let a publication list carry the signal

## Second pass: best-in-class comparables (14 more, fetched 2026-10-15)

| # | Person, title, org | Page | What they list | Education |
|---|---|---|---|---|
| 15 | Rémi Lam, Staff Research Scientist, Google DeepMind | https://orc.mit.edu/calendar_event/lam26/ | GraphCast, GenCast, FGN, DGMR; GNNs, diffusion, functional generative nets; model-validation pitfalls; Science Breakthrough runner-up 2023; Nature's 10 (2024) | PhD CSE, MIT |
| 16 | Paris Perdikaris, Assoc. Prof. Penn; Aurora co-lead | https://penntoday.upenn.edu/news/cloudy-chance-lifesaving-and-more-cost-effective-weather-predictions | Aurora (Nature 2025): pretrained on 1M+ hours of geophysical data, fine-tuned to air quality, waves, cyclones; GPU-parallel | Not on page |
| 17 | Christopher F. Brown, Research Engineer, Google DeepMind | https://arxiv.org/abs/2507.22291 | AlphaEarth Foundations: 10 m global embedding field, optical, radar, lidar, climate sims; 64-dim, annual layers 2017 to 2024 in Earth Engine; tested with 50+ organizations | Not on page |
| 18 | Karthik Kashinath, Principal Engineer and Scientist, NVIDIA Earth-2 | https://developer.nvidia.com/blog/author/kkashinath/ | FourCastNet, Earth-2; spherical Fourier neural operators, generative super-resolution, hindcast validation; DOE, NOAA, NWS users | PhD Cambridge |
| 19 | Aditya Grover, Asst. Prof. UCLA; CTO Inception | https://aditya-grover.github.io/ | ClimaX, Stormer (beat GraphCast; best paper CCAI at ICLR 2024), Mercury diffusion LLMs; NSF CAREER, Schmidt AI2050 | PhD Stanford |
| 20 | Johannes Jakubik, Research Scientist, IBM Research Europe | https://research.ibm.com/people/johannes-jakubik | Prithvi-EO-1.0/2.0, Prithvi-WxC-1.0-2300M (MERRA-2, 160 variables), TerraMind, TerraTorch; HF cards and Spaces; ICCV, CVPR; NASA Agency Group Award | PhD KIT and ETH |
| 21 | Gautam Prasad, SWE, Google Research (PDFM) | https://research.google/blog/insights-into-population-dynamics-a-foundation-model-for-geospatial-inference/ | PDFM: self-supervised GNN over counties and ZIPs; tasks interpolation, extrapolation, forecasting, super-resolution; baselines SatCLIP, GeoCLIP, IDW, ARIMA; 29-variable benchmark; embeddings dataset and Colab recipes | Not on page |
| 22 | Stan Humphries, former Chief Analytics Officer, Zillow | https://www.cxotalk.com/bio/stan-humphries-chief-analytics-officer-zillow-group | Zestimate creator; nightly runs at scale; median error 14% to 5% | PhD UVA |
| 23 | Daryl Fairweather, Chief Economist, Redfin | https://www.dallasfed.org/people/fed/councils/academic/fairweather | US housing, behavioral economics; Dallas Fed advisory council | PhD Economics, Chicago |
| 24 | Abe Stanway, co-founder and CTO, Amperon | https://www.amperon.co/blog/introducing-amperon | Smart-meter load and net-load forecasting: 76M+ meters, 5-minute settlements, PJM, CAISO, MISO, ERCOT; 15-day sub-hourly; probabilistic solar and wind; cnMAE; public accuracy calls vs ERCOT | Not on page |
| 25 | Max Kanter, CEO, Grid Status | https://www.gridstatus.io/about | Open US grid data and analytics; wholesale-market design; cited by FT, Bloomberg, NYT, Dallas Fed; $8M round | Not on page |
| 26 | Nikhil Shankar, co-founder, Silurian AI (YC S24) | https://silurian.ai/blog/gft-api-announce | GFT: 1.5B parameters, 14-day global at about 11 km, hourly; up to 30% better than NOAA and ECMWF; Earth API with Python and TypeScript SDKs; full-year 2023 evaluation vs stations, HRES, GraphCast, HRRR, ICON; 100 m wind and GHI for energy | Left applied-math PhD |
| 27 | Marvin Gabler, Founder and CEO, Jua | https://jua.ai/blog/scaling-ai-weather-models/ | EPT-2 family; 1,000+ H100 training, 100+ TB/hour ingest, petabytes of observations; FSDP/DDP, BF16, Rust serving, Slurm on Kubernetes; public skill table vs GenCast, Aurora, FourCastNet 3, HRES; customers Shell, EDF, Hydro-Quebec, Vitol | RWTH dropout |
| 28 | Tejal Patwardhan, Researcher, OpenAI, frontier evals lead | https://www.alphaxiv.org/@tejal-patwardhan | GDPval, PaperBench (8,316 gradable tasks, judge benchmark, open code), MLE-bench, SWE-Lancer; system cards | BA Statistics, Harvard |

Planet Labs chief scientist: no usable page found. Google Scholar returned 429 throughout.

## The bar: what the Worldcastr entry must contain to read at their level

Scored against Worldcastr's own verified record (preprint claims ledger of 2026-10-13, evidence scoreboard of 2026-10-07, release package). "Have" means a durable record supports the claim today.

| # | Bar, and who sets it | Worldcastr status | What can be written now |
|---|---|---|---|
| 1 | Named, versioned model with parameters, resolution, horizon (Silurian GFT 1.5B, Jua EPT-2, Prithvi-WxC-2300M) | Partial. Name FMTSFlow and origin-specific checkpoints per information cutoff 2019 to 2023 are in the repo registry; parameter count not in any record I read | Name and cutoffs; tract and county resolution; 1 to 4 year scored horizons. No parameter count |
| 2 | Training-data scale in concrete units (Aurora 1M+ hours, Jua petabytes, AlphaEarth 10 m global) | Have, with caveat (manifest on R2 not re-read on 2026-10-13) | 388,106,452-row panel, 16 jurisdictions, 4 countries, 32-target registry |
| 3 | Compute scale and stack (Jua 1,000+ H100, FSDP, Rust) | Not in hand for FMTSFlow | Nothing for Worldcastr; TACC-era 1M-node jobs stay under TACC |
| 4 | Scored comparison vs named incumbents under a fixed protocol with ground truth and period (Silurian vs HRES over 2023; PDFM vs SatCLIP, ARIMA) | Have, pre-registered, county-clustered bootstrap, but the 2020 county test is not information-matched (ledger C1, abstract) | 59.8% [58.4, 61.1] of 3,134 counties vs 18 published sources on 2020 Census counts; 54.9% of 11,466 tract cells vs 30 agencies, 44 vintages; must carry the information-matching caveat and that state demographers win at county (47.0%) |
| 5 | Benchmark as a product: task count, gradable units, leaderboard, scorer code, pre-registration (PaperBench, MLE-bench) | Have as a package, not public | 131 agency sources, 3,065 files, 27 normalized publication-dated vintages (6.96M native rows); three pre-registration records; GitHub scorer with leaderboard file and tests |
| 6 | Release URLs: arXiv ID, HF dataset and model card, GitHub, Colab (AlphaEarth, Prithvi, PDFM) | Prepared, none uploaded; arXiv id pending; publication needs Daniel's approval | "Prepared for release" only |
| 7 | Named architecture components with lineage (Lam: GNN, diffusion, FGN) | Have for the parcel model (diffusion, DDIM, spatial inducing tokens); FMTSFlow internals not read | Keep the existing architecture bullet |
| 8 | Downstream task list with per-task metric (PDFM four tasks; Aurora three) | Have | Population, households, housing units, occupied units at tract and county, 1 to 4 years; parcel value 1 to 4 years |
| 9 | Production evidence: API, cadence, named customers (Silurian Earth API; Amperon 15-day) | Partial | Homecastr serving at roughly 14M weekly requests (July resume); API-only model card drafted; no named customers, discovery only |
| 10 | External validation: venue, award, press, partner count (AlphaEarth 50+ orgs; GraphCast Science runner-up) | Not yet | PAA ADC abstract due 2026-11-07; a16z and MetaProp feedback is the only external marker |

## Draft Worldcastr entry at that bar (not yet applied to the CV)

Blurb unchanged. Bullets, each sourced to the ledger row in brackets:

- Trained FMTSFlow, a multi-target spatiotemporal forecaster, on a 388M-row panel of real public data across 16 jurisdictions in 4 countries and 32 targets (population, households, housing, rents, home values, income, employment, migration), one checkpoint per information cutoff, 2019 to 2023. [B4, A3, A4]
- Built a pre-registered benchmark scoring published U.S. projections against 2020 Census counts with county-clustered bootstrap intervals: 59.8% county win rate vs 18 agency and national sources (3,134 counties); 54.9% at tract vs 30 agencies and 44 vintages; held-flat and gradient-boosted baselines reported alongside; information-matched 2025 test under way. [C1, C2, C11, C14]
- Assembled the publication-dated archive behind it (131 agency sources, 3,065 files, 27 normalized vintages) and packaged an arXiv preprint, Hugging Face dataset, GitHub scorer with leaderboard, and API model card for release. [B1, B2, release/]
- Built a parcel-scale diffusion forecaster on 50M+ parcel-year observations: 7.0% one-year error, competitive with Zillow's valuation accuracy on a harder forward-looking task; 12.6% MdAE at 4 years, NYC. [July resume]
- Engineered spatial inducing tokens, per-horizon loss normalization, and DDIM sampling; validated via PIT uniformity, interval coverage, and sharpness before web delivery. [July resume]
- Owned the pipeline from data ingestion to real-time serving through the first product, Homecastr (roughly 14M production requests weekly); refined product strategy through direct feedback from a16z and MetaProp. [July resume]

Moves to Key Projects: the LLM chat engine with 30+ function-calling tools.

Assumptions to overturn: that FMTSFlow is the name to use publicly; that "information-matched 2025 test under way" is acceptable on a handout; that the 388M-row figure may be cited although the R2 manifest was not re-read on 2026-10-13.

## Implications for the CV

1. The Worldcastr benchmark preprint and the Hugging Face and GitHub releases prepared under the credit-request package would close the two largest gaps (open-source release, benchmark authorship) once approved for publication.
2. The CV already names Frontera and 1M-node jobs; the two-pager's Technologies block should add the supercomputer names and the diffusion and calibration vocabulary explicitly.
3. Vocabulary to adopt where it is true of Worldcastr's evaluation: CRPS, ensemble spread and skill, spectra. Do not claim it until the scoring code reports it.
