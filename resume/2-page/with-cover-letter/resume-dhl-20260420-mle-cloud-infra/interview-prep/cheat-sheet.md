# 📋 CHEAT SHEET — Prior Labs Call w/ Noah Hollmann
### Thu Feb 26 · 8:30am EST · meet.google.com/htr-aupy-dsp

---

## YOUR PITCH (30 sec)
> "I've spent 8 years building the exact layer you need — taking research ML models and shipping them as production systems at scale — and I've done it specifically with tabular data."

---

## 3 THINGS TO HIT

**1. Infra at scale** — TACC, $40M TDIS, million-node HPC, multi-million-dollar compute, containerized clusters, 6 partner agencies

**2. Tabular data fluency** — VAE on property records (Homecastr), CVAE on financial data (Columbia), Airflow/FastAPI pipelines (PoliBOM)

**3. End-to-end ownership** — 3 ventures founded, full stack from architecture → production → monitoring. Small team operator.

---

## 3 QUESTIONS TO ASK

1. **What's the current serving stack?** Cloud provider, orchestration, serving framework? Biggest infra pain point?
2. **How does the distillation pipeline (TabPFN-as-MLP) work in practice?** Is that batch or on-demand? What's the latency target?
3. **As you scale to millions of rows — retrieval, fine-tuning, new architectures — where do you see the most infra investment in the next 6-12 months?**

---

## THEIR INFRA (from paper + GitHub)
- **Cloud API**: REST + Python SDK, rate-limited (100M credits/day, 20M cells/request)
- **Model**: 18–24 layer transformer, alternating row-column attention, 64 "thinking rows"
- **Hardware**: H100/A100, multi-GPU parallelization, flash attention
- **Production**: TabPFN-as-MLP/Tree distillation for low-latency serving (enterprise product)
- **Deps**: PyTorch 2.8+, HuggingFace, pydantic, PostHog telemetry
- **Roadmap**: Millions of rows (retrieval + novel architectures), time series, multimodal, causal

---

## REMINDERS
- 20 min call — ~5 min you, ~5 min Q&A, ~10 min Noah shares
- **Lead with infra**, not research
- Reference Nature paper + v2.5 Scaling Mode — shows homework
- Mention NYC — role lists it as a location
- Be conversational — Noah said "no need to prepare"
