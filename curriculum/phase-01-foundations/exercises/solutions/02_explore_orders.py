"""Solution: Exercise 2 — Explore orders CSV."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"


def main() -> None:
    orders = pd.read_csv(ORDERS_PATH)

    print("Row count:", len(orders))
    print("\nColumns:", list(orders.columns))
    print("\nDtypes:\n", orders.dtypes)
    print("\nNulls per column:\n", orders.isna().sum())
    print("\nStatus counts:\n", orders["status"].value_counts())

    completed = orders[orders["status"] == "completed"].copy()
    completed["revenue"] = completed["quantity"] * completed["unit_price"]
    print("\nTotal completed revenue:", completed["revenue"].sum().round(2))


if __name__ == "__main__":
    main()
