# Write your MySQL query statement 
select p.firstName,p.lastName,a.city,a.state from Person as p LEFT JOIN Address as a ON p.personID = a.personID