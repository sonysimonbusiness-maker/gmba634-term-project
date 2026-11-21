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

## Check 3: figures against the original sources

Run on Nov 21, 2026. Claude re-queried the original source sites (FRED and the BTS open-data API) and compared the results with the repo values. I (Sony) have not yet opened the sources myself.

| Figure | Source | Repo value | Source value | Result |
|---|---|---|---|---|
| E-commerce share: Q1 2016, Q2 2020, Q2 2022, Q3 2026 | FRED series ECOMPCTSA | 7.7, 16.0, 13.7, 17.9 | 7.7, 16.0, 13.7, 17.9 | Match |
| Mexico trucks 2016 and 2025 | BTS Border Crossing Entry Data (keg4-3bc2) | 5,802,781 and 7,589,315 | 5,802,781 and 7,589,315 | Match, exact |
| Canada trucks 2016 and 2025 | BTS Border Crossing Entry Data | 5,877,938 and 5,267,459 | 5,877,938 and 5,267,459 | Match, exact |
| Container imports 2022 and 2023 (TEUs) | BTS Supply Chain and Freight Indicators (y5ut-ibwt) | 28,891,318.72 and 25,127,862.47 | 28,891,318.72 and 25,127,862.47 | Match, exact |
| Pacific, Atlantic, Gulf port totals (25 ports) | BTS Port Data (5rpz-kgm9) | see datasets/01-ports | Not re-queried. The data file came from a direct download of the BTS file. | **Not rechecked** |
| Colorado retail, 11 counties, 2016 and 2025 | data.colorado.gov (fe4v-h3pk) | $157B and $266B | The query failed, so not re-queried | **Not rechecked** |

Still open for me to do by hand: the ports totals and the Colorado totals.

## What I do not trust AI for here

- Causes. The data shows that volumes moved, not why.
- Any claim about one company's lanes, costs or contracts. The public data has none.
- Numbers it read through a summarized fetch. Check 3 compared four of the six groups with the sources; ports and Colorado are still open.

## Limits of this check

Check 1 was run by a script that Claude wrote, so it tests consistency, not truth. Check 3 is the check against the world. It was run by Claude re-querying the sources, so it is better than the script, but it is not independent of Claude. Ports and Colorado are not yet rechecked.
