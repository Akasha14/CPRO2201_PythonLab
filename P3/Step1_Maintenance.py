# Step 1:

from abc import ABC, abstractmethod

class Maintenance(ABC):
    @abstractmethod
    # Abstract used differently by all classes.
    def perform_maintenance(self):
        pass

# Car subclass (implements abstract method).
class CarMaintenance(Maintenance):
    def perform_maintenance(self):
        print("Car Maintenance List: \n -> Oil Change \n -> Tire Check \n -> Brake Check")

# Bike subclass (implements abstract method).
class BikeMaintenance(Maintenance):
    def perform_maintenance(self):
        print("Bike Maintenance List: \n -> Tire Pressure Check \n -> Chain Lubrication")

# Truck subclass (implements abstract method).
class TruckMaintenance(Maintenance):
    def perform_maintenance(self):
        print("Truck Maintenance List: \n -> Engine Inspection \n -> Cargo Inspection")
