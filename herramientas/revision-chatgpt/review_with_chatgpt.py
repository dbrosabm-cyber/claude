#!/usr/bin/env python3
"""Send a file's contents to ChatGPT (OpenAI API) for review.

Usage:
    export OPENAI_API_KEY=sk-...
    python3 review_with_chatgpt.py path/to/file.py
    python3 review_with_chatgpt.py path/to/file.py --model gpt-4o --instructions "Focus on security issues"
"""

import argparse
import os
import sys

from openai import OpenAI

DEFAULT_MODEL = "gpt-4o"
DEFAULT_INSTRUCTIONS = (
    "You are reviewing code or written work produced by another AI assistant "
    "(Claude). Give a thorough, critical review: point out bugs, security "
    "issues, unclear logic, missing edge cases, and style problems. Suggest "
    "concrete fixes. Be specific and reference line numbers or snippets "
    "where relevant."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Path to the file to review")
    parser.add_argument(
        "--model", default=DEFAULT_MODEL, help=f"OpenAI model to use (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--instructions",
        default=DEFAULT_INSTRUCTIONS,
        help="Custom review instructions/prompt for ChatGPT",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(
            "Error: set the OPENAI_API_KEY environment variable with your OpenAI API key.",
            file=sys.stderr,
        )
        return 1

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as exc:
        print(f"Error reading {args.file}: {exc}", file=sys.stderr)
        return 1

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=args.model,
        messages=[
            {"role": "system", "content": args.instructions},
            {
                "role": "user",
                "content": f"Review the following file ({args.file}):\n\n{content}",
            },
        ],
    )

    print(response.choices[0].message.content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
