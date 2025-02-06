from Step1_Maintenance import *

# Step 2:
class Vehicle:

    # Constructor.
    def __init__(self, make, model, year, mileage, maintenance_plan):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.maintenance_plan = maintenance_plan

    
    def display_info(self):
        print(f"\n------Vehicle Info------ \n - Make: {self.make} \n - Model: {self.model} \n - Year: {self.year} \n - Mileage: {self.mileage}")

    def perform_maintenance(self):
        print("------Maintenance------")
        # Use maintenance_plan from Car/Bike/Truck maintenance subclass.
        self.maintenance_plan.perform_maintenance()
        print("--------------------------------")
        print()


# Step 3:

# Car subclass.
class Car(Vehicle):
    # Constructor (use original - super(), add num_doors).
    def __init__(self, make, model, year, mileage, maintenance_plan, num_doors):
        super().__init__(make, model, year, mileage, maintenance_plan)
        self.num_doors = num_doors

    # Override parent method.
    def display_info(self):
        # Call original print, and num_doors at end.
        super().display_info()
        print(f" - Number of Doors: {self.num_doors}")

# Bike subclass.
class Bike(Vehicle):
    def __init__(self, make, model, year, mileage, maintenance_plan, type_of_bike):
        super().__init__(make, model, year, mileage, maintenance_plan)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f" - Type of Bike: {self.type_of_bike}")

# Subclass for Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, maintenance_plan, cargo_capacity):
        super().__init__(make, model, year, mileage, maintenance_plan)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        super().display_info()
        print(f" - Cargo Capacity: {self.cargo_capacity}kg")
