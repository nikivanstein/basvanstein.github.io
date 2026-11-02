---
title: "Curing ill-Conditionality via Representation-Agnostic Distance-Driven Perturbations"
collection: publications
permalink: /publication/2023-08-30-Curing-ill-Conditionality-via-Representation-Agnostic-Distance-Driven-Perturbations
date: 2023-08-30
venue: 'Proceedings of the 17th ACM/SIGEVO Conference on Foundations of Genetic Algorithms'
citation: ' Kirill Antonov,  Anna V. Kononova,  Thomas Bäck,  Niki van Stein, &quot;Curing ill-Conditionality via Representation-Agnostic Distance-Driven Perturbations.&quot; Proceedings of the 17th ACM/SIGEVO Conference on Foundations of Genetic Algorithms, 2023.'
authors:
- Kirill Antonov
- Anna V. Kononova
- Thomas Bäck
- Niki van Stein
doi: 10.1145/3594805.3607138
paperurl: https://doi.org/10.1145/3594805.3607138
pdf: https://dl.acm.org/doi/pdf/10.1145/3594805.3607138
venue_type: conference
abstract: >-
  The objective value of an ill-conditioned function may significantly change with a minor shift of
  the argument in the search space. Ill-conditioned functions do not have at all or exhibit very few
  hints towards better solutions and, thus, they are usually difficult to optimize with randomized
  search heuristics. However, problems that emerge in practical applications are likely to be
  formulated as ill-conditioned functions, as often Euclidean metric is used to measure distance in
  the search space. At the same time, it may be possible to use domain-specific knowledge to define
  such a metric in the search space so that the function stops being ill-conditioned. We consider
  finite search spaces and propose two mutation operators that leverage such metric to optimize the
  function more efficiently. The first operator assumes prior knowledge about the distance, the second
  operator uses the distance as a black box. Those operators apply an estimation of distribution
  algorithm to find the best mutant according to the defined function, which employs the given metric.
  For pseudo-Boolean and integer optimization problems, we experimentally show that both mutation
  operators speed up the search on most of the functions when applied in considered evolutionary
  algorithms and random local search. Moreover, those operators can be applied in any randomized
  search heuristic which uses perturbations. However, our mutation operators increase wall-clock time
  and so are helpful in practice when distance is (much) cheaper to compute than the real objective
  function.
---
