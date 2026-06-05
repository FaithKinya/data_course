# Phase 5 Project Checklist

- [ ] dbt project uses `dbt-duckdb` and `datasets_path` var
- [ ] Staging models for orders, customers, products
- [ ] `dim_customers` and `dim_products` built
- [ ] `fct_orders` has correct revenue logic
- [ ] `fct_revenue_daily` aggregates by date and category
- [ ] At least 5 generic tests defined in schema.yml
- [ ] Singular test for completed order revenue
- [ ] `dbt test` passes on clean data
- [ ] `dbt docs generate` produces manifest
- [ ] README explains profile setup and commands
