---
permalink: /projects/
title: "Projects"
excerpt: "All projects of the XAI group"
author_profile: true
excerpt: ' '
header:
  overlay_image: "banner1.png"
  og_image: "banner.png"
redirect_from: 
  - /projects.html
---

{% include base_path %}

{% for post in site.projects reversed %}
  {% include archive-single.html %}
  ---
{% endfor %}
