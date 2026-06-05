"""Solution: Exercise 2 — Clean and validate orders."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"
WORK_DIR = Path(__file__).resolve().parent.parent / "my_work"

VALID_STATUSES = {"completed", "cancelled", "refunded"}


def validate_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    mask = (
        df["order_id"].notna()
        & df["customer_id"].notna()
        & df["product_id"].notna()
        & (df["quantity"] > 0)
        & (df["unit_price"] >= 0)
        & df["status"].isin(VALID_STATUSES)
    )
    return df[mask].copy(), df[~mask].copy()


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    base = out["quantity"] * out["unit_price"]
    out["revenue"] = 0.0
    out.loc[out["status"] == "completed", "revenue"] = base
    out.loc[out["status"] == "refunded", "revenue"] = -base
    return out


def main() -> None:
    orders = pd.read_csv(ORDERS_PATH)
    valid, rejects = validate_orders(orders)

    print(f"Valid: {len(valid)}, Rejects: {len(rejects)}")
    valid = add_revenue(valid)
    print(valid[["order_id", "status", "revenue"]].head())

    if len(rejects) > 0:
        WORK_DIR.mkdir(parents=True, exist_ok=True)
        rejects.to_csv(WORK_DIR / "rejects.csv", index=False)
        print(f"Wrote rejects to {WORK_DIR / 'rejects.csv'}")


if __name__ == "__main__":
    main()
