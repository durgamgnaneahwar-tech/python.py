select * from employee_details;
+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai   |          5 |    NULL |
|    103 | Anil     |  32 | 60000.00 | Finance    | Delhi     |          8 | 8000.00 |
|    104 | Priya    |  26 | 40000.00 | IT         | Mumbai    |          3 | 3000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai    |          5 |    NULL |
+--------+----------+-----+----------+------------+-----------+------------+---------+
10 rows in set (0.0010 sec)

 select emp_name,salary+50000 as updated_salary  from employee_details;
+----------+----------------+
| emp_name | updated_salary |
+----------+----------------+
| Ravi     |       85000.00 |
| Siva     |       95000.00 |
| Anil     |      110000.00 |
| Priya    |       90000.00 |
| Kiran    |      120000.00 |
| Meena    |      105000.00 |
| Rahul    |       80000.00 |
| Sneha    |       98000.00 |
| Arjun    |      115000.00 |
| Pooja    |      100000.00 |
+----------+----------------+
10 rows in set (0.0055 sec)

 select emp_name , salary-2000 from employee_details;
+----------+-------------+
| emp_name | salary-2000 |
+----------+-------------+
| Ravi     |    33000.00 |
| Siva     |    43000.00 |
| Anil     |    58000.00 |
| Priya    |    38000.00 |
| Kiran    |    68000.00 |
| Meena    |    53000.00 |
| Rahul    |    28000.00 |
| Sneha    |    46000.00 |
| Arjun    |    63000.00 |
| Pooja    |    48000.00 |
+----------+-------------+
10 rows in set (0.0009 sec)

select emp_name , (salary*12)/2 from employee_details;
+----------+---------------+
| emp_name | (salary*12)/2 |
+----------+---------------+
| Ravi     | 210000.000000 |
| Siva     | 270000.000000 |
| Anil     | 360000.000000 |
| Priya    | 240000.000000 |
| Kiran    | 420000.000000 |
| Meena    | 330000.000000 |
| Rahul    | 180000.000000 |
| Sneha    | 288000.000000 |
| Arjun    | 390000.000000 |
| Pooja    | 300000.000000 |
+----------+---------------+
10 rows in set (0.0006 sec)

 select emp_name , (salary*12) from employee_details;
+----------+-------------+
| emp_name | (salary*12) |
+----------+-------------+
| Ravi     |   420000.00 |
| Siva     |   540000.00 |
| Anil     |   720000.00 |
| Priya    |   480000.00 |
| Kiran    |   840000.00 |
| Meena    |   660000.00 |
| Rahul    |   360000.00 |
| Sneha    |   576000.00 |
| Arjun    |   780000.00 |
| Pooja    |   600000.00 |
+----------+-------------+
10 rows in set (0.0006 sec)

 select emp_name , (salary/2)from employee_details;
+----------+--------------+
| emp_name | (salary/2)   |
+----------+--------------+
| Ravi     | 17500.000000 |
| Siva     | 22500.000000 |
| Anil     | 30000.000000 |
| Priya    | 20000.000000 |
| Kiran    | 35000.000000 |
| Meena    | 27500.000000 |
| Rahul    | 15000.000000 |
| Sneha    | 24000.000000 |
| Arjun    | 32500.000000 |
| Pooja    | 25000.000000 |
+----------+--------------+
10 rows in set (0.0006 sec)


 select emp_name , (salary%1000) from employee_details;
+----------+---------------+
| emp_name | (salary%1000) |
+----------+---------------+
| Ravi     |          0.00 |
| Siva     |          0.00 |
| Anil     |          0.00 |
| Priya    |          0.00 |
| Kiran    |          0.00 |
| Meena    |          0.00 |
| Rahul    |          0.00 |
| Sneha    |          0.00 |
| Arjun    |          0.00 |
| Pooja    |          0.00 |
+----------+---------------+
10 rows in set (0.0014 sec)

select emp_name , age+5 as updated_age from employee_details;
+----------+-------------+
| emp_name | updated_age |
+----------+-------------+
| Ravi     |          30 |
| Siva     |          33 |
| Anil     |          37 |
| Priya    |          31 |
| Kiran    |          40 |
| Meena    |          35 |
| Rahul    |          29 |
| Sneha    |          32 |
| Arjun    |          36 |
| Pooja    |          34 |
+----------+-------------+

+----------+-------+
| emp_name | age-1 |
+----------+-------+
| Ravi     |    24 |
| Siva     |    27 |
| Anil     |    31 |
| Priya    |    25 |
| Kiran    |    34 |
| Meena    |    29 |
| Rahul    |    23 |
| Sneha    |    26 |
| Arjun    |    30 |
| Pooja    |    28 |
+----------+-------+

+----------+----------+
| emp_name | bonus*2  |
+----------+----------+
| Ravi     | 10000.00 |
| Siva     |     NULL |
| Anil     | 16000.00 |
| Priya    |  6000.00 |
| Kiran    | 18000.00 |
| Meena    |     NULL |
| Rahul    |  4000.00 |
| Sneha    |  8000.00 |
| Arjun    | 14000.00 |
| Pooja    |     NULL |
+----------+----------+

+----------+--------------+
| emp_name | total_salary |
+----------+--------------+
| Ravi     |     40000.00 |
| Siva     |         NULL |
| Anil     |     68000.00 |
| Priya    |     43000.00 |
| Kiran    |     79000.00 |
| Meena    |         NULL |
| Rahul    |     32000.00 |
| Sneha    |     52000.00 |
| Arjun    |     72000.00 |
| Pooja    |         NULL |
+----------+--------------+

+----------+--------------+
| emp_name | total_salary |
+----------+--------------+
| Ravi     |     40000.00 |
| Siva     |         NULL |
| Anil     |     68000.00 |
| Priya    |     43000.00 |
| Kiran    |     79000.00 |
| Meena    |         NULL |
| Rahul    |     32000.00 |
| Sneha    |     52000.00 |
| Arjun    |     72000.00 |
| Pooja    |         NULL |
+----------+--------------+

+----------+----------------+
| emp_name | age+experience |
+----------+----------------+
| Ravi     |             27 |
| Siva     |             33 |
| Anil     |             40 |
| Priya    |             29 |
| Kiran    |             45 |
| Meena    |             36 |
| Rahul    |             25 |
| Sneha    |             31 |
| Arjun    |             38 |
| Pooja    |             34 |
+----------+----------------+

+----------+
| emp_name |
+----------+
| Pooja    |
+----------+
1 row in set (0.0010 sec)

 select * from employee_details where salary!=50000;
+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai   |          5 |    NULL |
|    103 | Anil     |  32 | 60000.00 | Finance    | Delhi     |          8 | 8000.00 |
|    104 | Priya    |  26 | 40000.00 | IT         | Mumbai    |          3 | 3000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
+--------+----------+-----+----------+------------+-----------+------------+---------+
9 rows in set (0.0005 sec)

+----------+
| emp_name |
+----------+
| Ravi     |
| Siva     |
| Anil     |
| Priya    |
| Kiran    |
| Meena    |
| Rahul    |
| Sneha    |
| Arjun    |
+----------+


+----------+
| emp_name |
+----------+
| Siva     |
| Anil     |
| Kiran    |
| Meena    |
| Rahul    |
| Sneha    |
| Pooja    |
+----------+

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai   |          5 |    NULL |
|    103 | Anil     |  32 | 60000.00 | Finance    | Delhi     |          8 | 8000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai    |          5 |    NULL |
+--------+----------+-----+----------+------------+-----------+------------+---------+

select * from employee_details where age>30;
+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    103 | Anil     |  32 | 60000.00 | Finance    | Delhi     |          8 | 8000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
+--------+----------+-----+----------+------------+-----------+------------+---------+
3 rows in set (0.0010 sec)

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    104 | Priya    |  26 | 40000.00 | IT         | Mumbai    |          3 | 3000.00 |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
+--------+----------+-----+----------+------------+-----------+------------+---------+

+----------+
| emp_name |
+----------+
| Siva     |
| Anil     |
| Kiran    |
| Meena    |
| Arjun    |
| Pooja    |
+----------+

+----------+
| emp_name |
+----------+
| Ravi     |
| Siva     |
| Priya    |
| Rahul    |
| Sneha    |
+----------+

+----------+
| emp_name |
+----------+
| Ravi     |
| Kiran    |
+----------+

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
+--------+----------+-----+----------+------------+-----------+------------+---------+

+----------+
| emp_name |
+----------+
| Anil     |
+----------+

+----------+
| emp_name |
+----------+
| Meena    |
| Rahul    |
| Sneha    |
| Arjun    |
| Pooja    |
+----------+


+----------+
| emp_name |
+----------+
| Ravi     |
| Priya    |
| Arjun    |
+----------+

+----------+
| emp_name |
+----------+
| Rahul    |
+----------+

+--------+----------+-----+----------+------------+---------+------------+-------+
| emp_id | emp_name | age | salary   | department | city    | experience | bonus |
+--------+----------+-----+----------+------------+---------+------------+-------+
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai |          5 |  NULL |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai  |          5 |  NULL |
+--------+----------+-----+----------+------------+---------+------------+-------+

+----------+
| emp_name |
+----------+
| Siva     |
| Anil     |
| Meena    |
| Sneha    |
+----------+

+----------+
| emp_name |
+----------+
| Anil     |
| Priya    |
| Sneha    |
| Pooja    |
+----------+

+----------+
| emp_name |
+----------+
| Ravi     |
| Kiran    |
| Rahul    |
+----------+

+----------+
| emp_name |
+----------+
| Siva     |
| Anil     |
| Kiran    |
| Meena    |
| Rahul    |
| Sneha    |
| Pooja    |
+----------+

| emp_name |
+----------+
| Siva     |
| Anil     |
| Kiran    |
| Meena    |
| Rahul    |
| Sneha    |
| Pooja    |
+----------+

+----------+
| emp_name |
+----------+
| Siva     |
| Anil     |
| Kiran    |
| Meena    |
| Rahul    |
| Sneha    |
| Pooja    |
+----------+

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai   |          5 |    NULL |
|    104 | Priya    |  26 | 40000.00 | IT         | Mumbai    |          3 | 3000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai    |          5 |    NULL |
+--------+----------+-----+----------+------------+-----------+------------+---------+
9 rows in set (0.0012 sec)

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    101 | Ravi     |  25 | 35000.00 | IT         | Hyderabad |          2 | 5000.00 |
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai   |          5 |    NULL |
|    104 | Priya    |  26 | 40000.00 | IT         | Mumbai    |          3 | 3000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    107 | Rahul    |  24 | 30000.00 | Sales      | Chennai   |          1 | 2000.00 |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai    |          5 |    NULL |
+--------+----------+-----+----------+------------+-----------+------------+---------+

+--------+----------+-----+----------+------------+---------+------------+---------+
| emp_id | emp_name | age | salary   | department | city    | experience | bonus   |
+--------+----------+-----+----------+------------+---------+------------+---------+
|    102 | Siva     |  28 | 45000.00 | HR         | Chennai |          5 |    NULL |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi   |          4 | 4000.00 |
+--------+----------+-----+----------+------------+---------+------------+---------+

+--------+----------+-----+----------+------------+-----------+------------+---------+
| emp_id | emp_name | age | salary   | department | city      | experience | bonus   |
+--------+----------+-----+----------+------------+-----------+------------+---------+
|    103 | Anil     |  32 | 60000.00 | Finance    | Delhi     |          8 | 8000.00 |
|    105 | Kiran    |  35 | 70000.00 | Sales      | Hyderabad |         10 | 9000.00 |
|    106 | Meena    |  30 | 55000.00 | Finance    | Bangalore |          6 |    NULL |
|    108 | Sneha    |  27 | 48000.00 | HR         | Delhi     |          4 | 4000.00 |
|    109 | Arjun    |  31 | 65000.00 | IT         | Bangalore |          7 | 7000.00 |
|    110 | Pooja    |  29 | 50000.00 | Marketing  | Mumbai    |          5 |    NULL |
+--------+----------+-----+----------+------------+-----------+------------+---------+