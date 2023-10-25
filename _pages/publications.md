---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% if author.researchgate %}
  In addition, you can find me active on  <u><a href="{{author.researchgate}}">my ResearchGate</a>.</u>. Follow me to keep up to date with my research activities.
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
