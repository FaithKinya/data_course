# Phase 8 Project: Production-Ready Pipeline

**Time:** 6–8 hours  
**Deliverable:** ShopStream ETL with GX validation, structured logs, data contract, and fail-fast gates

---

## Scenario

ShopStream is going live. Leadership requires **no bad data in marts**. Harden your batch pipeline with validation, observability, and a published data contract.

---

## Requirements

### 1. Project structure

```
project/
├── pipeline.py
├── validate.py          # GX + contract checks
├── logging_config.py    # JSON formatter
├── contracts/
│   └── orders_v1.yaml
├── expectations/        # optional saved GX suites
├── output/
├── logs/
└── README.md
```

### 2. Data contract

- `contracts/orders_v1.yaml` covering all order columns + SLA (`freshness_hours: 24`)
- `contracts/customers_v1.yaml` and `products_v1.yaml` (minimal)

### 3. Validation gate (`validate.py`)

- Load contract YAML
- Run Great Expectations (or equivalent checks) on each source **before** transform
- On failure: log structured error, write `output/quarantine/{dataset}_{run_id}.csv`, exit code 1
- On success: proceed to transform

### 4. Structured logging

- JSON logs to `logs/pipeline.jsonl`
- Every log line includes: `run_id`, `stage`, `timestamp`
- Stages: `extract`, `validate`, `transform`, `load`, `complete`

### 5. Pipeline behavior

- Read `shared/datasets/*.csv`
- Apply Phase 3 transform rules
- Write `output/marts/orders_enriched.parquet`
- Write `output/run_metadata.json` with validation results summary

### 6. CLI

```bash
python pipeline.py
python pipeline.py --dry-run   # validate only, no load
```

---

## Step-by-step guide

### Step 1: Contracts (1.5 hr)

Author YAML for three datasets; document versioning policy in README.

### Step 2: Validation module (2 hr)

Contract parser + GX expectations; quarantine path on failure.

### Step 3: Logging (1 hr)

`logging_config.py` with JsonFormatter; wire into pipeline.

### Step 4: Integrate (2 hr)

Fail-fast flow; dry-run mode for CI.

### Step 5: Test failure paths (1 hr)

Inject bad row; confirm exit 1, quarantine file, error logs.

---

## Acceptance criteria

- [ ] Valid data: pipeline succeeds, metadata + logs written
- [ ] Invalid `status` value: pipeline fails, quarantine created
- [ ] `--dry-run` validates without writing marts
- [ ] Logs are valid JSON lines queryable by `run_id`
- [ ] CHECKLIST.md complete

---

## What you learned

**Production data engineering** — quality gates, contracts, and observability that teams depend on.

**Graduation:** Complete both capstones in [PROGRESS.md](../../../PROGRESS.md).
