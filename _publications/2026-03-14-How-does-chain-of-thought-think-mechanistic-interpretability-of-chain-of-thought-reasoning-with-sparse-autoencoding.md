---
title: "How does chain of thought think? mechanistic interpretability of chain-of-thought reasoning with sparse autoencoding"
collection: publications
permalink: /publication/2026-03-14-How-does-chain-of-thought-think-mechanistic-interpretability-of-chain-of-thought-reasoning-with-sparse-autoencoding
date: 2026-03-14
venue: 'Proceedings of the AAAI Conference on Artificial Intelligence'
citation: ' Xi Chen,  Aske Plaat,  Niki van Stein, &quot;How does chain of thought think? mechanistic interpretability of chain-of-thought reasoning with sparse autoencoding.&quot; Proceedings of the AAAI Conference on Artificial Intelligence, 2026.'
authors:
- Xi Chen
- Aske Plaat
- Niki van Stein
doi: 10.1609/aaai.v40i36.40281
paperurl: https://doi.org/10.1609/aaai.v40i36.40281
arxiv: '2507.22928'
pdf: https://arxiv.org/pdf/2507.22928
venue_type: journal
abstract: >-
  Chain-of-thought (CoT) prompting boosts Large Language Models accuracy on multi-step tasks, yet
  whether the generated "thoughts" reflect the true internal reasoning process is unresolved. We
  present the first feature-level causal study of CoT faithfulness. Combining sparse autoencoders with
  activation patching, we extract monosemantic features from Pythia-70M and Pythia-2.8B while they
  tackle GSM8K math problems under CoT and plain (noCoT) prompting. Swapping a small set of
  CoT-reasoning features into a noCoT run raises answer log-probabilities significantly in the 2.8B
  model, but has no reliable effect in 70M, revealing a clear scale threshold. CoT also leads to
  significantly higher activation sparsity and feature interpretability scores in the larger model,
  signalling more modular internal computation. For example, the model's confidence in generating
  correct answers improves from 1.2 to 4.3. We introduce patch-curves and random-feature patching
  baselines, showing that useful CoT information is not only present in the top-K patches but widely
  distributed. Overall, our results indicate that CoT can induce more interpretable internal
  structures in high-capacity LLMs, validating its role as a structured prompting method.
---
