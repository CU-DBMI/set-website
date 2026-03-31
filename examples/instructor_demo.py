"""Compare manual JSON parsing with an Instructor response model."""

import json
import os

import instructor
from llama_cpp import Llama
from pydantic import BaseModel


MODEL_REPO_ID = os.getenv("MODEL_REPO_ID", "Qwen/Qwen2-0.5B-Instruct-GGUF")
MODEL_FILENAME = os.getenv("MODEL_FILENAME", "*q8_0.gguf")


class TicketSummary(BaseModel):
    """Structured output for a short support ticket summary."""

    title: str
    priority: str
    owner: str


PROMPT = (
    "Extract a support ticket summary from this text and return title, "
    "priority, and owner: "
    "'Production login errors are affecting clinicians. "
    "Assign this to Avery with high priority.'"
)


def load_llm() -> Llama:
    """Load a local GGUF model with llama-cpp-python."""
    return Llama.from_pretrained(
        repo_id=MODEL_REPO_ID,
        filename=MODEL_FILENAME,
        n_ctx=2048,
        verbose=False,
    )


def without_instructor(llm: Llama) -> TicketSummary:
    """Parse an LLM response manually."""
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": (
                    f"{PROMPT} "
                    "Return JSON with exactly these fields: title, priority, owner."
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
    return TicketSummary.model_validate(data)


def with_instructor(llm: Llama) -> TicketSummary:
    """Return a validated Pydantic model directly from the LLM call."""
    create = instructor.patch(
        create=llm.create_chat_completion_openai_v1,
        mode=instructor.Mode.MD_JSON,
    )
    return create(
        response_model=TicketSummary,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0,
    )


if __name__ == "__main__":
    llm = load_llm()
    print("Without instructor:")
    print(without_instructor(llm))
    print()
    print("With instructor:")
    print(with_instructor(llm))
