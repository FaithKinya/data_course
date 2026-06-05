# Exercise 1: Your First DAG

**Time:** ~45 minutes

---

## Goal

Create a minimal Airflow DAG and run it in the local Docker environment.

---

## Prerequisites

```bash
cd curriculum/phase-04-etl-orchestration
docker compose up -d
```

Wait for http://localhost:8080 to load. Login: `airflow` / `airflow`.

---

## Tasks

1. Create `curriculum/phase-04-etl-orchestration/dags/ex01_hello_dag.py`
2. DAG `ex01_hello_shopstream`:
   - Schedule: `@daily`
   - `catchup=False`
   - Three `BashOperator` tasks printing: extract, transform, load
   - Dependency chain: extract → transform → load
3. Unpause the DAG in the UI and trigger a manual run
4. Screenshot or note which task logs show success

---

## Verify

Compare with [solutions/ex01_hello_dag.py](solutions/ex01_hello_dag.py).

---

## Troubleshooting

- DAG not appearing? Check `dags/` mount and Airflow scheduler logs: `docker compose logs airflow-scheduler`
- Import errors? Keep DAG file simple — no pandas at module top level

**Next:** [Exercise 2: Task dependencies](02-task-dependencies.md)
