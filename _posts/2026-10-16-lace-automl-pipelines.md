---
title: 'From configurations to code: evolving AutoML pipelines with LLaMEA'
date: 2026-10-16
permalink: /posts/2026/10/lace-automl-pipelines/
related:
  - title: "Evolving Executable Pipeline Programs for AutoML with Language Models (arXiv:2608.16416)"
    url: https://arxiv.org/abs/2608.16416
    kind: Paper
  - title: "Keynote: Automated Algorithm Design, AutoML Conference 2026"
    url: /talks/2026-09-28-keynote-automl
    kind: Talk
  - title: "LLMs for Optimization in Code-Spaces (recording)"
    url: /talks/2026-07-30-invited-automl-summer-school-2
    kind: Talk
  - title: "LLaMEA"
    url: /projects/llamea
    kind: Project
excerpt: 'LACE lets a language model evolve complete, readable machine learning pipelines, the topic of my keynote at the AutoML Conference 2026.'
header:
  teaser: "talks/2026-09-28-automl-keynote.jpg"
  og_image: "talks/2026-09-28-automl-keynote.jpg"
tags:
  - automl
  - llamea
  - llm
  - automatic-algorithm-design
  - evolutionary-computation
---

At the [AutoML Conference 2026](/talks/2026-09-28-keynote-automl) in Ljubljana I gave a keynote on automated algorithm design, and on what happens when we apply it to AutoML itself. This post covers the work at the heart of that talk: **[LACE](https://arxiv.org/abs/2608.16416){:target="_blank"}**, which evolves complete machine learning pipelines as code.

## The limits of a fixed search space

Automated machine learning (AutoML) systems take a dataset and search for a good pipeline: how to preprocess the data, which model to train, and which hyperparameters to use. Systems such as auto-sklearn, H2O and AutoGluon are very good at this, but they all search inside a space that someone defined in advance: a fixed menu of preprocessing steps, learners and hyperparameter ranges.

That works well as long as the best pipeline is on the menu. They can select and tune known components, but they cannot invent a pipeline structure that nobody put in the search space.

## Searching over programs instead

With [LLaMEA](/projects/llamea) we have spent the past two years showing that a large language model inside an evolutionary loop can design new optimisation algorithms as code. LACE takes the same idea to AutoML. Instead of searching over configurations, it searches over **complete, executable pipeline programs**:

- The population consists of Python classes that follow the familiar scikit-learn interface (`fit`, `predict`).
- A language model acts as the variation operator: it takes promising pipelines and writes new variants, from small changes to entirely new structures.
- Each candidate is trained and evaluated, and the best ones survive into the next generation.

Because every candidate is ordinary Python, the result is not a configuration file or a black-box predictor: it is a pipeline you can read, run, reuse and edit, together with the search history that produced it.

## How well does it work?

We evaluated LACE on 68 classification tasks from OpenML, under a protocol designed to prevent leakage: the language model never learns which dataset it is working on, so it cannot simply recall a known solution.

- LACE (with GPT-5.4-mini as the generator) **significantly outperforms auto-sklearn, H2O and a fixed XGBoost baseline**.
- Against **AutoGluon**, the strongest search-based system in our comparison, we found **no detectable difference**.
- Recent **tabular foundation models** are more accurate on the tasks they support, but they do not support all of them, while LACE covers the full benchmark. They also apply a fixed pretrained predictor, rather than returning a task-specific program you can inspect.

For me, the most important result is not the raw accuracy. It is that the search space is now defined by code. That gives three things a fixed search space cannot: coverage of every task, pipelines that practitioners can directly reuse and adapt, and a search space you extend by editing a prompt rather than rewriting the framework.

## Back to the keynote

This is the message I brought to Ljubljana: once the search space is code, AutoML and automated algorithm design become the same problem. The same machinery that evolves a new optimisation heuristic can evolve a preprocessing step or a complete pipeline, and the result stays readable for the people who use it.

That readability also raises new questions. Why does the language model propose a particular pipeline structure, and can we steer it to search faster? Those questions connect directly to our new work on [mechanistic interpretability](/posts/2026/10/mechanistic-interpretability/).

If you want to see an earlier version of this story, the recording of my lecture [*LLMs for Optimization in Code-Spaces: From Metaheuristic Design to AutoML*](/talks/2026-07-30-invited-automl-summer-school-2) at the AutoML summer school in Dortmund is [on YouTube](https://youtu.be/gBlLYa-rMuo){:target="_blank"}.

**Paper:** Sofoklis Kitharidis, Cor J. Veenman, Jan N. van Rijn, Thomas Bäck, Niki van Stein. *Evolving Executable Pipeline Programs for AutoML with Language Models.* [arXiv:2608.16416](https://arxiv.org/abs/2608.16416){:target="_blank"} ([publication page](/publication/2026-08-17-Evolving-Executable-Pipeline-Programs-for-AutoML-with-Language-Models)).
