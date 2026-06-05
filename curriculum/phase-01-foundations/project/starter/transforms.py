"""Phase 1 project — transform functions."""

import pandas as pd


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out = out[(out["quantity"] > 0) & (out["unit_price"] > 0)]
    out = out[out["status"].isin(["completed", "refunded"])]

    out["revenue"] = out["quantity"] * out["unit_price"]
    out.loc[out["status"] == "refunded", "revenue"] *= -1

    out["order_date"] = pd.to_datetime(out["order_date"])
    out["order_month"] = out["order_date"].dt.strftime("%Y-%m")
    return out


def summarize_by_month_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["order_month", "category"], as_index=False)
        .agg(order_count=("order_id", "count"), total_revenue=("revenue", "sum"))
        .sort_values(["order_month", "category"])
    )
