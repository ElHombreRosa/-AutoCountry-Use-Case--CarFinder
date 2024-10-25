# CarFinder v0.1

class CarFinder:

    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

    def __init__(self):
        pass
    def menu_title(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")

    def menu_display(self):
        print("Please Enter the following number below from the following menu:")
        print("\n1. PRINT all Authorized Vehicles\n2. Exit")

    def authorized_vehicles(self):
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for authorizedvehicles in self.AllowedVehiclesList:
            print(authorizedvehicles)

    def main(self):
        while True: 
            self.menu_title
            self.menu_display
        
            selection_choices =  input()
        
            if selection_choices == "1":
                self.authorized_vehicles()
            elif selection_choices == "2":
                print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\n Invalid choice, please try again.")
            input("\n Press 1 or 2 to continue: ")

if __name__ == "__main__":
    car_finder = CarFinder
    car_finder.run()