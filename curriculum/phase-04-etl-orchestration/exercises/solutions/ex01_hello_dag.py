"""Solution: Exercise 1 — First Airflow DAG."""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="ex01_hello_shopstream",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["learning", "exercise-01"],
    doc_md="Print extract/transform/load steps in order.",
) as dag:
    extract = BashOperator(
        task_id="extract",
        bash_command='echo "EXTRACT: reading ShopStream CSVs"',
    )
    transform = BashOperator(
        task_id="transform",
        bash_command='echo "TRANSFORM: applying business rules"',
    )
    load = BashOperator(
        task_id="load",
        bash_command='echo "LOAD: writing Parquet marts"',
    )

    extract >> transform >> load
