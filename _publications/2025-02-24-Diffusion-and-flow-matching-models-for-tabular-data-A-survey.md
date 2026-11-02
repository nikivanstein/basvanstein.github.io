---
title: "Diffusion and flow matching models for tabular data: A survey"
collection: publications
permalink: /publication/2025-02-24-Diffusion-and-flow-matching-models-for-tabular-data-A-survey
date: 2025-02-24
venue: 'arXiv preprint arXiv:2502.17119'
citation: ' Zhong Li,  Qi Huang,  Lincen Yang,  Jiayang Shi,  Zhao Yang,  Niki van Stein,  Thomas Bäck,  Matthijs van Leeuwen, &quot;Diffusion and flow matching models for tabular data: A survey.&quot; arXiv preprint arXiv:2502.17119, 2025.'
authors:
- Zhong Li
- Qi Huang
- Lincen Yang
- Jiayang Shi
- Zhao Yang
- Niki van Stein
- Thomas Bäck
- Matthijs van Leeuwen
paperurl: https://arxiv.org/abs/2502.17119
arxiv: '2502.17119'
pdf: https://arxiv.org/pdf/2502.17119
venue_type: preprint
abstract: >-
  Deep generative models have made rapid progress in image, text, audio, and video generation, and are
  increasingly being applied to structured records. For tabular data, however, generative modeling
  remains difficult: a dataset may contain numerical and categorical attributes, missing values,
  sensitive fields, imbalanced categories, complex feature dependencies, and domain constraints.
  Earlier tabular data modeling methods based on GANs or VAEs have achieved useful results, but they
  can suffer from unstable training, mode collapse, weak modeling of multimodal distributions, and
  fragile handling of mixed-type features. Diffusion models have therefore attracted growing interest
  because their noising-and-denoising formulation provides a flexible and stable way to model complex
  data distributions, and has been adapted to tabular synthesis, missing-value imputation, trustworthy
  data generation, and anomaly detection. Flow matching offers a closely related route by learning
  transport vector fields along probability paths, often with more direct control over path design and
  sampling efficiency. Despite this progress, the literature on diffusion and flow matching models for
  tabular data remains difficult to compare because methods target different tasks and rely on
  different representations, objectives, evaluation protocols, and domain assumptions. To the best of
  our knowledge, this is the first survey dedicated specifically to diffusion and flow matching models
  for tabular data. We review work from June 2015 to May 2026, organize it around data-engineering
  challenges, tasks, design choices, and evaluation dimensions, and discuss open problems in
  scalability, feature dependency modeling, privacy, fairness, benchmarking, and constraint-aware
  generation. We maintain updates in a GitHub repository.
---
