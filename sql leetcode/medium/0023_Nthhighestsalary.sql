CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    --   select DISTINCT salary from employee order by salary DESC limit n - 1,1
    select salary from (
    select salary, DENSE_RANK() over (order by salary DESC) as rnk from Employee ) as t where n = t.rnk limit 1

  );
END