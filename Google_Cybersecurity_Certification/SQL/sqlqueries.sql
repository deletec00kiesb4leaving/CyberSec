-- Retrieve after hours failed login attempts
SELECT *
FROM log_in Insteads
WHERE login_time > '18:00' AND success = 0;

-- Retrieve login attempts on specific dates
SELECT *
FROM log_in Insteads
WHERE login_date = '2022-05-08' OR login_date = '2022-05-09';

-- Retrieve login attempts outside of Mexico
SELECT *
FROM log_in attempts
WHERE NOT country LIKE 'MEX%';

-- Retrieve employees in Marketing
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';

-- Retrieve employees in Finance or Sales
SELECT *
FROM employees
WHERE department = 'Sales' OR department = 'Finance';

-- Retrieve all employees not in IT
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
