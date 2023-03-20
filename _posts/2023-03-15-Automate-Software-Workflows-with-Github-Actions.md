---
title: "Tip of the Week: Automate Software Workflows with GitHub Actions"
author: Dave Bunten
member: dave-bunten
tags:
  - tip-of-the-week
  - software
  - github
  - workflow
  - github-actions
  - continuous-integration
---

# Tip of the Week: Automate Software Workflows with GitHub Actions

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. Views expressed in the content belong to the content creators and not the organization, its affiliates, or employees. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

There are many routine tasks which can be automated to help save time and increase reproducibility in software development. GitHub Actions provides one way to accomplish these tasks using code-based workflows and related workflow implementations. This type of automation is commonly used to perform tests, builds (preparing for the delivery of the code), or delivery itself (sending the code or related artifacts where they will be used).

__TLDR (too long, didn't read);__
Use [GitHub Actions](https://docs.github.com/en/actions) to perform [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) work automatically by leveraging [Github's workflow specification](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) and the [existing marketplace of already-created Actions](https://github.com/marketplace?type=actions). You can test these workflows with [Act](https://github.com/nektos/act), which can enhance development with this feature of Github. Consider making use of ["write once, run anywhere" (WORA)](https://en.wikipedia.org/wiki/Write_once,_run_anywhere) and [Dagger](https://docs.dagger.io/) in conjunction with GitHub Actions to enable reproducible workflows for your software projects.

## Workflows in Software

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

_An example workflow._
{:.center}

[Workflows](https://en.wikipedia.org/wiki/Workflow) consist of sequenced activities used by various systems. Software development  workflows help accomplish work the same way each time by using what are commonly called "workflow engines". Generally, workflow engines are provided code which indicate beginnings (what triggers a workflow to begin), actions (work being performed in sequence), and an ending (where the workflow stops). There are [many workflow engines](https://s.apache.org/existing-workflow-systems), including some which help accomplish work alongside version control.

## GitHub Actions

<pre class="mermaid">
flowchart LR
  subgraph workflow [GitHub Actions Workflow Run]
    direction LR
    action["action(s)"] --> en((end))
    start((event\ntrigger))
  end
  start --> action
  style start fill:#6EE7B7
  style en fill:#FCA5A5
</pre>

_A diagram showing GitHub Actions as a workflow._
{:.center}

[GitHub Actions](https://docs.github.com/en/actions) is a feature of GitHub which allows you to run workflows in relation to your code as a [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (including automated testing, builds, and deployments) and general automation tool. For example, one can use GitHub Actions to make sure code related to a [GitHub Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) passes certain tests before it is allowed to be merged. GitHub Actions may be specified using [YAML files](https://en.wikipedia.org/wiki/YAML) within your repository's `.github/workflows` directory by using syntax specific to [Github's workflow specification](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions). Each YAML file under the `.github/workflows` directory can specify workflows to accomplish tasks related to your software work. GitHub Actions workflows may be customized to your own needs, or use an [existing marketplace of already-created Actions](https://github.com/marketplace?type=actions).

{% include figure.html image="images/github_actions_tab.png" caption="Image showing GitHub Actions tab on GitHub website." %}

GitHub provides an ["Actions" tab](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#viewing-the-activity-for-a-workflow-run) for each repository which helps visualize and control Github Actions workflow runs. This tab shows a history of all workflow runs in the repository. For each run, it shows whether it was run successful or not, the associated logs, and controls to cancel or re-run it.

> __GitHub Actions Examples__
> GitHub Actions is sometimes better understood with examples. See the following references for a few basic examples of using GitHub Actions in a simulated project repository.
>
> - [1.example-action.yml](https://github.com/CU-DBMI/demo-github-actions/blob/main/.github/workflows/1.example-action.yml): demonstrates how to run a snippet of Python code in a basic GitHub Actions workflow.
> - [2.run-python-file.yml](https://github.com/CU-DBMI/demo-github-actions/blob/main/.github/workflows/2.run-python-file.yml): demonstrates how to reliably reproduce the environment by installing dependencies using [Poetry](https://python-poetry.org/docs/), and then run a Python file in that environment.
> - [3.run-matrixed-pytest-ghactions.yml](https://github.com/CU-DBMI/demo-github-actions/blob/main/.github/workflows/3.run-matrixed-pytest-ghactions.yml): demonstrates how to run pytest tests against multiple versions of Python (i.e., "matrixed" Python versions) using GitHub Actions with a [matrix strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).

## Testing with Act

<pre class="mermaid">
flowchart LR
  subgraph container ["local simulation container(s)"]
    direction LR
    subgraph workflow [GitHub Actions Workflow Run]
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

_A diagram showing how GitHub Actions workflows may be triggered from Act_
{:.center}

One challenge with GitHub Actions is a lack of standardized local testing tools. For example, how will you know that a new GitHub Actions workflow will function as expected (or at all) without pushing to the GitHub repository? One third-party tool which can help with this is [Act](https://github.com/nektos/act). Act uses [Docker images](https://github.com/nektos/act#runners) which require [Docker Desktop](https://docs.docker.com/desktop/) to simulate what running a GitHub Action workflow within your local environment. Using Act can sometimes avoid guessing what will occur when a GitHub Action worklow is added to your repository. See [Act's installation documentation](https://github.com/nektos/act#installation) for more information on getting started with this tool.

## Nested Workflows with GitHub Actions

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
  subgraph workflow [GitHub Actions Workflow Run]
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

_A diagram showing how GitHub Actions may leverage nested workflows with tools like Dagger._
{:.center}

There are times when GitHub Actions may be too constricting or Act may not accurately simulate workflows. We also might seek to ["write once, run anywhere" (WORA)](https://en.wikipedia.org/wiki/Write_once,_run_anywhere) to enable flexible development on many environments. One workaround to this challenge is to use nested workflows which are compatible with local environments and GitHub Actions environments. [Dagger](https://docs.dagger.io/) is one tool which enables programmatically specifying and using workflows this way. Using Dagger allows you to trigger workflows on your local machine or GitHub Actions with the same underlying engine, meaning there are fewer inconsistencies or guesswork for developers (see here for [an explanation of how Dagger works](https://docs.dagger.io/cli#how-does-it-work)).

There are also other alternatives to Dagger you may want to consider based on your usecase, preference, or interest. [Earthly](https://github.com/earthly/earthly) is similar to Dagger and uses "earthfiles" as a specification. Both Dagger and Earthly (in addition to GitHub Actions) use container-based approaches, which in-and-of themselves present additional alternatives outside the scope of this article.

> __GitHub Actions with Nested Workflow Example__
> Reference this example for a brief demonstration of how GitHub Actions and Dagger may be used together.
>
> - [4.run-matrixed-pytest-dagger.yml](https://github.com/CU-DBMI/demo-github-actions/blob/main/.github/workflows/4.run-matrixed-pytest-dagger.yml): demonstrates how to run matrixed Python versions for confirming passing pytest tests using GitHub Actions and Dagger together. A [GitHub Actions matrix strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs) is used to span concurrent work while retaining the reproducibility from Dagger task specification.

## Closing Remarks

Using GitHub Actions through the above methods can help automate your technical work and increase the quality of your code with sometimes very little additional effort. Saving time through this form of automation can provide additional flexibility accomplish more complex work which requires your attention (perhaps [using timeboxing techniques](https://cu-dbmi.github.io/set-website/2023/01/17/Timebox-Your-Software-Work.html)). Even small amounts of time saved can turn into large opportunities for other work. On this note, be sure to explore how GitHub Actions can improve things for your software endeavors.
