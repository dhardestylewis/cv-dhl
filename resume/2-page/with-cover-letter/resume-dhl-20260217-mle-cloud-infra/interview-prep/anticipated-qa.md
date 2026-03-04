# Anticipated Q&A — Noah Hollmann Interview

> Prep your answers out loud. Keep each answer under 60 seconds.

---

## "Tell me about yourself"

> I'm Daniel Hardesty Lewis — full-stack ML engineer and founder finishing my Master's at Columbia. For 8 years I've been building data-intensive infrastructure: distributed compute at TACC, ML training pipelines, production APIs. The throughline is taking research-grade models and shipping them as reliable production systems — which is exactly what this role describes. I've also worked specifically with tabular data: VAEs on property records at Homecastr, CVAE factor models on financial data at Columbia.

---

## "Why Prior Labs?"

> Three reasons. First, you're doing something genuinely novel — you've built the first foundation model for tabular data that actually beats tuned tree ensembles, published in Nature. That's a real technical moat. Second, the infrastructure challenge is exactly my sweet spot — taking a transformer that does in-context learning and making it serve millions of API calls reliably. Third, the team is incredibly small and selective, and I thrive in environments where I own large surface area end-to-end.

---

## "What's your experience with cloud infrastructure?"

> At TACC I managed HPC compute across multiple agencies — containerized clusters, million-node jobs, multi-million-dollar budgets. At Homecastr I built the full production stack: FastAPI model serving, Postgres/Redis, Docker, CI/CD, monitoring. At PoliBOM I specified the architecture for an agentic workflow with Airflow, Elasticsearch, and FastAPI. I've worked with Docker, Kubernetes, Terraform, and various orchestration tools across all of these.

---

## "What's your experience with ML serving / MLOps?"

> At Homecastr I built a diffusion-based forecasting system served via FastAPI with uncertainty fan charts — production model serving end-to-end. I've used Triton for inference serving. At TACC I owned the full ML lifecycle from data ingestion through model deployment and monitoring. I'm comfortable with the full stack: containerization, CI/CD, GPU resource management, observability.

---

## "Have you worked with tabular data specifically?"

> Yes, extensively. At Homecastr I built a semi-supervised VAE on tabular property records — tax data, sales, permits — handling sparsity and missing values in structured data. At Columbia I developed a multi-asset CVAE latent factor model on tabular financial datasets. I understand the unique challenges of tabular domains: heterogeneous feature types, missing values, outliers, mixed cardinality. Actually, those are the same challenges your paper describes TabPFN being designed to handle.

---

## "Do you have experience leading or mentoring?"

> Yes. I was primary technical POC on the $40M TDIS project across six agencies. I coordinated between engineering, Texas Emergency Management, and first-responder teams. I mentored Petrobras geoscientists in deep learning and HPC. I taught graduate courses at UT Austin in ML for Geosciences and Scientific Computation. And I've founded three ventures where I owned everything from architecture through product delivery.

---

## "What do you know about TabPFN?"

> I've read the Nature paper and the v2.5 report. The core insight is using in-context learning on synthetic tabular datasets — you train a transformer across millions of causal-graph-generated datasets so it learns a general prediction algorithm in a single forward pass. The architecture uses alternating row-column attention so it's permutation-invariant in both samples and features. v2.5 scales to 50K rows and 2K features, adds learned "thinking rows" for extra compute capacity, and introduces the distillation engine for production deployment.
>
> From the infrastructure side, what jumped out to me is the dual serving model — cloud API with rate limiting vs. local package with HuggingFace weights — and the distillation pipeline converting the transformer to MLPs or tree ensembles for low-latency production. Those are the kinds of serving problems I find most interesting.

---

## "What excites you about this role specifically?"

> The scaling challenge. You're going from 50K rows to millions — the paper mentions retrieval, fine-tuning, and new architectures. That means the serving infrastructure will need to evolve significantly: caching strategies, batching, multi-GPU orchestration, possibly asynchronous processing for large jobs. And the enterprise angle — GDPR compliance, on-prem/VPC deployments for healthcare and finance — adds real complexity. I want to be the person who builds that layer.

---

## "What's your salary expectation?" (if it comes up)

> [Redirect:] I'm flexible and more focused on the right role and team. I'd love to learn more about the compensation philosophy at Prior Labs — do you structure packages differently for your Berlin vs. NYC teams?

---

## "Do you have any questions for me?"

> *See cheat-sheet.md — 3 prepared questions*

---

## TRICKY SITUATIONS

**If Noah asks about something you don't know:**

> "I haven't worked with [X] directly, but here's the closest thing I've done: [analogy]. I'd be excited to learn it — can you tell me more about how you're using it?"

**If he asks about your timeline / other interviews:**

> "I'm actively interviewing, but Prior Labs is a top priority for me. I'm flexible on timeline."

**If he asks about relocation:**

> "I'm based in NYC, which is one of the listed locations. I'm also open to discussing other arrangements."
