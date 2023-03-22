---
title: "Tip of the Week: Software Linting with R"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - r
  - static-analysis
  - linting
  - continuous-testing
---

# Tip of the Week: Software Linting with R

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. Views expressed in the content belong to the content creators and not the organization, its affiliates, or employees. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

<!-- excerpt start -->

This article covers using the software technique of linting on R code in order to improve code quality, development velocity, and collaboration.

<!-- excerpt end -->

__TLDR (too long, didn't read);__
Use software linting ([static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)) practices on your R code with existing packages [`lintr`](https://github.com/r-lib/lintr) and [`styler`](https://github.com/r-lib/styler) (among others). These linters may be applied using [pre-commit](https://pre-commit.com) in your local development environment or as [continuous tests](https://en.wikipedia.org/wiki/Continuous_testing) using for example [Github Actions](https://docs.github.com/en/actions).

## Treating R as Software

> "Many users think of R as a statistics system. We prefer to think of it as an environment within which statistical techniques are implemented."

_([R-Project: What is R?](https://www.r-project.org/about.html))_

The [R programming language](https://en.wikipedia.org/wiki/R_(programming_language)) is sometimes treated as _only_ a statistics system instead of software. This treatment can sometimes lead to common issues in development which are experienced in other languages. Addressing R as software enables developers to enhance their work by taking benefit from existing concepts applied to many other languages.

## Linting with R

<pre class="mermaid">
flowchart LR
  write[Write R code] --> |check| check[Check code with linters]
  check --> |revise| write
</pre>
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

_Workflow loop depicting writing R code and revising with linters._
{:.center}

Software linting, or [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis), is one way to ensure a minimum level of code quality without writing new tests. Linting checks how your code is structured without running it to make sure it abides by common language paradigms and logical structures. Using linting tools allows a developer to gain quick insights about their code before it is viewed or used by others.

One way to lint your R code is by using the [`lintr`](https://github.com/r-lib/lintr) package. The `lintr` package is also complementary of the [`styler`](https://github.com/r-lib/styler) pacakge, which formats the syntax of R code in a consistent way. Both of these can be used independently or as part of continuous quality checks for R code repositories.

## Automated Linting Checks with R

<pre class="mermaid">
flowchart LR
  subgraph development
    write
    check
  end
  subgraph linters
    direction LR
    lintr
    styler
  end
  check <-.- linters
  write[Write R code] --> |check| check[Check code with pre-commit]
  check --> |revise| write
</pre>

_Workflow showing development with pre-commit using multiple linters._
{:.center}

`lintr` and `styler` can be incorporated into automated checks to help make sure linting (or other steps) are always used with new code. One tool which can help with this is [pre-commit](https://pre-commit.com/), which acts as both a local development tool in addition to providing observability within source control (more on this later).

Using pre-commit locally enables quick feedback loops using one or many checkers (such as `lintr`, `styler`, or others). Pre-commit may be used through the use of [git hooks](https://pre-commit.com/#usage) or manually using [`pre-commit run ...`](https://pre-commit.com/#pre-commit-run) from a command-line. See [this example of pre-commit checks with R](https://github.com/lorenzwalthert/precommit) for an example of multiple pre-commit checks for R code.

## Continuous and Observable Testing for R

<pre class="mermaid">
flowchart LR
  subgraph development [local development]
    direction LR
    write
    check
    commit
  end
  subgraph remote[Github repository]
    direction LR
    action["Check code (remotely)"]
  end
  write[Write R code] --> |check| check[Check code with pre-commit]
  check --> |revise| write
  check --> commit[commit + push]
  commit --> |optional trigger| action
  check -.-> |perform same checks| action
</pre>

_Workflow showing pre-commit used as continuous testing tool with Github._
{:.center}

Pre-commit linting checks can also be incorporated into [continuous testing](https://en.wikipedia.org/wiki/Continuous_testing) performed on your repository. One way to do this is using [Github Actions](https://docs.github.com/en/actions). Github Actions provides a programmatic way to specify automatic steps taken as changes occur to a repository.

Pre-commit provides [an example Github Action](https://github.com/pre-commit/action) which will automatically check and alert repository maintainers when code challenges are detected. Using pre-commit in this way allows R developers to ensure `lintr` checks are performed on any new work checked into a repository. This can have benefits towards decreasing pull request (PR) review time and standardize how code collaboration takes place for R developers.

## Resources

Please see the following the resources on this topic.

- [R programming language](https://en.wikipedia.org/wiki/R_(programming_language))
- [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)
- [R package: lintr](https://github.com/r-lib/lintr)
- [R package: styler](https://github.com/r-lib/styler)
- [pre-commit](https://pre-commit.com/)
- [Example of pre-commit checks with R](https://github.com/lorenzwalthert/precommit)
- [continuous testing](https://en.wikipedia.org/wiki/Continuous_testing)
- [Github Actions](https://docs.github.com/en/actions)
- [an example Github Action](https://github.com/pre-commit/action)
