SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY c.customer_name;