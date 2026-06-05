"""Phase 1 project starter — fill in the TODOs."""

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from transforms import clean_orders, summarize_by_month_category

ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "shared" / "datasets"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def run() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "started",
    }

    try:
        orders_path = DATA_DIR / "orders.csv"
        if not orders_path.exists():
            raise FileNotFoundError(f"Missing input: {orders_path}")

        orders = pd.read_csv(orders_path)
        metadata["input_rows"] = len(orders)

        # TODO: clean, join products, summarize, write outputs
        products = pd.read_csv(DATA_DIR / "products.csv")
        cleaned = clean_orders(orders)
        enriched = cleaned.merge(
            products[["product_id", "category"]], on="product_id", how="left"
        )
        summary = summarize_by_month_category(enriched)

        cleaned.to_parquet(OUTPUT_DIR / "clean_orders.parquet", index=False)
        summary.to_csv(OUTPUT_DIR / "monthly_category_summary.csv", index=False)

        metadata["output_rows"] = len(cleaned)
        metadata["status"] = "success"
    except Exception as exc:
        metadata["status"] = "failed"
        metadata["error"] = str(exc)
        raise
    finally:
        (OUTPUT_DIR / "run_metadata.json").write_text(
            json.dumps(metadata, indent=2), encoding="utf-8"
        )


if __name__ == "__main__":
    run()
