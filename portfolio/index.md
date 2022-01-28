---
title: Portfolio
nav:
  order: 1
  tooltip: Our current and past projects
---

# Portfolio

We support the labs and individuals within the Center by developing a variety of content and software.
Some of the things we create are:

- Modern, responsive web applications
- Powerful and flexible backend systems and APIs
- Interactive data visualizations
- Beautiful and polished websites
- Robust and reproducible data pipelines
- Logos and cohesive brand identities

But the best way to understand what we do is to see it for yourself!
Click on an item below to learn more about it.

**Filter by type:**
{:.center}
{%
  include tags.html
  tags="website, frontend, backend, devops, UI"
%}
{% include search-info.html %}

{% include section.html %}

## Current Projects

{%
  include list.html
  data="portfolio"
  component="card"
  filter="highlight: true, past:"
%}

{%
  include list.html
  data="portfolio"
  component="card"
  filter="highlight:, past:"
  style="small"
%}

{% include section.html %}

## Past Projects

{%
  include list.html
  data="portfolio"
  component="card"
  filter="highlight: true, past: true"
%}

{%
  include list.html
  data="portfolio"
  component="card"
  filter="highlight: , past: true"
  style="small"
%}
