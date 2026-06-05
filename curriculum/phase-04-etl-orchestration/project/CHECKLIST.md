# Phase 4 Project Checklist

- [ ] `docker compose up -d` starts webserver and scheduler
- [ ] `shared/datasets` mounted at `/opt/airflow/shared/datasets`
- [ ] ETL modules live under `project/` with container-compatible paths
- [ ] DAG `shopstream_daily_etl` has all 6 tasks wired correctly
- [ ] FileSensor uses `mode="reschedule"` and reasonable timeout
- [ ] `max_active_runs=1` set on DAG
- [ ] Manual DAG run succeeds end-to-end
- [ ] Task logs visible in Airflow UI for each step
- [ ] XCom metadata includes row counts
- [ ] Project README explains Docker workflow
