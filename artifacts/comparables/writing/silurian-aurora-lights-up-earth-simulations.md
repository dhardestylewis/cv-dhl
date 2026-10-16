---
author: "Silurian"
org: "Silurian"
url: "https://silurian.ai/blog/aurora-nature"
date: "2025-05-21"
fetch_date: "2026-10-15"
connects_to: "Gupta, Shankar (Silurian); Aurora (Bodnar, Perdikaris, Stanley)"
why_it_matters: "A startup comparing itself with a named published competitor (Aurora); read with care: self-reported comparison claim."
---

The shortcomings of today’s forecast systems have become impossible to ignore. Storm Ciarán deepened explosively over the English Channel in November 2023, catching even top‑tier models off‑guard. On 18 November 2024, Delhi’s Air‑Quality Index vaulted to off‑the‑charts levels, leaving schools and hospitals only hours to prepare. A 30‑foot rogue wave battered Roi‑Namur in the Marshall Islands on 20 January 2024, breaching defences believed safe, while at the end of June 2024, Hurricane Beryl rocketed from tropical storm to Category 5 in less than 24 hours - the fastest early‑season intensification on record.

Today, we’re thrilled to share that “**Aurora: A Foundation Model for the Earth System**”, a paper with leading contributions from the Silurian AI team, has been published in Nature. Aurora is the first AI system to unify high-resolution weather, air quality and atmospheric chemistry, global wave risk, and hurricane tracking within a single foundation model - surpassing the performance of today’s leading operational forecasting systems in each of these domains.

## **The challenge of Earth-system forecasting**

From Lewis Fry Richardson’s hand‑calculated forecast in 1922 to the first digital weather run on the ENIAC computer in 1950, numerical simulation has progressed by adding more physics and ever‑larger computers. Every leap in resolution - from 500 km in the 1960s to 9 km grids today - has sharpened skill but driven super‑computing budgets and energy demand sky‑high.

Modern operational centres still run separate, resource‑hungry systems for weather, air quality, ocean waves and hurricanes, making it hard to capture tightly coupled extremes such as rapid intensification, pollution spikes or wave run‑up. Bridging these phenomena calls for kilometre‑scale resolution, global coverage, and the ability to bridge heterogeneous observations from different components of the Earth System - requirements that, until now, have placed cutting‑edge forecasting beyond the reach of most of the world.

## **Aurora: one model, four specialised skills**

| Post-training task | Horizon & resolution | Benchmark beaten | Key metric |
| --- | --- | --- | --- |
| High-res weather | 10 days @ 0.1° | ECMWF IFS-HRES | 92% of targets improved |
| Air-pollution | 5 days @ 0.4° | ECMWF CAMS | 74% of targets improved |
| Ocean waves | 10 days @ 0.25° | ECMWF WAM-HRES | 86 % of targets improved |
| Hurricane tracking | 5 day tracks | Multi-agency consensus | 20 % lower track error |

---

Unlike traditional numerical simulations, which integrate the physical equations and grow costlier with every kilometre of resolution and every component of the Earth System being modeled, Aurora takes a foundation‑model approach.

*Aurora is post-trained to excel at four tasks: air pollution, wave modelling, hurricane tracking and weather modelling.*

Similarly to how ChatGPT internalised the grammar of human language, Aurora learns the “grammar” of the Earth. Aurora is first trained on a million hours of atmospheric data. During this stage the network discovers the general rules that bind physical variables such as temperature and pressure across space and time. Once that shared vocabulary is in place, Aurora is finetuned for just a few hours, transforming the same latent representation into high-resolution weather maps, pollution outlooks, global wave guidance and hurricane tracks - without ever retraining the core model.

The post-training procedure yields four domain expert models that consistently outperform the leading numerical systems in an operational setting. Aurora delivers lower forecasting error than ECMWF’s IFS‑HRES, the gold standard in numerical weather simulations, on 92 % of the 10‑day global weather targets; surpasses the ECMWF’s CAMS system on 74 % of five‑day pollutant fields; reduces error on 86 % of targets against ECMWF’s numerical wave model; and, finally, it cuts mean Atlantic hurricane‑track error by 20 % relative to the multi‑agency consensus. Aurora achieves all of this while operating orders of magnitude faster than numerical models - even capable of running on a single GPU.

## **Building on Aurora: the GFT family**

*“The acceptance of Aurora in* *Nature* *is a decisive scientific endorsement of Silurian’s core technology and Aurora is only the beginning.”* says **Cristian Bodnar**, Chief Scientist at Silurian AI and co‑lead author of the paper.

Silurian is now extending Aurora’s foundation‑model paradigm through the **Generative Forecasting Transformer (GFT)** family:

* **GFT**  -  A next‑generation global weather model that surpasses Aurora on all metrics, adds hourly forecasts, and significantly expands the variable set.
* **GFT‑US**  -  A regional model delivering kilometre‑scale forecasts for the United States, tailored for the next 30h.

Early adopters are already integrating GFT outputs into renewable‑energy scheduling, energy-trading and disaster response.

## **Learn more about Silurian and Aurora**

* Explore the open source Aurora code.
* Try the GFT and GFT-US public weather API.

Stay tuned - Aurora is just the dawn of truly planetary‑scale AI.
