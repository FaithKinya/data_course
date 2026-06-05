"""Solution: Exercise 3 — Idempotent Parquet load."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS_PATH = ROOT / "shared/datasets/orders.csv"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "my_work/output"

VALID_STATUSES = {"completed", "cancelled", "refunded"}


def validate_and_transform(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    mask = (
        df["order_id"].notna()
        & (df["quantity"] > 0)
        & (df["unit_price"] >= 0)
        & df["status"].isin(VALID_STATUSES)
    )
    valid = df[mask].copy()
    rejects = df[~mask].copy()
    base = valid["quantity"] * valid["unit_price"]
    valid["revenue"] = 0.0
    valid.loc[valid["status"] == "completed", "revenue"] = base
    valid.loc[valid["status"] == "refunded", "revenue"] = -base
    return valid, rejects


def atomic_parquet_write(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".parquet.tmp")
    df.to_parquet(tmp, index=False)
    tmp.replace(path)


def file_md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def run_pipeline() -> dict:
    orders = pd.read_csv(ORDERS_PATH)
    valid, rejects = validate_and_transform(orders)

    out_path = OUTPUT_DIR / "orders.parquet"
    atomic_parquet_write(valid, out_path)

    metadata = {
        "run_id": datetime.now(timezone.utc).isoformat(),
        "input_rows": len(orders),
        "valid_rows": len(valid),
        "reject_rows": len(rejects),
        "output_path": str(out_path.relative_to(ROOT)),
        "checksum": file_md5(out_path),
    }
    with open(OUTPUT_DIR / "run_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    return metadata


def main() -> None:
    meta1 = run_pipeline()
    meta2 = run_pipeline()
    print("Run 1 checksum:", meta1["checksum"])
    print("Run 2 checksum:", meta2["checksum"])
    assert meta1["checksum"] == meta2["checksum"], "Idempotency failed"
    print("Idempotent load verified.")


if __name__ == "__main__":
    main()
