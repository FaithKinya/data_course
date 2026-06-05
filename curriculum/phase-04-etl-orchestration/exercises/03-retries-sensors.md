# Exercise 3: Retries & Sensors

**Time:** ~45 minutes

---

## Goal

Use a `FileSensor` and retry configuration in a realistic mini-pipeline.

---

## Tasks

Create `dags/ex03_sensor_dag.py`:

1. DAG `ex03_file_sensor`, manual trigger, `default_args` with `retries=2`, `retry_delay=1 minute`
2. `FileSensor` `wait_for_orders`:
   - Path: `/opt/airflow/shared/datasets/orders.csv`
   - `poke_interval=10`, `timeout=60`, `mode="reschedule"`
3. `PythonOperator` `validate_file` — checks file exists and has > 0 bytes
4. Chain: `wait_for_orders` → `validate_file`
5. Trigger DAG; confirm green run in UI

---

## Experiment

Temporarily point sensor to `/opt/airflow/shared/datasets/missing.csv`. Observe timeout behavior. **Revert** before continuing.

---

## Verify

Compare with [solutions/ex03_sensor_dag.py](solutions/ex03_sensor_dag.py).

**Next:** [Phase project →](../project/README.md)
