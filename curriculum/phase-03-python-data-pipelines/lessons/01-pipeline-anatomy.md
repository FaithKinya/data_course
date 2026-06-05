# Lesson 1: Pipeline Anatomy

**Time:** ~50 minutes

---

## What is a data pipeline?

A **pipeline** is automated code that moves data from A to B on a schedule (or continuously), applying rules along the way.

Batch pipeline skeleton:

```
extract → validate → transform → load → notify
```

Each stage should be **separately testable** — not one 400-line script.

---

## Separation of concerns

| Module | Responsibility |
|--------|----------------|
| `extract.py` | Read files, APIs, DB cursors |
| `validate.py` | Schema checks, business rules |
| `transform.py` | Clean, join, aggregate |
| `load.py` | Write to warehouse/lake |
| `pipeline.py` | Orchestrate + logging + metadata |

Analysts care about outputs; operators care about **metadata** (rows in/out, duration, status).

---

## Configuration over hardcoding

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATASETS = ROOT / "shared/datasets"
OUTPUT = ROOT / "curriculum/phase-03-python-data-pipelines/project/output"
```

Paths relative to repo root survive team clones. Use env vars for secrets, not CSV paths.

---

## Failure modes to design for

1. **Source file missing** — fail fast with clear message
2. **Partial write** — write to temp path, rename atomically
3. **Bad rows** — quarantine to `rejects/` instead of crashing silently
4. **Re-run** — same inputs → same outputs (idempotency)

---

## Metadata every run should emit

```json
{
  "run_id": "2024-01-20T08:00:00Z",
  "status": "success",
  "input_rows": 1500,
  "output_rows": 1487,
  "rejected_rows": 13
}
```

Finance and downstream teams use this for audits.

---

## Testing mindset

- Unit-test `transform.clean_orders(df)` with 5-row fixtures
- Integration-test full pipeline against `shared/datasets/`
- Compare output hash or row counts to golden files

---

## Reflection

1. Why is "validate before transform" better than "fix in transform"?
2. Sketch modules for the Phase 1 CSV pipeline — what would you rename?

---

## Up next

[Lesson 2: Ingestion patterns →](02-ingestion.md)
