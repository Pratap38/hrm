import mysql.connector
from mysql.connector import Error

# Establish a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',         # MySQL server address
            database='hrm',           # The database you created
            user='your_username',     # MySQL username
            password='your_password'  # MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Insert a new employee
def insert_employee(connection, first_name, last_name, date_of_birth, contact_number, email, job_title, department, hire_date, salary):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO employees (first_name, last_name, date_of_birth, contact_number, email, job_title, department, hire_date, salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (first_name, last_name, date_of_birth, contact_number, email, job_title, department, hire_date, salary)
    
    cursor.execute(insert_query, data)
    connection.commit()
    print("Employee inserted successfully")

# Fetch all employees
def fetch_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Update employee salary
def update_salary(connection, employee_id, new_salary):
    cursor = connection.cursor()
    update_query = "UPDATE employees SET salary = %s WHERE employee_id = %s"
    cursor.execute(update_query, (new_salary, employee_id))
    connection.commit()
    print("Salary updated successfully")

# Delete an employee
def delete_employee(connection, employee_id):
    cursor = connection.cursor()
    delete_query = "DELETE FROM employees WHERE employee_id = %s"
    cursor.execute(delete_query, (employee_id,))
    connection.commit()
    print("Employee deleted successfully")

# Main function to run operations
def main():
    connection = create_connection()
    if connection:
        # Insert an employee
        insert_employee(connection, "John", "Doe", "1990-05-15", "1234567890", "johndoe@example.com", "Software Engineer", "IT", "2023-01-01", 50000.00)
        
        # Fetch and display all employees
        fetch_employees(connection)
        
        # Update salary of an employee (example)
        update_salary(connection, 1, 55000.00)
        
        # Delete an employee (example)
        delete_employee(connection, 2)

        # Close connection
        connection.close()

if __name__ == "__main__":
    main()
