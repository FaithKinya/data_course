# Exercise 2: Pipeline Logging

**Time:** ~45 minutes

---

## Goal

Add structured JSON logging to a mini pipeline.

---

## Tasks

Create `exercises/my_work/02_pipeline_logging.py`:

1. Configure JSON logging to stdout
2. Simulate three stages: `extract`, `validate`, `load`
3. Each stage logs: `run_id`, `stage`, `duration_ms`, `row_count`
4. Write `exercises/my_work/output/run_log.jsonl` — one JSON object per line (duplicate of stdout)
5. Final line: `status=success` or `status=failed` if any stage raises

Inject a `--fail-validate` flag to test failure logging.

---

## Verify

Compare with [solutions/02_pipeline_logging.py](solutions/02_pipeline_logging.py).

**Next:** [Exercise 3: Data contracts](03-data-contracts.md)
