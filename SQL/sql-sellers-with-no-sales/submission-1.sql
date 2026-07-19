SELECT seller_name
FROM seller
WHERE seller_id NOT IN (
    SELECT seller_id
    FROM orders
    WHERE sale_date >= '2020-01-01'
      AND sale_date < '2021-01-01'
)
ORDER BY seller_name;