# Solution: Data Lifecycle Quiz

1. **Batch.** Source (ad platform) → ingest (nightly pull) → raw storage → transform (aggregate by campaign/day) → curated mart → serve (dashboard).

2. Raw data is your **source of truth** for replay. If transform logic changes or a bug corrupts curated tables, you can rebuild without re-fetching from vendors.

3. **Parquet** (or ORC). Columnar compression reduces size; analytics queries scan only needed columns.

4. **Ingestion** moves data into your system with minimal change. **Transformation** applies business rules, joins, cleaning, aggregations.

5. **Latency vs complexity.** Batch is simpler and cheaper but data is stale until the next run. Streaming or more frequent batch would reduce staleness at higher cost.
