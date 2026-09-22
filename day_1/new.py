select * from employees;
+-------+---------+------------+----------+------------+
| EmpID | EmpName | Department | Salary   | HireDate   |
+-------+---------+------------+----------+------------+
|     1 | Alice   | HR         | 50000.00 | 2022-01-15 |
|     2 | Bob     | IT         | 75000.00 | 2021-06-20 |
|     3 | Charlie | Finance    | 70000.00 | 2023-03-10 |
|     4 | David   | IT         | 80000.00 | 2020-11-05 |
+-------+---------+------------+----------+------------+
4 rows in set (0.0014 sec)

describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(50)   | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | NULL    |       |
| Salary     | decimal(10,2) | YES  |     | NULL    |       |
| HireDate   | date          | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0106 sec)

describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(50)   | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | NULL    |       |
| Salary     | decimal(10,2) | YES  |     | NULL    |       |
| HireDate   | date          | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+

describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(50)   | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | NULL    |       |
| Salary     | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0037 sec)

describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | NULL    |       |
| Salary     | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0029 sec)

 describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | NULL    |       |
| BaseSalary | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0029 sec)

 describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | General |       |
| BaseSalary | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0171 sec)

 describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | General |       |
| BaseSalary | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0171 sec)

describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | General |       |
| BaseSalary | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0035 sec)

 describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| EmpID      | int           | NO   | PRI | NULL    |       |
| EmpName    | varchar(100)  | YES  |     | NULL    |       |
| Department | varchar(50)   | YES  |     | General |       |
| BaseSalary | decimal(10,2) | YES  |     | NULL    |       |
| Email      | varchar(100)  | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.0021 sec)

Empty set (0.0007 sec)

select * from employees;
+-------+---------+------------+------------+------------+
| EmpID | EmpName | Department | BaseSalary | Email      |
+-------+---------+------------+------------+------------+
|     1 | Alice   | HR         |   50000.00 | 2022-01-15 |
|     2 | Bob     | IT         |   75000.00 | 2021-06-20 |
|     3 | Charlie | Finance    |   70000.00 | 2023-03-10 |
|     4 | David   | IT         |   80000.00 | 2020-11-05 |
+-------+---------+------------+------------+------------+
4 rows in set (0.0012 sec)

select * from employees;
+-------+---------+------------+------------+------------+
| EmpID | EmpName | Department | BaseSalary | Email      |
+-------+---------+------------+------------+------------+
|     2 | Bob     | IT         |   75000.00 | 2021-06-20 |
|     3 | Charlie | Finance    |   70000.00 | 2023-03-10 |
|     4 | David   | IT         |   80000.00 | 2020-11-05 |
+-------+---------+------------+------------+------------+


select * from employees;
+-------+---------+------------+------------+------------+
| EmpID | EmpName | Department | BaseSalary | Email      |
+-------+---------+------------+------------+------------+
|     2 | Bob     | IT         |   75000.00 | 2021-06-20 |
|     3 | Charlie | Finance    |   70000.00 | 2023-03-10 |
+-------+---------+------------+------------+------------+
2 rows in set (0.0011 sec)

 select * from employees;
Empty set (0.0194 sec)

select * from employees;
ERROR: 1146 (42S02): Table 'd18r.employees' doesn't exist



Ravi
Siva
Anil
Priya
Kiran
Meena
Rahul
Sneha
Arjun