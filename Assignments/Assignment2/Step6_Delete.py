from Step1to2_SQLLiteDB import Employee, engine
from sqlalchemy.orm import sessionmaker

# Use engine from Step 1
Session = sessionmaker(bind=engine)
session = Session()

def delete_employee(employee_id):
    # Find employee by ID.
    employee = session.query(Employee).filter_by(employee_id=employee_id).first()

    if employee:
        session.delete(employee)  # Delete employee.
        session.commit() # Commit changes.
        print(f"Employee with ID {employee_id} has been deleted.")
    else:
        print(f"Employee with ID {employee_id} not found.")

    # Close session.
    session.close()


# Deletes employee with ID 3.
delete_employee(3)