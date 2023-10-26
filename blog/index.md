---
title: Blog
nav:
  order: 3
  tooltip: Musings and miscellany
---

# {% include icon.html icon="fa-solid fa-feather-pointed" %}Blog

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}

{% include tags.html tags=site.tags %}
