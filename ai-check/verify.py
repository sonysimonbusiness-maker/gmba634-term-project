"""Recompute the headline figures from the data files in this repo.
Run from the repo root:  python3 ai-check/verify.py
Covers ports, border crossings, container imports and Colorado retail.
E-commerce share (FRED) has no CSV in the repo, so it is NOT covered here.
This checks the claims against our own data files, not against the original source sites."""
import pandas as pd

def pct(a, b):
    return round((b / a - 1) * 100, 1)

p = pd.read_csv("datasets/01-ports/data.csv").set_index("reporting_year")
b = pd.read_csv("datasets/02-border-crossings/data.csv").set_index("year")
i = pd.read_csv("datasets/03-container-imports/data.csv").set_index("year").iloc[:, 0]
c = pd.read_csv("datasets/05-colorado-retail/data.csv").set_index("year").iloc[:, 0]

print("PORTS (million TEUs, 25 same ports)")
for col in p.columns:
    print(f"  {col}: 2021 to 2023 {pct(p.loc[2021, col], p.loc[2023, col])}%   2016 to 2023 {pct(p.loc[2016, col], p.loc[2023, col])}%")
print(f"  total 2016 {p.loc[2016].sum():.1f}, 2021 {p.loc[2021].sum():.1f}, 2023 {p.loc[2023].sum():.1f}")
print("BORDER (inbound trucks)")
print(f"  Mexico 2016 to 2025: {pct(b.loc[2016,'us_mexico_trucks'], b.loc[2025,'us_mexico_trucks'])}%")
print(f"  Canada 2016 to 2025: {pct(b.loc[2016,'us_canada_trucks'], b.loc[2025,'us_canada_trucks'])}%")
print("CONTAINER IMPORTS (TEUs)")
print(f"  2022 to 2023: {pct(i.loc[2022], i.loc[2023])}%   2023 to 2024: {pct(i.loc[2023], i.loc[2024])}%")
print("COLORADO RETAIL (11 counties, nominal)")
print(f"  2016 to 2025: {pct(c.loc[2016], c.loc[2025])}%")
print("  yearly growth %:", {int(y): round(v * 100, 1) for y, v in c.pct_change().dropna().items()})
