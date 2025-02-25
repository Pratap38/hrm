-- Step 1: Create the database
CREATE DATABASE hrm;

-- Step 2: Use the newly created database
USE hrm;

-- Step 3: Create the 'employees' table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    contact_number VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    job_title VARCHAR(100),
    department VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2),
    status ENUM('Active', 'Inactive') DEFAULT 'Active'
);

-- Step 4: Create the 'payroll' table
CREATE TABLE payroll (
    payroll_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    salary DECIMAL(10, 2),
    bonus DECIMAL(10, 2),
    deductions DECIMAL(10, 2),
    pay_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Step 5: Create the 'attendance' table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    status ENUM('Present', 'Absent', 'Leave', 'Holiday'),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Step 6: Create the 'training' table
CREATE TABLE training (
    training_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    training_name VARCHAR(100),
    training_date DATE,
    status ENUM('Completed', 'In Progress', 'Not Started'),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Step 7: (Optional) Create an index for better performance on common queries
CREATE INDEX idx_employee_email ON employees(email);
CREATE INDEX idx_employee_status ON employees(status);
CREATE INDEX idx_employee_department ON employees(department);
