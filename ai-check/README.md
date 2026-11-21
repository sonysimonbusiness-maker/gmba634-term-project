# AI use and output check

## What AI did in this project

Claude (Anthropic) did the following: pulled public data and aggregates, filtered and combined them, drew the charts, built the site, and drafted the claims, the six story boxes and the [executive case](../case/executive-case.md). I decide the question, the audience and the recommendation, and I rewrite the text in my words.

## The automation component

[`verify.py`](verify.py) recomputes every headline percentage from the CSV files in this repo. Anyone can run it from the repo root:

```
python3 ai-check/verify.py
```

Its saved output is in [`verify-output.txt`](verify-output.txt). It checks that the numbers in the READMEs, the site and the case follow from the data files. It does **not** check the data files against the original sources.

## Check 1: claims against the data files (done by script)

| Claim in the repo | Recomputed from data file | Match |
|---|---|---|
| West Coast ports -32%, 2021 to 2023 | -32.4% | Yes |
| Atlantic Coast -15% | -15.1% | Yes |
| Gulf Coast -7% | -6.8% | Yes |
| Mexico trucks +31%, 2016 to 2025 | +30.8% | Yes |
| Canada trucks -10% | -10.4% | Yes |
| Container imports -13% in 2023 | -13.0% | Yes |
| Colorado retail +70%, 2016 to 2025 | +69.7% | Yes |
| Colorado growth 11.5% in 2022, then 0.5%, 1.3%, 3.2% | 11.5, 0.5, 1.3, 3.2 | Yes |
| Same-port total 35.9 (2016), 45.3 (2021), 35.4 (2023) | 35.9, 45.3, 35.4 | Yes |

Not covered by the script: the e-commerce share (7.7%, 16.0%, 13.7%, 17.9%), which has no CSV in the repo, and the Houston (+76%) and Savannah (+31%) figures, which come from port-level data not saved here.

## Check 2: errors found in AI output, and fixed

| What was wrong | How it was caught | Fix |
|---|---|---|
| The Gulf Coast was described as "stayed about level" | Compared the wording with the numbers (it fell 7%) | Wording changed to a 7% dip |
| The old house-schedule worksheet said slack "after Fit Out", which is illogical because Fit Out is last | Read the logic of the box | Changed to "between Build interior and Fit Out" |
| The old deck said "four tasks" | Compared with my Tableau screenshots, which show five | Corrected to five |
| In chat, the Pacific -32% was described as covering 2016 to 2023 | Re-running the numbers: -32% is 2021 to 2023; 2016 to 2023 is -21% | The repo wording was already correct; the chat wording was not used |
| The ports file mixes units in its volume column | Inspected the data | Filtered to container TEUs and compared only the 25 ports present in all eight years |

## Check 3: figures against the original sources (mine to do)

Not yet done. Open each source, find the number, and tick the box. If a number differs, tell me and I will fix the repo.

| Figure | Where to look | My value | Source value | Done |
|---|---|---|---|---|
| E-commerce share, Q1 2016 7.7%, Q2 2020 16.0%, Q2 2022 13.7%, Q3 2026 17.9% | FRED series ECOMPCTSA | | | [ ] |
| Mexico trucks 2016 and 2025 (5.80 and 7.59 million) | BTS Border Crossing Entry Data | | | [ ] |
| Pacific Coast 2021 and 2023 (20.2 and 13.7 million TEUs) | BTS port performance data | | | [ ] |
| Container imports 2022 and 2023 (28.9 and 25.1 million TEUs) | Dataset 3 source, linked in its folder | | | [ ] |
| Colorado retail 2016 and 2025 ($157B and $266B) | Dataset 5 source, linked in its folder | | | [ ] |

## What I do not trust AI for here

- Causes. The data shows that volumes moved, not why.
- Any claim about one company's lanes, costs or contracts. The public data has none.
- Numbers it read through a summarized fetch, until I compare them with the source (Check 3).

## Limits of this check

Check 1 was run by a script that Claude wrote, so it tests consistency, not truth. Check 3 is the check against the world, and it is not finished until the table above is filled in.
