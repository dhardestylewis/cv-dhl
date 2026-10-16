---
author: "Sebastian Raschka"
org: "Independent"
url: "https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches"
date: "2025-10-05"
fetch_date: "2026-10-15"
connects_to: "Evals and credible results (applies to Hamel Husain, OpenAI Patwardhan, Anthropic evals lane)"
why_it_matters: "Explains what each evaluation method can and cannot show, which bounds what a benchmark claim can credibly say."
---

How do we actually evaluate LLMs?  
It’s a simple question, but one that tends to open up a much bigger discussion.

When advising or collaborating on projects, one of the things I get asked most often is how to choose between different models and how to make sense of the evaluation results out there. (And, of course, how to measure progress when fine-tuning or developing our own.)

Since this comes up so often, I thought it might be helpful to share a short overview of the main evaluation methods people use to compare LLMs. Of course, LLM evaluation is a very big topic that can’t be exhaustively covered in a single resource, but I think that having a clear mental map of these main approaches makes it much easier to interpret benchmarks, leaderboards, and papers.

I originally planned to include these evaluation techniques in my upcoming book, Build a Reasoning Model (From Scratch), but they ended up being a bit outside the main scope. (The book itself focuses more on verifier-based evaluation.) So I figured that sharing this as a longer article with from-scratch code examples would be nice.

In Build A Reasoning Model (From Scratch), I am taking a hands-on approach to building a reasoning LLM from scratch.  
If you liked “Build A Large Language Model (From Scratch)”, this book is written in a similar style in terms of building everything from scratch in pure PyTorch.

The book is currently in early-access with >100 pages already online, and I have just finished another 30 pages that are currently being added by the layout team. If you joined the early access program (a big thank you for your support!), you should receive an email when those go live.

PS: There’s a lot happening on the LLM research front right now. I’m still catching up on my growing list of bookmarked papers and plan to highlight some of the most interesting ones in the next article.

But now, let’s discuss the four main LLM evaluation methods along with their from-scratch code implementations to better understand their advantages and weaknesses.

# Understanding the main evaluation methods for LLMs

There are four common ways of evaluating trained LLMs in practice: multiple choice, verifiers, leaderboards, and LLM judges, as shown in Figure 1 below. Research papers, marketing materials, technical reports, and model cards (a term for LLM-specific technical reports) often include results from two or more of these categories.

Furthermore the four categories introduced here fall into two groups: benchmark-based evaluation and judgment-based evaluation, as shown in the figure above.

(There are also other measures, such as training loss, perplexity, and rewards, but they are usually used internally during model development.)

The following subsections provide brief overviews and examples of each of the four methods.

# Method 1: Evaluating answer-choice accuracy

We begin with a benchmark‑based method: multiple‑choice question answering.

Historically, one of the most widely used evaluation methods is multiple-choice benchmarks such as MMLU (short for Massive Multitask Language Understanding, https://huggingface.co/datasets/cais/mmlu). To illustrate this approach, figure 2 shows a representative task from the MMLU dataset.

Figure 2 shows just a single example from the MMLU dataset. The complete MMLU dataset consists of 57 subjects (from high school math to biology) with about 16 thousand multiple-choice questions in total, and performance is measured in terms of accuracy (the fraction of correctly answered questions), for example 87.5% if 14,000 out of 16,000 questions are answered correctly.

Multiple-choice benchmarks, such as MMLU, test an LLM’s knowledge recall in a straightforward, quantifiable way similar to standardized tests, many school exams, or theoretical driving tests.

> Note that figure 2 shows a simplified version of multiple-choice evaluation, where the model’s predicted answer letter is compared directly to the correct one. Two other popular methods exist that involve log-probability scoring. I implemented them here on GitHub. (As this builds on the concepts explained here, I recommended checking this out after completing this article.)

The following subsections illustrate how the MMLU scoring shown in figure 2 can be implemented in code.

## 1.2 Loading the model

First, before we can evaluate it on MMLU, we have to load the pre-trained model. Here, we are going to use a from-scratch implementation of Qwen3 0.6B in pure PyTorch, which requires only about 1.5 GB of RAM.

Note that the Qwen3 model implementation details are not important here; we simply treat it as an LLM we want to evaluate. However, if you are curious, a from-scratch implementation walkthrough can be found in my previous Understanding and Implementing Qwen3 From Scratch article, and the source code is also available here on GitHub.

Instead of copy & pasting the many lines of Qwen3 source code, we import it from my reasoning\_from\_scratch Python library, which can be installed via

```
```
pip install reasoning_from_scratch
```
```

or

```
```
```
uv add reasoning_from_scratch
```
```
```

#### Code block 1: Loading a pre-trained model

```
```
from pathlib import Path
import torch
from reasoning_from_scratch.ch02 import get_device
from reasoning_from_scratch.qwen3 import (
    download_qwen3_small, Qwen3Tokenizer,
    Qwen3Model, QWEN_CONFIG_06_B
)

device = get_device()

# Set matmul precision to "high" to 
# enable Tensor Cores on compatible GPUs
torch.set_float32_matmul_precision("high")

# Uncomment the following line 
# if you encounter device compatibility issues
# device = "cpu"

# Use the base model by default
WHICH_MODEL = "base"

if WHICH_MODEL == "base":
    download_qwen3_small(
        kind="base", tokenizer_only=False, out_dir="qwen3"
    )
    tokenizer_path = Path("qwen3") / "tokenizer-base.json"
    model_path = Path("qwen3") / "qwen3-0.6B-base.pth"
    tokenizer = Qwen3Tokenizer(tokenizer_file_path=tokenizer_path)

elif WHICH_MODEL == "reasoning":
    download_qwen3_small(
        kind="reasoning", tokenizer_only=False, out_dir="qwen3"
    )
    tokenizer_path = Path("qwen3") / "tokenizer-reasoning.json"
    model_path = Path("qwen3") / "qwen3-0.6B-reasoning.pth"
    tokenizer = Qwen3Tokenizer(
        tokenizer_file_path=tokenizer_path,
        apply_chat_template=True,
        add_generation_prompt=True,
        add_thinking=True,
    )

else:
    raise ValueError(f"Invalid choice: WHICH_MODEL={WHICH_MODEL}")

model = Qwen3Model(QWEN_CONFIG_06_B)
model.load_state_dict(torch.load(model_path))
model.to(device)

# Optionally enable model compilation for potential performance gains
USE_COMPILE = False
if USE_COMPILE:
    torch._dynamo.config.allow_unspec_int_on_nn_module = True
    model = torch.compile(model)
```
```

## 1.3 Checking the generated answer letter

In this section, we implement the simplest and perhaps most intuitive MMLU scoring method, which relies on checking whether a generated multiple-choice answer letter matches the correct answer. This is similar to what was illustrated earlier in Figure 2, which is shown below again for convenience.

For this, we will work with an example from the MMLU dataset:

```
```
example = {
    "question": (
        "How many ways are there to put 4 distinguishable"
        " balls into 2 indistinguishable boxes?"
    ),
    “choices”: ["7", "11", "16", "8"],
    “answer”: "D",
}
```
```

Next, we define a function to format the LLM prompts.

#### Code block 2: Loading a pre-trained model

```
```
def format_prompt(example):
    return (
        f"{example['question']}\n"
        f"A. {example['choices'][0]}\n"
        f"B. {example['choices'][1]}\n"
        f"C. {example['choices'][2]}\n"
        f"D. {example['choices'][3]}\n"
        "Answer: "
    )
# Trailing space in "Answer: " encourages a single-letter next token
```
```

Let’s execute the function on the MMLU example to get an idea of what the formatted LLM input looks like:

```
```
prompt = format_prompt(example)
print(prompt)
```
```

The output is:

How many ways are there to put 4 distinguishable balls into 2  
indistinguishable boxes?

```
```
How many ways are there to put 4 distinguishable balls into 2
indistinguishable boxes?
A. 7
B. 11
C. 16

[Excerpt truncated at the line cap; see url for the remainder.]
