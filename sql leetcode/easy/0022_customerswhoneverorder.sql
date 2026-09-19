# Write your MySQL query statement below
select name as Customers from Customers as c LEFT JOIN Orders as o ON c.id=o.customerId where c.id not in (select customerID from Orders)