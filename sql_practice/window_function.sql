-- Write your PostgreSQL query statement below A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

--Write a solution to find the employees who are high earners in each of the departments.

--Return the result table in any order.


select Department,Employee,Salary
from (
select d.name as department,e.name as employee,e.salary, DENSE_RANK() OVER (partition by d.name ORDER BY E.SALARY desc ) AS RN from employee e join department d on e.departmentid = d.id )
where rn <=3

