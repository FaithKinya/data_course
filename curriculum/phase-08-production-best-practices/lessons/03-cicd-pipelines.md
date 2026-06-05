# Lesson 3: CI/CD for Pipelines

**Time:** ~50 minutes

---

## Pipeline code is production code

Treat `pipeline.py` like application code:

- Version control (git)
- Code review (PRs)
- Automated tests (CI)
- Controlled deploys (CD)

---

## CI checks for data projects

```yaml
# .github/workflows/ci.yml (conceptual)
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest tests/
      - run: python -m compileall curriculum/
```

Add:

- `pytest` on transform functions
- `sqlfluff lint` on dbt models
- `dbt run --select staging` on sample data in CI

---

## Testing pyramid for DE

| Level | Example |
|-------|---------|
| **Unit** | `clean_orders()` drops cancelled |
| **Integration** | Full pipeline on fixture CSVs |
| **Data diff** | Compare output to golden Parquet |

Fast unit tests run every commit; integration nightly.

---

## Environments

```
dev → staging → prod
```

- **Dev** — your laptop, sample data
- **Staging** — prod-like Airflow + masked data
- **Prod** — scheduled, monitored, change-controlled

Never test schema changes directly in prod.

---

## Data contracts in CI

Store `contracts/orders.yaml` in git. CI validates:

1. Producer output matches contract schema
2. Breaking changes require version bump

Consumers trust `orders.v1` until `orders.v2` is announced.

---

## Deployment patterns

- **Airflow** — sync `dags/` to S3 or git-sync sidecar
- **dbt** — `dbt run` in CI staging; prod via tagged release
- **Containers** — build image in CI, deploy to ECS/K8s

---

## Reflection

1. What should block a merge to main?
2. How do data contracts differ from unit tests?

---

## Up next

[Exercise 1: Great Expectations intro →](../exercises/01-great-expectations.md)
