---
title: "State Design Matters: How Representations Shape Dynamic Reasoning in Large Language Models"
collection: publications
permalink: /publication/2026-01-25-State-Design-Matters-How-Representations-Shape-Dynamic-Reasoning-in-Large-Language-Models
date: 2026-01-25
venue: 'arXiv preprint arXiv:2602.15858'
citation: ' Annie Wong,  Aske Plaat,  Thomas Bäck,  Niki van Stein,  Anna V. Kononova, &quot;State Design Matters: How Representations Shape Dynamic Reasoning in Large Language Models.&quot; arXiv preprint arXiv:2602.15858, 2026.'
authors:
- Annie Wong
- Aske Plaat
- Thomas Bäck
- Niki van Stein
- Anna V. Kononova
paperurl: https://arxiv.org/abs/2602.15858
arxiv: '2602.15858'
pdf: https://arxiv.org/pdf/2602.15858
venue_type: preprint
abstract: >-
  As large language models (LLMs) move from static reasoning tasks toward dynamic environments, their
  success depends on the ability to navigate and respond to an environment that changes as they
  interact at inference time. An underexplored factor in these settings is the representation of the
  state. Holding model parameters fixed, we systematically vary three key aspects: (1) state
  granularity (long form versus summary), (2) structure (natural language versus symbolic), and (3)
  spatial grounding (text-only versus images or textual map encodings) across sequential
  decision-making benchmarks. We find that trajectory summarisation improves performance by reducing
  noise and stabilising long-horizon reasoning. Second, natural language representations are the most
  robust across models, whereas structured encodings help mainly for models with strong code or
  structured output priors, such as JSON schemas. Third, while image-inputs show some benefit,
  text-based spatial encodings prove most effective. This advantage stems not from the spatial
  information itself, but from the act of construction, which compels the model to perform the spatial
  reasoning that static input does not elicit. Overall, we demonstrate that design choices for
  representing state are a decisive factor in performance, distinct from the availability of
  information itself. We note, however, that even with improved representations, current LLMs and VLMs
  remain brittle over long horizons, particularly when they must synthesise information to manage
  multiple subtasks to reach a goal.
---
