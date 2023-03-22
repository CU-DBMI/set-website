---
title: "Tip of the Week: Timebox Your Software Work"
author: dave-bunten
tags:
  - tip-of-the-week
  - software
  - timeboxing
  - timeblocking
  - productivity
  - modularization
  - projectmanagement
---

# Tip of the Week: Timebox Your Software Work

> Each week we seek to provide a software tip of the week geared towards helping you achieve your software goals. Views expressed in the content belong to the content creators and not the organization, its affiliates, or employees. If you have any software questions or suggestions for an upcoming tip of the week, please don’t hesitate to reach out to #software-engineering on Slack or email DBMISoftwareEngineering at olucdenver.onmicrosoft.com

<!-- excerpt start -->

Programming often involves long periods of problem solving which can sometimes lead to unproductive or exhausting outcomes. This article covers one way to avoid less productive time expense or protect yourself from overexhaustion through a technique called "timeboxing" (also sometimes referenced as "timeblocking").

<!-- excerpt end -->

__TLDR (too long, didn't read);__
Use timeboxing techniques such as [Pomodoro®](https://en.wikipedia.org/wiki/Pomodoro_Technique) or [52/17](https://en.wikipedia.org/wiki/52/17_rule) to help [modularize](https://en.wikipedia.org/wiki/Modularity) your software work to ensure you don't fall victim to [Parkinson's Law](https://en.wikipedia.org/wiki/Parkinson%27s_law). Timeboxing may also map well to [Github Issues](https://github.com/features/issues), which allows your software tasks to be further aligned, documented, and chunked in collaboration with others.

## Controlling Work Time Expansion

{% include figure.html image="images/work_timebox.png" caption="Image depicting work as a creature with a timebox around it."  %}
{:.center}

Have you ever spent more time than you thought you would on a task? An adage which helps explain this phenomenon is [Parkinson's Law](https://www.economist.com/news/1955/11/19/parkinsons-law):

>"... work expands so as to fill the time available for its completion."

The practice of writing software is not protected from this "law". It may be affected by it in sometimes worse ways during long periods of uninterrupted programming where we may have an inclination to forget productive goals.

One way to address this is through the use of [timeboxing](https://en.wikipedia.org/wiki/Timeboxing) techiques. Timeboxing sets a fixed limit to the amount of time one may spend on a specific activity. One can use timeboxing to systematically address many tasks, for example, as with the [Pomodoro® Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) (developed by Francesco Cirillo) or [52/17 rule](https://en.wikipedia.org/wiki/52/17_rule). While there are many ways to apply timeboxing, make sure to balance activity with short breaks and focus switches to help ensure we don't become overwhelmed.

## Timeboxing Means Modularization

Timeboxing has an auxiliary benefit of framing your work as objective and oftentimes smaller chunks (we have to know what we're timeboxing in order to use this technique). Creating distinct chunks of work applies for both our daily time schedule as well as code itself. This concept is more broadly called "[modularization](https://en.wikipedia.org/wiki/Modularity)" and helps to distinguish large portions of work (whether in real life or in code) as smaller and more maintainable chunks.

{% capture col1content %}

```markdown
# Goals
- Finish writing paper




```

_Vague and possibly large task_

{% endcapture %}
{% capture col2content %}

```markdown
# Goals
- Finish writing paper
  - Create paper outline
  - Finish writing introduction
  - Check for dead hyperlinks
  - Request internal review
```

_Modular and more understandable tasks_
{% endcapture %}

{% include cols.html col1=col1content col2=col2content %}

Breaking down large amounts of work as smaller chunks within our code helps to ensure long-term maintainability and understandability. Similarly, keeping our tasks small can help ensure our goals are achievable and understandable (to ourselves or others). Without this modularity, tasks can be impossible to achieve (subjective in nature) or very difficult to understand. Stated differently, taking many small steps can lead to a big change in an organized, oftentimes less exhausting way ([related graphic](https://www.fosslien.com/liz-fosslien-the-power-of-small-steps)).

## Version Control and Timeboxing

```markdown
# Repo Issues
- "Prevent foo warning" - 20 minutes
- "Remove bar feature" - 20 minutes
- "Address baz error" - 20 minutes

```

_List of example version control repository issues with associated time duration._
{:.center}

The parallels between the time we give a task and related code can work towards your benefit. For example, [Github Issues](https://github.com/features/issues) can be created to outline a timeboxed task which relates to a distinct chunk of code to be created, updated, or fixed. Once development tasks have been outlined as issues, a developer can use timeboxing to help organize how much time to allocate on each issue.

Using Github Issues in this way provides a way to observe task progress associated with one or many repositories. It also increases collaborative opportunities for task sizing and description. For example, if a task looks too large to complete in a reasonable amount of time, developers may work together to break the task down into smaller modules of work.

## Be Kind to Yourself: Take Breaks

While timeboxing is often a conversation about how to be more productive, it's also worth remembering: __take breaks to be kind to yourself and more effective__. Some studies and thought leadership have shown that taking breaks may be necessary to avoid performance decreases and impacts to your health. There's also some indication that taking breaks may lead to better work. See below for just a few examples:

- [The Importance of Taking Breaks](https://thewellbeingthesis.org.uk/foundations-for-success/importance-of-taking-breaks-and-having-other-interests/)
- [Brief and rare mental “breaks” keep you focused: Deactivation and reactivation of task goals preempt vigilance decrements](https://www.sciencedirect.com/science/article/pii/S0010027710002994?via%3Dihub)
- [Give your ideas some legs: the positive effect of walking on creative thinking](https://pubmed.ncbi.nlm.nih.gov/24749966/)

## Additional Resources

- [Parkinson's Law](https://en.wikipedia.org/wiki/Parkinson%27s_law)
- [Timeboxing](https://en.wikipedia.org/wiki/Timeboxing)
- [Timeblocking](https://en.wikipedia.org/wiki/Timeblocking) Additional similar notes on time management.
- [Pomodoro® Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
- [52/17 Rule](https://en.wikipedia.org/wiki/52/17_rule)
- [Modularity](https://en.wikipedia.org/wiki/Modularity)
- [Github Issues](https://github.com/features/issues)
