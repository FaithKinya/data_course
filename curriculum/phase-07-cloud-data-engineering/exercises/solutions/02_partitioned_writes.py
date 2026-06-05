"""Solution: Exercise 2 — Hive-partitioned Parquet writes."""

import json
from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS = ROOT / "shared/datasets/orders.csv"
LAKE = Path(__file__).resolve().parent.parent / "my_work/lake/raw/orders"


def write_partitions(df: pd.DataFrame, lake_root: Path) -> dict:
    df = df.copy()
    df["dt"] = pd.to_datetime(df["order_date"]).dt.strftime("%Y-%m-%d")
    manifest: dict[str, int] = {}

    for dt, group in df.groupby("dt"):
        out_dir = lake_root / f"dt={dt}"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "part-0000.parquet"
        group.drop(columns=["dt"]).to_parquet(out_file, index=False)
        manifest[f"dt={dt}"] = len(group)

    manifest_path = lake_root / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    orders = pd.read_csv(ORDERS, parse_dates=["order_date"])
    manifest = write_partitions(orders, LAKE)
    print("Manifest:", manifest)

    sample_dt = next(iter(manifest))
    glob = str(LAKE / f"{sample_dt}" / "*.parquet")
    n = duckdb.sql(f"SELECT COUNT(*) FROM read_parquet('{glob}')").fetchone()[0]
    print(f"Rows in {sample_dt}: {n}")


if __name__ == "__main__":
    main()
