"""Solution: Exercise 2 — Parallel PythonOperators with join."""

from datetime import datetime

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

DATASETS = "/opt/airflow/shared/datasets"


def _count_rows(filename: str, key: str, **context) -> None:
    path = f"{DATASETS}/{filename}"
    n = len(pd.read_csv(path))
    context["ti"].xcom_push(key=key, value=n)
    print(f"{key}={n}")


def report_totals(**context) -> None:
    ti = context["ti"]
    orders = ti.xcom_pull(task_ids="count_orders", key="orders")
    customers = ti.xcom_pull(task_ids="count_customers", key="customers")
    products = ti.xcom_pull(task_ids="count_products", key="products")
    print(f"orders={orders} customers={customers} products={products}")


with DAG(
    dag_id="ex02_row_counts",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["learning", "exercise-02"],
) as dag:
    count_orders = PythonOperator(
        task_id="count_orders",
        python_callable=_count_rows,
        op_kwargs={"filename": "orders.csv", "key": "orders"},
    )
    count_customers = PythonOperator(
        task_id="count_customers",
        python_callable=_count_rows,
        op_kwargs={"filename": "customers.csv", "key": "customers"},
    )
    count_products = PythonOperator(
        task_id="count_products",
        python_callable=_count_rows,
        op_kwargs={"filename": "products.csv", "key": "products"},
    )
    report = PythonOperator(task_id="report_totals", python_callable=report_totals)

    [count_orders, count_customers, count_products] >> report
