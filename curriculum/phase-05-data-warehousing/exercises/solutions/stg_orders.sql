-- Solution: staging model for orders
-- Place in models/staging/stg_orders.sql

with source as (
    select * from read_csv_auto('{{ var("datasets_path") }}/orders.csv')
),

renamed as (
    select
        cast(order_id as integer) as order_id,
        cast(customer_id as integer) as customer_id,
        cast(product_id as integer) as product_id,
        cast(order_date as date) as order_date,
        cast(quantity as integer) as quantity,
        cast(unit_price as double) as unit_price,
        lower(cast(status as varchar)) as status
    from source
)

select * from renamed
