---
title: "LinkML for Scientific Software: One Schema, Many Outputs"
author: dave-bunten
tags:
  - python
  - data-models
  - bioinformatics
  - data-validation
  - scientific-software
  - reproducibility
  - schema-design
---

# LinkML for Scientific Software: One Schema, Many Outputs

{% include blog-post-intro.html %}

## Introduction

<!-- excerpt start -->
**Scientific software pipelines usually break at interfaces, not algorithms.**
[LinkML](https://linkml.io/linkml/) lets you define a single schema once and then generate validators, Python models, and visualizations from that same source.
That gives you a typed contract for domain metadata, sample sheets, and analysis outputs, with less drift across scripts, notebooks, and downstream tools.
<!-- excerpt end -->

## Why Use LinkML Instead of Ad-hoc Dicts?

Without a schema, pipelines often rely on implied conventions:

- IDs are "supposed" to follow some pattern.
- `status` is "supposed" to be one of a few values.
- Numeric fields are "supposed" to have sensible bounds.

Those assumptions are typically encoded in multiple places and diverge over time.
LinkML centralizes those constraints into one model and reuses it across tooling.

## A Minimal (Slightly Comical) Schema

```yaml
id: https://example.org/coffee-queue
name: coffee_queue
prefixes:
  ex: https://example.org/
  linkml: https://w3id.org/linkml/
default_prefix: ex
default_range: string

classes:
  CafeQueue:
    tree_root: true
    attributes:
      queue_id:
        identifier: true
      cafe_name:
        required: true
      barista_on_shift:
        required: true
      orders:
        range: Order
        multivalued: true
        inlined_as_list: true

  Order:
    attributes:
      order_id:
        identifier: true
      customer_name:
        required: true
      drink:
        required: true
      size:
        range: SizeEnum
        required: true
      status:
        range: OrderStatusEnum
        required: true
      shots:
        range: integer
        minimum_value: 1

enums:
  SizeEnum:
    permissible_values:
      small:
      medium:
      large:
  OrderStatusEnum:
    permissible_values:
      queued:
      brewing:
      ready:
```

This still enforces IDs, enums, nested structures, and numeric bounds, just with a model that is easier to remember.

## Pydantic Tie-in

LinkML can generate Pydantic models directly:

```bash
gen-pydantic examples/omics_study_schema.yaml > examples/coffee_queue_pydantic.py
```

Then use generated models in your app:

```python
from coffee_queue_pydantic import CafeQueue

queue = CafeQueue(**payload)  # raises on invalid data
```

That pattern keeps LinkML as the source of truth while giving you first-class Pydantic ergonomics in APIs and services.

## Visualizing the Model

You can render the same schema as a diagram:

```bash
gen-erdiagram examples/omics_study_schema.yaml > examples/coffee_queue_schema.mmd
```

The Mermaid output is useful in docs and design reviews because wet-lab and data teams can quickly verify structure before implementation details distract the conversation.

## Useful for Bioinformaticians

- The same pattern maps cleanly to sample sheets and assay metadata.
- Controlled vocabularies for conditions, assays, and cohorts become explicit enums.
- Provenance fields (batch, instrument, protocol version) can be required instead of implied.
- The schema stays reusable across notebooks, CLIs, and workflow engines.
- Generated artifacts make handoffs to warehouse or graph layers less brittle.

## Caveats

- Schema design still takes thought; LinkML reduces drift, not modeling complexity.
- Very large legacy payloads may need an incremental migration plan.
- Teams should agree on schema versioning strategy early.

The runnable companion demo for this post is in [examples/linkml_quickstart_demo.py](https://github.com/CU-DBMI/set-website/blob/main/examples/linkml_quickstart_demo.py).

## Run It Locally

```bash
uv run examples/linkml_quickstart_demo.py
```
