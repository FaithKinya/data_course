-- Solution: customer dimension mart
-- models/marts/dim_customers.sql

select
    customer_id,
    name,
    email,
    city,
    country,
    cast(signup_date as date) as signup_date
from {{ ref('stg_customers') }}
