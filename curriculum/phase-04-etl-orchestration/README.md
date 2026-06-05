# Phase 4: ETL Orchestration

**Goal:** Schedule and monitor pipelines with Apache Airflow using Docker.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 3: Python Data Pipelines](../phase-03-python-data-pipelines/README.md)

---

## What You'll Learn

- Why orchestration beats cron + hope
- Airflow concepts: DAGs, operators, tasks, dependencies
- Running Airflow locally with Docker Compose
- Retries, sensors, and DAG best practices

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [Why orchestration?](lessons/01-why-orchestration.md) | 45 min |
| 2 | Lesson | [Airflow concepts](lessons/02-airflow-concepts.md) | 50 min |
| 3 | Lesson | [DAG best practices](lessons/03-dag-best-practices.md) | 50 min |
| 4 | Exercise | [Your first DAG](exercises/01-first-dag.md) | 45 min |
| 5 | Exercise | [Task dependencies](exercises/02-task-dependencies.md) | 45 min |
| 6 | Exercise | [Retries & sensors](exercises/03-retries-sensors.md) | 45 min |
| 7 | **Project** | [**Scheduled Daily Pipeline**](project/README.md) | 6–8 hrs |

---

## Local Airflow setup

From this phase directory:

```bash
docker compose up -d
```

Open http://localhost:8080 (default user: `airflow` / `airflow`).

See [docker-compose.yml](docker-compose.yml) for services and volume mounts.

---

## Phase Project Preview

Wrap your Phase 3 ETL in a daily Airflow DAG with task dependencies, retries, and a file sensor waiting for CSV drops.

---

## Success Criteria

Before moving to Phase 5, you should be able to:

- [ ] Explain DAG, task, and operator in your own words
- [ ] Start local Airflow with Docker Compose
- [ ] Trigger a DAG and read task logs in the UI
- [ ] Model extract → transform → load as separate tasks
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 5: Data Warehousing →](../phase-05-data-warehousing/README.md)
