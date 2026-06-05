# Lesson 2: Airflow Concepts

**Time:** ~50 minutes

---

## Core vocabulary

| Term | Meaning |
|------|---------|
| **DAG** | Directed acyclic graph — your workflow definition |
| **Task** | One step in the DAG |
| **Operator** | Template for a task (Python, Bash, SQL) |
| **DagRun** | One execution of the DAG for a logical date |
| **TaskInstance** | One execution of a task within a DagRun |

DAGs are defined in Python files under `dags/`.

---

## Minimal DAG

```python
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_shopstream",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["learning"],
) as dag:
    greet = BashOperator(task_id="greet", bash_command='echo "Hello ShopStream"')
```

`catchup=False` prevents Airflow from firing 365 historical runs on first enable.

---

## Task dependencies

```python
extract >> transform >> load
# equivalent:
extract.set_downstream(transform)
transform.set_downstream(load)
```

Branches and parallel tasks:

```python
extract >> [validate_orders, validate_customers] >> transform
```

---

## Common operators

- `BashOperator` — shell commands
- `PythonOperator` — call a Python function
- `EmptyOperator` — marker / join point
- `FileSensor` — wait for file on disk

For production, prefer `PythonOperator` wrapping your Phase 3 modules over inline bash.

---

## Docker setup in this course

`docker-compose.yml` mounts:

- `./dags` → Airflow DAG folder
- `../../shared` → datasets at `/opt/airflow/shared/datasets/`
- `./project` → your ETL code

Paths inside containers differ from host — use `/opt/airflow/shared/datasets/orders.csv`.

---

## Scheduler loop (simplified)

1. Parse DAG files every ~30s
2. Create DagRuns for due schedules
3. Queue tasks whose upstreams succeeded
4. Worker/executor runs task; logs to UI

---

## Reflection

1. What does `start_date` control vs `schedule`?
2. Why keep DAG files free of heavy data processing logic?

---

## Up next

[Lesson 3: DAG best practices →](03-dag-best-practices.md)
