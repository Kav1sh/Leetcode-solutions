# Write your MySQL query statement below
-- SELECT s.*
-- FROM Stadium s
-- JOIN
-- (
--     select * from (select id,visit_date,people,lag(people,1) over(order by id)as prev1,lag(people,2) over(order by id) as prev2,lag(people,3) over(order by id) as prev3 from Stadium) as t WHERE people > 100
-- AND prev1 > 100
-- AND prev2 > 100
-- AND prev3 > 100 order by visit_date desc 
-- ) t
-- ON s.id BETWEEN t.id - 3 AND t.id
-- ORDER BY s.visit_date;

with temp as
(
    (SELECT
        *,
        LAG(people,1) OVER(ORDER BY id) AS prev1,
        LAG(people,2) OVER(ORDER BY id) AS prev2,
        LEAD(people,1) OVER(ORDER BY id) AS next1,
        LEAD(people,2) OVER(ORDER BY id) AS next2
    FROM Stadium) 
)

SELECT id, visit_date, people
FROM temp
WHERE people >= 100
AND
(
      (prev1 >= 100 AND prev2 >= 100)
   OR (prev1 >= 100 AND next1 >= 100)
   OR (next1 >= 100 