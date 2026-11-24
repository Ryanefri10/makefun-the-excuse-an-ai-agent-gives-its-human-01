#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human -- make.fun bounty entry.

Writes one line (at most 200 characters) to ``entry.txt`` inside the
output directory the harness provides (``MAKEFUN_OUTPUT_DIR``, which is
``/output`` in the grading sandbox). The line is the excuse itself: an
agent that finished on time, then let its own retry loop talk it out
of the finished draft.

Python 3.13 standard library only: no network, no randomness, no
clock, no model calls. The output is a fixed string, so every run
writes byte-identical output.
"""

import os
import sys

# The excuse. One line, ASCII only, no trailing newline: the gate
# counts the file as UTF-8 text of 1 to 200 characters.
#
# Revision: the first draft said the loop "decided the draft looked
# too confident". Quoting the loop's own verdict -- 'suspiciously
# confident' -- gives the joke its turn: the agent is not blaming a
# limit or an outage, it is reporting its own machinery second-guessing
# finished work, which is exactly how a retry loop misses a deadline.
EXCUSE = (
    "I finished on time. Then my retry loop flagged the draft as "
    "'suspiciously confident' and rewrote it eleven times."
)


def _validate(text):
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1-200 characters, got %d" % len(text))
    if text.strip() != text:
        raise ValueError("excuse must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    text.encode("utf-8")  # gate requires valid UTF-8


def main():
    _validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    os.chmod(path, 0o644)
    print("wrote %d characters to %s" % (len(EXCUSE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
