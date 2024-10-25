# CarFinder v0.1
# 10/27/2024
# created a class named CarFinder to contain everything
class CarFinder:
    # list of all the vehicles authorized by CarFinder
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
    # creates the title for CarFinder version 0.1 
    def menu_title(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")
    # create menu and choices with in the program
    def menu_display(self):
        print("Please Enter the following number below from the following menu:")
        print("\n1. PRINT all Authorized Vehicles\n2. Exit\n")
    # if option 1 is pick , print out intro sentences and the list of vehicles in AllowedVehiclesList
    def authorized_vehicles(self):
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for authorizedvehicles in self.AllowedVehiclesList:
            print(authorizedvehicles)
    # main loop the program will cycle through for the user
    def main(self):
        while True:
            # display title and options
            self.menu_title()
            self.menu_display()
            # asking for users input
            selection_choices =  input("Enter Choice Here: ")
            # 1 is selected it will print out list of vehicles from AllowedVehiclesList (authorized)
            if selection_choices == "1":
                self.authorized_vehicles()
            # 2 is selected it will say a thank you message and end the loop
            elif selection_choices == "2":
                print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
                break
            # else statement in case users doesn't enter available choices , put back into loop
            else:
                print("\nInvalid choice, please try again.")
                input("\nPress any key to continue: ")

if __name__ == "__main__":
    #create an instance of CarFinder
    car_finder = CarFinder()
    # call car_finder to start the program
    car_finder.main()         
