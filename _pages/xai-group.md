---
permalink: /xai-group/
title: "XAI group"
excerpt: "The XAI research group"
author_profile: true
excerpt: ' '
header:
  overlay_image: "banner1.png"
  og_image: "banner.png"
redirect_from: 
  - /projects.html
  - /projects/

people:
  - stein
  - huang
  - kitharidis
  - wagner
  - lamers
  - antonov
  - zeiser
  - baratov
  - yin
  - preintner
  - shahane
  - ye
---

{% include base_path %}
<div class="author__avatar" style="float:left;"> 
  <img src="/img/groups/xai logo-512px.png" style="background-color:#FFF; border-radius: 10%; padding: 5px;
    border: 1px solid #51555d; max-width: 200px; margin-top:50px; margin-right:20px; margin-bottom:10px;">
</div>

<h2>Explainable AI Research Group</h2>

The XAI (Explainable Artificial Intelligence) research group at <a href="https://liacs.leidenuniv.nl" target="_blank">LIACS</a>, Leiden University focuses on making AI and Evolutionary Computing (EC) systems more understandable and interpretable. Led by Dr. Niki van Stein, the team delves into methods and techniques that allow for the explanation of AI decision-making processes, aiming to enhance transparency and trust in AI technologies. Their work spans various scientific domains and industry applications, such as predictive maintenance, the analysis of heuristic optimization algorithms and the development of novel explainable AI methods. This interdisciplinary effort involves collaboration with experts in machine learning, optimization, and domain-specific experts to develop explainable systems that are both effective and user-friendly.

<h2>Research projects:</h2>
<div class="grid__wrapper">
{% for post in site.projects reversed %}
  {% include archive-single.html type="grid" %}
{% endfor %}
</div>
<hr>