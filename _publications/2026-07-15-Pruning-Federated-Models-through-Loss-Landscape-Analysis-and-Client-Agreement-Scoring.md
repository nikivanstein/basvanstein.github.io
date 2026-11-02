---
title: "Pruning Federated Models through Loss Landscape Analysis and Client Agreement Scoring"
collection: publications
permalink: /publication/2026-07-15-Pruning-Federated-Models-through-Loss-Landscape-Analysis-and-Client-Agreement-Scoring
redirect_from:
  - /publication/2024-01-01-Automated-Federated-Learning-via-Informed-Pruning
date: 2026-07-15
venue: 'IEEE Internet of Things Journal'
citation: ' Christian Internò,  Elena Raponi,  Markus Olhofer,  Ali Raza,  Thomas Bäck,  Niki van Stein,  Yaochu Jin,  Barbara Hammer, &quot;Pruning Federated Models through Loss Landscape Analysis and Client Agreement Scoring.&quot; IEEE Internet of Things Journal, 2026.'
authors:
- Christian Internò
- Elena Raponi
- Markus Olhofer
- Ali Raza
- Thomas Bäck
- Niki van Stein
- Yaochu Jin
- Barbara Hammer
doi: 10.1109/jiot.2026.3686028
paperurl: https://doi.org/10.1109/jiot.2026.3686028
arxiv: '2405.10271'
pdf: https://arxiv.org/pdf/2405.10271
venue_type: journal
abstract: >-
  The practical deployment of Federated Learning (FL) on resource-constrained devices is fundamentally
  limited by the high cost of training large models and the instability caused by heterogeneous
  (non-IID) client data. Conventional pruning methods often treat data heterogeneity as a problem to
  be mitigated. In this work, we introduce a paradigm shift: we reframe client diversity as a feature
  to be harnessed. We propose AutoFLIP, a framework that begins not with training, but with a one-time
  federated loss exploration. During this phase, clients collaboratively build a map of the collective
  loss landscape, using their diverse data to reveal the problem's essential structure. This shared
  intelligence then guides an adaptive pruning strategy that is dynamically refined by client
  agreement throughout training. This approach allows AutoFLIP to identify robust and efficient
  sub-networks from the outset. Our extensive experiments show that AutoFLIP reduces computational
  overhead by an average of 52% and communication costs by over 65% while simultaneously achieving
  state-of-the-art accuracy in challenging non-IID settings.
---
