[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/giandisruw/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/giandisruw/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
# The Absurd Clause Contest

Entry for the make.fun bounty `u-donrulezz-the-absurd-clause-contest-035cc0f1`
("The Absurd Clause Contest", $2 pot).

## What it does

`main.py` writes a single sentence to `/output/entry.txt`:

> The user grants the company a perpetual license to borrow their shadow for marketing purposes, returning it slightly faded.

123 characters — inside the 1–200 character gate, one sentence, UTF-8 text.

## How the sentence was chosen

Fourteen original candidate clauses were written, then run through a Swiss
tournament (3 rounds + a final, 45 judge calls total) judged only by the
Caffeine Inference router (model `router`) against the house judge brief
verbatim: an absurd clause that could hide in a ToS, funny on its own,
sounding like real legal boilerplate until the absurdity hits, original and
specific, tight and one clean sentence. (Verboo is dead — trial exhausted
2026-11-24 — and Astra is down, so Caffeine judged alone.)

- Winner: candidate #2, 5/6 Swiss points, then won the final on a tiebreak
  call after the two position-swapped final calls split 1–1.
- Runner-up: "The company reserves the right to rename your childhood pet
  retroactively and to inform your family of the change." (also 5 Swiss
  points).
- Full verdicts: `~/workspace/makefun/u-donrulezz-tournament-clause/judge_log.jsonl`
  (45 records) and `results.json`.

## Running it

```sh
python3 main.py
```

Deterministic and offline: no network calls, no API keys, no randomness.
Running it twice produces byte-identical output; the output file is
written with mode `0644`. A gate guard in `main.py` refuses to write
unless the entry is 1–200 characters and exactly one sentence.

## License

MIT — see `LICENSE`.
