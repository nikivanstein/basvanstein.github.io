---
title: "LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI"
collection: publications
selected: true
topic: AAD
permalink: /publication/2026-01-29-LLaMEA-SAGE-Guiding-Automated-Algorithm-Design-with-Structural-Feedback-from-Explainable-AI
date: 2026-01-29
venue: 'arXiv preprint arXiv:2601.21511'
citation: ' Niki van Stein,  Anna V. Kononova,  Lars Kotthoff,  Thomas Bäck, &quot;LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI.&quot; arXiv preprint arXiv:2601.21511, 2026.'
authors:
- Niki van Stein
- Anna V. Kononova
- Lars Kotthoff
- Thomas Bäck
paperurl: https://arxiv.org/abs/2601.21511
arxiv: '2601.21511'
pdf: https://arxiv.org/pdf/2601.21511
venue_type: preprint
abstract: >-
  Large language models have enabled automated algorithm design (AAD) by generating optimization
  algorithms directly from natural-language prompts. While evolutionary frameworks such as LLaMEA
  demonstrate strong exploratory capabilities across the algorithm design space, their search dynamics
  are entirely driven by fitness feedback, leaving substantial information about the generated code
  unused. We propose a mechanism for guiding AAD using feedback constructed from graph-theoretic and
  complexity features extracted from the abstract syntax trees of the generated algorithms, based on a
  surrogate model learned over an archive of evaluated solutions. Using explainable AI techniques, we
  identify features that substantially affect performance and translate them into natural-language
  mutation instructions that steer subsequent LLM-based code generation without restricting
  expressivity. We propose LLaMEA-SAGE, which integrates this feature-driven guidance into LLaMEA, and
  evaluate it across several benchmarks. We show that the proposed structured guidance achieves the
  same performance faster than vanilla LLaMEA in a small controlled experiment. In a larger-scale
  experiment using the MA-BBOB suite from the GECCO-MA-BBOB competition, our guided approach achieves
  superior performance compared to state-of-the-art AAD methods. These results demonstrate that
  signals derived from code can effectively bias LLM-driven algorithm evolution, bridging the gap
  between code structure and human-understandable performance feedback in automated algorithm design.
---
