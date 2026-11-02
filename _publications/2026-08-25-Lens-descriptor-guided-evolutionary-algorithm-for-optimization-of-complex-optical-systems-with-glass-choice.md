---
title: "Lens-descriptor guided evolutionary algorithm for optimization of complex optical systems with glass choice"
collection: publications
permalink: /publication/2026-08-25-Lens-descriptor-guided-evolutionary-algorithm-for-optimization-of-complex-optical-systems-with-glass-choice
date: 2026-08-25
venue: 'International Conference on Parallel Problem Solving from Nature'
citation: ' Kirill Antonov,  Teus Tukker,  Tiago Botari,  Thomas Bäck,  Anna V. Kononova,  Niki van Stein, &quot;Lens-descriptor guided evolutionary algorithm for optimization of complex optical systems with glass choice.&quot; International Conference on Parallel Problem Solving from Nature, 2026.'
authors:
- Kirill Antonov
- Teus Tukker
- Tiago Botari
- Thomas Bäck
- Anna V. Kononova
- Niki van Stein
doi: 10.1007/978-3-032-36229-2_25
paperurl: https://doi.org/10.1007/978-3-032-36229-2_25
arxiv: '2601.22075'
pdf: https://arxiv.org/pdf/2601.22075
venue_type: chapter
abstract: >-
  Designing high-performance optical lenses entails exploring a high-dimensional, tightly constrained
  space of surface curvatures, glass choices, element thicknesses, and spacings. In practice, standard
  optimizers (e.g., gradient-based local search and evolutionary strategies) often converge to a
  single local optimum, overlooking many comparably good alternatives that matter for downstream
  engineering decisions. We propose the Lens Descriptor-Guided Evolutionary Algorithm (LDG-EA), a
  two-stage framework for multimodal lens optimization. LDG-EA first partitions the design space into
  behavior descriptors defined by curvature-sign patterns and material indices, then learns a
  probabilistic model over descriptors to allocate evaluations toward promising regions. Within each
  descriptor, LDG-EA applies the Hill-Valley Evolutionary Algorithm with covariance-matrix
  self-adaptation to recover multiple distinct local minima, optionally followed by gradient-based
  refinement. On a 24-variable (18 continuous and 6 integer), six-element Double-Gauss topology,
  LDG-EA generates on average around 14500 candidate minima spanning 636 unique descriptors, an order
  of magnitude more than a CMA-ES baseline, while keeping wall-clock time at one hour scale. Although
  the best LDG-EA design is slightly worse than a fine-tuned reference lens, it remains in the same
  performance range. Overall, the proposed LDG-EA produces a diverse set of solutions while
  maintaining competitive quality within practical computational budgets and wall-clock time.
---
