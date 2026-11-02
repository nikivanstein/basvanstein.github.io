---
title: "Scalable, Explainable and Provably Robust Anomaly Detection with One-Step Flow Matching"
collection: publications
permalink: /publication/2025-10-21-Scalable-Explainable-and-Provably-Robust-Anomaly-Detection-with-One-Step-Flow-Matching
date: 2025-10-21
venue: 'Advances in Neural Information Processing Systems'
citation: ' Zhong Li,  Qi Huang,  Yuxuan Zhu,  Lincen Yang,  Mohammad Mohammadi Amiri,  Niki van Stein,  Matthijs van Leeuwen, &quot;Scalable, Explainable and Provably Robust Anomaly Detection with One-Step Flow Matching.&quot; Advances in Neural Information Processing Systems, 2025.'
authors:
- Zhong Li
- Qi Huang
- Yuxuan Zhu
- Lincen Yang
- Mohammad Mohammadi Amiri
- Niki van Stein
- Matthijs van Leeuwen
doi: 10.52202/085713-2936
paperurl: https://doi.org/10.52202/085713-2936
arxiv: '2510.18328'
pdf: https://arxiv.org/pdf/2510.18328
venue_type: conference
abstract: >-
  We introduce Time-Conditioned Contraction Matching (TCCM), a novel method for semi-supervised
  anomaly detection in tabular data. TCCM is inspired by flow matching, a recent generative modeling
  framework that learns velocity fields between probability distributions and has shown strong
  performance compared to diffusion models and generative adversarial networks. Instead of directly
  applying flow matching as originally formulated, TCCM builds on its core idea -- learning velocity
  fields between distributions -- but simplifies the framework by predicting a time-conditioned
  contraction vector toward a fixed target (the origin) at each sampled time step. This design offers
  three key advantages: (1) a lightweight and scalable training objective that removes the need for
  solving ordinary differential equations during training and inference; (2) an efficient scoring
  strategy called one time-step deviation, which quantifies deviation from expected contraction
  behavior in a single forward pass, addressing the inference bottleneck of existing continuous-time
  models such as DTE (a diffusion-based model with leading anomaly detection accuracy but heavy
  inference cost); and (3) explainability and provable robustness, as the learned velocity field
  operates directly in input space, making the anomaly score inherently feature-wise attributable;
  moreover, the score function is Lipschitz-continuous with respect to the input, providing
  theoretical guarantees under small perturbations. Extensive experiments on the ADBench benchmark
  show that TCCM strikes a favorable balance between detection accuracy and inference cost,
  outperforming state-of-the-art methods -- especially on high-dimensional and large-scale datasets.
  The source code is available at our GitHub repository.
---
