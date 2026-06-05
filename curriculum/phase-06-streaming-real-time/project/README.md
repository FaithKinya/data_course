# Phase 6 Project: Clickstream Aggregator

**Time:** 6–8 hours  
**Deliverable:** Kafka producer + streaming consumer with persistent aggregates

---

## Scenario

ShopStream's product team wants **near-real-time** page view counts by URL. Build a clickstream pipeline: simulate events, stream through Kafka, aggregate, and sink results.

---

## Requirements

### 1. Event producer `project/producer.py`

- Topic: `shopstream.clicks`
- Events: `page_view`, `add_to_cart` (mix both types)
- Fields: `event`, `user_id`, `page`, `product_id` (nullable), `ts` (UTC ISO)
- CLI: `python producer.py --count 100 --delay 0.1`

Derive some events from `shared/datasets/products.csv` pages like `/products/{product_id}`.

### 2. Stream aggregator `project/consumer.py`

- Consumer group: `shopstream-aggregator`
- Running totals: views per `page`
- 5-minute tumbling windows: count per `(window, page)`
- Flush snapshots every 30s to `project/output/aggregates.json`

### 3. Optional enrichment

Join `product_id` to product name from CSV for `/products/*` pages in printed output.

### 4. Documentation

README: start Kafka, run producer in one terminal, consumer in another.

---

## Step-by-step guide

### Step 1: Kafka up (30 min)

`docker compose up -d`; verify UI.

### Step 2: Producer (2 hr)

JSON schema, CLI args, realistic page mix.

### Step 3: Consumer (2.5 hr)

In-memory state + periodic file sink; graceful Ctrl+C handler.

### Step 4: Enrichment (1 hr)

Load products CSV once at startup.

### Step 5: Demo (1 hr)

Run 100 events; verify `aggregates.json` updates.

---

## Acceptance criteria

- [ ] Producer and consumer run against local Kafka
- [ ] `aggregates.json` contains `total_by_page` and `windowed` sections
- [ ] Consumer survives producer restart (continues from committed offset)
- [ ] README documents full workflow
- [ ] CHECKLIST.md complete

---

## What you learned

**Event-driven pipelines** complement batch ETL — same ShopStream data, different latency profile.

**Next phase:** [Phase 7: Cloud Data Engineering](../../phase-07-cloud-data-engineering/README.md)
