---
title: "Tip of the Week: Remove Unused Code to Avoid Software Decay"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - code-quality
  - software-decay
  - code-decay
  - vulture
  - pylint
  - coverage.py
---

# Tip of the Week: Remove Unused Code to Avoid Software Decay

{% include tip-of-the-week-intro.html %}

<!-- excerpt start -->

The act of creating software often involves many iterations of writing, personal collaborations, and testing. During this process it's common to lose awareness of code which is no longer used, and thus may not be tested or otherwise linted. Unused code may contribute to ["software decay"](https://en.wikipedia.org/wiki/Software_rot), the gradual diminishment of code quality or functionality. This post will cover software decay and strategies for addressing unused code to help keep your code quality high.

<!-- excerpt end -->

__TLDR (too long, didn't read);__
Unused code is easy to amass and may cause your code quality or code functionality to diminish ("decay") over time. Effort must be taken to maintain any code or artifacts you add to your repositories, including those which are unused. Consider using [Vulture](https://github.com/jendrikseipp/vulture), [Pylint](https://pylint.pycqa.org/), or [Coverage](https://coverage.readthedocs.io/) to help illuminate sections of your code which may need to be removed.

## Code Lifecycle and Maintenance

<pre class="mermaid">
stateDiagram
    direction LR
    removal : removed or archived
    changes : changes needed
    [*] --> added
    added --> maintenance
    state maintenance {
      direction LR
      updated --> changes
      changes --> updated
    }
    maintenance --> removal
    removal --> [*]
</pre>
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
_Diagram showing code lifecycle activities._

Adding code to a project involves a loose agreement to maintenance for however long the code is available. The maintenance of the code can involve added efforts in changes as well as passive impacts like longer test durations or decreased readability (simply from more code).

<div id="vis"></div>
{:.center}

<script src="https://cdn.jsdelivr.net/npm/vega@5.22.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.6.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.21.0"></script>
<script>
var spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.5.0.json",
    "description": "A simple line chart to demonstrate lines of code and associated theoretical time cost.",
    "title":"Time Cost per Line of Code",
    "width": 500,
    "height": 200,
    "config": {
      "title":{"fontSize":14},
      "axisY":{"titleFontSize":14, "labelFontSize":12},
      "axisX":{"titleFontSize":14, "labelFontSize":12}
    },
    "data": {
      "values": [
        {"x": 1, "y": 28},
        {"x": 1000, "y": 500}
      ]
    },
    "mark": {"type": "line", "point": {"filled": false,
      "fill": "white", "size":50
    }},
    "encoding": {
      "x": {"title": "Lines of Code", "field": "x", "type": "quantitative", "scale": {"domain": [1, 1000]}
      },
      "y": {"title": "Time (minutes)", "field": "y", "type": "quantitative", "scale": {"domain": [1, 500]}}
    }
  }
const embed_opt = {"mode": "vega-lite"};
const el = document.getElementById('vis');
const view = vegaEmbed("#vis", spec, embed_opt);
</script>

When considering multiple parts of code in many files, this maintenance can become untenable, leading to the gradual decay of your code quality or functionality. For example, let's assume one line of code costs 30 seconds to maintain (feel free to substitute time with monetary or personnel aspects as an example measure here too). 1000 lines of code would cost 500 minutes (or about 8 hours) to maintain. This becomes more complex when considering multiple files, collaborators, or languages.

<i class="fas fa-hiking" style="font-size:4em;"></i>
{:.center}

Think about your project as if it were on a hiking trail: __"Carry as little as possible, but choose that little with care."__ (Earl Shaffer). Be careful what code you choose to carry; it may impact your ability to address needs over time and lead to otherwise unintended software decay.

## Detecting Unused Code with Vulture

Understanding the cost of added content, it's important to routinely examine which parts of your code are still necessary. You can prepare your code for a long journey by detecting (and removing) unused code with various automated tools. These tools are generally designed for static analysis and linting, meaning they may also be incorporated into automated and routine testing.

```shell
$ vulture unused_code_example.py
unused_code_example.py:3: unused import 'os' (90% confidence)
unused_code_example.py:4: unused import 'pd' (90% confidence)
unused_code_example.py:7: unused function 'unused_function' (60% confidence)
unused_code_example.py:14: unused variable 'unused_var' (60% confidence)
```

_Example of Vulture command line usage to discover unused code._

[Vulture](https://github.com/jendrikseipp/vulture) is one tool dedicated to finding unused python code. Vulture provides both a command line interface and Python API for discovering unused code. It also provide a rough confidence to show how certain it was about whether the block of code was unused. See the following interactive example for a demonstration of using Vulture.

[Interactive Example on Unused Code Detection](https://cu-dbmi.github.io/notebooks/lab?path=unused_code_detection.ipynb)

## Further Code Usefulness Detection with Pylint and Coverage.py

In addition to Vulture, [Pylint](https://pylint.pycqa.org/en/latest/index.html) and [Coverage.py](https://coverage.readthedocs.io/) can be used in a similar way to help show where code may not have been used within your project.

[Pylint](https://pylint.pycqa.org/en/latest/index.html) focuses on code style and other static analysis in addition to unused variables. See [Pylint's Checkers](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html) page for more details here, using "unused-*" as a reference to checks it performs which focus on unused code.

[Coverage.py](https://coverage.readthedocs.io/) helps show you which parts of your code have been executed or not. A common usecase for Coverage involves measuring "test coverage", or which parts of your code are executed in relationship to tests written for that code. This provides another perspective on code utility: if there's not a test for the code, is it worth keeping?

## Additional Resources

- [Software Rot](https://en.wikipedia.org/wiki/Software_rot)
- [Vulture](https://github.com/jendrikseipp/vulture)
- [Pylint](https://pylint.pycqa.org/en/latest/index.html)
- [Coverage](https://coverage.readthedocs.io/)
