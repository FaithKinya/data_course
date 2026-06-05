# Phase 1 Project: Local CSV Pipeline

**Time:** 4–6 hours  
**Deliverable:** A small Python pipeline + short README you can put on GitHub

---

## Scenario

You're the new data engineer at **ShopStream**, a small e-commerce company. Finance needs a daily summary of order revenue by month. IT gives you CSV exports — no database access yet.

Build a pipeline that ingests orders, cleans them, and produces analytics-ready outputs.

---

## Requirements

### 1. Extract
- Read `shared/datasets/orders.csv`
- Log row count on ingest

### 2. Transform
- Apply the same rules as [Exercise 3](../exercises/03-first-transform.md)
- Join `product_id` to `shared/datasets/products.csv` to add `category`
- Aggregate: total revenue and order count **by** `order_month` and `category`

### 3. Load
Write to `curriculum/phase-01-foundations/project/output/`:
- `clean_orders.parquet` — row-level cleaned data
- `monthly_category_summary.csv` — aggregated report
- `run_metadata.json` — `run_timestamp`, `input_rows`, `output_rows`, `status`

### 4. Structure
```
project/
├── README.md          # you write: how to run, what it does
├── pipeline.py        # main entry point
├── transforms.py      # clean + aggregate functions
├── CHECKLIST.md       # mark items done
└── output/            # generated (gitignored)
```

---

## Step-by-step guide

### Step 1: Scaffold (30 min)
Copy patterns from exercise solutions. Create `transforms.py` with `clean_orders()` and `summarize_by_month_category()`.

### Step 2: Build pipeline.py (1 hr)
Chain: load → clean → join products → summarize → write outputs.

### Step 3: Add metadata (30 min)
Use `datetime.utcnow().isoformat()` and row counts in `run_metadata.json`.

### Step 4: Error handling (45 min)
- Fail clearly if input file missing
- Use `try/except` around write step; set `status: failed` in metadata on error

### Step 5: Document (45 min)
Your project README should include: purpose, how to run, sample output screenshot or table.

### Step 6: Review CHECKLIST.md

---

## Acceptance criteria

- [ ] `python pipeline.py` runs without errors from project folder
- [ ] Parquet and CSV outputs match expected business rules
- [ ] Cancelled orders excluded from revenue
- [ ] Refunded orders count as negative revenue
- [ ] `run_metadata.json` written every run

---

## Starter code

See [starter/](starter/) for skeleton files. **Try building from scratch first** — use starter only if stuck after 45 minutes.

---

## What you learned

You built a miniature **medallion** flow: raw CSV → cleaned table → gold summary. Phases 2–8 scale this pattern to SQL, orchestration, and the cloud.

**Next phase:** [Phase 2: SQL & Data Modeling](../../phase-02-sql-data-modeling/README.md)
