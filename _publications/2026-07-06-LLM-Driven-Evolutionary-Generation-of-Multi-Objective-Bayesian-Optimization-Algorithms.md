---
title: "LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms"
collection: publications
permalink: /publication/2026-07-06-LLM-Driven-Evolutionary-Generation-of-Multi-Objective-Bayesian-Optimization-Algorithms
date: 2026-07-06
venue: 'arXiv preprint arXiv:2607.08791'
citation: ' Georgios Laskaris,  Reuben Brasher,  Niki van Stein,  Elena Raponi,  Thomas Bäck,  Florian Neukart, &quot;LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms.&quot; arXiv preprint arXiv:2607.08791, 2026.'
authors:
- Georgios Laskaris
- Reuben Brasher
- Niki van Stein
- Elena Raponi
- Thomas Bäck
- Florian Neukart
paperurl: https://arxiv.org/abs/2607.08791
arxiv: '2607.08791'
pdf: https://arxiv.org/pdf/2607.08791
venue_type: preprint
abstract: >-
  Designing effective multi-objective Bayesian optimization (MOBO) algorithms requires balancing many
  interdependent design choices whose optimal configuration is problem-dependent and typically demands
  deep expertise. We extend the LLaMEA framework to MOBO, using large language models as mutation and
  crossover operators within evolutionary strategies to generate complete algorithm implementations,
  with SMAC hyperparameter optimization integrated into the evolutionary loop. Across nine
  evolutionary runs we generated approximately 900 algorithms and benchmarked them on twelve synthetic
  problems (ZDT, DTLZ, WFG) and three real-world engineering problems (RE), using a BoFire qParEGO
  implementation as a state-of-the-art Bayesian-optimization baseline. On the synthetic suite the
  strongest generated algorithm attains the highest mean normalized hypervolume (0.971, vs. 0.869 for
  qParEGO) while requiring roughly 60x less wall-clock time; a Friedman test with post-hoc analysis
  places the two in a single top-performing group, and per-problem tests find the generated algorithm
  significantly better than qParEGO on 7 of the 12 problems and never worse, matching state-of-the-art
  accuracy at an order-of-magnitude lower cost. On the three unseen real-world engineering problems a
  generated algorithm attains the best mean normalized hypervolume (0.985, vs. 0.971 for
  qParEGO)--significantly better than qParEGO on two of the three problems--at roughly 3.4x lower
  wall-clock cost, confirming that the gains transfer beyond the synthetic regime. LLM-driven
  evolutionary search can thus discover algorithm designs that achieve Pareto-efficient trade-offs
  difficult to reach through manual design.
---
