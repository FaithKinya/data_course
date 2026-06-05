# Lesson 3: DAG Best Practices

**Time:** ~50 minutes

---

## Keep DAGs thin

DAG file = wiring only. Business logic stays in `project/` modules.

```python
def run_extract(**context):
    from extract import extract_all
    extract_all()

PythonOperator(task_id="extract", python_callable=run_extract)
```

Testable Python functions; Airflow is just the scheduler.

---

## Naming and tags

- `dag_id`: `shopstream_daily_etl` — descriptive, snake_case
- `task_id`: verb_noun — `extract_orders`, `load_marts`
- `tags`: `["shopstream", "daily"]` — filter in UI

---

## Retries and timeouts

```python
default_args = {
    "owner": "data-eng",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(hours=1),
}
```

Retry **transient** failures (network blips). Don't retry bad data — fail and alert.

---

## Sensors: use wisely

`FileSensor` waits for `orders.csv`. Pitfalls:

- **Reschedule mode** — frees worker slot between pokes
- **Timeout** — fail after N hours, don't wait forever
- **poke_interval** — don't hammer NFS every 10s

For object storage, prefer object-key sensors or event-driven triggers (S3 → Lambda → Airflow).

---

## Idempotent backfills

`catchup=True` + date-partitioned loads = reprocess each `{{ ds }}` independently.

Use Airflow macros:

```python
bash_command="python pipeline.py --date {{ ds }}"
```

---

## Don't put secrets in DAGs

Use Airflow Connections / Variables or env vars from Docker secrets — never hardcode API keys.

---

## Production hygiene checklist

- [ ] `catchup` intentional
- [ ] `max_active_runs=1` for pipelines that can't overlap
- [ ] SLA or email on failure (`email_on_failure`)
- [ ] DAG docs string explains purpose and owner
- [ ] No top-level heavy imports or DB connections at parse time

---

## Reflection

1. Why set `max_active_runs=1` on ShopStream daily ETL?
2. When should retries be set to 0?

---

## Up next

[Exercise 1: Your first DAG →](../exercises/01-first-dag.md)
