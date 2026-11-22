# Number trail

Every number in my findings has one line here. Years and dates need no line. Claude built these pivot files with scripts; the last column says where each number sits.

| Number | Page | What it is | How I got it | Where it is in the pivot |
|---|---|---|---|---|
| 32.4% | port-containers | Change in Pacific Coast container volume, 2021 to 2023 | Sum of TEUs by region and year, then 2023 divided by 2021 minus 1 | analysis/port-containers-pivot.csv, row Pacific Coast, column change_2021_to_2023_pct |
| 20.22 million | port-containers | Pacific Coast TEUs in 2021, in millions | Sum of volume for 7 Pacific ports, divided by 1,000,000 | analysis/port-containers-pivot.csv, row Pacific Coast, column teu_millions_2021 |
| 13.67 million | port-containers | Pacific Coast TEUs in 2023, in millions | Sum of volume for 7 Pacific ports, divided by 1,000,000 | analysis/port-containers-pivot.csv, row Pacific Coast, column teu_millions_2023 |
| 30.8% | border-trucks | Change in inbound trucks from Mexico, 2016 to 2025 | 2025 trucks divided by 2016 trucks minus 1 | analysis/border-trucks-pivot.csv, row Mexico, column change_2016_to_2025_pct |
| 5.80 million | border-trucks | Mexico trucks in 2016, in millions | Sum of Trucks value for the year, divided by 1,000,000 | analysis/border-trucks-pivot.csv, row Mexico, column millions_2016 |
| 7.59 million | border-trucks | Mexico trucks in 2025, in millions | Sum of Trucks value for the year, divided by 1,000,000 | analysis/border-trucks-pivot.csv, row Mexico, column millions_2025 |
| 10.4% | border-trucks | Change in inbound trucks from Canada, 2016 to 2025 (a fall) | 2025 trucks divided by 2016 trucks minus 1 | analysis/border-trucks-pivot.csv, row Canada, column change_2016_to_2025_pct |
| 5.88 million | border-trucks | Canada trucks in 2016, in millions | Sum of Trucks value for the year, divided by 1,000,000 | analysis/border-trucks-pivot.csv, row Canada, column millions_2016 |
| 5.27 million | border-trucks | Canada trucks in 2025, in millions | Sum of Trucks value for the year, divided by 1,000,000 | analysis/border-trucks-pivot.csv, row Canada, column millions_2025 |
| 13.0% | container-imports | Change in US container imports, 2022 to 2023 (a fall) | 2023 TEUs divided by 2022 TEUs minus 1 | analysis/container-imports-pivot.csv, row 2023, column change_vs_prior_year_pct |
| 28.89 million | container-imports | TEUs in 2022, in millions | Sum of monthly TEUs for 2022, divided by 1,000,000 | analysis/container-imports-pivot.csv, row 2022, column teu_millions |
| 25.13 million | container-imports | TEUs in 2023, in millions | Sum of monthly TEUs for 2023, divided by 1,000,000 | analysis/container-imports-pivot.csv, row 2023, column teu_millions |
| 7.7% | ecommerce-share | E-commerce share of retail sales, 2016 Q1 | Value read from the FRED series ECOMPCTSA | analysis/ecommerce-share-pivot.csv, row 2016 Q1, column share_of_retail_pct |
| 17.9% | ecommerce-share | E-commerce share of retail sales, 2026 Q3 | Value read from the FRED series ECOMPCTSA | analysis/ecommerce-share-pivot.csv, row 2026 Q3, column share_of_retail_pct |
| 10.2 percentage points | ecommerce-share | Gain in share, 2016 Q1 to 2026 Q3 | 17.9 minus 7.7 | analysis/ecommerce-share-pivot.csv, row 2026 Q3, column change_vs_2016_q1_pct_points |
| 69.7% | colorado-retail | Change in retail sales, 11 counties, 2016 to 2025 | 2025 sales divided by 2016 sales minus 1 | analysis/colorado-retail-pivot.csv, row 2025, column change_vs_2016_pct |
| $157.05 billion | colorado-retail | Retail sales in 2016, in billions of dollars | Sum of Total retail sales for 11 counties, divided by 1,000,000,000 | analysis/colorado-retail-pivot.csv, row 2016, column retail_sales_billions |
| $266.47 billion | colorado-retail | Retail sales in 2025, in billions of dollars | Sum of Total retail sales for 11 counties, divided by 1,000,000,000 | analysis/colorado-retail-pivot.csv, row 2025, column retail_sales_billions |
