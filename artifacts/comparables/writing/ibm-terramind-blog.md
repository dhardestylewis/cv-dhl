---
author: "IBM Research with ESA Phi-lab"
org: "IBM Research"
url: "https://research.ibm.com/blog/terramind-esa-earth-observation-model"
date: "2025-04-21"
fetch_date: "2026-10-15"
connects_to: "Jakubik, Ramachandran (Prithvi / IBM-NASA lineage)"
why_it_matters: "Names the model, states modalities and benchmark basis, and releases openly."
---

# IBM and ESA open-source TerraMind, the best performing generative AI model for Earth observation

The new foundation model from IBM and the European Space Agency (ESA) combines insights from nine types of Earth observation data to provide an intuitive understanding of our planet.

What information would an AI model need to truly understand our planet? That’s the question researchers from IBM, ESA, KP Labs, Jülich Supercomputing Center (JSC), and the German Aerospace Center (DLR) set out to answer this year as part of an ESA led initiative to improve access to foundation models within the earth observation community.

That’s why today, IBM and ESA have released TerraMind, a new earth-observation model that the group has open-sourced on Hugging Face. It was pre-trained on TerraMesh, the largest geospatial data set available, built by researchers as part of the TerraMind project.

## A leader in geospatial model performance

TerraMind has a unique symmetric transformer-based encoder-decoder architecture, which is designed to work with pixel-base, token-base, and sequence-base inputs and learn correlations across modalities. Despite being trained across 500 billion tokens, TerraMind is a small, lightweight model, using 10 times less compute than using standard models for each modality. This means users can deploy it at scale at a lower cost, while reducing the overall energy consumption at inference time.

“To me, what sets TerraMind apart is its ability to go beyond simply processing earth observations with computer vision algorithms. It instead has an intuitive understanding of geospatial data and our planet,” said Juan Bernabé-Moreno, director of IBM Research UK and Ireland, and IBM's Accelerated Discovery lead for climate and sustainability. “At present, TerraMind is the best performing AI foundation model for Earth observation according to well-established community-benchmarks,” Bernabé-Moreno added.

In an ESA evaluation, TerraMind was compared against 12 popular Earth observation foundation models on PANGAEA, a community-standard benchmark, to measure the model’s performance on real-world tasks, like land cover classification, change detection, environmental monitoring and multi-sensor and multi-temporal analysis. The benchmark showed TerraMind outperformed other models on these tasks by 8% or more.

“TerraMind combines insights from several modalities of training data to increase the accuracy of its outputs,” said Simonetta Cheli, director of ESA Earth Observation Programmes and Head of ESRIN. “The ability to intuitively bring in contextual information and generate unseen scenarios is a critical step in unlocking the value of ESA data. Compared to competitive models, it can uncover a deeper understanding of the Earth for researchers and businesses alike.”

In practice, to predict the risk of water scarcity, researchers need to consider many different factors like land use, climate, vegetation, agricultural activities, and location. Before TerraMind, all of this data was locked away in separate places. Bringing this information together enables users to predict the potential risk of water scarcity informed by a larger, more accurate picture of conditions on Earth.

## Nine million data points, nine different modalities

During the dataset creation, researchers included data from all biomes, land use/land cover types, and regions, allowing the model to be equally applicable to any use case across the globe, with limited bias.

The dataset includes 9 million globally distributed, spatiotemporally aligned data samples across nine core data modalities – including observations made by sensors on satellites, the geomorphology of the Earth’s surface, surface characteristics that are important to life on Earth (vegetation and land use) and the basics of how to describe locations and features (latitude, longitude, and simple text descriptions).

## Self-tuning to create artificial data

From a technical perspective, TerraMind is groundbreaking even beyond the domain of Earth observation. It is the first “any-to-any” multi-modal generative AI model for Earth observation. This means it can self-generate additional training data from other modalities  -  a technique IBM researchers coined “Thinking-in-Modalities” (TiM) tuning. TiM is a novel approach for computer vision models similar to chain-of-thought in language models. Empirical evidence demonstrates that TiM tuning can enhance the model performance beyond normal fine-tuning.

“TiM tuning boosts data efficiency by self-generating the additional training data relevant to the problem being addressed  -  for example, by telling the model to “think” about land cover when mapping water bodies. This breakthrough can unlock unprecedented accuracy when specializing TerraMind for particular use cases,” said Johannes Jakubik, an IBM Research scientist based in Zurich.

## Building on a solid foundation

Applying AI and machine learning techniques to Earth-related data, including satellites and land use patterns, isn’t new. Existing geospatial foundation models, such as those developed by IBM and NASA, enable scientists to make sense of this data  -  helping them better address use cases in high-precision agriculture, natural disaster management, environment monitoring (through water, heat and, drought), urban and regional planning, critical infrastructure monitoring, forestry and bio-diversity monitoring, and more.

However, these existing models currently process data from sources that occasionally can’t capture the rich reality of conditions on our planet. While satellites circle the globe, providing time-lapse data on natural events, they revisit the same location every five days. For analyzing climate events over the long-term, this provides enough data to predict and review trends. When monitoring short-term events like wildfires and floods, every day counts, and researchers need the latest data to make predictions or assess risk using AI models.

To solve this challenge, IBM researchers combined their technical knowledge in preparing data and building foundation models with the ESA’s valuable earth observation data and expertise in model evaluation to develop a new multi-modal AI foundation model for Earth observation. It was trained using the infrastructure and expertise of the Jülich Supercomputing Center. Other partners contributed to the overall model development process by conducting scaling experiments and preparing downscaling applications.

## A continuous effort

TerraMind is a part of IBM’s effort to use AI technology to explore our planet. Currently, governments, companies, and public institutions are using the IBM-NASA Prithvi models and IBM Granite geospatial specialized models to examine changes in disaster patterns, biodiversity, and land use, as well as for detecting and predicting severe weather patterns. Experts from NASA were also involved in the validation of TerraMind, as part of NASA’s Open Science initiative. All geospatial models can be found on Hugging Face and on the IBM Geospatial Studio.

Fine-tuned versions of TerraMind for disaster response and additional high-impact use cases will be added to the IBM Granite Geospatial repository in the next month, to enable communities and businesses to leverage the power of this new generation of Earth observation analytics.

“With Earth observation science, technology, and international collaboration, we are unlocking the full potential of space-based data to protect our planet,” said Nicolas Longepe, Earth Observation Data Scientist at ESA.

“This project is a perfect example where the scientific community, big tech companies, and experts have collaborated to leverage this technology for the benefit of Earth sciences. The magic happens when earth observation data experts, machine learning experts, data scientists, and HPC engineers come together.”

## Related posts

* NewsPeter Hess
* ### How distributed inference keeps large AI models moving

  ExplainerPeter Hess
* ### Demonstrating a theoretical separation between quantum computers and large language models

  ResearchSrinivasan Arunachalam, Arkopal Dutt, Hari Krovi, Rik Sengupta, and Ryan Mandelbaum
* ### A rough guide for going back to the Moon

  ReleaseKim Martineau
  + Accelerated Discovery
  + AI
  + Algorithms
