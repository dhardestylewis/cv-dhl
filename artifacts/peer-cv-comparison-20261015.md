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

## Implications for the CV

1. The Worldcastr benchmark preprint and the Hugging Face and GitHub releases prepared under the credit-request package would close the two largest gaps (open-source release, benchmark authorship) once approved for publication.
2. The CV already names Frontera and 1M-node jobs; the two-pager's Technologies block should add the supercomputer names and the diffusion and calibration vocabulary explicitly.
3. Vocabulary to adopt where it is true of Worldcastr's evaluation: CRPS, ensemble spread and skill, spectra. Do not claim it until the scoring code reports it.
