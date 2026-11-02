---
title: "Every Component is a Lookup: Token Attribution and Composition from a Single Decomposition"
collection: publications
permalink: /publication/2026-05-22-Every-Component-is-a-Lookup-Token-Attribution-and-Composition-from-a-Single-Decomposition
date: 2026-05-22
venue: 'arXiv preprint arXiv:2605.23393'
citation: ' Po-Kai Chen,  Aske Plaat,  Niki van Stein, &quot;Every Component is a Lookup: Token Attribution and Composition from a Single Decomposition.&quot; arXiv preprint arXiv:2605.23393, 2026.'
authors:
- Po-Kai Chen
- Aske Plaat
- Niki van Stein
paperurl: https://arxiv.org/abs/2605.23393
arxiv: '2605.23393'
pdf: https://arxiv.org/pdf/2605.23393
venue_type: preprint
abstract: >-
  Interpretability methods for transformers are typically built around separate questions: which
  components interact, how information routes to the output, and which input tokens contribute.
  Because these methods rely on different assumptions, their answers are difficult to relate. We argue
  that two architecturally motivated assumptions suffice to address all three questions: attention and
  MLPs share a key-value form, $φ(S)\,U$, in which $φ(S)$ selects over values $U$, and components read
  from an additive residual stream, the sum of component outputs. Holding these selections at their
  forward-pass values turns the model into a computational graph, of which component interactions,
  composition paths, and token attribution are different readouts. We develop Unpack, a backward
  attribution procedure over this graph, and validate each readout against the corresponding
  established test: interaction scores predict ablation effects across models from 160M to 6.9B
  parameters, recovered routes reproduce established circuits down to the key, query, or value branch
  the circuit specifies, and token attribution passes the same faithfulness test as dedicated
  attribution methods. The results suggest that these two assumptions suffice for the interpretability
  questions above. On a task with a known circuit, we find that contribution and causal effect can
  differ, and that the difference has a recognisable signature: components that matter for the task
  change their contribution when the task is removed from the input, while components that act like a
  bias term do not. Code is available at https://github.com/Fun-Cry/unpacklm.
---
