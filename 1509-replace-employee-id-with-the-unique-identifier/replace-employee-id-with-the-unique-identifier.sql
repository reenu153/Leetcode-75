# Write your MySQL query statement below
select name, unique_id from Employees E left join EmployeeUNI U on E.id=U.id 