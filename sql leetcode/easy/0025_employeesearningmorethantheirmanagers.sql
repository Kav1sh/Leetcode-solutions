# Write your MySQL query statement below

-- select a.name Employee from employee a 
-- where a.salary > (select salary from employee d where d.id = a.managerid) 
select e.name as Employee 
from Employee as e JOIN Employee as m on e.managerid=m.id 
where e.salary>m.salary