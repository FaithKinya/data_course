"""Solution: Exercise 1 — S3-style path helpers."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def s3_uri(bucket: str, key: str) -> str:
    return f"s3://{bucket}/{key.lstrip('/')}"


def partition_key(col: str, val: str) -> str:
    return f"{col}={val}"


def local_lake_path(
    root: Path,
    layer: str,
    table: str,
    partition_col: str,
    partition_val: str,
) -> Path:
    return root / "lake" / layer / table / partition_key(partition_col, partition_val)


def main() -> None:
    dates = ["2024-01-15", "2024-01-16"]
    for dt in dates:
        key = f"raw/orders/dt={dt}/part-0000.parquet"
        uri = s3_uri("shopstream-lake", key)
        local = local_lake_path(ROOT, "raw", "orders", "dt", dt)
        print(f"URI:  {uri}")
        print(f"Path: {local}")
        print()


if __name__ == "__main__":
    main()
