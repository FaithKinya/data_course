"""Solution: Exercise 3 — Small files vs partitioned layout."""

import time
from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
ORDERS = ROOT / "shared/datasets/orders.csv"
BASE = Path(__file__).resolve().parent.parent / "my_work/lake"


def timed_read(glob: str) -> float:
    start = time.perf_counter()
    duckdb.sql(f"SELECT COUNT(*) FROM read_parquet('{glob}')").fetchone()
    return time.perf_counter() - start


def main() -> None:
    df = pd.read_csv(ORDERS, parse_dates=["order_date"])
    subset = df[df["order_date"] == "2024-01-15"].copy()

    bad_dir = BASE / "bad/orders/dt=2024-01-15"
    bad_dir.mkdir(parents=True, exist_ok=True)
    for _, row in subset.iterrows():
        row.to_frame().T.to_parquet(bad_dir / f"row-{row['order_id']}.parquet", index=False)

    good_dir = BASE / "good/orders/dt=2024-01-15"
    good_dir.mkdir(parents=True, exist_ok=True)
    subset.to_parquet(good_dir / "part-0000.parquet", index=False)

    bad_glob = str(bad_dir / "*.parquet")
    good_glob = str(good_dir / "*.parquet")

    bad_time = timed_read(bad_glob)
    good_time = timed_read(good_glob)

    all_glob = str(BASE / "good/orders/dt=*/*.parquet")
    one_glob = str(BASE / "good/orders/dt=2024-01-15/*.parquet")
    all_rows = duckdb.sql(f"SELECT COUNT(*) FROM read_parquet('{all_glob}', hive_partitioning=true)").fetchone()[0]
    one_rows = duckdb.sql(f"SELECT COUNT(*) FROM read_parquet('{one_glob}')").fetchone()[0]

    print(f"Bad layout read time:  {bad_time:.4f}s ({len(list(bad_dir.glob('*.parquet')))} files)")
    print(f"Good layout read time: {good_time:.4f}s (1 file)")
    print(f"All partitions rows: {all_rows}; single partition rows: {one_rows}")
    print("Summary: fewer larger files + partition filters reduce metadata overhead and bytes scanned.")


if __name__ == "__main__":
    main()
