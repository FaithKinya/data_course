# Lesson 1: Why Orchestration?

**Time:** ~45 minutes

---

## The cron trap

```bash
0 2 * * * /usr/bin/python /pipelines/daily_etl.py
```

Works until:

- Extract succeeds, transform fails — load runs on stale data
- File arrives late — pipeline runs on empty folder
- Job takes 3 hours — overlapping runs corrupt output
- Something breaks at 2 AM — you find out at 9 AM from Finance

**Orchestration** adds dependencies, retries, monitoring, and backfill.

---

## What orchestrators provide

| Feature | Benefit |
|---------|---------|
| **DAG** | Define task order explicitly |
| **Retries** | Transient API failures self-heal |
| **Sensors** | Wait for files/events before proceeding |
| **UI / alerts** | See failures immediately |
| **Backfill** | Re-run historical date ranges |
| **SLAs** | Alert if job misses deadline |

Popular tools: **Apache Airflow**, Dagster, Prefect, Luigi. This course uses Airflow — largest job-market footprint.

---

## Orchestration vs execution

- **Orchestrator** — when and in what order tasks run
- **Execution engine** — Spark, Python, SQL, dbt

Airflow tasks often call `python pipeline.py` or `dbt run` — it doesn't replace your code.

---

## Idempotency + orchestration

Re-runs are normal (retries, backfills). Pipelines **must** be idempotent — Phase 3 prepared you for this.

---

## When cron is still fine

- Single script, no dependencies, failure is obvious
- Personal projects with manual triggers

Once you have 3+ dependent steps or stakeholders, upgrade.

---

## Reflection

1. What happens if your load task runs twice without idempotency?
2. Name a sensor you'd use for ShopStream CSV drops.

---

## Up next

[Lesson 2: Airflow concepts →](02-airflow-concepts.md)
