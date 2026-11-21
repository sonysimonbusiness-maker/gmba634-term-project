# Executive case: Is the US goods supply chain keeping up with what consumers buy?

**Audience:** the planning manager at a freight company, who decides where to put trucks and carriers.
**Decision:** where to put carrier capacity next year.
**Main claim:** trucks coming in from Mexico rose about 31% from 2016 to 2025, while trucks from Canada fell about 10%.

## Situation

People buy more of their goods online than they used to. E-commerce was 7.7% of US retail sales in early 2016. It peaked at 16.0% in 2020, dropped to 13.7% in 2022, and reached 17.9% in the third quarter of 2026. Spending is also growing. In eleven Colorado counties, retail sales went from about $157 billion in 2016 to about $266 billion in 2025 (not adjusted for inflation). Growth was strong until 2022 (11.5%), then slowed to 0.5%, 1.3% and 3.2%.

All of that stuff has to travel by freight, and a planner has to pick routes and carriers well before it moves.

## Complication

The freight routes did not all move the same way.

- **Border trucks shifted south.** Trucks coming in from Mexico went from 5.80 million in 2016 to 7.59 million in 2025 (+31%). Trucks from Canada went from 5.88 million to 5.27 million (-10%).
- **Ports swung and the coasts split.** I compared the 25 ports that report in all eight years. Their container volume peaked at 45.3 million TEUs in 2021 and was back to 35.4 million in 2023, about where it began in 2016 (35.9 million). From 2021 to 2023 the Pacific Coast fell 32%, the Atlantic 15% and the Gulf 7%. Measured from 2016, the Pacific is down 21% while the Atlantic is up 13% and the Gulf up 33%.
- **Imports bounce around.** Container imports fell 13% in 2023 (28.9 to 25.1 million TEUs) and were back to 29.1 million in 2024 and 29.5 million in 2025.
- **Counts are not value.** Trucks are counted, not weighed or priced, and ports count containers, not what is inside them.

If a plan copies last year's mix of routes, it can end up in the wrong place when the mix moves this much.

## Resolution

I recommend the planning manager shift some capacity toward Mexico-border routes and Gulf and Atlantic port routes before next year's contracts are set. Trucks from Mexico grew 31% over nine years while Canada shrank 10%, so last year's mix probably doesn't fit anymore. I would also look hard at any Pacific-coast commitments before renewing them.

- **Owner:** the planning manager.
- **When:** before next year's carrier contracts are set. The date is UNKNOWN.
- **Cost:** UNKNOWN. This public data has no rates or contract terms.
- **Rejected option:** keep last year's mix. The data shows the mix changing at the border and at the ports.

This is a recommendation, not a proven result.

## What would change my mind

I would drop this if the next border data release showed trucks from Mexico flat or falling, or if the Pacific ports got back to their 2021 level of 20.2 million TEUs. I would look in the same BTS tables I used here. I would also drop it if the company's own lane data showed its freight does not follow these public trends.

## Limits and unknowns

- This is national, public data. It can't show what any one company's routes look like. The first step before acting is to compare it with the company's own lane volumes.
- Trucks and containers are counted, not weighed or priced.
- I compared only the 25 ports that report in all eight years, because the number of ports reporting changed from 26 to 41.
- Colorado is eleven counties in nominal dollars, so part of its growth is inflation.
- The numbers are recomputed from the data files in this repo. I compared the e-commerce, border and import figures with the original source sites, and they match. The port and Colorado figures are **not yet rechecked** against their sources (see [../ai-check/](../ai-check/)).
- The data shows that volumes moved, not why.

## Evidence and where to check it

| Finding | Folder | Chart |
|---|---|---|
| Mexico +31%, Canada -10% | [datasets/02-border-crossings](../datasets/02-border-crossings/) | [Tableau line chart](../datasets/02-border-crossings/tableau-chart.png) |
| Pacific -32%, Atlantic -15%, Gulf -7% (2021 to 2023) | [datasets/01-ports](../datasets/01-ports/) | Line chart by coast |
| Imports -13% in 2023 | [datasets/03-container-imports](../datasets/03-container-imports/) | Line chart |
| E-commerce 7.7% to 17.9% | [datasets/04-ecommerce-share](../datasets/04-ecommerce-share/) | Line chart (FRED link) |
| Colorado +70% | [datasets/05-colorado-retail](../datasets/05-colorado-retail/) | Bar chart |

## AI use

Claude (Anthropic) pulled and added up the public data, drew the charts, and wrote the first draft of this case. I chose the question, the audience and the recommendation, reviewed the wording and approved it as my own. Numbers were recomputed with a script (see [../ai-check/](../ai-check/)), and the check against the original sources is still open there.
