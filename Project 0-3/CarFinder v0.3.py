# CarFinder v0.3
# 11/10/2024
# created a class named CarFinder to contain everything
class CarFinder:
    # list of all the vehicles authorized by CarFinder
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
    
    
    # creates the title for CarFinder version 0.3  
    def menu_title(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3")
        print("********************************")
        
        
    # create menu and choices with in the program
    def menu_display(self):
        print("Please Enter the following number below from the following menu:")
        print("\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. Exit")
        print("********************************")
        
        
    # if option 1 is pick , print out intro sentences and the list of vehicles in AllowedVehiclesList
    def authorized_vehicles(self):
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for authorizedvehicles in self.AllowedVehiclesList:
            print(authorizedvehicles)
            
            
    # search for options 2 for vehicles in list AllowedVehiclesList
    def vehicles_search(self):
        vehicle_userinput = input("Please Enter the full Vehicle name: ")
        if vehicle_userinput in self.AllowedVehiclesList: #checking for vehicles in AllowedVehiclesList
            print(f"{vehicle_userinput} is an authorized vehicle")
        else:
            print(f"{vehicle_userinput} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    
    
    # option 3 is pick this allows Sales Manger to add an authorized vehicles to AllowedVehiclesList
    def add_vehicles(self):
        added_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
        if added_vehicle in self.AllowedVehiclesList:
            print(f"{added_vehicle} is an authorized vehicle already")
        else:
            self.AllowedVehiclesList.append(added_vehicle) # add input vehicle to AllowedVehiclesList
            print(f"You have added {added_vehicle} as an authorized vehicle")
            
    # main loop the program will cycle through for the user
    def main(self):
        while True:
            # display title and options
            self.menu_title()
            self.menu_display()
            
            # asking for users input
            selection_choices =  input("Enter Choice Here: ")
            
            # if 1 is selected it will print out list of vehicles from AllowedVehiclesList (authorized)
            if selection_choices == "1":
                self.authorized_vehicles()
                
            # if 2 is selected , it will allow the user to search for vehicles / check if authorized
            elif selection_choices == "2":
                self.vehicles_search()
                
            # if 3 is selected, allow user to input new vehicle to list    
            elif selection_choices == "3":
                self.add_vehicles()
                    
            # if 4 is selected it will say a thank you message and end the loop
            elif selection_choices == "4":
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
