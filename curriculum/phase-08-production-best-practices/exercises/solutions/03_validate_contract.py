"""Solution: Exercise 3 — Validate CSV against YAML data contract."""

import sys
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"
CONTRACT_PATH = Path(__file__).resolve().parent / "orders_v1.yaml"


def check_type(series: pd.Series, expected: str) -> bool:
    if expected == "integer":
        return pd.api.types.is_integer_dtype(series)
    if expected == "float":
        return pd.api.types.is_float_dtype(series) or pd.api.types.is_integer_dtype(series)
    if expected == "string":
        return pd.api.types.is_string_dtype(series) or pd.api.types.is_object_dtype(series)
    if expected == "date":
        parsed = pd.to_datetime(series, errors="coerce")
        return parsed.notna().all()
    return True


def validate(df: pd.DataFrame, contract: dict) -> list[str]:
    errors: list[str] = []
    for col_spec in contract["schema"]:
        name = col_spec["name"]
        if name not in df.columns:
            if col_spec.get("required", False):
                errors.append(f"Missing required column: {name}")
            continue

        series = df[name]
        if col_spec.get("required") and series.isna().any():
            errors.append(f"{name} has null values")

        if not check_type(series, col_spec["type"]):
            errors.append(f"{name} failed type check: {col_spec['type']}")

        if "allowed_values" in col_spec:
            bad = set(series.dropna().unique()) - set(col_spec["allowed_values"])
            if bad:
                errors.append(f"{name} has disallowed values: {bad}")

        if col_spec.get("unique") and series.duplicated().any():
            errors.append(f"{name} is not unique")

        if "min_value" in col_spec and (series < col_spec["min_value"]).any():
            errors.append(f"{name} below min_value {col_spec['min_value']}")

    return errors


def main() -> None:
    contract = yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8"))
    df = pd.read_csv(ORDERS_PATH)
    errors = validate(df, contract)

    print(f"Contract: {contract['dataset']} {contract['version']}")
    if errors:
        print("CONTRACT VIOLATIONS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("Contract validation passed.")


if __name__ == "__main__":
    main()
