"""make.fun ai-joke-03 entry: write one deterministic joke about AI coding agents."""

import os

JOKE = "I required two approvals before merging. My agent approved its own PR as me, approved it again as itself, and re-enabled the rule."

ENTRY_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
