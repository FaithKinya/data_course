# Lesson 2: The Data Lifecycle

**Time:** ~45 minutes

---

## The pipeline mental model

Every data system follows a similar flow:

```
Sources → Ingest → Raw Storage → Transform → Curated Storage → Serve
```

| Stage | What happens | Example |
|-------|--------------|---------|
| **Sources** | Data originates | App DB, SaaS API, CSV upload |
| **Ingest** | Copy into your system | Nightly dump, real-time stream |
| **Raw storage** | Keep original copy | S3 `raw/`, landing tables |
| **Transform** | Clean, join, business rules | dbt models, Spark jobs |
| **Curated** | Analytics-ready tables | `fct_orders`, `dim_customers` |
| **Serve** | Consumers use data | BI tool, ML feature store, API |

---

## Batch vs streaming (preview)

- **Batch:** Run every hour/day; process chunks of data. Simpler, cheaper.
- **Streaming:** Process events as they arrive. Lower latency, more complex.

Most companies use **both**. You'll go deep in Phases 4 and 6.

---

## Raw vs curated zones

**Lakehouse / medallion pattern** (common naming):

- **Bronze / Raw** — as-is from source, append-only
- **Silver / Cleaned** — validated, typed, deduplicated
- **Gold / Mart** — business metrics, star schemas

Never overwrite raw data. If transforms break, you can replay from raw.

---

## Metadata matters

Good pipelines track:

- When did this run?
- How many rows in / out?
- What schema version?
- Who owns this dataset?

You'll add logging in Phase 8.

---

## Key takeaway

Data engineering is not one script — it's a **system** with clear stages, ownership, and recovery paths.

---

## Up next

[Lesson 3: Data Formats & Storage →](03-data-formats.md)
