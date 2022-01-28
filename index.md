---
title: Home
---

{% capture text %}
We are the Software Engineering Team (SET) of the [Center for Health AI](https://medschool.cuanschutz.edu/ai) at the [University of Colorado Anschutz](https://www.cuanschutz.edu/).

{%
  include link.html
  link="about"
  text="Learn more about us"
  icon="fas fa-arrow-right"
  style="button"
%}
{:.center}
{% endcapture %}

{% 
  include feature.html
  image="images/hsb.png"
  headline="Who we are"
  text=text
  link="about"
%}

{% include section.html %}

{% capture text %}
We are the Software Engineering Team (SET) of the [Center for Health AI](https://medschool.cuanschutz.edu/ai) at the [University of Colorado Anschutz](https://www.cuanschutz.edu/).

{%
  include link.html
  link="portfolio"
  text="Our portfolio"
  icon="fas fa-arrow-right"
  style="button"
%}
{:.center}
{% endcapture %}

{% 
  include feature.html
  image="images/hsb.png"
  headline="Our work"
  text=text
  link="about"
%}
