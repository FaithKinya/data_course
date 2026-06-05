# Data Engineering Glossary

Quick reference as you learn. Terms are introduced in order across phases.

| Term | Definition | First seen |
|------|------------|------------|
| **ETL** | Extract, Transform, Load — move and reshape data into a target system | Phase 1 |
| **ELT** | Extract, Load, Transform — load raw data first, transform in the warehouse | Phase 5 |
| **Pipeline** | Automated sequence of steps that moves/processes data | Phase 1 |
| **Batch** | Processing data in scheduled chunks (hourly, daily) | Phase 1 |
| **Streaming** | Processing events as they arrive in near real-time | Phase 6 |
| **Grain** | The level of detail one row represents (e.g. one order line) | Phase 2 |
| **Fact table** | Central table in a star schema with measurable metrics | Phase 2 |
| **Dimension table** | Descriptive attributes (customer, product, date) | Phase 2 |
| **Normalization** | Splitting data to reduce redundancy (3NF) | Phase 2 |
| **DAG** | Directed Acyclic Graph — workflow with dependencies, no cycles | Phase 4 |
| **Orchestration** | Scheduling and coordinating pipeline tasks | Phase 4 |
| **OLTP** | Online Transaction Processing — operational databases | Phase 5 |
| **OLAP** | Online Analytical Processing — analytics warehouses | Phase 5 |
| **dbt** | Data build tool — SQL transformations with tests | Phase 5 |
| **Incremental model** | Only process new/changed rows on each run | Phase 5 |
| **Topic** | Kafka channel where events are published | Phase 6 |
| **Partition** | Splitting storage by date/region for performance & cost | Phase 7 |
| **Data contract** | Agreed schema & quality rules between producer/consumer | Phase 8 |
| **Idempotent** | Running twice produces the same result (no duplicates) | Phase 3 |
