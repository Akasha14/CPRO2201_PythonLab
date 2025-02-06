from Step1_Maintenance import *
from Step2and3_Vehicle import *

# Step 4:

def main():
    car = Car("Ford", "Fusion", 2018, 120000, CarMaintenance(), 4)
    bike = Bike("Trek", "X-Caliber", 2021, 2000, BikeMaintenance(), "Road")
    truck = Truck("Ford", "F-350", 2022, 25000, TruckMaintenance(), 5000)

    # Add vehicles to list.
    vehicle_list = [car, bike, truck]

    # Iterate through the vehicles.
    for vehicle in vehicle_list:
        vehicle.display_info()
        vehicle.perform_maintenance()


main()