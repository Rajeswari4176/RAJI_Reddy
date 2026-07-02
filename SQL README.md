-- 1. Create Employee Table with 2 Columns
CREATE TABLE employee (
    emp_name CHAR(20),
    location VARCHAR(30)
);

-- 2. Add Column at Last (Address)
ALTER TABLE employee
ADD address VARCHAR(50);

-- 3. Add Column at First (emp_id)
ALTER TABLE employee
ADD emp_id INT FIRST;

-- 4. Add Column at Specific Position (email after location)
ALTER TABLE employee
ADD email VARCHAR(25) AFTER location;

-- 5. Modify emp_name from CHAR to VARCHAR
ALTER TABLE employee
MODIFY emp_name VARCHAR(20);

-- 6. Add sid and department at the Same Time
ALTER TABLE employee
ADD sid INT,
ADD department VARCHAR(30);

-- 7. Rename emp_name to employeeName
ALTER TABLE employee
RENAME COLUMN emp_name TO employeeName;

-- 8. Drop sid Column
ALTER TABLE employee
DROP COLUMN sid;
