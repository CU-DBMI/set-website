#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "linkml",
#   "linkml-runtime",
#   "pyyaml",
# ]
# ///

"""Small LinkML demo with a playful but practical schema.

This script reads a schema from disk, writes two payload examples (valid and
invalid), then optionally runs LinkML generators/validator commands.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import textwrap

VALID_DATA = textwrap.dedent(
    """\
    queue_id: CAFE-001
    orders:
      - order_id: O001
        drink: Latte
        status: queued
      - order_id: O002
        drink: Cappuccino
        status: brewing
    """
)

INVALID_DATA = textwrap.dedent(
    """\
    queue_id: CAFE-002
    orders:
      - order_id: O101
        drink: Mocha
        status: delayed
    """
)


def run(cmd: list[str]) -> None:
    """Run a command and print a compact success/failure message."""
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"[ok] {' '.join(cmd)}")
        if result.stdout.strip():
            print(result.stdout.strip())
    except FileNotFoundError:
        print(f"[skip] command not found: {cmd[0]}")
    except subprocess.CalledProcessError as exc:
        print(f"[fail] {' '.join(cmd)}")
        if exc.stdout.strip():
            print(exc.stdout.strip())
        if exc.stderr.strip():
            print(exc.stderr.strip())


def run_to_file(cmd: list[str], output_path: Path) -> None:
    """Run a command and write stdout to a file."""
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        output_path.write_text(result.stdout, encoding="utf-8")
        print(f"[ok] {' '.join(cmd)} -> {output_path}")
    except FileNotFoundError:
        print(f"[skip] command not found: {cmd[0]}")
    except subprocess.CalledProcessError as exc:
        print(f"[fail] {' '.join(cmd)}")
        if exc.stdout.strip():
            print(exc.stdout.strip())
        if exc.stderr.strip():
            print(exc.stderr.strip())


def main() -> None:
    examples_dir = Path(__file__).resolve().parent

    schema_path = examples_dir / "omics_study_schema.yaml"
    valid_path = examples_dir / "omics_study_valid.yaml"
    invalid_path = examples_dir / "omics_study_invalid.yaml"
    py_out = examples_dir / "coffee_queue_python.py"
    pyd_out = examples_dir / "coffee_queue_pydantic.py"
    mmd_out = examples_dir / "coffee_queue_schema.mmd"
    puml_out = examples_dir / "coffee_queue_schema.puml"

    if not schema_path.exists():
        raise FileNotFoundError(f"Missing schema file: {schema_path}")

    valid_path.write_text(VALID_DATA, encoding="utf-8")
    invalid_path.write_text(INVALID_DATA, encoding="utf-8")

    print("Using schema:")
    print(f"  - {schema_path}")
    print("Wrote:")
    print(f"  - {valid_path}")
    print(f"  - {invalid_path}")

    run(["gen-python", str(schema_path), "-o", str(py_out)])
    run(["gen-pydantic", str(schema_path), "-o", str(pyd_out)])
    run_to_file(["gen-erdiagram", str(schema_path)], mmd_out)
    run_to_file(["gen-plantuml", str(schema_path)], puml_out)

    print("\\nValidation checks:")
    run(["linkml-validate", "-s", str(schema_path), str(valid_path)])
    run(["linkml-validate", "-s", str(schema_path), str(invalid_path)])


if __name__ == "__main__":
    main()
