# Executive case: Is the US goods supply chain keeping up with what consumers buy?

**Audience:** a logistics planning manager at a freight broker or shipper.
**Decision:** where to place carrier capacity next year.
**Main claim:** inbound truck crossings from Mexico rose about 31% from 2016 to 2025, while crossings from Canada fell about 10%.

## Situation

Consumers now buy more of their goods online. The US Census series on FRED shows e-commerce rising from 7.7% of retail sales in early 2016 to a peak of 16.0% in the second quarter of 2020, easing to 13.7% in the second quarter of 2022, and reaching 17.9% in the third quarter of 2026. Retail demand is also growing in dollar terms: across eleven Colorado counties, retail sales grew from about $157 billion in 2016 to about $266 billion in 2025 (nominal, not adjusted for inflation). Growth was strong through 2022 (11.5%) and then slowed to 0.5%, 1.3% and 3.2% in 2023 to 2025.

That demand reaches shoppers through freight. A planner has to decide in advance which routes and carriers to commit to.

## Complication

The freight routes did not move together. Four findings from the public data:

- **Border trucks shifted south.** Inbound trucks from Mexico rose from 5.80 million in 2016 to 7.59 million in 2025 (+31%). Trucks from Canada fell from 5.88 million to 5.27 million (-10%).
- **Port volume swung and moved between coasts.** On the 25 ports that report in all eight years, container volume peaked at 45.3 million TEUs in 2021 and was back to 35.4 million in 2023, about where it started in 2016 (35.9 million). From 2021 to 2023 the Pacific Coast fell 32%, the Atlantic Coast 15% and the Gulf Coast 7%. Measured from 2016 to 2023, the Pacific Coast is down 21% while the Atlantic is up 13% and the Gulf up 33%.
- **Imports are volatile.** Containerized imports fell 13% in 2023 (28.9 million to 25.1 million TEUs) and recovered to 29.1 million in 2024 and 29.5 million in 2025.
- **Counts are not the same as value.** Truck crossings count trucks, not weight or dollars, and port volume counts containers, not what is inside them.

A plan built on last year's lane mix can be badly placed when the mix moves this much.

## Resolution

**Recommendation (a recommendation, not a result):** plan next year's capacity around the lanes that grew. Add carrier capacity for Mexico-border lanes and Gulf and Atlantic port lanes, and review commitments tied to Pacific-coast ports before renewing them.

- **Owner:** the logistics planning manager.
- **When:** before next year's carrier contracts are set. Date UNKNOWN.
- **Cost:** UNKNOWN. This public data has no rates, contract terms or lane volumes.
- **Rejected option:** keep last year's lane mix unchanged. Rejected because the public data shows the mix changing in both border and port traffic.

**What would change my mind (reversal test):** I would withdraw this if the next release of the BTS border data showed Mexico crossings flat or falling, or if the next port release showed the Pacific Coast back near its 2021 level of 20.2 million TEUs. I would look in the same BTS data tables used here. I would also withdraw it if the company's own lane data showed its volume does not follow these public trends.

## Limits and unknowns

- This is public, national-level data. It cannot say what any one company's lanes look like. The first step before acting is to compare it with the company's own lane volumes.
- Truck counts are not freight value or weight. Port counts mix cargo.
- Only the 25 ports present in all eight years were compared, because the number of reporting ports changed from 26 to 41 over the period.
- Colorado is eleven counties and nominal dollars, so part of its growth is inflation.
- The e-commerce figures were read through a summarized fetch and are NOT VERIFIED against FRED.
- Cause is not shown. The data does not say why the shifts happened.

## Evidence and where to check it

| Finding | Folder | Chart |
|---|---|---|
| Mexico +31%, Canada -10% | [datasets/02-border-crossings](../datasets/02-border-crossings/) | [Tableau line chart](../datasets/02-border-crossings/tableau-chart.png) |
| Pacific -32%, Atlantic -15%, Gulf -7% (2021 to 2023) | [datasets/01-ports](../datasets/01-ports/) | Line chart by coast |
| Imports -13% in 2023 | [datasets/03-container-imports](../datasets/03-container-imports/) | Line chart |
| E-commerce 7.7% to 17.9% | [datasets/04-ecommerce-share](../datasets/04-ecommerce-share/) | Line chart (FRED link) |
| Colorado +70% | [datasets/05-colorado-retail](../datasets/05-colorado-retail/) | Bar chart |

## AI use

Claude (Anthropic) pulled and aggregated the public data, drew the charts, and drafted the claims, the six story boxes and this outline. I own the audience, the decision and the recommendation, and I rewrite the text in my words. How the figures were checked, what was found and what is still unchecked is in [../ai-check/](../ai-check/).
