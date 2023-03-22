---
title: "Tip of the Week: Branch, Review, and Learn"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - git
  - branching
  - pull-requests
  - merging
---

# Tip of the Week: Branch, Review, and Learn

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. Views expressed in the content belong to the content creators and not the organization, its affiliates, or employees. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

<!-- excerpt start -->

Git provides a feature called [branching](https://git-scm.com/docs/git-branch) which facilitates parallel and segmented programming work through [commits](https://git-scm.com/docs/git-commit) with version control. Using branching enables both work concurrency (multiple people working on the same repository at the same time) as well as a chance to isolate and review specific programming tasks. This article covers some conceptual best practices with branching, reviewing, and merging code using Github.

<!-- excerpt end -->

__Please note:__ the content below represents one opinion in a larger space of Git workflow concepts (it's not perfect!). Developer cultures may vary on these topics; be sure to acknowledge people and culture over exclusive or absolute dedication to what is found below.

__TLDR (too long, didn't read);__
Use [git branching techniques](https://www.atlassian.com/git/tutorials/using-branches) to segment the completion of programming tasks, gradually and consistently committing small changes (practicing [_festina lente_ or "make haste, slowly"](https://en.wikipedia.org/wiki/Festina_lente)). When a group of small changes are ready from branches, request [pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) and take advantage of [comments](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request) to [continuously improve](https://en.wikipedia.org/wiki/Continual_improvement_process) the work. Prepare for a branch [merge](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) after review by deciding [which merge strategy](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github) is appropriate and automating merge requirements with [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches).

## Concept: Coursework Branching

<pre class="mermaid">
flowchart LR
 subgraph Course
    direction LR
    open["open\nassignment"]
    turn_in["review\nassignment"]
  end
  subgraph Student ["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Student"]
    direction LR
    work["completed\nassignment"]
  end
  open -.-> turn_in
  open --> |works towards| work
  work --> |seeks review| turn_in
</pre>
<script type="module">
  import mermaid from 'https://unpkg.com/mermaid@9/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

_An example course and student assignment workflow._
{:.center}

[Git branching](https://www.atlassian.com/git/tutorials/using-branches) practices may be understood in context with similar workflows from real life. Consider a student taking a course, where an assignment is given to them to complete. In addition to the steps shown in the diagram above, it's important to think about _why_ this pattern is beneficial:

- Completing an assignment allows us as social, inter-dependent beings to present new findings which enable learning and amalgamation of additional ideas from others.
- The timebound nature of assignments enables us to practice some form of [timeboxing](https://cu-dbmi.github.io/set-website/2023/01/17/Timebox-Your-Software-Work.html) so as to minimize tasks which may take too much time.
- Segmenting applied learning in distinct, goal-orientated chunks helps make larger topics easier to understand.

## Branching to Complete an "Assignment"

<pre class="mermaid">
%%{init: { 'logLevel': 'debug', 'theme': 'default' , 'themeVariables': {
      'git0': '#4F46E5',
      'git1': '#10B981',
      'gitBranchLabel1': '#ffffff'
} } }%%
    gitGraph
       commit id: "..."
       commit id: "opened"
       branch assignment
       checkout assignment
       commit id: "completed"
       checkout main
</pre>

_An example git diagram showing assignment branch based off main._
{:.center}

Following the course assignment workflow, the diagram above shows an in-progress `assignment` branch based off of the `main` branch. When the `assignment` branch is created, we bring into it everything we know from `main` (the course) so far in the form of [commits](https://github.com/git-guides/git-commit), or groups of changes to various files. [Branching](https://github.com/git-guides#create-a-branch) allows us to make consistent and well described changes based on what's already happened without impacting others work in the meantime.

> Branching best practices:
>
> - __Keep the name and work with branches dedicated to a specific and focused purpose.__ For example: a branch named `fix-links-in-docs` might entail work related to fixing HTTP links within documentation.
> - __Consider the use of [Github Forks](https://docs.github.com/en/get-started/quickstart/fork-a-repo)__ (along with branches within the fork) to help further isolate and enrich work potential. Forks also allow remixing existing work into new possibilities.
> - __[_festina lente_](https://en.wikipedia.org/wiki/Festina_lente) or "make haste, slowly":__ Commits on any branch represent small chunks of a cohesive idea which will eventually be brought to `main`. It is often beneficial to be consistent with small, gradual commits to avoid a rushed or incomplete submission. The same applies more generally for software; taking time upfront to do things well can mean time saved later.

## Reviewing the Branched Work

<pre class="mermaid">
%%{init: { 'logLevel': 'debug', 'theme': 'default' , 'themeVariables': {
      'git0': '#6366F1',
      'git1': '#10B981',
      'gitBranchLabel1': '#ffffff'
} } }%%
    gitGraph
       commit id: "..."
       commit id: "opened"
       branch assignment
       checkout assignment
       commit id: "completed"
       checkout main
       merge assignment id: "reviewed"
</pre>

_An example git diagram showing assignment branch being merged with main after a review._
{:.center}

The diagram above depicts a merge from the `assignment` branch to pull the changes into the `main` branch, simulating an assignment being returned for review within a course. While merges may be forced without review, it's a best practice create a [Pull Request (PR) Review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) (also known as a [Merge Request (MR)](https://docs.gitlab.com/ee/user/project/merge_requests/) on some systems) and then ask other members of your team to review it. Doing this provides a chance to make revisions before code changes are "finalized" within the `main` branch.

> Github provides special tools for reviews which can assist both the author and reviewer:
>
> - __Keep code changes intended for review small__, enabling reviewers to reason through the work to more quickly provide feedback and practicing [incremental continuous improvement](https://en.wikipedia.org/wiki/Continual_improvement_process) (it may be difficult to address everything at once!). This also may denote the git history for a repository in a clearer way.
> - __Github comments:__ [Overall review comments](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#about-pull-request-comments) (encompassing all work from the branch) and [Inline comments](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request) (inquiring about individual lines of code) may be provided. Inline comments may also include code suggestions, which allows for code-based revision suggestions that may be committed directly to the branch using markdown codeblocks (` ```suggestion `).
> - __Github issues:__ [Creating issues from comments](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-comment) allows the creation of new repository issues to address topics outside of the current PR.

## Merging the Branch after Review

<pre class="mermaid">
%%{init: { 'logLevel': 'debug', 'theme': 'default' , 'themeVariables': {
      'git0': '#6366F1'
} } }%%
    gitGraph
       commit id: "..."
       commit id: "opened"
       commit type: HIGHLIGHT id: "reviewed"
       commit id: "...."
</pre>

_An example git diagram showing the main branch after the assignment branch has been merged (and removed)._
{:.center}

Changes may be made within the `assignment` branch until the work is in a state where the authors and reviewers are satisfied. At this point, the branch changes may be [merged](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) into `main`. Approvals are sometimes provided informally (for ex., with a comment: "LGTM (looks good to me)!") or explicitly (for ex., [approvals within Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)) to indicate or enable branch merge readiness . After the merge, changes may continue to be made in a similar way (perhaps accounting for concurrently branched work elsewhere). Generally, a merged branch may be removed afterwards to help maintain an organized working environment (see [Github PR branch removal](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request)).

> Github provides special tools for merging:
>
> - __Decide which merge strategy is appropriate (there are many!):__ There are many [merge strategies within Github](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github) (merge commits, squash merges, and rebase merging). Take time to understand them and choose which one works best.
> - __Consider using branch protection to automate merge requirements:__ The `main` or other branches may be "protected" against merges using [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches). These rules can require reviewer approvals or automatic status checks to pass before changes may be merged.
> - __Use merge queuing to manage multiple PR's:__ When there are many unmerged PR's, it can sometimes be difficult to document and ensure each are merged in a desired sequence. Consider using [merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) to help with this process.

## Additional Resources

The links below may provide additional guidance on using these git features, including in-depth coverage of various features and related configuration.

- [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/)
- [Github: Git Guide](https://github.com/git-guides)
- [Atlassian: What is version control?](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [Git Lab: Git](https://docs.gitlab.com/ee/topics/git/)
