# Lesson 1: What is Data Engineering?

**Time:** ~45 minutes

---

## The problem data engineers solve

Companies generate data everywhere: app clicks, payments, support tickets, sensors. That data is messy, scattered, and often unusable for decisions.

**Data engineers build the plumbing** that collects, cleans, organizes, and delivers data so analysts, scientists, and products can trust it.

---

## DE vs DS vs Analytics

| Role | Primary question | Typical output |
|------|------------------|----------------|
| **Data Engineer** | How do we reliably move and store data? | Pipelines, warehouses, lakes |
| **Data Analyst** | What happened in the business? | Dashboards, reports |
| **Data Scientist** | What will happen / what should we do? | Models, experiments |

You don't need to be a data scientist to be a great data engineer. Strong SQL, Python, and systems thinking matter more.

---

## Core responsibilities

1. **Ingestion** — Pull data from APIs, databases, files, streams
2. **Storage** — Lakes, warehouses, databases (right tool for the job)
3. **Transformation** — Clean, join, aggregate, model
4. **Orchestration** — Schedule and monitor pipelines
5. **Quality & governance** — Tests, documentation, access control

---

## A day in the life (simplified)

- Morning: Check if last night's pipelines succeeded; fix a failed DAG
- Midday: Design schema for a new product event stream
- Afternoon: Pair with analyst on a slow dashboard query
- End of day: Review PR for a new dbt model

---

## Tools you'll meet in this course

- **Python + pandas** — glue for small/medium pipelines
- **SQL** — the language of data transformation
- **Airflow** — workflow scheduling
- **dbt** — warehouse transformations
- **Kafka** — event streaming
- **Cloud storage** — S3-style patterns

---

## Reflection (write in your notes)

1. Why might a company hire a data engineer before a data scientist?
2. Name one data source you've used (spreadsheet, app, website) — where would it enter a pipeline?

---

## Up next

[Lesson 2: Data Lifecycle →](02-data-lifecycle.md)
