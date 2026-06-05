"""Solution: Exercise 3 — Clean orders transform."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "my_work" / "output"


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out = out[(out["quantity"] > 0) & (out["unit_price"] > 0)]
    out = out[out["status"].isin(["completed", "refunded"])]

    out["revenue"] = out["quantity"] * out["unit_price"]
    out.loc[out["status"] == "refunded", "revenue"] *= -1

    out["order_date"] = pd.to_datetime(out["order_date"])
    out["order_month"] = out["order_date"].dt.strftime("%Y-%m")

    return out


def main() -> None:
    orders = pd.read_csv(ORDERS_PATH)
    cleaned = clean_orders(orders)
    print(cleaned.head())

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cleaned.to_parquet(OUTPUT_DIR / "clean_orders.parquet", index=False)
    print(f"\nWrote {OUTPUT_DIR / 'clean_orders.parquet'}")


if __name__ == "__main__":
    main()
