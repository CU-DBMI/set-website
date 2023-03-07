---
title: "Tip of the Week: Repository Workflows with Github Actions"
author: Dave Bunten
member: dave-bunten
tags:
  - tip-of-the-week
  - software
  - git
  - branching
  - pull-requests
  - merging
---

# Tip of the Week: Repository Workflows with Github Actions

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. Views expressed in the content belong to the content creators and not the organization, its affiliates, or employees. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

There are many routine tasks which can be automated to help save time and increase reproducibility in software development. Github Actions provides one way to accomplish these tasks using code-based workflows and related workflow implementations. This type of automation is commonly used to perform checks or tests, builds (preparing for the delivery of the code), or delivery itself (sending the code or related artifacts where they will be used).

__TLDR (too long, didn't read);__
Use [Github Actions](https://docs.github.com/en/actions) to perform [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) work automatically by leveraging [Github's workflow specification](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions). You can test these workflows with [Act](https://github.com/nektos/act), which can enhance development with this feature of Github. Consider making use of ["write once, run anywhere" (WORA)](https://en.wikipedia.org/wiki/Write_once,_run_anywhere) and [Dagger](https://docs.dagger.io/) in conjunction with Github Actions to enable reproducible workflows for your software projects.

## Workflows

<pre class="mermaid">
flowchart LR
  start((start)) --> action
  action["action(s)"] --> en((end))
  style start fill:#6EE7B7
  style en fill:#FCA5A5
</pre>
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

{:.center}

[Workflows](https://en.wikipedia.org/wiki/Workflow) consist of sequenced activities used by various systems. Software development uses workflows to help accomplish work the same way each time. Generally, workflow engines consist of start (what triggers a workflow to begin), actions (work being performed in sequence), and an ending (where the work stops). There are [many workflow engines](https://s.apache.org/existing-workflow-systems), including some which help accomplish work alongside version control.

## Github Actions

<pre class="mermaid">
flowchart LR
  subgraph workflow [Github Actions Workflow Run]
    direction LR
    action["action(s)"] --> en((end))
    start((event\ntrigger))
  end
  start --> action
  style start fill:#6EE7B7
  style en fill:#FCA5A5
</pre>

{:.center}

[Github Actions](https://docs.github.com/en/actions) is a feature of Github which allows you to run workflows in relation to your code as a [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) tool (including automated testing, builds, and deployments). For example, one can use Github actions to make sure code related to a [Github Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) passes all tests for the repository. Github Actions may be specified using [YAML files](https://en.wikipedia.org/wiki/YAML) within your repository's `.github/workflows` directory by using syntax specific to [Github's workflow specification](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions).

## Testing with Act

<pre class="mermaid">
flowchart LR
  subgraph container ["local simulation container(s)"]
    direction LR
    subgraph workflow [Github Actions Workflow Run]
      direction LR
      start((event\ntrigger))
      action --> en((end))
    end
  end
  start --> action
  act[Run Act] -.-> |Simulate\ntrigger| start
  style start fill:#6EE7B7
  style en fill:#FCA5A5
</pre>

{:.center}

One challenge with Github Actions is a lack of standardized local testing tools. For example, how will you know that a new Github Actions workflow will function as expected (or at all) without pushing to the Github repository? One third-party tool which can help with this is [Act](https://github.com/nektos/act). Act uses [Docker images](https://github.com/nektos/act#runners) which require [Docker Desktop](https://docs.docker.com/desktop/) to simulate what running a Github Action workflow within your local environment.

## Nested Workflows with Github Actions

<pre class="mermaid">
flowchart LR

  subgraph action ["Nested Workflow (Dagger, etc)"]
    direction LR
    actions
    start2((start)) --> actions
    actions --> en2((end))
    en2((end))
  end
  subgraph workflow2 [Local Environment Run]
    direction LR
    run2[run workflow]
    en3((end))
    start3((event\ntrigger))
  end
  subgraph workflow [Github Actions Workflow Run]
    direction LR
    start((event\ntrigger))
    run[run workflow]
    en((end))
  end
  
  start --> run
  start3 --> run2
  action -.-> run
  run --> en
  run2 --> en3
  action -.-> run2
  style start fill:#6EE7B7
  style start2 fill:#D1FAE5
  style start3 fill:#6EE7B7
  style en fill:#FCA5A5
  style en2 fill:#FFE4E6
  style en3 fill:#FCA5A5
</pre>

{:.center}

There are times when Github Actions may be too constricting or Act may not accurately simulate workflows. We also might seek to ["write once, run anywhere" (WORA)](https://en.wikipedia.org/wiki/Write_once,_run_anywhere) to enable flexible development on many environments. One workaround to this challenge is to use nested workflows which are compatible with local environments and Github Actions environments. [Dagger](https://docs.dagger.io/) is one tool which enables programmatically specifying and using workflows this way. Using Dagger allows you to trigger workflows on your local machine or Github Actions with the same underlying engine, meaning there are fewer inconsistencies or guesswork for developers (see here for [an explanation of how Dagger works](https://docs.dagger.io/cli#how-does-it-work)).

## Additional Resources
