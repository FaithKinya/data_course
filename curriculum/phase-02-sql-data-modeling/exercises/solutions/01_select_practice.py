"""Solution: Exercise 1 — SELECT practice with DuckDB."""

from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[4]
ORDERS = str(ROOT / "shared/datasets/orders.csv")


def main() -> None:
    con = duckdb.connect()

    print("=== Task 1: counts ===")
    print(
        con.sql(
            f"""
            SELECT
                COUNT(*) AS row_count,
                COUNT(DISTINCT customer_id) AS distinct_customers
            FROM read_csv_auto('{ORDERS}')
            """
        ).df()
    )

    print("\n=== Task 2: refunded orders ===")
    print(
        con.sql(
            f"""
            SELECT
                order_id,
                customer_id,
                ROUND(quantity * unit_price, 2) AS revenue
            FROM read_csv_auto('{ORDERS}')
            WHERE status = 'refunded'
            """
        ).df()
    )

    print("\n=== Task 3: top 3 customers by completed revenue ===")
    print(
        con.sql(
            f"""
            SELECT
                customer_id,
                ROUND(SUM(quantity * unit_price), 2) AS total_revenue
            FROM read_csv_auto('{ORDERS}')
            WHERE status = 'completed'
            GROUP BY customer_id
            ORDER BY total_revenue DESC
            LIMIT 3
            """
        ).df()
    )

    print("\n=== Task 4: orders per status ===")
    print(
        con.sql(
            f"""
            SELECT status, COUNT(*) AS order_count
            FROM read_csv_auto('{ORDERS}')
            GROUP BY status
            ORDER BY order_count DESC
            """
        ).df()
    )


if __name__ == "__main__":
    main()
