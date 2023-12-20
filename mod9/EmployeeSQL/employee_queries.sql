select * from Employees;
select * from Salaries;
select * from Titles;
select * from Managers;
select * from Departments;
select * from Departments_Employees;

-- 1. List the employee number, last name, first name, sex, and salary of each employee.
select Employees.emp_no, 
	Employees.last_name,
	Employees.first_name,
	Employees.sex,
	salaries.salary
from Employees
INNER JOIN salaries ON
salaries.emp_no = Employees.emp_no;

-- 2. List the first name, last name, and hire date for the employees who were hired in 1986.
select Employees.first_name,
	Employees.last_name,
	Employees.hire_date
from Employees
INNER JOIN salaries ON
salaries.emp_no = Employees.emp_no
WHERE extract(year from to_date(employees.hire_date, 'MM/DD/YYYY')) = 1986;


-- 3. List the manager of each department along with their department number, 
-- department name, employee number, last name, and first name.
select managers.emp_no as Manager_emp_no,
	managers.dept_no,
	departments.dept_name,
	departments_employees.emp_no,
	Employees.emp_no,
	Employees.last_name,
	Employees.first_name
from managers
INNER JOIN departments_employees ON
managers.dept_no = departments_employees.dept_no
INNER JOIN departments ON
managers.dept_no = departments.dept_no
INNER JOIN employees ON
managers.emp_no = employees.emp_no;

	
-- 4. List the department number for each employee along with that employee’s employee number, 
-- last name, first name, and department name.
select departments.dept_no,
	Employees.emp_no,
	Employees.last_name,
	Employees.first_name,
	departments.dept_name
from Employees
INNER JOIN departments_employees ON
Employees.emp_no = departments_employees.emp_no
INNER JOIN departments ON
departments_employees.dept_no = departments.dept_no;

	
-- 5. List first name, last name, and sex of each employee whose first name is Hercules and
-- whose last name begins with the letter B.
select Employees.first_name,
	Employees.last_name,
	Employees.sex
from Employees
WHERE Employees.first_name = 'Hercules'
AND Employees.last_name LIKE 'B%';

-- 6. List each employee in the Sales department, including their employee number, last name, 
-- and first name.
select Employees.emp_no,
	Employees.last_name,
	Employees.first_name
from Employees
INNER JOIN departments_employees ON
Employees.emp_no = departments_employees.emp_no
INNER JOIN departments ON
departments_employees.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales';


-- 7. List each employee in the Sales and Development departments, including their employee number, 
-- last name, first name, and department name.
select Employees.emp_no,
	Employees.first_name,
	Employees.last_name,
	Departments.dept_name
from Employees
INNER JOIN departments_employees ON
Employees.emp_no = departments_employees.emp_no
INNER JOIN departments ON
departments_employees.dept_no = departments.dept_no
WHERE departments.dept_name = 'Sales'
OR departments.dept_name = 'Development';

-- 8. List the frequency counts, in descending order, of all the employee last names 
-- (that is, how many employees share each last name).
select last_name, COUNT(*)
FROM Employees
GROUP BY last_name
ORDER BY COUNT(*) DESC;
