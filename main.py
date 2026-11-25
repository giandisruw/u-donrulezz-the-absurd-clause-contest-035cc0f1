"""Entry for make.fun bounty u-donrulezz-the-absurd-clause-contest-035cc0f1
("The Absurd Clause Contest", $2 pot).

Writes one original English sentence -- an absurd clause buried deep
inside a terms-of-service agreement -- to /output/entry.txt.

The sentence was chosen by a Swiss tournament (3 rounds + final, 45 judge
calls) over 14 original candidate clauses, judged only by the Caffeine
Inference router (model "router") against the house judge brief verbatim.
Winner: candidate #2, 5/6 Swiss points, then won the final on a tiebreak
call after the two position-swapped final calls split 1-1.

Deterministic and offline: no network calls, no API keys, no randomness.
"""
import os

SENTENCE = (
    "The user grants the company a perpetual license to borrow their "
    "shadow for marketing purposes, returning it slightly faded."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate guard: the sealed scorer requires 1-200 chars of UTF-8 text.
    if not (1 <= len(SENTENCE) <= 200):
        raise ValueError(f"entry is {len(SENTENCE)} chars, must be 1-200")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
