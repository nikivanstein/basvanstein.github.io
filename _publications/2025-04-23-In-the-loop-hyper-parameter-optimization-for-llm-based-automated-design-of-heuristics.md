---
title: "In-the-loop hyper-parameter optimization for llm-based automated design of heuristics"
collection: publications
permalink: /publication/2025-04-23-In-the-loop-hyper-parameter-optimization-for-llm-based-automated-design-of-heuristics
date: 2025-04-23
venue: 'ACM Transactions on Evolutionary Learning'
citation: ' Niki van Stein,  Diederick Vermetten,  Thomas Bäck, &quot;In-the-loop hyper-parameter optimization for llm-based automated design of heuristics.&quot; ACM Transactions on Evolutionary Learning, 2025.'
authors:
- Niki van Stein
- Diederick Vermetten
- Thomas Bäck
doi: 10.1145/3731567
paperurl: https://doi.org/10.1145/3731567
arxiv: '2410.16309'
pdf: https://arxiv.org/pdf/2410.16309
venue_type: journal
abstract: >-
  Large Language Models (LLMs) have shown great potential in automatically generating and optimizing
  (meta)heuristics, making them valuable tools in heuristic optimization tasks. However, LLMs are
  generally inefficient when it comes to fine-tuning hyper-parameters of the generated algorithms,
  often requiring excessive queries that lead to high computational and financial costs. This paper
  presents a novel hybrid approach, LLaMEA-HPO, which integrates the open source LLaMEA (Large
  Language Model Evolutionary Algorithm) framework with a Hyper-Parameter Optimization (HPO) procedure
  in the loop. By offloading hyper-parameter tuning to an HPO procedure, the LLaMEA-HPO framework
  allows the LLM to focus on generating novel algorithmic structures, reducing the number of required
  LLM queries and improving the overall efficiency of the optimization process. We empirically
  validate the proposed hybrid framework on benchmark problems, including Online Bin Packing,
  Black-Box Optimization, and the Traveling Salesperson Problem. Our results demonstrate that
  LLaMEA-HPO achieves superior or comparable performance compared to existing LLM-driven frameworks
  while significantly reducing computational costs. This work highlights the importance of separating
  algorithmic innovation and structural code search from parameter tuning in LLM-driven code
  optimization and offers a scalable approach to improve the efficiency and effectiveness of LLM-based
  code generation.
---
