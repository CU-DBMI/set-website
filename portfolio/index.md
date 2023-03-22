---
title: Portfolio
nav:
  order: 1
  tooltip: Our past, present, and future projects
---

# Portfolio

{% include section.html %}

## Collaborators

Some of the individual groups we work with:
{:.center}

{% capture content %}
{% include figure.html width="100%" link="https://greenelab.com/" image="images/greene-lab.jpg" tooltip="Greene Lab" %}
{% include figure.html width="100%" link="https://tislab.org/" image="images/tis-lab.jpg" tooltip="TIS Lab" %}
{% include figure.html width="100%" link="https://www.waysciencelab.com/" image="images/way-lab.jpg" tooltip="Way Lab" %}
{% endcapture %}

{% include grid.html content=content style="square" %}

{% include section.html %}

**Filter**:
{:.center}
{%
  include tags.html
  tags="website,frontend,backend,devops,UI,API"
%}
{% include search-info.html %}

## Projects

{%
  include list.html
  data="portfolio"
  component="card"
%}
