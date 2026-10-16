---
author: "Salesforce AI Research"
org: "Salesforce"
url: "https://www.salesforce.com/blog/gift-eval-time-series-benchmark/"
date: "2024-11-12"
fetch_date: "2026-10-15"
connects_to: "The Forecasting Company (Negiar, Fainberg)"
why_it_matters: "Explains benchmark design choices: breadth of domains, frequencies, pretraining/test separation."
---

## Share article

**TL;DR:** Time series forecasting is becoming increasingly important across various domains, thus having high-quality, diverse benchmarks are crucial for fair evaluation across model families. Such benchmarks also help identify model strengths and limitations, driving progressive advancements in the field. **GIFT-Eval** is a new comprehensive benchmark designed for evaluating general time series forecasting models, particularly foundation models. It introduces a diverse dataset collection that encompasses **28 datasets** and over **144,000 time series**, with **177 million data points**. GIFT-Eval is structured to support both full-shot and zero-shot evaluation as it provides train validation and test splits for each dataset along with a **non-leaking pretraining dataset** to promote robust development and comparison of foundation forecasting models. Moreover the datasets are analyzed in detail across four time series characteristics and six time series features, and results are aggregated across all the characteristics for more useful insights across model families.

## Why We Need a New Benchmark for Time Series Forecasting

Time series forecasting has become critical in numerous fields, ranging from finance and healthcare to cloud operations. As universal forecasting models emerge, there is a need for diverse benchmarks that support a wide array of datasets, frequencies, and forecasting tasks. Especially in foundation model research, having such a diverse high-quality benchmark becomes very crucial, ensuring fair evaluation and highlighting model weaknesses. For instance Natural Language Processing (NLP) research has benefited from diverse benchmarks like GLUE or MMLU, however, time series forecasting lacks such comprehensive resources. Existing datasets are often narrow in scope, focusing on specific tasks and failing to test models’ ability to handle varied forecasting scenarios, particularly in zero-shot settings. Inconsistent data splits across models also increase the risk of data leakage, complicating comparisons.

## The GIFT-Eval Benchmark: Addressing the Challenges

GIFT-Eval fills these identified gaps by introducing a comprehensive time series forecasting benchmark that consists of both pretraining and train/test components. GIFT-Eval supports a wide range of forecasting tasks, from short to long-term predictions, and evaluates models in both univariate and multivariate settings, providing a much-needed diversity in time series data.

Moreover, GIFT-Eval ensures fair and consistent model evaluation, particularly for foundation models, by offering pretraining data without leakage. It stands apart from previous benchmarks by introducing a broader spectrum of frequencies and prediction lengths, as well as the evaluation of zero-shot forecasting capabilities.

###### Benchmark Overview

GIFT-Eval consists of two key components:

* **Train/Test Component**: This includes 28 datasets with 144,000 time series and 177 million data points, providing comprehensive coverage across different domains, frequencies, and variate settings.
* **Pretraining Dataset**: This contains 230 billion data points spread over 88 datasets, curated to facilitate large-scale model pretraining.

Our paper presents a detailed analysis and benchmarking across 17 models, providing insights into model performance, highlighting strengths and identifying failure cases to guide the future development of universal time series models. In order to get granular insights from the results we categorize the datasets in our paper according to distinct time series characteristics that influence their structure and modeling. These include the domain from which the data originates (e.g., finance, healthcare), the frequency of observations (e.g., hourly, daily), the prediction length or forecast horizon, and whether the series is univariate or multivariate. Additionally, time series possess statistical features such as trend, seasonal strength, entropy, Hurst exponent, stability, and lumpiness, which help capture the patterns and variability within the data. GIFT-Eval considers these characteristics and features to ensure a comprehensive evaluation of forecasting models across diverse real-world scenarios.

## Experimental Results

Experiments were conducted using 17 models, spanning traditional statistical approaches (e.g., ARIMA, Theta), deep learning models (e.g., PatchTST, iTransformer), and foundation models (e.g., Moirai, Chronos). We present the results across five sections, covering key characteristics such as domain, prediction length, frequency, and number of variates, followed by an aggregation of results across all configurations. Here, we share only the gist of our findings, but for a more detailed and fine-grained analysis, interested readers can refer to our full paper.

###### **Domain**

Foundation models generally outperform both statistical and deep learning models across most domains. However, they face difficulties in domains like **Web/CloudOps** and **Transport**, where high entropy, low trend, and lumpiness make the data less predictable for zero-shot foundation models. In contrast, deep learning models perform better in these challenging domains when given full-shot training, likely benefiting from more targeted training data compared to foundation models.

###### **Prediction Length**

Foundation models excel in short-term forecasts, effectively capturing immediate trends and fluctuations. However, as prediction lengths extend to medium and long-term forecasts, their performance declines, while deep learning models like PatchTST and iTransformer perform better, successfully capturing longer-term dependencies. Although fine-tuning foundation models improves their ability to handle long-term forecasts, a notable performance gap remains between foundation models and deep learning models for medium to long-term predictions. This gap highlights an opportunity for further research to enhance foundation models’ ability to manage extended forecast horizons.

###### **Frequency**

For the highest frequency data, such as second-level granularity, statistical models lead the performance. As the frequency shifts to minutely and hourly data, deep learning models begin to dominate. Foundation models seem to struggle while handling the noisy patterns in high-frequency data, where specialized deep learning and statistical models perform better. However, when it comes to lower frequencies, such as daily to yearly data, foundation models consistently outperform other approaches, leveraging their extensive pretraining to capture broader patterns and slower dynamics.

###### **Variate Count**

In multivariate settings, deep learning models outperform all others across metrics, while Moirai leads among foundation models but still falls short of deep learning performance. This highlights a gap in foundation model research, where multivariate forecasting remains a challenge compared to deep learning models. Conversely, in univariate scenarios, foundation models, especially the large variant of Moirai, excel, delivering superior performance over their deep learning counterparts.

###### **General**

**PatchTST** stands out as the top-performing model across all metrics, with **Moirai Large** consistently ranking second and frequently appearing in the top two across all datasets. PatchTST proves to be a strong generalist, delivering reliable performance across diverse datasets, while **Moirai Large** excels in specific cases. However, the scaling law - where larger models perform better - only holds in select domains like energy and univariate forecasting.

## Conclusion

In conclusion, GIFT-Eval has been introduced as a comprehensive and diverse benchmark designed to evaluate time series forecasting models across key characteristics such as domain, frequency, number of variates, and prediction length. A diverse pretraining dataset and detailed analysis are provided to enable fair comparisons of statistical, deep learning, and foundation models. It is hoped that this benchmark will foster the development of more robust and adaptable foundation models, advancing the field of time series forecasting.

## Explore More

Salesforce AI invites you to dive deeper into the concepts discussed in this blog post (see links below). Connect with us on social media and our website to get regular updates on this and other research projects.

* Learn more about this work in our research paper
* Get our code on GitHub
* Check out GIFT-Eval data on Hugging Face: https://huggingface.co/datasets/Salesforce/GiftEval
* Check out the results of our benchmark on the public leaderboard: https://huggingface.co/spaces/Salesforce/GIFT-Eval
* Contact us:*iaksu@salesforce.com* chenghao.liu@salesforce.com
* Follow us on Twitter:@SalesforceResearch, @Salesforce
* To read other blog posts, please see blog.salesforceairesearch.com
* To learn more about all of the exciting projects at Salesforce AI Research, please visit us at salesforceairesearch.com.

## Share article

## Explore related content by topic

* AI Research

Taha Aksu
Research Scientist - Salesforce AI Research

Taha Aksu is a Research Scientist at Salesforce AI Research Asia. His main focus of interest lies in training and evaluating foundation models in time series. He is also interested in bridging the gap between text and time series modality.

More by Taha

Gerald Woo

More by Gerald

Juncheng Liu
Research Scientist - Salesforce AI Research

Juncheng Liu is a Research Scientist at Salesforce AI Research Asia, working on time series forecasting for AIOps. His current research interests are foundation models for time series and graph representation learning.

More by Juncheng

Xu Liu
PhD Intern - AI Research

Xu Liu is a Ph.D. candidate at the National University of Singapore and is currently working as a research intern at Salesforce AI Research Asia. His research focuses on time series forecasting and spatio-temporal data mining.

More by Xu

Chenghao Liu

More by Chenghao

Caiming Xiong
SVP Salesforce Research

More by Caiming

Doyen Sahoo
Director, Research

Doyen Sahoo is the Director, of Salesforce AI Research Asia. Doyen leads several projects pertaining to AI for IT Operations or AIOps, AI for Software, and Time-Series intelligence – working on both fundamental and applied research.

More by Doyen

6 min read

7 min read

7 min read

6 min read

7 min read

4 min read

7 min read

7 min read
