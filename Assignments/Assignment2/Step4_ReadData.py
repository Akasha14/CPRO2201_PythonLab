from Step1to2_SQLLiteDB import Employee, engine
from sqlalchemy.orm import sessionmaker
from datetime import date

# Use engine from Step 1.
Session = sessionmaker(bind=engine)
session = Session()

# Get all employees in DB.
def get_all_employees():
    employees = session.query(Employee).all()
    # Print all.
    for employee in employees:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}, Hire Date: {employee.hire_date}, Salary: {employee.salary}")

# Get employee by provided id.
def employee_by_id(employee_id):
    employee = session.query(Employee).filter_by(employee_id=employee_id).first()
    # If exists, print details.
    if employee:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}, Hire Date: {employee.hire_date}, Salary: {employee.salary}")
    else:
        print(f"Employee with ID {employee_id} not found.")

# Get all employees whose salary is greater than $50,000.
def employees_with_large_salary(base_salary=50000):
    # Get all whose salary > base_salary, then print each.
    employees = session.query(Employee).filter(Employee.salary > base_salary).all()
    for employee in employees:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Salary: {employee.salary}")

# Get all employees hired after a provided date.
def employees_hired_after(base_date):
    # Get all whose hire_date > base_date, then print each.
    employees = session.query(Employee).filter(Employee.hire_date > base_date).all()
    for employee in employees:
        print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Hire Date: {employee.hire_date}")

# Using the functions
print("\nGet All Employees:")
get_all_employees()

print("\nSearch for Employee by ID:")
employee_by_id(3)

print("\nFind Employees with Salary > $50,000:")
employees_with_large_salary()

print("\nFind Employees Hired After 2021-01-01:")
employees_hired_after(date(2021, 1, 1))

# Close session.
session.close()