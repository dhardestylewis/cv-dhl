---
author: "Salesforce AI Research"
org: "Salesforce"
url: "https://github.com/SalesforceAIResearch/gift-eval"
date: "2024-2026"
fetch_date: "2026-10-15"
connects_to: "The Forecasting Company (Negiar, Fainberg), Jua, Zillow-style forecasting claims"
why_it_matters: "States the rules for a fair zero-shot time-series leaderboard entry, including training-data leakage handling."
---

BranchesTags

## Latest commit

## History

178 Commits

## Folders and files

## Repository files navigation

# GIFT-EVAL: A Benchmark for General Time Series Forecasting Model Evaluation

| Benchmark | Freq. Range | Num. of Domain | Pretraining data | Num. of var. | Pred. Len. | Benchmark Methods | Prob. Forecasting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Monash (Godahewa et al., 2021) | Secondly ~ Yearly | 7 | No | Uni | Short | Stat./DL | No |
| TFB (Qiu et al., 2024) | Minutely ~ Yearly | 6 | No | Uni/Multi | Short | Stat./DL | No |
| LTSF (Zeng et al., 2022) | Minutely ~ Weekly | 5 | No | Multi | Long | Stat./DL | No |
| BasicTS+ (Shao et al., 2023) | Minutely ~ Daily | 3 | No | Multi | Short/Long | Stat./DL | No |
| GIFT-Eval (our work) | Secondly ~ Yearly | 7 | Yes | Uni/Multi | Short/Long | Stat./DL/FM | Yes |

GIFT-Eval is a comprehensive benchmark designed to evaluate general time series forecasting models across diverse datasets, promoting the advancement of zero-shot forecasting capabilities in foundation models.

To facilitate the effective pretraining and evaluation of foundation models, we also provide a non-leaking pretraining dataset --> GiftEvalPretrain.

## Update Log

### 2025-10-17

* Added new column: Replication Code to indicate whether the model's evaluation replication code is made available. This column is a binary indicator specifying whether the evaluation code is made available to the public by the submission author. The preferable way to share the evaluation code is to share a notebook in the GIFT-Eval github repository (as many previous submissions have done), but a standalone repo for the evaluation code is also acceptable as long as it is accessible to the public and the link is provided in the config.json file through the `code_link` field.

### 2025-08-25

* Added new model type: Zero-shot to distinguish between foundation model submissions that don't use training data of GIFT-Eval. Now models tagged with zero-shot indicate that the model is not trained on the GIFT-Eval training data. Test data leakage is still separately tracked with the TestData Leakage column. For a model be tagged as `zero-shot`, it must both not have test data leakage and not use any training split from GIFT-Eval. (You can check the discussion that led to this change.)

### 2025-08-05

* Added new columns to the leaderboard: Organization, TestData Leakage, and MASE\_Rank. TestData Leakage is a binary indicator specifying whether any test data was present in the training set. MASE\_Rank reflects the model's ranking based on the MASE metric, aligned with the ranking scheme used for CRPS\_Rank. These additions were made in response to multiple requests from independent groups seeking fairer comparisons. With these updates, the leaderboard now supports sorting by models that do not leak test data, and viewers can choose to rank models based on either MASE\_Rank or CRPS\_Rank, depending on their use case.
* Added new model type: Agentic to indicate submissions that use agentic system to generate the forecasts.

### 2025‑07‑24

* Corrected the Naive and Seasonal Naive scores to match the latest GIFT‑Eval notebooks. Most model rankings remain unchanged; only a few near the bottom shifted slightly (AutoETS and Timer each dropped two places now at 35th and 36th places respectively, while NBEATS moved up one now at 27th place).

## Installation

1. Clone the repository and change the working directory to `GIFT_Eval`.
2. Create a conda environment:

```
python3 -m venv myenv
source myenv/bin/activate
```

3. Install required packages:

If you just want to explore the dataset, you can install the required dependencies as follows:

```
pip install -e .
```

If you want to run baselines, you can install the required dependencies as follows:

```
pip install -e .[baseline]
```

Note: The specific instructions for installing the Moirai and Chronos models are available in their relevant notebooks.

4. Get the train/test dataset from huggingface.

```
hf download Salesforce/GiftEval --repo-type=dataset --local-dir PATH_TO_SAVE
```

5. Set up the environment variables and add the path to the data:

```
echo "GIFT_EVAL=PATH_TO_SAVE" >> .env
```

## Getting Started

### Iterating the dataset

We provide a simple class, `Dataset` to load each dataset in our benchmark following the gluonts interface. It is highly recommended to use this class to split the data to train/val/test for compatibility with the evaluation framework and other baselines in the leaderboard. You don't have to stick to gluonts interface though as you can easily implement a wrapper class to load the data iterator in a different format than gluonts.

This class provides the following properties:

* `training_dataset`: The training dataset.
* `validation_dataset`: The validation dataset.
* `test_data`: The test dataset.

Please refer to the dataset.ipynb for an example of how to iterate the train/val/test splits of the dataset.

### Running baselines

We provide examples of how to run the statistical, deep learning, and foundation baselines in the naive.ipynb, feedforward.ipynb and moirai.ipynb and chronos.ipynb notebooks. Each of these notebooks wrap models available in different libraries to help you get started. You can either follow these examples or implement your own wrapper class to iterate over the splits of the dataset as explained in the dataset.ipynb notebook.

Each of these notebooks will generate a csv file called `all_results.csv` under the `results/<MODEL_NAME>` folder containing the results for your model on the gift-eval benchmark. Regardless of the model you choose and how you run it, you can submit your results to the leaderboard by following the instructions in the Submitting your results section.

### Sample output file

A sample output file is located at `results/Naive/all_results.csv`.

The file contains the following columns:

* `dataset`: The name of the dataset configuration, e.g. `electricity/15T/short`.
* `model`: The name of the model, e.g. `naive`.
* A column for each evaluation metric used, e.g. `eval_metrics/MSE[mean]`, `eval_metrics/MSE[0.5]`, etc.
* `domain`: The domain of the dataset, e.g. `Web/CloudOps`.
* `num_variates`: The number of variates in the dataset, e.g. `1`.

The first column in the csv file is the dataset config name which is a combination of the prettified dataset name, frequency and the term (The sample notebooks, e.g. naive.ipynb, show how to get this name, please follow the same format to align with the leaderboard.):

```
f"{dataset_name}/{freq}/{term}"
```

## Submitting your results

### Evaluation

```
res = evaluate_model(
        predictor,
        test_data=dataset.test_data,
        metrics=metrics,
        batch_size=512 ,
        axis=None,
        mask_invalid_label=True,
        allow_nan_forecast=False,
        seasonality=season_length,
    )
```

We highly recommend you to evaluate your model using gluonts `evaluate_model` function as it is compatible with the evaluation framework and other baselines in the leaderboard. Please refer to the sample notebooks where we show its use with statistical, deep learning and foundation models for more details. However, if you decide to evaluate your model in a different way please follow the below conventions for compatibility with the rest of the baselines in our leaderboard. Specifically:

1. Aggregate results over all dimensions (following `axis=None`)
2. Do not count `nan` values in the target towards calculation (following `mask_invalid_label=True`).
3. Make sure the prediction does not have `nan` values (following `allow_nan_forecast=False`).

### Submission

Submit your results to the leaderboard by creating a pull request that adds your results to the `results/<YOUR_MODEL_NAME>` folder. Your PR should contain only a folder with two files called `all_results.csv` and `config.json`. The `config.json` file should contain the following fields:

```
{
    "model": "YOUR_MODEL_NAME",
    "model_type": "one of statistical, deep-learning, agentic, pretrained, fine-tuned or zero-shot",
    "model_dtype": "float32, etc.",
    "model_link": "To your HF model link, e.g., https://huggingface.co/amazon/chronos-t5-small",
    "code_link": "To you replication code, e.g., https://github.com/SalesforceAIResearch/gift-eval/blob/main/notebooks/chronos.ipynb",
    "org": "YOUR_ORG_NAME",
    "testdata_leakage": "one of Yes or No",
    "replication_code_available": "one of Yes or No"
}
```

#### Field Descriptions

* **`model`**:  
  A short identifier for your model (e.g., `my_model_v1`).
* **`model_type`**:  
  Choose one of the following:

  + `statistical`: Traditional time series models such as ARIMA, ETS, etc.
  + `deep-learning`: Neural network models trained from scratch.
  + `agentic`: Multi-step systems that use agents or LLMs to reason, generate or select forecasts.
  + `pretrained`: Foundation models trained once on large-scale data and applied as-is
    to each dataset. The pretraining corpus may include GIFT-Eval train splits.
  + `zero-shot`: A specific version of pretrained models whose pretraining data has no
    common datasets with GiftEval data pool (both train and test).
  + `fine-tuned`: Models that start from a completed pretrained checkpoint and undergo a
    further training stage using GIFT-Eval train/validation data. This covers both
    per-dataset fine-tuning (a separate training job and set of weights for each of the
    97 tasks) and continual pretraining (a single additional training run whose data mix
    includes GIFT-Eval train splits, producing one checkpoint applied to all tasks).
  > **Note:** The key difference between `pretrained` and `fine-tuned` is the presence of a
  > separate training stage with GIFT-Eval train/validation data on top of an already-complete base checkpoint. A model whose
  > single pretraining run happens to include GIFT-Eval train data is `pretrained`; a model
  > that takes a finished checkpoint and trains it further on GIFT-Eval data is `fine-tuned`.

  > **Note:** For a model to be tagged as `zero-shot` it should satisfy two requirements:

[Excerpt truncated at the line cap; see url for the remainder.]
