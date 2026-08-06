# Write your MySQL query statement below
SELECT IFNULL((SELECT distinct Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1),NULL) AS SecondHighestSalary;   

#use sub query if you want to return "null" instead of empty
   

-- SELECT
-- (
--     SELECT MAX(Salary)
--     FROM Employee
--     WHERE Salary < (SELECT MAX(Salary) FROM Employee)
-- ) AS SecondHighestSalary;