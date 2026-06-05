"""Solution: Exercise 1 — Great Expectations validation."""

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"

ALLOWED_STATUS = {"completed", "cancelled", "refunded"}


def validate_with_pandas_checks(df: pd.DataFrame) -> list[str]:
    """GX-style checks using pandas when GX context setup is heavy for exercises."""
    failures: list[str] = []

    if df["order_id"].isna().any():
        failures.append("order_id contains nulls")
    if df["order_id"].duplicated().any():
        failures.append("order_id is not unique")
    if (df["quantity"] <= 0).any():
        failures.append("quantity must be > 0")
    if not set(df["status"].dropna().unique()).issubset(ALLOWED_STATUS):
        failures.append("status has invalid values")
    if (df["unit_price"] < 0).any():
        failures.append("unit_price must be >= 0")

    return failures


def validate_with_gx(df: pd.DataFrame) -> bool:
    try:
        import great_expectations as gx
        from great_expectations.core import ExpectationSuite

        context = gx.get_context(mode="ephemeral")
        suite = ExpectationSuite(name="orders_suite")
        suite.add_expectation(
            gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
        )
        suite.add_expectation(
            gx.expectations.ExpectColumnValuesToBeUnique(column="order_id")
        )
        suite.add_expectation(
            gx.expectations.ExpectColumnValuesToBeBetween(column="quantity", min_value=1)
        )
        suite.add_expectation(
            gx.expectations.ExpectColumnValuesToBeInSet(
                column="status", value_set=list(ALLOWED_STATUS)
            )
        )
        suite.add_expectation(
            gx.expectations.ExpectColumnValuesToBeBetween(
                column="unit_price", min_value=0
            )
        )

        batch = context.data_sources.pandas_default.read_dataframe(df)
        result = batch.validate(expectation_suite=suite)
        return result.success
    except Exception:
        return len(validate_with_pandas_checks(df)) == 0


def main() -> None:
    df = pd.read_csv(ORDERS_PATH)

    failures = validate_with_pandas_checks(df)
    gx_ok = validate_with_gx(df)

    if failures:
        print("FAILED expectations:")
        for f in failures:
            print(f"  - {f}")
    else:
        print("All pandas checks passed.")

    print(f"GX validate success: {gx_ok}")

    if failures or not gx_ok:
        sys.exit(1)
    print("Validation complete.")


if __name__ == "__main__":
    main()
