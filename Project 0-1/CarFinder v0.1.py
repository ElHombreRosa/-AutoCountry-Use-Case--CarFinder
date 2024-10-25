# CarFinder v0.1

AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

def menu_title():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")

def menu_display():
    print("Please Enter the following number below from the following menu:")
    print("\n1. PRINT all Authorized Vehicles\n2. Exit")

def authorized_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for authorizedvehicles in AllowedVehiclesList:
        print(authorizedvehicles)