-- Module 9 Challenge SQL query

CREATE TABLE Employees (
    emp_no VARCHAR NOT NULL,
    emp_title_id VARCHAR NOT NULL,
    birth_date VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    sex VARCHAR(1) NOT NULL,
    hire_date VARCHAR NOT NULL,
    PRIMARY KEY (emp_no)
);

select * from Employees;

CREATE TABLE Salaries (
    emp_no VARCHAR NOT NULL,
    salary VARCHAR NOT NULL
);

select * from Salaries;

CREATE TABLE Titles (
    title_id VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    PRIMARY KEY (title_id)
);

select * from Titles;

CREATE TABLE Managers (
    dept_no VARCHAR NOT NULL,
    emp_no VARCHAR NOT NULL
);

select * from Managers;

CREATE TABLE Departments (
    dept_no VARCHAR NOT NULL,
    dept_name VARCHAR NOT NULL,
    PRIMARY KEY (dept_no)
);

select * from Departments;

CREATE TABLE Departments_Employees (
    emp_no VARCHAR NOT NULL,
    dept_no VARCHAR NOT NULL
);

select * from Departments_Employees;


ALTER TABLE Employees ADD CONSTRAINT fk_Employees_emp_title_id FOREIGN KEY(emp_title_id)
REFERENCES Titles (title_id);

ALTER TABLE Salaries ADD CONSTRAINT fk_Salaries_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Managers ADD CONSTRAINT fk_Managers_dept_no FOREIGN KEY(dept_no)
REFERENCES Departments (dept_no);

ALTER TABLE Managers ADD CONSTRAINT fk_Managers_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Departments_Employees ADD CONSTRAINT fk_Departments_Employees_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Departments_Employees ADD CONSTRAINT fk_Departments_Employees_dept_no FOREIGN KEY(dept_no)
REFERENCES Departments (dept_no);

