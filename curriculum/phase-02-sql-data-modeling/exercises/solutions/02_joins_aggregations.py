"""Solution: Exercise 2 — JOINs and aggregations with DuckDB."""

from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[4]
ORDERS = str(ROOT / "shared/datasets/orders.csv")
CUSTOMERS = str(ROOT / "shared/datasets/customers.csv")
PRODUCTS = str(ROOT / "shared/datasets/products.csv")


def main() -> None:
    con = duckdb.connect()

    base_cte = f"""
    WITH base AS (
        SELECT
            o.order_id,
            o.order_date,
            o.status,
            o.quantity,
            o.unit_price,
            o.quantity * o.unit_price AS revenue,
            c.customer_id,
            c.name,
            c.country,
            p.category
        FROM read_csv_auto('{ORDERS}') o
        JOIN read_csv_auto('{CUSTOMERS}') c ON o.customer_id = c.customer_id
        JOIN read_csv_auto('{PRODUCTS}') p ON o.product_id = p.product_id
        WHERE o.status = 'completed'
    )
    """

    print("=== Task 1: revenue by country ===")
    print(
        con.sql(
            base_cte
            + """
            SELECT country, ROUND(SUM(revenue), 2) AS total_revenue
            FROM base
            GROUP BY country
            ORDER BY total_revenue DESC
            """
        ).df()
    )

    print("\n=== Task 2: revenue by category ===")
    print(
        con.sql(
            base_cte
            + """
            SELECT
                category,
                COUNT(*) AS order_count,
                ROUND(SUM(revenue), 2) AS total_revenue
            FROM base
            GROUP BY category
            ORDER BY total_revenue DESC
            """
        ).df()
    )

    print("\n=== Task 3: top customer per country ===")
    print(
        con.sql(
            base_cte
            + """
            , ranked AS (
                SELECT
                    country,
                    name,
                    ROUND(SUM(revenue), 2) AS total_revenue,
                    ROW_NUMBER() OVER (
                        PARTITION BY country ORDER BY SUM(revenue) DESC
                    ) AS rn
                FROM base
                GROUP BY country, name
            )
            SELECT country, name, total_revenue
            FROM ranked
            WHERE rn = 1
            ORDER BY total_revenue DESC
            """
        ).df()
    )

    print("\n=== Task 4: daily trend ===")
    print(
        con.sql(
            base_cte
            + """
            SELECT
                order_date,
                COUNT(*) AS order_count,
                ROUND(SUM(revenue), 2) AS total_revenue
            FROM base
            GROUP BY order_date
            ORDER BY order_date
            """
        ).df()
    )


if __name__ == "__main__":
    main()
