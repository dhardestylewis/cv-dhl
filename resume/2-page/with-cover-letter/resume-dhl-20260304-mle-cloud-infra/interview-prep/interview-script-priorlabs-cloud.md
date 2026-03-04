# Prior Labs — ML Engineer, Cloud Platform — Interview Script

> ⏰ **Thu Feb 26, 2026 · 8:30–8:50am EST** · Google Meet: meet.google.com/htr-aupy-dsp
>
> **Interviewer**: Noah Hollmann — Co-founder & CTO · ETH CS · ex-Google (Machine Perception) · ex-BCG · MD PhD (Charité)
>
> **Format**: Informal conversation — get to know each other, learn about your background, share about Prior Labs and the role. *No special prep needed per Noah's email.*

---

## Your 2-min Intro (keep tight — it's a 20-min call)

> Hi Noah, thanks for reaching out — I'm really excited about this conversation.
>
> I'm Daniel Hardesty Lewis. I'm a full-stack ML engineer and founder finishing my Master's at Columbia. For the past eight years I've been building data-intensive infrastructure — ML training pipelines, distributed compute, production APIs — primarily in geospatial and tabular domains.
>
> The throughline of my work is taking research-grade models and shipping them as reliable, scalable production systems — which is exactly what the Cloud Platform role describes.

---

## Key Talking Points (mapped to the role)

### 1. Infrastructure at Scale — TACC & TDIS

> At the Texas Advanced Computing Center, I was the Senior Data Scientist and Technical Lead on the **$40M Texas Disaster Information System**. I designed and ran **million-node distributed jobs** on leadership-class supercomputers, managed **multi-million-dollar compute budgets** across NOAA, NSF, the Army Corps, and the Texas General Land Office.
>
> Concretely, this meant:
> - Orchestrating **containerized HPC clusters** for climate and flood model training
> - Building **data pipelines** that ingested, processed, and served terabyte-scale geospatial data
> - Owning the full ML lifecycle from data ingestion through model deployment and monitoring
> - Authoring **inter-agency RFP and MOU frameworks** — translating technical requirements into scopes across six partners
>
> **Why this maps to Prior Labs**: You need someone who can architect and operate the infrastructure that takes TabPFN from research to production. I've done exactly that — taking research models and building the pipelines, serving, and monitoring around them at scale.

### 2. Tabular Data — Direct Experience

> I have direct, hands-on experience with **tabular data** workloads:
>
> - At **Homecastr**, I deployed a **semi-supervised VAE on tabular property records** (tax, sales, permits) handling sparsity and noise in structured data — achieving 12% holdout error. Then shipped a **diffusion-based forecasting system** with uncertainty fan charts, production-served via FastAPI + React.
> - At **Columbia**, I developed a **multi-asset CVAE latent factor model** for tabular financial data with Skew-T Mixture priors — 85% R² vs. 75% for commercial SaaS.
> - At **PoliBOM**, I specified an agentic workflow with **Airflow, Elasticsearch, embeddings, and FastAPI** backed by Supabase and Redis — structured data pipelines end-to-end.
>
> **Why this maps to Prior Labs**: I'm not just an infrastructure person — I understand the *data* that flows through the pipes. Tabular data is exactly the domain I've been building in.

### 3. Cloud & Production Systems

> - **Docker, Kubernetes, Terraform** — containerized deployments across cloud and HPC environments
> - **Python/FastAPI** — production APIs for model serving (Homecastr, PoliBOM)
> - **Postgres, Redis, Elasticsearch, BigQuery** — production data stack
> - **CI/CD, monitoring, observability** — standard practice across all my projects
> - **Ray, Dask, Airflow** — distributed orchestration
>
> I've also worked with **Triton** for model serving and **CUDA/C++** for performance-critical workloads.

### 4. Technical Leadership

> - **Primary technical POC** between engineering, Texas Emergency Management, and first-responder agencies on TDIS
> - **Mentored engineers** — Petrobras geoscientists in deep learning & HPC, junior data scientists
> - **Taught graduate courses** — ML for the Geosciences, Scientific Computation (C++, CUDA, HPC) at UT Austin
> - **Founded three ventures** — end-to-end ownership from architecture through product delivery

---

## Questions to Ask Noah

### About the Role & Team
1. **What does the current cloud infrastructure look like?** What stack are you running (cloud provider, orchestration, serving framework)? What's the biggest infrastructure pain point right now?
2. **How does the ML Engineer, Cloud Platform role interact with the research team day-to-day?** How tightly coupled is model iteration with infra changes?
3. **What does "production" look like for TabPFN today?** Is it API-served, SDK-distributed, or both? What's the serving latency target?

### About Prior Labs
4. **You mentioned scaling TabPFN to 10M rows with Scaling Mode — what were the hardest infrastructure challenges in enabling that?**
5. **What's the split between inference serving vs. training infrastructure work?** Where do you anticipate the most infra investment in the next 6-12 months?
6. **You're commercializing across finance and healthcare — do enterprise deployments look like hosted API or on-prem/VPC?** That has big infra implications.

### About Noah (rapport-building)
7. **You went from ETH CS → Google Machine Perception → BCG → med school → founding Prior Labs — what was the moment you decided to go all-in on tabular foundation models?**
8. **The XPRIZE experience with Saffron Safety is fascinating — building AI for wearables in Mumbai. How did that shape how you think about product engineering?**

---

## Things to Know About Prior Labs

| Fact | Detail |
|------|--------|
| **Product** | TabPFN — tabular foundation model, now v2.5 |
| **Core claim** | 2.8 sec inference beats CatBoost tuned 4 hours (5,000× speedup) |
| **Training approach** | Pre-trained on 130M+ synthetic datasets generated from causal graphs |
| **Architecture** | Two-way attention (across features within a row, across samples within a column) |
| **Published** | Nature (2024) |
| **Traction** | 2.5M+ downloads, 5,500+ GitHub stars |
| **Funding** | €9M pre-seed led by Balderton Capital |
| **Team** | ~20 people, from 5,000+ applicants |
| **SAB** | Yann LeCun, Bernhard Schölkopf |
| **Investors/angels** | Thomas Wolf (HuggingFace), Edward Grefenstette (DeepMind), Robin Rombach (Black Forest Labs) |
| **Key verticals** | Finance, healthcare, insurance, industrials |
| **New hire** | Philipp Singer — Kaggle Grandmaster, held #1 global rank |
| **Location** | Berlin, Freiburg, San Francisco, NYC |

---

## 🎯 Delivery Guide

| Tip | Detail |
|-----|--------|
| **Keep it tight** | 20-min call. You'll have ~5 min to talk about yourself, ~5 min Q&A, ~10 min for Noah to share. |
| **Lead with infra** | This is a *cloud platform* role. Lead with your infrastructure and production systems experience, not research. |
| **Show tabular fluency** | Mention your VAE on tabular property records, CVAE on financial data, the diffusion model. You understand the data domain. |
| **Reference their work** | Mention the Nature paper, TabPFN v2.5, Scaling Mode, the Forbes $600B article. Shows you've done homework. |
| **Be genuine** | Noah's email said "no need to prepare anything" — he wants to see if you're a fit, not test you. Be conversational. |
| **NYC angle** | The role lists NYC as a location. Mention you're based in New York. |
| **Frame correctly** | You're not pivoting to ML infra. You've *been doing* ML infra at supercomputer scale. You're bringing that to a startup. |
