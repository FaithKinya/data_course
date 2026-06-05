"""Solution: Exercise 1 — Read multiple sources."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
DATASETS = ROOT / "shared/datasets"


def load_sources() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    paths = {
        "orders": DATASETS / "orders.csv",
        "customers": DATASETS / "customers.csv",
        "products": DATASETS / "products.csv",
    }
    for name, path in paths.items():
        if not path.exists():
            raise FileNotFoundError(f"Missing {name}: {path}")

    orders = pd.read_csv(
        paths["orders"],
        parse_dates=["order_date"],
        dtype={"order_id": int, "customer_id": int, "product_id": int},
    )
    customers = pd.read_csv(
        paths["customers"],
        parse_dates=["signup_date"],
        dtype={"customer_id": int},
    )
    products = pd.read_csv(paths["products"], dtype={"product_id": int})
    return orders, customers, products


def main() -> None:
    orders, customers, products = load_sources()

    for name, df in [("orders", orders), ("customers", customers), ("products", products)]:
        print(f"\n=== {name} ===")
        print("Shape:", df.shape)
        print("Dtypes:\n", df.dtypes)

    joined = (
        orders.merge(customers, on="customer_id")
        .merge(products, on="product_id")
        .head()
    )
    print("\n=== joined preview ===")
    print(joined)

    total_mem = sum(
        df.memory_usage(deep=True).sum()
        for df in (orders, customers, products)
    )
    print(f"\nTotal memory (bytes): {total_mem}")


if __name__ == "__main__":
    main()
