---
title: "LLaMEA"
excerpt: "Large Language Evolutionary Algorithm for the automatic design of algorithms."
collection: projects
permalink: /projects/llamea
header:
  teaser: "llamea.png"
  og_image: "llamea.png"

people:
  - shahane
  - yin
  - raponi
  - kononova
  - back
  - stein

projects:
  - 2022-xaipre
  - 2023-ai4oversight
---

<img class="img-fluid" src="/img/projects/llamea-wide.png" alt="LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics"/>

LLaMEA, or Large Language Model Evolutionary Algorithm, is an innovative framework developed by the XAI research group at NACO with the lead of Niki van Stein. It leverages large language models (LLMs), such as GPT-4, to automate the generation and refinement of algorithms such as metaheuristic optimizers. By iteratively evolving algorithms based on performance metrics and runtime evaluations, LLaMEA streamlines the optimization process without requiring extensive prior algorithmic knowledge. 

See also the introductory [Youtube video](https://www.youtube.com/embed/LtFc8K5Uc4w).

Key features of LLaMEA include:

- **Automated Algorithm Generation**: Utilizes GPT models to create and enhance algorithms automatically.

- **Performance Evaluation**: Integrates with IOHexperimenter and other evaluators for real-time feedback, guiding the evolutionary process.

- **Customizable Evolution Strategies**: Allows configuration of strategies to effectively explore algorithmic design spaces.

- **Extensible and Modular Design**: Offers flexibility for users to incorporate other models and evaluation tools.

This framework is particularly beneficial for both research and practical applications in fields where optimization is crucial. For more details, including installation instructions and usage guidelines, please visit the project's [Github Repository](https://github.com/XAI-liacs/LLaMEA).
In addition, a accompanying benchmarking framework with additional real-world problems and baselines is available in the [BLADE Github Repository](https://github.com/XAI-liacs/BLADE).

## Awards

The research on LLaMEA and generated algorithms from LLaMEA have won the following prestiguous awards:

🥈 Silver Award at the [GECCO 2025 Humies competition](https://gecco-2025.sigevo.org/Humies-Awards)  
🏅 Winner of the [GECCO 2025 Any-Time Performance for Affine BBOB competition](https://gecco-2025.sigevo.org/Competition-Awards#AA4AffineBBOB_Competition)  
🏅 Winner of the [GECCO 2024 Any-Time Performance for Affine BBOB competition](https://gecco-2024.sigevo.org/Competition-Awards.html#Anytime_Algorithms_for_Many-affine_BBOB_Functions)

## Related papers

### Methodology
<div class="card-columns row">
  <div class="card col-md-4">
    <a href="https://dl.acm.org/doi/abs/10.1109/TEVC.2024.3497793" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea1.png" alt="LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics"/>
    </a>
    <div class="card-body">
      <p class="card-title">LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics</p>
    </div>
  </div>
  <div class="card col-md-4">
    <a href="https://dl.acm.org/doi/10.1145/3731567" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea2-hpo.png" alt="In-the-loop hyper-parameter optimization for LLM-based automated design of heuristics"/>
    </a>
    <div class="card-body">
      <p class="card-title">In-the-loop hyper-parameter optimization for LLM-based automated design of heuristics</p>
    </div>
  </div>
  <div class="card col-md-4">
    <a href="https://link.springer.com/chapter/10.1007/978-3-031-90065-5_25" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea3-mutation.png" alt="Controlling the mutation in large language models for the efficient evolution of algorithms"/>
    </a>
    <div class="card-body">
      <p class="card-title">Controlling the mutation in large language models for the efficient evolution of algorithms</p>
    </div>
  </div>
  <div class="card col-md-4">
    <a href="https://arxiv.org/abs/2505.21034" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea4-bo.png" alt="LLaMEA-BO: A Large Language Model Evolutionary Algorithm for Automatically Generating Bayesian Optimization Algorithms"/>
    </a>
    <div class="card-body">
      <p class="card-title">LLaMEA-BO: Automatically Generating Bayesian Optimization Algorithms</p>
    </div>
  </div>
  <div class="card col-md-4">
    <a href="https://arxiv.org/abs/2505.15741" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea5-survey.png" alt="Evolutionary Computation and Large Language Models: A Survey of Methods, Synergies, and Applications"/>
    </a>
    <div class="card-body">
      <p class="card-title">Evolutionary Computation and Large Language Models: A Survey of Methods, Synergies, and Applications</p>
    </div>
  </div>
</div>

### Benchmarking and Analysis
<div class="card-columns">
  <div class="card">
    <a href="https://dl.acm.org/doi/10.1145/3712256.3726328" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea6-ceg.png" alt="Code evolution graphs: Understanding large language model driven design of algorithms"/>
    </a>
    <div class="card-body">
      <p class="card-title">Code evolution graphs: Understanding large language model driven design of algorithms</p>
    </div>
  </div>
  <div class="card">
    <a href="https://dl.acm.org/doi/10.1145/3712255.3734347" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea9-blade.png" alt="BLADE: Benchmark suite for LLM-driven Automated Design and Evolution of iterative optimisation heuristics"/>
    </a>
    <div class="card-body">
      <p class="card-title">BLADE: Benchmark suite for LLM-driven Automated Design and Evolution</p>
    </div>
  </div>
  <div class="card">
    <a href="https://arxiv.org/abs/2507.03605" target="_blank">
      <img class="img-fluid mb-2" src="/img/llamea/llamea7-behaviour.png" alt="Behaviour Space Analysis of LLM-driven Meta-heuristic Discovery"/>
    </a>
    <div class="card-body">
      <p class="card-title">Behaviour Space Analysis of LLM-driven Meta-heuristic Discovery</p>
    </div>
  </div>
</div>

### Real World Applications
<div class="card-columns">
  <div class="card">
    <a href="https://dl.acm.org/doi/10.1145/3712255.3734288">
      <img class="img-fluid mb-2" src="/img/llamea/llamea8-optics.png" alt="Optimizing Photonic Structures with Large Language Model Driven Algorithm Discovery"/>
    </a>
    <div class="card-body">
      <p class="card-title">Optimizing Photonic Structures with Large Language Model Driven Algorithm Discovery</p>
    </div>
  </div>
</div>


