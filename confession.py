"""A robot's two-line apology, written to entry.txt.

The program takes no input and prints nothing: its whole job is to
leave the confession in the file the judge reads.
"""

import os

APOLOGY = (
    "I am sorry I set the table for four when only two were coming, "
    "because I counted the chairs instead of the guests.",
    "I have learned to count people, not chairs, so I check the guest "
    "list first.",
)


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    target = output_path()
    folder = os.path.dirname(target)
    if folder and not os.path.isdir(folder):
        os.makedirs(folder)
    text = "\n".join(APOLOGY) + "\n"
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
