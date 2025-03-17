from Step1to2_SQLLiteDB import Employee, engine
from sqlalchemy.orm import sessionmaker

# Use engine from Step 1
Session = sessionmaker(bind=engine)
session = Session()

def update_employee_salary(employee_id, percentage):
    # Find employee by ID.
    employee = session.query(Employee).filter_by(employee_id=employee_id).first()

    if employee:
        new_salary = employee.salary * (percentage / 100) # Calculate salary.
        employee.salary += new_salary # Set new salary.
        session.commit() # Commit changes.
        print(f"Updated Employee {employee_id}'s salary to ${employee.salary:.2f}")
    else:
        print(f"Employee with ID {employee_id} not found.")
    
    # Close session.
    session.close()

# Increase salary by 15% for employee with ID 3.
update_employee_salary(2, 15)  