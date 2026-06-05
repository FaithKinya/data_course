# Phase 7: Cloud Data Engineering

**Goal:** Model cloud storage patterns locally — S3-style paths, partitioning, and lake layouts.

**Time:** ~1–2 weeks (10–14 hours)

**Prerequisites:** [Phase 6: Streaming & Real-Time](../phase-06-streaming-real-time/README.md)

---

## What You'll Learn

- Cloud DE landscape (AWS-centric concepts portable to GCP/Azure)
- Object storage URIs and hive-style partitioning
- Partitioned Parquet writes for query pruning
- Cost awareness: list vs scan, small files problem

---

## Learning Path

Complete in order:

| # | Type | Item | Time |
|---|------|------|------|
| 1 | Lesson | [Cloud DE landscape](lessons/01-cloud-landscape.md) | 45 min |
| 2 | Lesson | [Object storage patterns](lessons/02-object-storage.md) | 50 min |
| 3 | Lesson | [Managed warehouses](lessons/03-managed-warehouses.md) | 50 min |
| 4 | Exercise | [S3-style paths](exercises/01-s3-paths.md) | 30 min |
| 5 | Exercise | [Partitioned writes](exercises/02-partitioned-writes.md) | 45 min |
| 6 | Exercise | [Cost awareness](exercises/03-cost-awareness.md) | 30 min |
| 7 | **Project** | [**Cloud-Native Batch Load**](project/README.md) | 6–8 hrs |

---

## Phase Project Preview

Build a local "data lake" under `project/lake/` mirroring `s3://shopstream-lake/raw/orders/dt=YYYY-MM-DD/` layout, with partitioned Parquet and a manifest.

---

## Success Criteria

Before moving to Phase 8, you should be able to:

- [ ] Explain `s3://bucket/prefix/partition=value/` structure
- [ ] Write hive-partitioned Parquet from Python
- [ ] Query only relevant partitions with DuckDB
- [ ] Articulate list vs scan cost tradeoffs
- [ ] Complete the phase project checklist

---

## Next Phase

[Phase 8: Production & Pro Practices →](../phase-08-production-best-practices/README.md)
