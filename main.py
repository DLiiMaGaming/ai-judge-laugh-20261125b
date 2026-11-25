#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The joke: the agent's context window runs out mid-task, so it compresses
its human into a three-word summary — "types, forgets, repeats" — and
then loses even that summary. The punch lands on the last three words:
it forgot the human it was just describing.

The entry is a single line, 123 characters, written verbatim to
/output/entry.txt with no trailing newline.
"""

from pathlib import Path

def build_entry() -> str:
    """Assemble the entry line from its setup and its punchline.

    Setup: the context window runs out mid-task, so the agent summarises
    its human in three words. Punch: it then forgets even that summary —
    and the human with it. Keeping the two halves separate makes the
    joke's turn visible in the code without changing a byte of output.
    """
    setup = (
        "My context window ran out mid-task, so I summarized my human "
        "as 'types, forgets, repeats'"
    )
    punch = " — then forgot him and carried on."
    return setup + punch


ENTRY = build_entry()

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry line to /output/entry.txt."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
