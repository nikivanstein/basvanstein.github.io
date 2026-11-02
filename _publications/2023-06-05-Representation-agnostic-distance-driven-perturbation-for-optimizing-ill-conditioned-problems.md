---
title: "Representation-agnostic distance-driven perturbation for optimizing ill-conditioned problems"
collection: publications
permalink: /publication/2023-06-05-Representation-agnostic-distance-driven-perturbation-for-optimizing-ill-conditioned-problems
date: 2023-06-05
venue: 'Preprint on arXiv preprint arXiv:2306.02985'
citation: ' Kirill Antonov,  Anna V. Kononova,  Thomas Bäck,  Niki van Stein, &quot;Representation-agnostic distance-driven perturbation for optimizing ill-conditioned problems.&quot; Preprint on arXiv preprint arXiv:2306.02985, 2023.'
authors:
- Kirill Antonov
- Anna V. Kononova
- Thomas Bäck
- Niki van Stein
paperurl: https://arxiv.org/abs/2306.02985
arxiv: '2306.02985'
pdf: https://arxiv.org/pdf/2306.02985
venue_type: preprint
abstract: >-
  Locality is a crucial property for efficiently optimising black-box problems with randomized search
  heuristics. However, in practical applications, it is not likely to always find such a genotype
  encoding of candidate solutions that this property is upheld with respect to the Hamming distance.
  At the same time, it may be possible to use domain-specific knowledge to define a metric with
  locality property. We propose two mutation operators to solve such optimization problems more
  efficiently using the metric. The first operator assumes prior knowledge about the distance, the
  second operator uses the distance as a black box. Those operators apply an estimation of
  distribution algorithm to find the best mutant according to the defined in the paper function, which
  employs the given distance. For pseudo-boolean and integer optimization problems, we experimentally
  show that both mutation operators speed up the search on most of the functions when applied in
  considered evolutionary algorithms and random local search. Moreover, those operators can be applied
  in any randomized search heuristic which uses perturbations. However, our mutation operators
  increase wall-clock time and so are helpful in practice when distance is (much) cheaper to compute
  than the real objective function.
---
