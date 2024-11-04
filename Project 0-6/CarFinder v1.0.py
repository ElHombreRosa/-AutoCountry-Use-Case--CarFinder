# CarFinder v1.0
# 11/24/2024


import os
import getpass
# created a class named CarFinder to contain everything
class CarFinder:
    # list of all the vehicles authorized by CarFinder
    AllowedVehiclesFile = 'allowed_vehicles.txt'
    AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500' ]
    # initialize list from text file
    def __init__(self):
        self.AllowedVehiclesList = self.load_allowed_vehicles()
    
    
    # load vehicles from text file / create file if it doesnt exist    
    def load_allowed_vehicles(self):
        if not os.path.exists(self.AllowedVehiclesFile):
            self.create_allowed_vehicles_file()
        # read each line of text file
        with open(self.AllowedVehiclesFile, 'r') as file:
            return [line.strip() for line in file.readlines()]
    
        
    # create the text file from List(array) in AllowedVehiclesList
    def create_allowed_vehicles_file(self):
        with open(self.AllowedVehiclesFile, 'w') as file:
            for vehicle in self.AllowedVehiclesList:
                file.write(vehicle + '\n')


    # sends changes done to text from add and delete functions
    def changes_allowed_vehicles(self):
        with open(self.AllowedVehiclesFile, 'w') as file:
            for vehicle in self.AllowedVehiclesList:
                file.write(vehicle + '\n')
    
           
    # creates the title for CarFinder version 1.0  
    def menu_title(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v1.0")
        print("********************************")
        
        
    # create menu and choices with in the program
    def menu_display(self):
        print("Please Enter the following number below from the following menu:")
        print("\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit")
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
            self.changes_allowed_vehicles()
            print(f"You have added {added_vehicle} as an authorized vehicle")
    
    # option 4 is for deleting vehicles form AllowedVehiclesList
    def delete_vehicles(self): 
        erase_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
        if erase_vehicle in self.AllowedVehiclesList:
            while True: # loop back through
                confirming = input(f"Are you sure you want to remove {erase_vehicle} from the Authorized Vehicles List?\n")
                if confirming.lower()== "yes":
                    self.AllowedVehiclesList.remove(erase_vehicle)# remove vehicle off list
                    self.changes_allowed_vehicles()
                    print(f"You have REMOVED {erase_vehicle} as an authorized vehicle")
                    break
                elif confirming.lower() == "no":
                    break
                else:
                    print("Invalid input. Please enter yes or no ")
        else:
            print(f"{erase_vehicle} is not on Authorized Vehicle List")
        
    # main loop the program will cycle through for the user
    def main(self):
        while True:
            # display title and options
            self.menu_title()
            self.menu_display()
            
            # asking for users input
            selection_choices =  getpass.getpass("") # make users input invisible , less clutter on interface
            
            # if 1 is selected it will print out list of vehicles from AllowedVehiclesList (authorized)
            if selection_choices == "1":
                self.authorized_vehicles()
                
            # if 2 is selected , it will allow the user to search for vehicles / check if authorized
            elif selection_choices == "2":
                self.vehicles_search()
                
            # if 3 is selected, allow user to input new vehicle to list    
            elif selection_choices == "3":
                self.add_vehicles()
            
            # if 4 is selected, allow user to delete vehicle from list
            elif selection_choices == "4":
                self.delete_vehicles()
                        
            # if 5 is selected it will say a thank you message and end the loop
            elif selection_choices == "5":
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
