# Their Open Issues → Your Resume: Interview Cheat Sheet

> **Interview with Noah Hollmann** — Co-founder & CTO at Prior Labs
> ETH Zürich CS → Google (Machine Perception) → BCG → Charité MD PhD → Prior Labs
> His LinkedIn quote: *"The model is only half the product. The other half is the machine around it: training pipelines, evaluation, deployment, reliability, and developer experience."*

---

## 🔥 KILLER CONNECTIONS (Noah will notice these)

### 1. DARPA World Modelers → African Maize Yield Paper
Noah reshared a paper using TabPFN for **African crop yield prediction** (Halder et al., *Science of Remote Sensing* 2026). Your resume says you **competed in DARPA World Modelers to improve disaster resiliency and food security modeling in East Africa**.
**Script**: "I saw the Halder et al. maize yield mapping paper you shared — that's exactly the domain I worked in at DARPA World Modelers. We were building automated scientific models for food security in East Africa. I can immediately see how TabPFN would have transformed that work — we spent weeks on feature engineering for tabular agricultural data that TabPFN handles in seconds."

### 2. Causal Inference — He Flagged It as a Future Direction
Noah's Nature paper post asks: *"Where should tabular AI research focus next? Multi-modal fusion? **Causal inference**? Time series?"* He also reshared DoubleML's TabPFN integration (causal ML).
**Your angle**: Your Columbia research (CVAE + SHAP) does causal-adjacent work (Hessian-based feature attribution, regime-dependent attributions). Your DARPA work was explicitly about causal scientific models (DAGs for hydrology).
**Script**: "I noticed you flagged causal inference as a key future direction. My Columbia research derives stable per-feature attributions using Hessian-based recursive clustering — it's not full causal identification, but it's pushing toward understanding *why* a tabular model gives a particular answer, which I think is where TabPFN needs to go for high-stakes domains like healthcare and finance."

### 3. "The Machine Around the Model"
Noah's hiring post: *"training pipelines, evaluation, deployment, reliability, and developer experience"*
**Your entire resume is this**. Lead with:
- Containerized HPC clusters at supercomputer scale (TACC)
- Production web platform end-to-end (Homecastr, Summit Geospatial)
- CI/CD, Docker, Kubernetes, Terraform, Ray, monitoring & observability
- FastAPI serving + Postgres + Redis + Elasticsearch (PoliBOM)

---

## Noah's Background → Smart Questions for Him

| His experience | Your question |
|---|---|
| Google Machine Perception intern | "How does your experience with perception models inform TabPFN's architecture? The two-way attention seems very different from standard vision transformers." |
| BCG consulting on 5G spectrum auctions | "The auction theory background is interesting — does that influence how you think about the API pricing/credits model?" |
| MD PhD at Charité (precision medicine) | "Healthcare seems like a huge market for TabPFN — are you seeing clinical trial or patient outcome use cases? My Columbia CVAE work is on financial tabular data, but the patterns transfer." |
| €9M pre-seed, Balderton Capital | "With Yann LeCun on the advisory board and the Nature publication, you have incredible research credibility. What's the biggest engineering bottleneck in translating that to enterprise customers?" |

---

## Open Issues → Your Resume Match

### 🟢 STRONG MATCHES

#### GPU Memory & Inference Speed (#354, #523, #787)
**Their pain**: Memory grows per estimator; model reloads between fit/predict; slow feature importance
**Your line**: *"Scaled climate and flood models on supercomputers, orchestrating million-node distributed jobs across containerized HPC clusters"*
**Tech**: *CUDA; Docker; Kubernetes; Ray; Triton*
**Script**: "At TACC I managed GPU memory across multi-node jobs — tensor lifecycle and device placement were daily concerns. At Homecastr I keep models GPU-resident between fit/predict to avoid reload overhead, which is the same problem as your #523."

#### Batch Predictions for Large Datasets (#125)
**Their pain**: Need to warn/batch when test set is large
**Your line**: *"semi-supervised VAE on tabular property records"* — you process 500K+ row county-scale datasets
**Script**: "I chunk predictions to stay within GPU memory for large tabular datasets. I use PyArrow/Parquet for efficient serialization, which I notice your SageMaker integration already recommends."

#### CI/CD & Testing Infrastructure (#51, #513)
**Their pain**: Example tests disabled (CPU timeouts); need cross-repo testing
**Your line**: *Infrastructure: CI/CD; monitoring & observability*
**Script**: "At TACC our HPC test suite had the same problem — CPU-only CI runners too slow for GPU workloads. I've used GH Actions caching for large artifacts and test timeout strategies."

#### API vs Local Feature Parity (tabpfn-client #213)
**Their pain**: API and local TabPFN differ, not documented
**Your line**: *"schema definitions... FastAPI serving"*
**Script**: "At PoliBOM our API and local SDK had to maintain parity. Pydantic schemas shared between client and server — which you already do via `tabpfn_common_utils` — plus automated comparison tests."

#### Tabular Data Expertise (core product alignment)
**Your lines**:
- *"semi-supervised VAE on **tabular property records**"* (Homecastr)
- *"CVAE latent factor model for **tabular financial data**"* (Columbia)
- *"oppsAlert: property-level ML model using 15,000+ individual homeowner protest records"*
**Script**: "I've spent years on tabular prediction — real estate, financial, geospatial. Mixed types, missing data, feature engineering. TabPFN is fascinating because it sidesteps feature engineering entirely via in-context learning."

#### Dependency & Build Tooling (PR #217)
Oscar Key's open PR switching to `uv`, merging CI jobs
**Your tech**: *Python; Docker; Git; CI/CD*
**Script**: "I've been using `uv` myself — massive speedup. I also use `ruff` and `pre-commit`, same as your stack."

---

### 🟡 NEAR-MATCHES (fallback script)

#### Multi-Device Inference (#684)
**Closest**: Ray distributed inference at TACC; multi-GPU training
**Script**: "I haven't built a multi-device inference engine for a transformer specifically, but I've used Ray to distribute inference across GPU nodes at TACC. How are you handling the single vs multi-device split — DataParallel, or something custom for TabPFN's context window?"

#### Architecture Registry (#781)
**Closest**: Plugin patterns in PoliBOM (Airflow DAGs, schema-driven)
**Script**: "I haven't implemented a model architecture registry, but at PoliBOM our Airflow DAGs use a plugin pattern where new task types register themselves. How are you managing backward compatibility when architectures change?"

#### Causal Benchmarks (Noah's interest)
**Closest**: DARPA World Modelers (causal scientific models with DAGs for hydrology), Columbia SHAP work
**Script**: "I haven't worked with specific causal benchmarks like ITE estimation, but my DARPA work was explicitly about causal scientific models — DAGs for hydrology in East Africa. At Columbia I push toward causal-adjacent feature attribution. I'd be excited to learn what causal direction you're exploring — is it more about treatment effect estimation, or about learning the causal graph from TabPFN's representations?"

---

### 🔴 GAPS (honest "I don't know" answers)

#### Conformal Prediction (#231 PR)
**Script**: "I haven't implemented conformal prediction, but my Homecastr fan charts are uncertainty-aware — prediction intervals from diffusion model samples. I'd be interested in how TabPFN's bar distributions compare to conformal methods."

#### Error-Correcting Codes for Many-Class (#107)
**Script**: "I haven't used error-correcting output codes. My classification tasks have been binary or low-cardinality. The hierarchical approach sounds more intuitive — can you tell me more about why the class limit exists?"

---

## 5 Questions to Ask Noah

1. **"You mentioned the machine around the model — what's the biggest engineering bottleneck right now? Training pipeline, serving latency, or DX?"** *(Maps to his exact LinkedIn framing)*

2. **"The Halder et al. maize yield paper showed TabPFN matching XGBoost with way less data in Africa. Are you seeing similar patterns in healthcare or finance?"** *(Shows you read his reshares AND connects to your DARPA work)*

3. **"TabPFN Scaling Mode removes the dataset size limit — is that pushing you toward different serving infrastructure than the original small-data regime?"** *(Shows you understand the product evolution)*

4. **"You reshared the DoubleML + TabPFN integration for causal ML — is that a direction Prior Labs is investing in, or more community-driven?"** *(Probes his causal interest directly)*

5. **"What does a typical week look like for the cloud platform engineer? Is it more greenfield infrastructure, or optimizing what exists?"** *(Practical role question)*

---

## Noah's Own Words to Echo

- *"No more fragile task-specific pipelines"* → You can validate this from your own experience: "At TACC and Homecastr, I've built exactly those fragile pipelines. The appeal of a foundation model that eliminates per-task tuning is immediately clear to me."
- *"Seconds vs. hours/days of tuning"* → "My Homecastr VAE takes hours to retrain monthly. If TabPFN gives comparable results in seconds, that changes the entire deployment architecture."
- *"2.5M+ downloads"* → Demonstrates scale of the developer experience problem you'd help solve
