---
title: "MM-OptBench: A Solver-Grounded Benchmark for Multimodal Optimization Modeling"
collection: publications
permalink: /publication/2026-05-12-MM-OptBench-A-Solver-Grounded-Benchmark-for-Multimodal-Optimization-Modeling
date: 2026-05-12
venue: 'arXiv preprint arXiv:2605.12154'
citation: ' Zhong Li,  Qi Huang,  Yuxuan Zhu,  Mohammad Mohammadi Amiri,  Niki van Stein,  Thomas Bäck,  Matthijs van Leeuwen,  Zaiwen Wen,  Lincen Yang, &quot;MM-OptBench: A Solver-Grounded Benchmark for Multimodal Optimization Modeling.&quot; arXiv preprint arXiv:2605.12154, 2026.'
authors:
- Zhong Li
- Qi Huang
- Yuxuan Zhu
- Mohammad Mohammadi Amiri
- Niki van Stein
- Thomas Bäck
- Matthijs van Leeuwen
- Zaiwen Wen
- Lincen Yang
paperurl: https://arxiv.org/abs/2605.12154
arxiv: '2605.12154'
pdf: https://arxiv.org/pdf/2605.12154
venue_type: preprint
abstract: >-
  Optimization modeling translates real decision-making problems into mathematical optimization models
  and solver-executable implementations. Although language models are increasingly used to generate
  optimization formulations and solver code, existing benchmarks are almost entirely text-only. This
  omits many optimization-modeling tasks that arise in operational practice, where requirements are
  described in text but instance information is conveyed through visual artifacts such as tables,
  graphs, maps, schedules, and dashboards. We introduce multimodal optimization modeling, a benchmark
  setting in which models must construct both a mathematical formulation and executable solver code
  from a text-and-visual problem specification. To evaluate this setting, we develop a solver-grounded
  framework that generates structured optimization instances, verifies each with an exact solver, and
  builds both the model-facing inputs and hidden reference files from the same verified source. We
  instantiate the framework as MM-OptBench, a benchmark of 780 solver-verified instances spanning 6
  optimization families, 26 subcategories, and 3 structural difficulty levels. We evaluate 9
  multimodal large language models (MLLMs), including 6 frontier general-purpose models and 3
  math-specialized models, with aggregate, family-level, difficulty-level, and failure-mode analyses.
  The results show that the task remains far from solved: the best two models reach 52.1% and 51.3%
  pass@1, while on average across the six general-purpose MLLMs, pass@1 is 43.4% on easy instances and
  15.9% on hard instances. All three math-specialized MLLMs solve 0/780 instances. Failure attribution
  shows that errors arise both when extracting instance data from text and visuals and when turning
  extracted data into solver-correct formulations and code. MM-OptBench provides a testbed for
  solver-grounded, decision-oriented multimodal intelligence.
---
