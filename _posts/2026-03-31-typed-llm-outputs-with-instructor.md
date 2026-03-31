---
title: "Typed LLM Outputs with Instructor"
author: dave-bunten
tags:
  - python
  - machine-learning
  - llm
  - data-validation
---

# Typed LLM Outputs with Instructor

{% include blog-post-intro.html %}

## Introduction

<!-- excerpt start -->
**LLMs are good at generating text, but applications usually need structured data.**
[`instructor`](https://python.useinstructor.com/) is a small Python library that lets you describe the output you want with a [Pydantic](https://docs.pydantic.dev/latest/) model and have the model response validated automatically.
Here, Pydantic provides the schema for the LLM output, and `instructor` uses that schema to validate the response.
That means less prompt glue, less manual parsing, and clearer types in your code, even when running a local model in-process with `llama-cpp-python`.
<!-- excerpt end -->

## Without `instructor`

Without a typing layer, we often ask for JSON and then parse the response ourselves.

```python
import json

from llama_cpp import Llama
from pydantic import BaseModel


class TicketSummary(BaseModel):
    title: str
    priority: str
    owner: str


llm = Llama.from_pretrained(
    repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
    filename="*q8_0.gguf",
    n_ctx=2048,
    verbose=False,
)

response = llm.create_chat_completion(
    messages=[
        {
            "role": "user",
            "content": (
                "Extract a support ticket summary from this text and return "
                "JSON with title, priority, and owner fields only: "
                "'Production login errors are affecting clinicians. "
                "Assign this to Avery with high priority.'"
            ),
        }
    ],
    response_format={
        "type": "json_object",
        "schema": TicketSummary.model_json_schema(),
    },
    temperature=0,
)

data = json.loads(response["choices"][0]["message"]["content"])
ticket = TicketSummary.model_validate(data)
print(ticket)
```

This works, but the prompt, parsing, and validation are all still your responsibility.
Even though `TicketSummary` is a Pydantic model, you still have to coerce the raw LLM text into JSON yourself before validation can happen.

## With `instructor`

With `instructor`, the schema becomes part of the request.

```python
import instructor
from llama_cpp import Llama
from pydantic import BaseModel


class TicketSummary(BaseModel):
    title: str
    priority: str
    owner: str


llm = Llama.from_pretrained(
    repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
    filename="*q8_0.gguf",
    n_ctx=2048,
    verbose=False,
)

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
                "Extract a support ticket summary from this text: "
                "'Production login errors are affecting clinicians. "
                "Assign this to Avery with high priority.'"
            ),
        }
    ],
    temperature=0,
)

print(ticket)
```

For this local `llama-cpp-python` setup, `instructor.Mode.MD_JSON` was the more reliable choice during testing than stricter JSON-schema mode.

Example result:

```python
TicketSummary(
    title="Production login errors are affecting clinicians",
    priority="high",
    owner="Avery",
)
```

## Why we like it

For short extraction tasks, `instructor` makes LLM code feel more like ordinary Python.
You define a Pydantic model once, pass it as `response_model`, and work with validated objects instead of raw strings.
The full demo used for this post is included in this repository as `examples/instructor_demo.py`.

## Run It Locally

This version does not require Ollama or a local model server. On first run, `llama-cpp-python` downloads a small public GGUF model from Hugging Face, may build its native backend, and then runs the model in-process:

```bash
uv run --with instructor --with llama-cpp-python --with huggingface-hub --with pydantic \
  python examples/instructor_demo.py
```
