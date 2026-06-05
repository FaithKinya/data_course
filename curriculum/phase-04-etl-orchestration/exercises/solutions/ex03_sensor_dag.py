"""Solution: Exercise 3 — FileSensor with retries."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor

ORDERS_PATH = "/opt/airflow/shared/datasets/orders.csv"

default_args = {
    "owner": "learning",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


def validate_file(**context) -> None:
    from pathlib import Path

    path = Path(ORDERS_PATH)
    if not path.exists():
        raise FileNotFoundError(f"Missing: {path}")
    size = path.stat().st_size
    if size == 0:
        raise ValueError("orders.csv is empty")
    print(f"Validated {path} ({size} bytes)")


with DAG(
    dag_id="ex03_file_sensor",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["learning", "exercise-03"],
) as dag:
    wait_for_orders = FileSensor(
        task_id="wait_for_orders",
        filepath=ORDERS_PATH,
        poke_interval=10,
        timeout=60,
        mode="reschedule",
    )
    validate = PythonOperator(task_id="validate_file", python_callable=validate_file)

    wait_for_orders >> validate
