---
title: "Typed LLM Outputs with Instructor"
author: dave-bunten
tags:
  - python
  - llm
  - data-validation
  - data-models
  - software-education
  - machine-learning
  - software-design
  - scientific-software
  - reproducibility
---

# Typed LLM Outputs with Instructor

{% include blog-post-intro.html %}

## Introduction

<!-- excerpt start -->
**LLMs are good at generating natural-language text, but applications usually need structured data.**
[`instructor`](https://python.useinstructor.com/) is a small Python library that lets you describe the output you want with a [Pydantic](https://docs.pydantic.dev/latest/) model and have the model response validated automatically.
Here, Pydantic provides the schema for the LLM output, and `instructor` uses that schema to validate the response.
That means less prompt glue, less manual parsing, and clearer types in your code, even when running a local model in-process with [llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/).
<!-- excerpt end -->

## Without `instructor`

Without a typing layer, we often end up asking for JSON through prompting alone and hoping the model follows the format closely enough.

```python
from pydantic import BaseModel


class TicketSummary(BaseModel):
    title: str
    priority: str
    owner: str

response = llm.create_chat_completion(
    messages=[
        {
            "role": "user",
            "content": (
                "Extract a support ticket summary from this text. Return title, "
                "priority, and owner. Use the first name only for the owner. "
                "'Our benchmark says the refactor is 10x faster, but only if "
                "we start the timer after the function returns. Assign this to "
                "Avery with high priority.' Return JSON with exactly these "
                "fields: title, priority, owner."
            ),
        }
    ],
    temperature=0,
)

print(response["choices"][0]["message"]["content"])
```

This is where the prompt-only path often falls apart: even when you ask for JSON, the model may still return headings, prose, or a shape that is close to what you wanted but not quite what your application expects.

Example output from the prompt-only path:

```text
Here is the extracted support ticket summary in JSON format:

{
  "title": "Refactor Performance Issue",
  "priority": "High",
  "owner": "Avery"
}
```

## With `instructor`

With `instructor`, the schema becomes part of the request.

```python
import instructor
from pydantic import BaseModel


class TicketSummary(BaseModel):
    title: str
    priority: str
    owner: str

create = instructor.patch(
    create=llm.create_chat_completion_openai_v1,
    mode=instructor.Mode.MD_JSON,
)

ticket = create(
    response_model=TicketSummary,
    messages=[
        {
            "role": "user",
            "content": (
                "Extract a support ticket summary from this text. Return title, "
                "priority, and owner. Use the first name only for the owner. "
                "'Our benchmark says the refactor is 10x faster, but only if "
                "we start the timer after the function returns. Assign this to "
                "Avery with high priority.'"
            ),
        }
    ],
    temperature=0,
)

print(ticket)
```

For this local `llama-cpp-python` setup, `instructor.Mode.MD_JSON` was the more reliable choice during testing than stricter JSON-schema mode.
We use `instructor.patch(...)` here because this example runs the model in-process through `llama-cpp-python`; if you are using an OpenAI-compatible server, `instructor.from_provider(...)` is often a cleaner option.

Example result:

```python
TicketSummary(
    title="Refactor Optimization Issue",
    priority="High",
    owner="Avery",
)
```

{% capture benchmark_warning %}
We do not recommend starting benchmarks after the function returns, no matter how impressive the speedup looks!
{% endcapture %}

{%
  include alert.html
  type="warning"
  content=benchmark_warning
%}

## How It Works

At a high level, `instructor` takes your Pydantic model, turns it into output guidance for the LLM call, and then validates what comes back.
If the response matches the expected shape, you get a normal Python object.
If not, `instructor` can retry or raise an error instead of quietly leaving you with malformed output text.

## Advantages of `instructor`

- You define a Pydantic model once and work with validated Python objects instead of raw strings.
- It reduces prompt glue and manual parsing code for structured extraction tasks.
- It becomes more useful as the response shape grows beyond a couple of flat fields.

## Disadvantages

- There can be a small token overhead because the output schema has to be communicated to the model.
- Model compatibility varies, especially with smaller local models.
- The exact integration style depends on your runtime; in-process `llama-cpp-python` uses patching, while server-based setups can use cleaner provider-style APIs.

The full demo used for this post is included in this repository as [examples/instructor_demo.py](https://github.com/CU-DBMI/set-website/blob/main/examples/instructor_demo.py).

## Run It Locally

This version does not require Ollama or a local model server. On first run, the script downloads a small public GGUF model, may build the native `llama-cpp-python` backend, and then runs the model in-process:

```bash
uv run --with instructor --with llama-cpp-python --with pydantic \
  https://raw.githubusercontent.com/CU-DBMI/set-website/main/examples/instructor_demo.py
```
