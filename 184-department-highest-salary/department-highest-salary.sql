select d.name as Department, e.name as Employee, e.salary as Salary
from Department d join Employee e
on e.departmentId = d.id
where (salary,departmentId) in (select max(salary), departmentId from Employee group by departmentId);