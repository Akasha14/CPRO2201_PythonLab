from Step1to2_SQLLiteDB import Employee, engine
from sqlalchemy.orm import sessionmaker
from datetime import date

# Use engine from Step 1.
Session = sessionmaker(bind=engine)
session = Session()

# Step 3: Function to insert a new employee into the employees table.
def add_employee(first_name, last_name, email, hire_date, salary):
    new_employee = Employee(
        first_name=first_name,
        last_name=last_name,
        email=email,
        hire_date=hire_date,
        salary=salary
    )
    # Add new employee to the session, and commit.
    session.add(new_employee)
    session.commit() 
    print(f"Employee {first_name} {last_name} added successfully.")

# Step 3: Insert at least 3 Employee records.
add_employee("Ricky", "Bobby", "r.bobby@example.com", date(2020, 2, 14), 66000.0)
add_employee("Casey", "Brown", "casey.b@example.com", date(2022, 4, 19), 58000.0)
add_employee("Mike", "Smith", "mike.smith@example.com", date(2024, 11, 2), 40000.0)

# Close session.
session.close()