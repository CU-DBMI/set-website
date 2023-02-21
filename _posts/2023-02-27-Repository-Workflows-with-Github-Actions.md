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

__TLDR (too long, didn't read);__

## Workflows

```mermaid
flowchart LR
  start((start)) --> action
  action --> en((end))
```

[Workflows](https://en.wikipedia.org/wiki/Workflow) consist of sequenced activities used by various systems. Software development uses workflows to help accomplish work the same way each time. Generally, workflow engines consist of triggers (what starts a workflow), actions (work being performed in sequence), and an ending (where the work stops).

## Github Actions

```mermaid
flowchart LR
  subgraph workflow
    direction LR
    start((start)) --> action
    action --> en((end))
  end
  trigger -.-> start
```

## Testing with Act

```mermaid
flowchart LR
  subgraph container [local simulation container]
    direction LR
    subgraph workflow
      direction LR
      start((start)) --> action
      action --> en((end))
    end
    
  end
  trigger -.-> |run act| start
```

## Moving Beyond Act

```mermaid
flowchart LR
  subgraph container [local simulation container]
    direction LR
    subgraph workflow
      direction LR
      subgraph action [nested container]
        actions
      end
      start((start)) --> action
      action --> en((end))
    end
    
  end
  trigger -.-> |run act| start
```

## Additional Resources
