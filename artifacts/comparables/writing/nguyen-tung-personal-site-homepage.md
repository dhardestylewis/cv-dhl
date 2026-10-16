---
author: "Tung Nguyen"
org: "UCLA (Grover group)"
url: "https://tung-nd.github.io"
date: "current"
fetch_date: "2026-10-15"
connects_to: "Tung Nguyen, Aditya Grover (ClimaX)"
why_it_matters: "How a ClimaX first author presents an AI-resident-to-PhD path with paper links and news."
---

I’m a final-year PhD candidate in Computer Science at UCLA, advised by Aditya Grover. I earned my Bachelor’s degree in Computer Science from the Hanoi University of Science and Technology. Prior to my PhD, I spent two wonderful years at VinAI Research as an AI Resident, where I had the privilege of working under the supervision of Hung Bui and collaborating with amazing colleagues like Rui Shu and Tuan Pham. **I’m currently looking for full-time Research Scientist roles in industry (start: Summer 2026).**

I’m always open to collaborations, discussions, and new opportunities. Feel free to reach out if you’re interested in my research or would like to discuss potential projects.

**Research:** My research focuses on building large-scale foundation models for scientific simulation and reasoning, particularly in areas related to climate change, sustainability, and the physical sciences.

**1. AI for Scientific Simulation.** I develop machine learning models to simulate real-world phenomena such as weather and climate dynamics using large-scale scientific datasets. These models aim to be accurate, adaptable, and capable of representing uncertainty in complex systems.

**2. AI for Experimental Design.** I also work on using AI to solve optimization problems in scientific and engineering domains, such as molecular design and drug discovery. My goal is to build generalizable models that can perform across tasks with limited supervision, offering efficient and robust tools for real-world scientific discovery.

## Recent News

|  |  |
| --- | --- |
| Sep 18, 2025 | OmniCast got accepted at NeurIPS 2025. |
| Jun 16, 2025 | Started my internship at NVIDIA on the Weather and Climate Simulation team. |
| May 30, 2025 | Honored to receive the **Dissertation Year Award (DYA)** from UCLA. |
| Jan 22, 2025 | LICO got accepted at ICLR 2025. |
| Sep 25, 2024 | Stormer, ChaosBench, and Probing LLM got accepted at NeurIPS 2024. Probing LLM won the **best paper award** at the Foundation Model Interventions Workshop, NeurIPS 2024. |
| Jun 17, 2024 | Started my internship at Google Deepmind to work with Richard Song on LLM embeddings for universal Bayesian optimization. |
| May 11, 2024 | Stormer won the **best paper award** at the Climate Change in AI (CCAI) Workshop at ICLR 2024. |
| Apr 30, 2024 | Honored to receive the **Outstanding Graduate Student Research Award**, Department of Computer Science, UCLA. |
| Dec 07, 2023 | We released Stormer, which achieves state-of-the-art performance for data-driven weather forecasting. |
| Sep 21, 2023 | ExPT and ClimateLearn got accepted at NeurIPS 2023. |
| Apr 24, 2023 | ClimaX got accepted at ICML 2023 and won the **best paper award** at the Synergy of Scientific and Machine Learning Modeling Workshop, ICML 2023. |
|  | ClimaX has been featured in major media outlets, including Washington Post, MIT Tech Review, InfoQ, and Nature. |
| Jan 26, 2023 | We released ClimaX – the first foundation model for weather and climate. |
| Sep 05, 2022 | Honored to receive the Amazon Fellowship. |
| Jun 20, 2022 | Started my internship at Microsoft Research to work with Ashish Kapoor and Jayesh K. Gupta on foundation models for weather and climate. |
| May 15, 2022 | Transformer Neural Processes, my first paper as a PhD student, got accepted at ICML 2022. |
| Sep 20, 2021 | Started my PhD at UCLA, working with Adtitya Grover! |

## Selected Publications

1. ICLR

   LICO: Large language models for in-context molecular optimization

   *Tung Nguyen*, and Aditya Grover

   *International Conference on Learning Representations*, 2025

   Abs PDF

   Optimizing black-box functions is a fundamental problem in science and engineering. To solve this problem, many approaches learn a surrogate function that estimates the underlying objective from limited historical evaluations. Large Language Models (LLMs), with their strong pattern-matching capabilities via pretraining on vast amounts of data, stand out as a potential candidate for surrogate modeling. However, directly prompting a pretrained language model to produce predictions is not feasible in many scientific domains due to the scarcity of domain-specific data in the pretraining corpora and the challenges of articulating complex problems in natural language. In this work, we introduce LICO, a general-purpose model that extends arbitrary base LLMs for black-box optimization, with a particular application to the molecular domain. To achieve this, we equip the language model with a separate embedding layer and prediction layer, and train the model to perform in-context predictions on a diverse set of functions defined over the domain. Once trained, LICO can generalize to unseen molecule properties simply via in-context prompting. LICO achieves state-of-the-art performance on PMO, a challenging molecular optimization benchmark comprising over 20 objective functions.
2. NeurIPS   Best Paper

   Probing the Decision Boundaries of In-context Learning in Large Language Models

   Siyan Zhao, *Tung Nguyen*, and Aditya Grover

   *Neural Information Processing Systems*, 2024

    Best Paper Award, Foundation Model Interventions Workshop, NeurIPS 2024 

   Abs PDF Code

   Best Paper

   In-context learning is an emergent paradigm in large language models (LLMs) that enables them to generalize to new tasks and domains by simply prompting these models with a few exemplars without explicit parameter updates. Many attempts have been made to understand in-context learning in LLMs as a function of model scale, pretraining data, and other factors. In this work, we propose a new mechanism to probe and understand in-context learning from the lens of decision boundaries for in-context binary classification. Decision boundaries are straightforward to visualize and provide important information about the qualitative behavior of the inductive biases of standard classifiers. To our surprise, we find that the decision boundaries learned by current LLMs in simple binary classification tasks are often irregularly non-smooth, regardless of task linearity. This paper investigates the factors influencing these decision boundaries and explores methods to enhance their generalizability. We assess various approaches, including training-free and fine-tuning methods for LLMs, the impact of model architecture, and the effectiveness of active prompting techniques for smoothing decision boundaries in a data-efficient manner. Our findings provide a deeper understanding of in-context learning dynamics and offer practical improvements for enhancing robustness and generalizability of in-context learning.
3. NeurIPS   Best Paper

   Scaling transformer neural networks for skillful and reliable medium-range weather forecasting

   *Tung Nguyen*, Rohan Shah, Hritik Bansal, Troy Arcomano, Romit Maulik, Rao Kotamarthi, Ian Foster, Sandeep Madireddy, and Aditya Grover

   *Neural Information Processing Systems*, 2024

    Best Paper Award, Tackling Climate Change with Machine Learning Workshop, ICLR 2024 

   Abs PDF Code

   Best Paper

   Weather forecasting is a fundamental problem for anticipating and mitigating the impacts of climate change. Recently, data-driven approaches for weather forecasting based on deep learning have shown great promise, achieving accuracies that are competitive with operational systems. However, those methods often employ complex, customized architectures without sufficient ablation analysis, making it difficult to understand what truly contributes to their success. Here we introduce Stormer, a simple transformer model that achieves state-of-the art performance on weather forecasting with minimal changes to the standard transformer backbone. We identify the key components of Stormer through careful empirical analyses, including weather-specific embedding, randomized dynamics forecast, and pressure-weighted loss. At the core of Stormer is a randomized forecasting objective that trains the model to forecast the weather dynamics over varying time intervals. During inference, this allows us to produce multiple forecasts for a target lead time and combine them to obtain better forecast accuracy. On WeatherBench 2, Stormer performs competitively at short to medium-range forecasts and outperforms current methods beyond 7 days, while requiring orders-of-magnitude less training data and compute. Additionally, we demonstrate Stormer’s favorable scaling properties, showing consistent improvements in forecast accuracy with increases in model size and training tokens. Code and checkpoints are available at https://github.com/tung-nd/stormer.
4. NeurIPS

   ExPT: Synthetic Pretraining for Few-Shot Experimental Design

   *Tung Nguyen*, Sudhanshu Agrawal, and Aditya Grover

   *Neural Information Processing Systems*, 2023

   Abs PDF Code

   Experimental design is a fundamental problem in many science and engineering fields. In this problem, sample efficiency is crucial due to the time, money, and safety costs of real-world design evaluations. Existing approaches either rely on active data collection or access to large, labeled datasets of past experiments, making them impractical in many real-world scenarios. In this work, we address the more challenging yet realistic setting of few-shot experimental design, where only a few labeled data points of input designs and their corresponding values are available. We approach this problem as a conditional generation task, where a model conditions on a few labeled examples and the desired output to generate an optimal input design. To this end, we introduce Experiment Pretrained Transformers (ExPT), a foundation model for few-shot experimental design that employs a novel combination of synthetic pretraining with in-context learning. In ExPT, we only assume knowledge of a finite collection of unlabelled data points from the input domain and pretrain a transformer neural network to optimize diverse synthetic functions defined over this domain. Unsupervised pretraining allows ExPT to adapt to any design task at test time in an in-context fashion by conditioning on a few labeled data points from the target task and generating the candidate optima. We evaluate ExPT on few-shot experimental design in challenging domains and demonstrate its superior generality and performance compared to existing methods. The source code is available at https://github.com/tung-nd/ExPT.
5. ICML   Best Paper

   ClimaX: A foundation model for weather and climate

   *Tung Nguyen*, Johannes Brandstetter, Ashish Kapoor , Jayesh K Gupta, and Aditya Grover

   *International Conference on Machine Learning*, 2023

    Best Paper Award, Synergy of Scientific and Machine Learning Modeling Workshop, ICML 2023 

   Abs PDF Code

   Best Paper

   Most state-of-the-art approaches for weather and climate modeling are based on physics-informed numerical models of the atmosphere. These approaches aim to model the non-linear dynamics and complex interactions between multiple variables, which are challenging to approximate. Additionally, many such numerical models are computationally intensive, especially when modeling the atmospheric phenomenon at a fine-grained spatial and temporal resolution. Recent data-driven approaches based on machine learning instead aim to directly solve a downstream forecasting or projection task by learning a data-driven functional mapping using deep neural networks. However, these networks are trained using curated and homogeneous climate datasets for specific spatiotemporal tasks, and thus lack the generality of numerical models. We develop and demonstrate ClimaX, a flexible and generalizable deep learning model for weather and climate science that can be trained using heterogeneous datasets spanning different variables, spatio-temporal coverage, and physical groundings. ClimaX extends the Transformer architecture with novel encoding and aggregation blocks that allow effective use of available compute while maintaining general utility. ClimaX is pre-trained with a self-supervised learning objective on climate datasets derived from CMIP6. The pre-trained ClimaX can then be fine-tuned to address a breadth of climate and weather tasks, including those that involve atmospheric variables and spatio-temporal scales unseen during pretraining. Compared to existing data-driven baselines, we show that this generality in ClimaX results in superior performance on benchmarks for weather forecasting and climate projections, even when pretrained at lower resolutions and compute budgets. The source code is available at https://github.com/microsoft/ClimaX.
6. ICML

   Transformer Neural Processes: Uncertainty-Aware Meta Learning Via Sequence Modeling

   *Tung Nguyen*, and Aditya Grover

   *International Conference on Machine Learning*, 2022

   Abs PDF Code

   Neural Processes (NPs) are a popular class of approaches for meta-learning. Similar to Gaussian Processes (GPs), NPs define distributions over functions and can estimate uncertainty in their predictions. However, unlike GPs, NPs and their variants suffer from underfitting and often have intractable likelihoods, which limit their applications in sequential decision making. We propose Transformer Neural Processes (TNPs), a new member of the NP family that casts uncertainty-aware meta learning as a sequence modeling problem. We learn TNPs via an autoregressive likelihood-based objective and instantiate it with a novel transformer-based architecture. The model architecture respects the inductive biases inherent to the problem structure, such as invariance to the observed data points and equivariance to the unobserved points. We further investigate knobs within the TNP framework that tradeoff expressivity of the decoding distribution with extra computation. Empirically, we show that TNPs achieve state-of-the-art performance on various benchmark problems, outperforming all previous NP variants on meta regression, image completion, contextual multi-armed bandits, and Bayesian optimization.

## Selected Preprints

1. Preprint

   Predicting from Strings: Language Model Embeddings for Bayesian Optimization

   *Tung Nguyen*, Qiuyi Zhang, Bangding Yang, Chansoo Lee, Jorg Bornschein, Yingjie Miao, Sagi Perel, Yutian Chen, and Xingyou Song

   *Under Review*, 2025

   Abs PDF Code

   Bayesian Optimization is ubiquitous in the field of experimental design and blackbox optimization for improving search efficiency, but has been traditionally restricted to regression models which are only applicable to fixed search spaces and tabular input features. We propose Embed-then-Regress, a paradigm for applying in-context regression over string inputs, through the use of string embedding capabilities of pretrained language models. By expressing all inputs as strings, we are able to perform general-purpose regression for Bayesian Optimization over various domains including synthetic, combinatorial, and hyperparameter optimization, obtaining comparable results to state-of-the-art Gaussian Process-based algorithms. Code can be found at https://github.com/google-research/optformer/tree/main/optformer/embed\_then\_regress.

*This webpage was adapted from my friend's webpage at https://khainb.com/*
