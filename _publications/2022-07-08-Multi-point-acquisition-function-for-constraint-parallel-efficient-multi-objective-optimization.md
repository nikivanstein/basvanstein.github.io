---
title: "Multi-point acquisition function for constraint parallel efficient multi-objective optimization"
collection: publications
permalink: /publication/2022-07-08-Multi-point-acquisition-function-for-constraint-parallel-efficient-multi-objective-optimization
date: 2022-07-08
venue: 'Proceedings of the Genetic and Evolutionary Computation Conference'
citation: ' Roy de Winter,  Niki van Stein,  Thomas Bäck, &quot;Multi-point acquisition function for constraint parallel efficient multi-objective optimization.&quot; Proceedings of the Genetic and Evolutionary Computation Conference, 2022.'
authors:
- Roy de Winter
- Niki van Stein
- Thomas Bäck
doi: 10.1145/3512290.3528696
paperurl: https://doi.org/10.1145/3512290.3528696
pdf: https://dl.acm.org/doi/pdf/10.1145/3512290.3528696
venue_type: conference
abstract: >-
  Bayesian optimization is often used to optimize expensive black box optimization problems with long
  simulation times. Typically Bayesian optimization algorithms propose one solution per iteration. The
  downside of this strategy is the sub-optimal use of available computing power. To efficiently use
  the available computing power (or a number of licenses etc.) we introduce a multi-point acquisition
  function for parallel efficient multi-objective optimization algorithms. The multi-point acquisition
  function is based on the hypervolume contribution of multiple solutions simultaneously, leading to
  well spread solutions along the Pareto frontier. By combining this acquisition function with a
  constraint handling technique, multiple feasible solutions can be proposed and evaluated in parallel
  every iteration. The hypervolume and feasibility of the solutions can easily be estimated by using
  multiple cheap radial basis functions as surrogates with different configurations. The acquisition
  function can be used with different population sizes and even for one shot optimization. The
  strength and generalizability of the new acquisition function is demonstrated by optimizing a set of
  black box constraint multi-objective problem instances. The experiments show a huge time saving
  factor by using our novel multi-point acquisition function, while only marginally worsening the
  hypervolume after the same number of function evaluations.
---
