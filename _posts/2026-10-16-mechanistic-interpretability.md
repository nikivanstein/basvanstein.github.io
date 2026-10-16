---
title: 'Looking inside the model: mechanistic interpretability, and why LLaMEA needs it'
date: 2026-10-16
permalink: /posts/2026/10/mechanistic-interpretability/
related:
  - title: "Every Component Is a Lookup (arXiv:2605.23393)"
    url: https://arxiv.org/abs/2605.23393
    kind: Paper
  - title: "LLaMEA-SAGE (arXiv:2601.21511)"
    url: https://arxiv.org/abs/2601.21511
    kind: Paper
  - title: "LLaMEA"
    url: /projects/llamea
    kind: Project
  - title: "Our new book: Agentic Large Language Models"
    url: /posts/2026/10/agentic-llms-book/
    kind: Blog
excerpt: 'A plain-language tour of our paper "Every Component Is a Lookup", and why understanding how LLMs make design decisions matters for evolving code.'
header:
  teaser: "teasers/mechanistic-interpretability.png"
  og_image: "teasers/mechanistic-interpretability.png"
tags:
  - explainable-ai
  - mechanistic-interpretability
  - llm
  - llamea
  - automatic-algorithm-design
---

Most of explainable AI looks at a model from the outside: which input features mattered for a prediction, and how much. **Mechanistic interpretability** asks a different question: what actually happens *inside* the model? Which internal components do the work, how do they pass information to each other, and which route through the network produces the answer?

For large language models this is a hard question. A transformer has many layers, each with attention heads and MLP blocks, all writing into the same internal signal. In this post I explain, in plain language, a recent paper from our group that makes this question more manageable, and why it matters for our work on automated algorithm design with [LLaMEA](/projects/llamea).

## Three questions, three toolboxes

When researchers open up a transformer, they usually ask one of three questions:

1. **Interaction:** which components work together? If I switch one off, which others are affected?
2. **Composition:** how does information travel from the input to the output? Which chain of components forms a "circuit" for a task?
3. **Attribution:** which words in the input mattered for the output?

Until now, each of these questions has had its own methods, each built on its own assumptions. That makes the answers hard to compare: if two methods disagree, is the model doing something subtle, or are the methods simply measuring different things?

## One graph for all three

In **[Every Component Is a Lookup](https://arxiv.org/abs/2605.23393){:target="_blank"}**, Po-Kai Chen, Aske Plaat and I show that all three questions can be answered from one and the same picture of the model.

The idea rests on two observations about how transformers are built:

- **Every component behaves like a lookup.** Both attention heads and MLP blocks first *select* (decide how much weight to give to each stored item) and then *read out* a mix of values. Attention selects over earlier words; an MLP selects over the patterns it has learned.
- **Everything is added to one shared stream.** Each component writes its result into the residual stream by simple addition, and later components read from that sum.

Now take one specific input and run the model on it. If we keep all the "selections" fixed at the values they had in that run, what remains is linear: a graph in which every component's contribution can be traced exactly through the additions. Interaction, composition and attribution then become three different ways of *reading the same graph*. We introduce a procedure, called **Unpack**, that walks this graph backwards from the output to find which components and which input tokens contributed.

## Does it hold up?

A new view of a model is only useful if it agrees with what the model really does. We tested it in three ways:

- The interaction scores from the graph predict what happens when components are actually switched off (ablated), across models from 160 million to 6.9 billion parameters.
- The routes we recover match circuits that other researchers had already found by hand, down to whether information flows through the key, query or value of an attention head.
- The token attributions pass the same faithfulness test that dedicated attribution methods are judged by.

We also found something I find intriguing. *Contributing* to an output and *causing* it are not the same thing. Some components change their contribution when the task is removed from the input: they really take part in solving the task. Others behave more like a constant offset, a bias that is always there, whatever the input. Telling the two apart matters if you want to know what a model is actually computing.

The code is available on GitHub; see the paper for the link.

## Why this matters for LLaMEA

[LLaMEA](/projects/llamea) uses an LLM inside an evolutionary loop to write, mutate and improve optimisation algorithms. It works well, but the LLM itself is still a black box. When it proposes a new mutation operator, switches to a covariance-based update, or adds a restart strategy, we see the code, but not *why* it made that design decision.

That is exactly the kind of question mechanistic interpretability can help answer, and it is a direction we want to push much further. Three questions drive our plans:

- **Understanding design decisions.** Which internal mechanisms lead an LLM to propose a particular algorithmic idea? Are its choices driven by the problem description, by patterns it has seen in training code, or by the feedback we give it?
- **Steering those decisions.** If we know which components are responsible for, say, "make the search more exploratory", we can try to steer the model in that direction directly, instead of only rewriting the prompt.
- **Intervening to search faster.** Searching through the space of programs is expensive: every candidate algorithm has to be generated and then evaluated. Targeted interventions inside the model could help it avoid unpromising directions and produce useful variations sooner, speeding up the search in code space.

This builds on work we already do from the outside. In [LLaMEA-SAGE](https://arxiv.org/abs/2601.21511){:target="_blank"}, for example, we use explainable AI to give the LLM structural feedback about the algorithms it generates. Mechanistic interpretability lets us take the next step and also look at the generator itself.

It is also why our new textbook, [*Agentic Large Language Models*](/posts/2026/10/agentic-llms-book/), has a chapter on mechanistic interpretability for LLM agents. When LLMs start to act and design on our behalf, understanding how they reach their decisions becomes more important, not less.

**Paper:** Po-Kai Chen, Aske Plaat, Niki van Stein. *Every Component Is a Lookup: One Linear Graph for Interaction, Composition and Attribution.* [arXiv:2605.23393](https://arxiv.org/abs/2605.23393){:target="_blank"} ([publication page](/publication/2026-05-22-Every-Component-is-a-Lookup-Token-Attribution-and-Composition-from-a-Single-Decomposition)).
