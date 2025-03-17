from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

# Step 1: SQLite database configuration.
DATABASE_URL = "sqlite:///Assignments/Assignment2/employees.db"
engine = create_engine(DATABASE_URL, echo=True)

# Base class from sql alchemy.
Base = declarative_base()

# Step 1: Employee model(like an object).
class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hire_date = Column(Date, nullable=False)
    salary = Column(Float, nullable=False)

# Step 2: Create the employees table in the DB.
Base.metadata.create_all(engine)

print("Database and employees table created successfully!")