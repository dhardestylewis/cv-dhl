# Prior Labs Stack — Reverse-Engineered from Source Code

All findings below are backed by source code downloaded locally:
- [tabpfn-client repo](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client) (full clone)
- [TabPFN examples](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/source-code) (downloaded scripts)
- [TabPFN_Demo_Local.ipynb](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/source-code/TabPFN_Demo_Local.ipynb)

---

## Cloud Provider: Google Cloud Platform + AWS SageMaker ✅

| Evidence | File | Line |
|----------|------|------|
| `class GCPOverloaded(Exception)` — "Google Cloud Platform service is overloaded or unavailable" | [client.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L70-L76) | L70-76 |
| Server returns `error_class: "GCPOverloaded"` during predict | [client.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L636-L637) | L636-637 |
| Model weights hosted at `storage.googleapis.com/tabpfn-v2-model-files/` | TabPFN main repo, `model_loading.py` | (read via URL) |
| **AWS SageMaker enterprise endpoint** — full deployment example with `boto3` | [sagemaker.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/source-code/tabpfn--sagemaker.py) | L1-410 |
| SageMaker code recommends **Arrow/Parquet** for larger datasets | [sagemaker.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/source-code/tabpfn--sagemaker.py#L93-L94) | L93-94 |

> [!IMPORTANT]
> They run a **dual-cloud strategy**: GCP for their own API (`api.priorlabs.ai`), AWS SageMaker for enterprise customers deploying in their own accounts. This is a key infrastructure insight for the interview.

## API Architecture

**Production endpoint:** `https://api.priorlabs.ai:443`
**GUI:** `https://ux.priorlabs.ai`

Source: [server_config.yaml](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/server_config.yaml#L7-L9) L7-9

### Endpoints (from [server_config.yaml](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/server_config.yaml))

| Endpoint | Path | Method |
|----------|------|--------|
| Auth (register/login/verify) | `/auth/register/`, `/auth/login/`, etc. | POST |
| Upload train set | `/upload/train_set/` | POST |
| **Fit** | `/fit/` | POST |
| **Predict** | `/predict/` | POST |
| Predict proba | `/predict_proba/` | POST |
| **Fit (reasoning/thinking)** | `/beta/tabpfn-r/fit/` | POST |
| **Predict (reasoning/thinking)** | `/beta/tabpfn-r/predict/` | POST |
| Data summary | `/get_data_summary/` | GET |
| Download all data | `/download_all_data/` | GET |
| Delete dataset | `/delete_dataset/` | DELETE |
| API usage | `/get_api_usage/` | POST |

### Protocol Details

| Feature | Evidence | File:Line |
|---------|----------|-----------|
| **HTTP/2 only for `/fit/`** — all other endpoints use HTTP/1.1 | `SelectiveHTTP2Transport(http2_paths=[fit_path])` | [client.py:L242-275](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L242-L275) |
| **20-min timeout** | `4 * 5 * 60 + 15` = 1215s, comment: *"temporary workaround for slow computation on server side"* | [client.py:L267-268](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L267-L268) |
| **SSE streaming** for predict | `sseclient.SSEClient(response.iter_bytes())` | [client.py:L603](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L603) |
| **SSE line-delimited JSON** for fit progress | `FitProgressEvent`, `FitCompleteEvent`, `FitErrorEvent` | [client.py:L202-233](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L202-L233) |
| **Exponential backoff retry** on `GCPOverloaded` + 5xx errors | `max_tries=6, base=2, max_value=120` | [client.py:L367-384](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L367-L384) |
| **Bearer token auth** | `Authorization: Bearer {token}` | [client.py:L357-358](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L357-L358) |
| **Client version header** sent with every request | `headers={"client-version": get_client_version()}` | [client.py:L274](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L274) |
| **HTTP 426 for version enforcement** | Forces client upgrade when server requires newer version | [client.py:L749-753](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L749-L753) |
| **Retryable status codes:** 408, 502, 503, 504 | Treated as `RetryableServerError` | [client.py:L758](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L758) |

### Data Flow

1. Client serializes X, y as CSV bytes → uploads via multipart POST to `/fit/`
2. Server streams SSE progress events → returns `train_set_uid`
3. Client caches dataset hash → `train_set_uid` mapping (LRU-50, xxhash)
4. Predict sends `train_set_uid` + test data → SSE stream → result JSON
5. If cache miss (invalid UID), auto-retries by re-uploading train set

Source: [client.py:L385-507](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/client.py#L385-L507)

### Config & Server-Side Features

| Feature | Evidence |
|---------|----------|
| **TabPFN-R "Thinking" mode** (beta) | `/beta/tabpfn-r/fit/` and `/beta/tabpfn-r/predict/` endpoints; `thinking_params` in config |
| **Server-side preprocessing + text** | `tabpfn_systems = ["preprocessing", "text"]` sent as params |
| **YAML-driven endpoint config** | `OmegaConf.load(server_config.yaml)` |
| **GDPR data controls** | `/download_all_data/`, `/delete_user_account/`, `/delete_all_datasets/` endpoints |

---

## Additional Stack Components (Previously Missing)

### Deployment & CI/CD
| Component | Evidence |
|-----------|----------|
| **GCP Cloud Functions** | [`tabpfn-cloud-function`](https://github.com/PriorLabs/tabpfn-cloud-function) repo — serverless deployment with GCS model storage |
| **GCP Cloud Build** | `cloudbuild.yaml` in cloud-function repo — builds and deploys functions |
| **GCP Cloud Storage** | Model `.pkl` files stored in GCS buckets; `gsutil` used for uploads |
| **Google Apps Script** | `Code.gs` — Google Sheets integration for end-user predictions |
| **GitHub Actions CI** | [pull_request.yml](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/.github/workflows/pull_request.yml) — ruff linting, pytest, compatibility matrix (Python 3.9-3.13, Ubuntu + macOS) |
| **Dependabot** | [dependabot.yml](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/.github/dependabot.yml) — weekly pip + GitHub Actions updates |
| **License compliance** | `licensecheck` in CI — only APACHE/MIT/BSD/ISC/PYTHON/UNLICENSE allowed |
| **CODEOWNERS** | `* @PriorLabs/engineering` — all PRs require engineering team review |

### Telemetry & Observability
| Component | Evidence |
|-----------|----------|
| **PostHog** | [TELEMETRY.md](https://github.com/PriorLabs/TabPFN/blob/main/TELEMETRY.md) — `tabpfn-common-utils[telemetry]` dependency |
| Events tracked | `ping`, `fit_called`, `predict_called`, `session` |
| Metadata collected | python_version, tabpfn_version, gpu_type, num_rows (rounded), num_columns (rounded), duration_ms |
| GDPR compliance | Dataset shapes rounded to ranges (e.g. `953→1000`), no inputs/outputs sent, opt-out via `TABPFN_DISABLE_TELEMETRY=1` |

### Auth System
| Component | Evidence |
|-----------|----------|
| **Browser-based OAuth** | [browser_auth.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/src/tabpfn_client/browser_auth.py) — opens `ux.priorlabs.ai/login`, receives token via localhost callback |
| **CLI fallback** | Falls back to command-line login if browser can't open |
| **Token caching** | Tokens stored locally in `CACHE_DIR` |
| **Password auth endpoints** | `/auth/register/`, `/auth/login/`, `/auth/verify_email/`, `/auth/send_reset_password_email/` |

### Documentation
| Component | Evidence |
|-----------|----------|
| **Mintlify** (external docs) | [`docs`](https://github.com/PriorLabs/docs) repo — "Home of the official Prior Labs Mintlify docs page" (MDX) |
| **mkdocs-material** (API docs) | Dev dependency in pyproject.toml — used for Python API reference docs |

### Products & Repos (Full org inventory)
| Repo | Purpose | Stars |
|------|---------|-------|
| `TabPFN` | Core model (v6.4.1) | 5,742 |
| `tabpfn-client` | Cloud API SDK | 228 |
| `tabpfn-extensions` | Community extensions | 258 |
| `tabpfn-time-series` | Time series forecasting (NeurIPS 2024) | 354 |
| `tabpfn_common_utils` | Shared client/server utils | 0 |
| `R-tabpfn` | R language bindings | 17 |
| `tabpfn-cloud-function` | GCP Cloud Functions deployment (fork) | 1 |
| `docs` | Mintlify docs | 0 |
| `dataset-requirements-guide` | Enterprise data prep guide | 3 |
| `awesome-tabpfn` | Community resources | 31 |

### Team (from pyproject.toml authors)
Noah Hollmann, Samuel Müller, Lennart Purucker, Arjun Krishnakumar, Max Körfer, Shi Bin Hoo, Robin Tibor Schirrmeister, Frank Hutter, Eddie Bergman, Leo Grinsztajn, Felix Jabloski, Klemens Flöge, Oscar Key, Felix Birkel, Philipp Jund, Brendan Roof, Dominik Safaric, Benjamin Jaeger, Alan Arazi

### Dev Environment
| Tool | Evidence |
|------|----------|
| **Gemini Code Assist** | `.gemini` directory in TabPFN repo |
| **uv** | Package manager (lockfile in client repo) |
| **ruff 0.14.0** | Linter/formatter (pinned, synced with pre-commit) |
| **mypy 1.19.1** | Type checker (pinned) |
| **pre-commit** | Git hooks for linting |
| **towncrier** | Changelog management |
| **setuptools** | Build backend for core package |
| **hatchling** | Build backend for client package |

---

## What We DON'T Know (Server-Side Unknowns)

These are inferred gaps — things they **must** have but aren't visible in public code:

| Component | What's likely | Why we think so |
|-----------|--------------|-----------------|
| **Database** | PostgreSQL or Firestore | User accounts, dataset UIDs, API usage tracking, rate limits (100M credits/day) need persistent storage |
| **GPU serving framework** | Custom PyTorch / TorchServe | No Triton or vLLM evidence; TabPFN is a custom transformer, likely served directly via custom PyTorch |
| **Task queue** | GCP Cloud Tasks or Pub/Sub | 20-min timeout suggests synchronous processing, but scaling to many users requires queue |
| **Container orchestration** | GKE or Cloud Run on GPU | The job listing mentions Docker + Kubernetes |
| **IaC** | Terraform or Pulumi | Job listing mentions "Infrastructure as Code" |
| **Billing/Payments** | Stripe or custom | Credit system (100M/day) must have metering + billing backend |
| **Load balancer** | GCP Cloud Load Balancing | `api.priorlabs.ai` needs SSL termination + routing |
| **Monitoring** | Cloud Monitoring / Grafana | Production GPU serving needs alerting |
| **Secrets management** | GCP Secret Manager | API tokens, model access keys, DB credentials |
| **Model registry** | HuggingFace Hub + GCS | Gated access via HF hub for local; GCS for cloud serving |

> [!TIP]
> These unknowns are great "curious question" material for the interview: "What does your serving layer look like behind api.priorlabs.ai? Are you using TorchServe or a custom solution?"

---

## Dependency Stack

### Client SDK (`tabpfn-client` — [pyproject.toml](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/tabpfn-client/pyproject.toml))
`httpx[http2]`, `sseclient-py`, `backoff`, `xxhash`, `pydantic`, `omegaconf`, `rich`, `tqdm`, `tabpfn-common-utils`

### Core (`tabpfn` package)
`torch>=2.1`, `einops`, `huggingface-hub`, `pydantic`/`pydantic-settings`, `joblib`, `filelock`, `scipy`, `pandas`, `scikit-learn`, `tabpfn-common-utils[telemetry]`

### Shared Code
`tabpfn-common-utils` — common package between client and server (serialization, hashing, Singleton pattern)

### Dev Tools
`uv` (lockfile), `ruff`, `mypy`, `pytest`/`pytest-xdist`, `pre-commit`, `towncrier` (changelogs), `mkdocs-material` (docs), `hatchling` (build)

---

## 🔧 Specific Recommendations for the Interview

### 1. The 20-min timeout → Async job queue
> "I noticed your client holds HTTP connections open for 20 minutes during fit. You could move long-running fits to an async job queue — Cloud Tasks or Pub/Sub — and notify via webhook or polling, which would also let you scale horizontally without connection limits."

### 2. GCP capacity issues → Auto-scaling GPU pools
> "The GCPOverloaded exception tells me you're hitting capacity limits. GKE with auto-scaling GPU node pools and a request queue would smooth out spikes instead of returning overload errors."

### 3. Selective HTTP/2 → gRPC for internal serving
> "You're already using HTTP/2 for fit but not predict. gRPC on the internal serving layer would give you bidirectional streaming, better multiplexing, and proto-defined contracts between client and server."

### 4. Client-side dataset caching → Server-side dedup
> "The xxhash-based LRU cache on the client is clever but limited to 50 entries per machine. Content-addressed storage on the server would deduplicate across all users and eliminate the re-upload retry logic."

### 5. CSV serialization → Arrow/Parquet (THEY ALREADY KNOW THIS)
> **Their own `sagemaker.py` says on L93-94:** *"For larger datasets, we recommend preparing and sending the request data using the multipart/form-data content type, where datasets are compressed and serialized using e.g. PyArrow and Parquet."*
>
> Frame this as: "I noticed you're already thinking about Arrow/Parquet for the SageMaker path — happy to help bring that to the main API too."

---

## Model Checkpoints (from [sagemaker.py](file:///c:/Users/dhl/data/Portfolio/cv-dhl.git/resume/2-page/with-cover-letter/resume-dhl-20260217-priorlabs-cloud/reference/source-code/tabpfn--sagemaker.py#L206-L224))

**Classification:**
- `tabpfn-v2.5-classifier-v2.5_default.ckpt` (+ `-2` variant)
- `tabpfn-v2.5-classifier-v2.5_large-features-L.ckpt` / `-XL.ckpt`
- `tabpfn-v2.5-classifier-v2.5_large-samples.ckpt`
- `tabpfn-v2.5-classifier-v2.5_real.ckpt` / `_real-large-*`
- `tabpfn-v2.5-classifier-v2.5_variant.ckpt`

**Regression:**
- `tabpfn-v2.5-regressor-v2.5_default.ckpt`
- `tabpfn-v2.5-regressor-v2.5_low-skew.ckpt` / `_quantiles.ckpt`
- `tabpfn-v2.5-regressor-v2.5_real.ckpt` / `_real-variant.ckpt`
- `tabpfn-v2.5-regressor-v2.5_small-samples.ckpt` / `_variant.ckpt`

This reveals they have **specialized model variants** for different data characteristics (large features, large samples, real data, low-skew). The ensemble (`n_estimators=8`) likely runs multiple checkpoints in parallel.

---

## Citation Verification ✅

Every claim verified against local files:

| Claim | Verified at |
|-------|-------------|
| GCPOverloaded exception | `reference/tabpfn-client/src/tabpfn_client/client.py` L70 |
| 20-min timeout | `reference/tabpfn-client/src/tabpfn_client/client.py` L267-268 |
| SelectiveHTTP2Transport | `reference/tabpfn-client/src/tabpfn_client/client.py` L242-255 |
| SSE streaming (sseclient) | `reference/tabpfn-client/src/tabpfn_client/client.py` L603 |
| Bearer token auth | `reference/tabpfn-client/src/tabpfn_client/client.py` L357-358 |
| api.priorlabs.ai endpoint | `reference/tabpfn-client/src/tabpfn_client/server_config.yaml` L7-9 |
| Backoff retry (6 tries) | `reference/tabpfn-client/src/tabpfn_client/client.py` L367-384 |
| HTTP 426 version enforcement | `reference/tabpfn-client/src/tabpfn_client/client.py` L749 |
| Retryable status codes 408/502/503/504 | `reference/tabpfn-client/src/tabpfn_client/client.py` L758 |
| Dataset caching (xxhash, LRU-50) | `reference/tabpfn-client/src/tabpfn_client/client.py` L98-175 |
| SageMaker enterprise deployment | `reference/source-code/tabpfn--sagemaker.py` L1-410 |
| Arrow/Parquet recommendation | `reference/source-code/tabpfn--sagemaker.py` L93-94 |
| GDPR data endpoints | `reference/tabpfn-client/src/tabpfn_client/server_config.yaml` L93-121 |
| OmegaConf config loading | `reference/tabpfn-client/src/tabpfn_client/client.py` L183-184 |
| TabPFN-R "thinking" beta endpoints | `reference/tabpfn-client/src/tabpfn_client/server_config.yaml` L98-106 |
| Client version header | `reference/tabpfn-client/src/tabpfn_client/client.py` L274 |

> [!CAUTION]
> **Do NOT** volunteer these critiques unsolicited. Use them ONLY if Noah asks "how would you approach our infrastructure?" or "what would you improve?" Frame as "I noticed X, here's what I'd explore" — not "your code is wrong."
