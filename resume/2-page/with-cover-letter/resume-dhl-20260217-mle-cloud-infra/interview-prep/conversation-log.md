# Interview Prep Conversation Log — Prior Labs
### Feb 25, 2026

---

## Session Overview

Conversation with Antigravity preparing for interview with Noah Hollmann (Co-founder & CTO, Prior Labs) for the ML Engineer, Cloud Platform role. Interview: Thu Feb 26, 2026, 8:30–8:50am EST via Google Meet.

---

## What Was Done

### 1. Interviewer Research
- Saved Noah Hollmann's full LinkedIn profile and contact info to `interviewer-noah-hollmann.md`
- Key background: ETH Zurich CS → Google Machine Perception → BCG → MD PhD (Charité) → Co-founder/CTO Prior Labs
- Email: noah@priorlabs.ai
- Google Meet: meet.google.com/htr-aupy-dsp
- Reschedule link: https://you.ashbyhq.com/meeting/3daf83d0-89e6-4e65-8ce5-99ff482b9b88/

### 2. Interview Script Created
- Full interview script in `interview-script-priorlabs-cloud.md`
- 2-min intro, key talking points mapped to role requirements, questions to ask Noah, company facts, delivery guide

### 3. Downloaded Reference Materials
- `tabpfn-nature-paper.pdf` — arXiv version of the Nature paper (full PDF)
- `tabpfn-v2.5-paper.pdf` — v2.5 paper from arXiv (full PDF)
- `tabpfn-github-readme.md` — verbatim GitHub README
- `tabpfn-paper-docs-reference.md` — extracted highlights from Nature paper, API docs, and GitHub README with infrastructure notes

### 4. Deep Dive into Infrastructure
User asked: "what exactly is their infra?"

**What we know for sure:**
- Python — core language (job listing says Python/FastAPI)
- PyTorch + CUDA — TabPFN local package runs on GPU
- HuggingFace — model checkpoints hosted there (gated, non-commercial license for v2.5)
- Cloud API — hosted inference service with REST API + Python SDK (tabpfn-client)
- scikit-learn interface — `.fit()` / `.predict()`
- Flash attention in the model architecture
- Mintlify — docs platform

**What the job listing implies:**
- Docker + Kubernetes (required qualifications)
- Terraform (required)
- CI/CD pipelines
- GDPR-compliant data storage
- Monitoring & observability

**From the v2.5 paper:**
- **Model architecture**: 18 layers (regression) / 24 layers (classification) transformer
- **Alternating row-column attention**: each cell attends across its row (features), then down its column (samples)
- **64 learned "thinking rows"** — inspired by LLM attention sinks
- **Feature group size = 3** (up from 2 in v2)
- **Scaling**: O(r² × min(c,500) + r × min(c,500)²)
- **Memory**: on H100 80GB with FP16 + FlashAttention-3, fits ~160K rows × 500 features
- **Recommended hardware**: NVIDIA H100 or A100

**Production pipeline:**
- **TabPFN-as-MLP/Tree** — proprietary distillation engine, converts transformer → compact MLP or tree ensemble for low-latency production. This is the enterprise product.
- **KV-Cache**: `fit_mode='fit_with_cache'` stores training context during `.fit()` → fast `.predict()`. 6.1 KB GPU + 48.8 KB CPU per cell.
- **Multi-GPU parallelization** via `device` parameter
- **Cloud API**: rate-limited (100M credits/day), max 20M cells/request, response headers expose `X-RateLimit-*`

**Dependencies/stack:**
- PyTorch 2.8+, FlashAttention-3, einops, pydantic/pydantic-settings
- HuggingFace Hub for model weight hosting
- PostHog for product telemetry
- uv for development/packaging

**Team (from v2.5 paper Appendix A):**
- Model dev & Deployment: ~22 people (incl. Noah Hollmann, Frank Hutter)
- Distribution & Product: 4 people
- 53 GitHub contributors total

**Roadmap (from paper conclusion):**
> "The next step is scaling to datasets with millions of rows. We are actively developing new techniques — including retrieval, fine-tuning, and novel architectures."
> "Our broader vision... is to tackle the entire stack of problems with tabular-like data, including time series, multimodal tabular data, causal inference, unsupervised tasks..."

### 5. Colab Notebook Analysis
User shared the full TabPFN_Demo_Local.ipynb notebook. Key reveals:
- **Dual backend architecture**: `from tabpfn import TabPFNClassifier` (local) vs `from tabpfn_client import TabPFNClassifier` (cloud) — same sklearn interface, swappable
- **HuggingFace gated access**: requires HF token with gated repo permissions
- **tabpfn-extensions**: separate package for interpretability, unsupervised, embeddings
- **tabpfn-time-series**: separate package for time series forecasting
- **Text data handling**: only via client API (server-side NLP)
- **Capabilities beyond classification/regression**: imputation, anomaly detection, clustering, embeddings, SHAP, causal inference (econml)
- **Causal inference integration**: TabPFN as base learner in econml's SLearner and CausalForestDML
- **"Do-PFN"**: upcoming foundation model for causal inference
- **PostHog telemetry**: product analytics

### 6. Interview Format Discussion
User asked: "what exactly is my pitch? should i be prepping a presentation?"

**Answer: No presentation.** Noah's email said "no need to prepare anything — just bring yourself and any questions."

**Pitch in one sentence:**
> "I've spent 8 years building the exact infrastructure layer you need — taking research ML models and shipping them as production systems at scale — and I've done it specifically with tabular data."

**Three standout points:**
1. ML infra at scale (TACC, TDIS, million-node HPC, multi-million-dollar compute)
2. Tabular data fluency (VAE on property records, CVAE on financial data, structured data pipelines)
3. End-to-end ownership (3 ventures, full stack, small team operator)

### 7. Prep Materials Created
- **`cheat-sheet.md`** — one-page glanceable reference for during the call (pitch, 3 key points, 3 questions, their infra summary, reminders)
- **`anticipated-qa.md`** — 9 most likely questions Noah will ask with pre-written <60 sec answers, plus tricky situation handlers (salary, timeline, don't-know-the-answer)

Format decisions:
| Format | Decision | Reason |
|--------|----------|--------|
| Presentation/slides | ❌ Skip | Noah said "just bring yourself" |
| Speaker notes | ❌ Skip | No presentation to annotate |
| Full interview script | ✅ Done | `interview-script-priorlabs-cloud.md` |
| One-page cheat sheet | ✅ Done | Glanceable during call |
| Anticipated Q&A | ✅ Done | Rehearse out loud |
| Deep reference | ✅ Done | PDFs + extracted notes |

### 8. Alan Arazi Follow-Up
User asked whether to message Alan Arazi on LinkedIn (who directed him to apply via careers page on Feb 17).

**Answer: Yes, send a short thank-you:**
> Hey Alan! Just wanted to let you know I got an interview with Noah on Thursday — really appreciate the nudge to submit through the careers page. Thanks again! 🙌

Keep it brief. Don't over-explain, don't ask him to advocate, just close the loop.

---

## Key Questions Still Unanswered (for the interview)
1. Which cloud provider? GCP, AWS, Azure?
2. How is serving done — Triton, vLLM, custom FastAPI, something else?
3. Is training on their own infra or rented GPU clusters?
4. How is the API gateway structured — queue/async for large jobs?
5. What's the monitoring stack — Datadog, Prometheus/Grafana?
6. Enterprise deployments: hosted API or on-prem/VPC?

---

## Final Directory Structure
```
resume-dhl-20260217-priorlabs-cloud/
├── job-listing.md
├── resume-dhl-20260217-priorlabs-cloud.tex
├── resume-dhl-20260217-priorlabs-cloud.pdf
├── interview-prep/
│   ├── cheat-sheet.md
│   ├── anticipated-qa.md
│   ├── interview-script-priorlabs-cloud.md
│   ├── interviewer-noah-hollmann.md
│   └── conversation-log.md          ← this file
└── reference/
    ├── tabpfn-nature-paper.pdf
    ├── tabpfn-v2.5-paper.pdf
    ├── tabpfn-github-readme.md
    └── tabpfn-paper-docs-reference.md
```

---

## Email Draft (not yet sent — Gmail auth blocked)
Short reply to Noah confirming the interview:
> Subject: Re: [interview confirmation]
> Hi Noah, looking forward to our conversation on Thursday! I've been reading through the Nature paper and API docs — really impressive work. See you at 8:30am EST. Best, Daniel
