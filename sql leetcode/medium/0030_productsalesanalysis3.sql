# Write your MySQL query statement below
-- select product_id,MIN(year) as first_year, quantity,price from Sales group by product_id

SELECT s.product_id,
       s.year AS first_year,
       s.quantity,
       s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) first
ON s.product_id = first.product_id
AND s.year = first.first_year;