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

## Testing

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

## Additional Resources
