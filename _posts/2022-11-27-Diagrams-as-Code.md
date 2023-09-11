---
title: "Tip of the Week: Diagrams as Code"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - diagrams
  - mermaid
  - markdown
---

# Tip of the Week: Diagrams as Code

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

Diagrams can be a useful way to illuminate and communicate ideas. Free-form drawing or drag and drop tools are one common way to create diagrams. With this tip of the week we introduce another option: diagrams as code (DaC), or creating diagrams by using code.

<!-- excerpt end -->

__TLDR (too long, didn't read);__
Diagrams as code (DaC) tools provide an advantage for illustrating concepts by enabling __quick visual positioning__, __source controllable input__, __portability (both for input and output formats)__, and __open collaboration through reproducibility__. Consider using [Mermaid](https://mermaid-js.github.io/mermaid/) (as well as many other DaC tools) to assist your diagramming efforts which can be used directly, within in your markdown files, or [Github commentary](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams) using code blocks (for example, ` ```mermaid `).

## Example Mermaid Diagram as Code

{% capture col1content %}

```
flowchart LR
    a --> b
    b --> c
    c --> d1
    c --> d2
```

_Mermaid code_
{% endcapture %}
{% capture col2content %}

<pre class="mermaid">
flowchart LR
    a --> b
    b --> c
    c --> d1
    c --> d2
</pre>
_Mermaid rendered_
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

{% endcapture %}
{% include cols.html col1=col1content col2=col2content %}

The above shows an example [mermaid flowchart](https://mermaid-js.github.io/mermaid/#/flowchart) code and its rendered output. The syntax is specific to mermaid and acts as a simple coding language to help you depict ideas. Mermaid also includes options for sequence, class, Gantt, and other diagram types. Mermaid provides a [live editor](https://mermaid.live/edit#pako:eNpVzD1PwzAQBuC_Et2cRv6KL_HABBtT2SovV9vQCBxXlqPSRvnvhFRI9KZ73vuYwSUfwMD7V7q4E-VSve7tWK1F1W73VB3vOG5wd7gNnj9IQA0x5EiDX9_NvzML5RRisGDW1lP-tGDHZd2jqaS36-jAlDyFGqazpxKeB_rIFB_DFz-UlP-yM42HlOI_gpnhGww2vMMee62kapliqoYrmJ41SjONrOVSSN21Sw237Z43DLVgXCNKIWSHuPwAvLtMeg) which can be used to quickly draft and share content.

## Mermaid Github Integration

{% capture col1content %}
{% include figure.html image="images/github_mermaid_code.png" caption="Github comment"  %}
{% endcapture %}
{% capture col2content %}
{% include figure.html image="images/github_mermaid_preview.png" caption="Github comment preview"  %}
{% endcapture %}

{% include cols.html col1=col1content col2=col2content %}

Mermaid diagrams may be rendered directly from markdown (`.md`) and text communication content (like pull request or issue comments) within Github. See [Github's blog post on mermaid](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/) for more details covering this topic.

## Mermaid Jupyter Notebook Integration

{% include figure.html image="images/jupyter_mermaid_example.png" caption="Mermaid content rendered in a Jupyter notebook"  width="500px" %}
Mermaid diagrams can be rendered directly within [Jupyter notebooks](https://en.wikipedia.org/wiki/Project_Jupyter#Jupyter_Notebook_Documents) with a small amount of additional code and a rendering service. One way to render mermaid and other diagrams within notebooks is to use [Kroki.io](https://kroki.io/). See [this example](https://cu-dbmi.github.io/notebooks/lab?path=mermaid_example.ipynb) for an interactive demonstration.

## Version Controlling Your Diagrams

<pre class="mermaid">
graph LR
    subgraph Compose
      write[Write Diagram Code]
      render[Render Diagram]
    end
    subgraph Store[Save and Share]
      save[Upload Diagram]
    end
    write --> | create | render
    render --> | revise | write
    render --> | code and exports | save
</pre>
_Mermaid version control workflow example_

Creating your diagrams with code means you can enable reproducible and collaborative work on version control systems (like git). Using git in this way allows you to reference and remix your diagrams as part of development. It also allows others to collaborate on diagrams together making modifications as needed.

## Additional Resources

Please see the following the additional resources which are related to diagrams as code.

- [PlantUML](https://plantuml.com/)
- [Vega](https://vega.github.io/vega/)
- [Kroki.io](https://kroki.io/)
