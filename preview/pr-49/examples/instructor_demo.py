"""Compare prompt-only JSON output with an Instructor response model."""

import os
from pathlib import Path
from urllib.request import urlretrieve

import instructor
from llama_cpp import Llama
from pydantic import BaseModel


MODEL_REPO_ID = os.getenv(
    "MODEL_REPO_ID", "hugging-quants/Llama-3.2-3B-Instruct-Q4_K_M-GGUF"
)
MODEL_FILENAME = os.getenv("MODEL_FILENAME", "llama-3.2-3b-instruct-q4_k_m.gguf")
MODEL_CONTEXT_SIZE = int(os.getenv("MODEL_CONTEXT_SIZE", "32768"))
MODEL_URL = (
    f"https://huggingface.co/{MODEL_REPO_ID}/resolve/main/{MODEL_FILENAME}?download=true"
)
MODEL_CACHE_DIR = Path(os.getenv("MODEL_CACHE_DIR", Path.home() / ".cache" / "set-website"))


class TicketSummary(BaseModel):
    title: str
    priority: str
    owner: str


PROMPT = (
    "Extract a support ticket summary from this text. Return title, priority, "
    "and owner. Use the first name only for the owner. "
    "'Our benchmark says the refactor is 10x faster, but only if we start the "
    "timer after the function returns. Assign this to Avery with high priority.'"
)


def load_llm() -> Llama:
    """Load a local GGUF model with llama-cpp-python."""
    MODEL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    model_path = MODEL_CACHE_DIR / MODEL_FILENAME
    if not model_path.exists():
        urlretrieve(MODEL_URL, model_path)
    return Llama(
        model_path=str(model_path),
        n_ctx=MODEL_CONTEXT_SIZE,
        verbose=False,
    )


def without_instructor(llm: Llama) -> str:
    """Ask for JSON using prompting alone."""
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": (
                    f"{PROMPT} "
                    "Return JSON with these fields: title, priority, owner."
                ),
            }
        ],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"]


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
