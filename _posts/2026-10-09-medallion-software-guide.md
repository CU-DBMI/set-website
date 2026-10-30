---
title: "From Bronze to Gold: A Medallion Guide to Software in the Generative Era"
author: dave-bunten
tags:
  - scientific-software
  - software-quality
  - testing
  - data-engineering
  - ai
  - software-design
---

# From Bronze to Gold: A Medallion Guide to Software in the Generative Era

{% include blog-post-intro.html %}

<style>
img.mermaid {
  display: block;
  width: 100%;
  max-width: 420px;
  height: auto;
  margin: 1.5rem auto;
}
</style>

## Introduction

<img class="mermaid" src="{{ '/images/medallion-guide/overview.svg' | relative_url }}" alt="Overview of bronze, silver, and gold quality levels.">

_Code moves forward as we find evidence that it works for the task. A problem can send us back._

<!-- excerpt start -->
**Bronze is a first attempt. Silver has evidence behind it. Gold is ready for a clear use.**
These levels give us a way to discuss research software without treating every piece of code as finished work.
We borrow them from [medallion architecture](https://dataengineering.wiki/Concepts/Medallion+Architecture), which organizes data through stages of refinement.
Here, ten questions help us apply the same idea to software.
<!-- excerpt end -->

The move from small data to big data offers a useful parallel.
A table you can inspect row by row calls for different checks than a collection too large to review by hand.
We can think of AI-assisted work as a move from small code to big code.
We may have more code and more possible versions than we can inspect at once.
That makes selection, testing, and removal part of the task, not work to leave until later.
More code is not the goal. A result we can trust is.

In data work, the medallion architecture helps us move from raw records to tested data and then to data prepared for use.
Here, we adapt that pattern to software: try an idea, test its results, and prepare it for others.
These ten questions are our proposed guide, not a validated standard for software quality.
The medals describe the evolution of the code as it is clarified to realized value.

Imagine a ceramics class that makes one sculpture together.
The teacher explains the goal, and the students shape different parts.
The teacher helps them judge whether those parts fit and guides the next round of changes.
A smooth surface cannot hide a weak joint. The shared piece needs attention as a whole.

Alberto Denia's [Code is clay now](https://www.albertodenia.com/writing/code-is-clay-now) offers a related image for code that AI tools help us reshape.
The class extends that image to shared work.
A research team guides the task, while people and AI tools contribute parts of the code.
AI tools are not students, but the teaching role gives us a useful question: what guidance does the next revision need?
The team remains responsible for the scientific choices and the evidence behind them.

Here is the guide at a glance:

| Level | Question | What you need |
|---|---|---|
| 🪵 Wooden | Is there an idea worth a first try? | A rough sketch or code fragment. Expect gaps and errors. Do not rely on its results. |
| 🥉 Bronze | 1. What is the job? | A clear task and its limits. |
| 🥉 Bronze | 2. What goes in and comes out? | A description of the data the code takes and returns. |
| 🥉 Bronze | 3. Can a small example run safely? | A first attempt that leaves the original data untouched. |
| 🥈 Silver | 4. Does it give a known answer? | An expected result worked out separately from the code. |
| 🥈 Silver | 5. What happens with difficult data? | Tests for missing values, unusual inputs, and rules that must hold. |
| 🥈 Silver | 6. Does the code follow the plan? | A review of the code against the intended method. |
| 🥈 Silver | 7. Does it work on real examples? | A small trial with realistic data and clear limits. |
| 🥇 Gold | 8. Can someone run it again? | Saved data references, software versions, and instructions. |
| 🥇 Gold | 9. Can someone understand and use it? | A guide that explains the method, its limits, and who to contact. |
| 🥇 Gold | 10. Do we know which version to use? | A named version tied to its test results. |

Wooden is our label for work before the ten questions: a sketch to discuss, not a result to trust.
It is an addition to this guide, not a layer in medallion architecture.

**Judge the shared work, not each individual's output.**
[DORA's team guidance](https://dora.dev/guides/how-to-empower-software-delivery-teams/) states: "Software delivery performance is not an individual measure".
It gives a useful example: slow code reviews can hold back someone's commits, regardless of that person's skill.
DORA recommends looking at the team's working process and tracking the same application over time, rather than ranking people by activity.
The [SPACE framework](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/) also warns against reducing productivity to one measure of activity.

For our levels, ask whether the team can trust the result, change it safely, and help someone else use it.
Commit counts and lines of code cannot answer those questions alone.
If you work solo, consider those who will use or maintain the code after you.
These are not scores to average. Success in one area does not cancel a failure in another.

## Babel: More Code Does Not Mean Better Answers

<img class="mermaid" src="{{ '/images/medallion-guide/babel.svg' | relative_url }}" alt="Choosing and testing a possible version.">

_A clear task helps us choose what to test. Known answers help us judge the result._

Jorge Luis Borges imagines an unusual library in [The Library of Babel](https://en.wikipedia.org/wiki/The_Library_of_Babel).
It contains every possible book within a fixed set of rules.
Most books contain gibberish.
Meaningful books sit among countless false or slightly wrong versions.
Its readers still need a way to recognize the right answers.

This is an analogy, not a description of how AI works. AI tools do not write by choosing every letter at random.
**A believable answer is not always a correct answer.**

Our cell-measurement code can fail in that way.
It can run without errors and produce a tidy table, but use treated cells as their own reference.
The result looks useful while it answers the wrong question.

A clear task and tests with known answers help us find that mistake.
The teacher in our class faces a similar problem: more pieces do not guarantee a better sculpture.
Each contribution needs to serve the shared goal. The medallion levels help us decide what evidence it needs next.

## Bronze: Try an Idea

<img class="mermaid" src="{{ '/images/medallion-guide/bronze.svg' | relative_url }}" alt="Bronze steps for a safe first attempt.">

_Bronze gives us a first attempt and a clear reason to test it._

In medallion architecture, bronze holds raw data before later work improves it.
For our code, bronze means a first attempt whose quality we do not yet know.
A person can write it, an AI tool can draft it, or we can adapt existing code.
**We judge the code by what it does, not where it came from.**
In our class, the teacher guides the first shared attempt.

**1. Describe the job.**
Write down the task before you ask for code.
For our example: "Adjust each cell measurement against control wells from the same plate. Do not use treated wells to set the reference."
This gives us something clearer than "adjust the data."
Code that does a different job is not ready to move forward, even if it runs.

**2. Describe what goes in and comes out.**
List the columns the code needs and what it must return.
Name the columns that identify the cells, plates, and control wells.
Describe what happens to missing values and which labels must stay unchanged.
Keep unresolved questions in the written plan rather than letting the code choose an answer without your knowledge.

**3. Try a small example safely.**
Use a copy of a tiny table.
Make sure that the code accepts it and returns something you can read.
Keep the original data untouched.
Do not give unreviewed code access to passwords or private data.
A successful run means you have something to test. It does not mean the method is correct.

Bronze needs a useful first attempt, not a finished product.

## Silver: Test the Results

<img class="mermaid" src="{{ '/images/medallion-guide/silver.svg' | relative_url }}" alt="Silver steps for checking the results.">

_Silver tests whether the code does the right job, not merely whether it runs._

In medallion architecture, silver holds data after cleaning and testing.
For our code, this level asks whether the results match the method we intended.
Wilson and colleagues' [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745) recommends automated tests and code review for scientific software.
All four questions matter.
In our class, the teacher helps students test whether the pieces fit. For code, tests and review serve that role.

**4. Compare with known answers.**
Choose a few values whose expected results you can work out separately.
Compare the code results with those answers.
For decimal calculations, state how much difference you will allow and why.
An AI tool can help write tests, but tests can repeat the same mistake as the code.
Do not treat the output of the code itself as the expected answer.

**5. Try difficult inputs.**
Try a plate with no control wells, a column of identical values, or missing measurements.
Decide whether each case needs an error, a warning, or a defined result.
Also test rules that must always hold.
For example, a different row order must not change the result for a cell.
Each measurement must stay linked to the correct cell label.

**6. Read the code against the plan.**
Make sure that the code uses only the intended control wells as its reference.
Look at how it separates plates and whether it removes or changes any values.
Remove extra steps that make the method hard to follow.
Another reviewer can help, but agreement alone is not proof.
Several reviewers can share the same wrong assumption.

**7. Run a small trial with real data.**
Choose a small set that includes the differences and problems you expect in practice.
If you have a trusted method, compare the results with it.
Explain any differences.
Make sure that the code fits your time and memory limits.
Save what you tested, what counted as success, and which cases you did not cover.

**A successful trial supports the cases you tested, not every future use.**
If the results reveal a problem, change the code or the plan and test again.

## Gold: Make It Ready to Use

<img class="mermaid" src="{{ '/images/medallion-guide/gold.svg' | relative_url }}" alt="Gold steps for preparing a tested version for use.">

_Gold means ready for a clear use. It does not mean perfect._

In medallion architecture, gold holds data prepared for a particular use.
For our code, this level helps the next person use the tested version responsibly.
A notebook for one study needs less support than a tool that many teams share.
Both need clear instructions and limits.
In our class, this means preparing the shared piece for use and explaining how to care for it.

**8. Save enough to run it again.**
Record the code version, other software it needs, input data, and values that control the run.
Save the test results.
If the method uses randomness, record its starting value, often called a random seed.
Follow the instructions on a fresh setup to make sure that they work.
State any machine or calculation differences that can change the results.
This follows Sandve and colleagues' [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285).
Their guidance includes recording how each result was produced, exact software versions, and random seeds.

**9. Write a guide for the next person.**
Explain the method, the required control wells, and the data the code expects.
Describe warnings and known problems.
Name the person or team responsible for the software.
Provide a way to report errors.
State whether anyone will update the code or whether it stays as a record of a finished analysis.

**10. Name and save the tested version.**
Give the code a version name, such as a release number.
Include a license that states how others can use it.
Keep its test results with that version.
Make sure that the version you share is the one you tested.
For published data, record which code version produced it.
Used this way, code almost acts as metadata: information about the data.
Alongside the saved settings, it describes how the inputs became the outputs.
Peter Naur's essay [Programming as Theory Building](https://doi.org/10.1016/0165-6074%2885%2990032-8) argues that a program is a theory held by the people who build it, and the code text records only part of that theory.
When those builders leave, the text remains, and the theory can fade with them.
The saved plan, tests, and guides cannot hold the whole theory, but they give the next person evidence to rebuild it from.

If the method, required software, or intended data changes, return to the relevant tests.
**A new version does not inherit trust from its name.**
Not every idea needs to reach gold, but research conclusions need more support than an untested first attempt.
For work where errors can cause serious harm, this guide is only a starting point.

## Guide the Work from Bronze to Gold

The medallion levels help us decide what the shared work needs next.
In our ceramics class, the teacher moves between workbenches, looks at each contribution, and helps the students bring the pieces together.

A chat interface can support a similar rhythm.
Spend a little time on each part of the code before you bring the parts together.
Ask what changed, look at the result, and give one clear next step.
An AI tool's explanation gives you something to investigate, not proof that its code works.
The tests and the shared result still need your attention.

Problems give these conversations direction.
A failed test can reveal a missing rule or a mistake that several contributors share.
Treat that discovery as progress toward a better result, rather than pressure to hide the problem.
Accept that mistakes happen, then use the evidence to guide the next revision.
This is part of [research decision engineering](https://bssw.io/items/research-decision-engineering-managing-cognitive-load-in-the-generative-era): deciding where to direct effort and how to judge the result.

As the work improves, the next useful change can be a removal.
An unused feature or a repeated step can make the code harder to understand without helping the task.
Remove that extra weight, but keep the tests, safety measures, and evidence that support trust.
A shorter program is not better if it loses something the work needs.
The focus on removal echoes Saint-Exupéry's [discussion of design in *Terre des hommes*](https://www.lelivrescolaire.fr/page/7089680).

So when do we know we are finished, for now?
When the shared result does the agreed job, the tests support it, and someone else can use it within its stated limits.
**We know the work is done when nothing is left to remove without losing something the task needs.**
That assumes the work passes its checks and has no known problem that defeats its purpose.
New evidence or a changed task can bring us back to the workbench.
Until then, we can save the tested version and let it do its job.
