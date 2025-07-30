# Project: Travel Agency Management System
# Name: Farhan Muhib Efty
# ID: 190105022, Lab Group: A1, Year: 2, Semester: 1

# Class to manage a new travel trip for a user
class NewTravelTrip:
    def __init__(self):
        # Auto-incremented invoice ID
        global inv
        self.invoice = inv
        inv += 1

        # User input for basic information
        self.name = input("         Enter User Name: ")
        self.date = input("              Enter Date: ")
        self.address = input("      Enter User Address: ")
        self.phoneno = input("    Enter User Phone No.: ")
        self.email = input("Enter User Email Address: ")

        # Input for first trip details
        t_date = input("         Enter Trip Date: ")
        print("     Enter Trip Location ")
        s_loc = input("           Start Location: ")
        f_des = input("        Final Destination: ")

        # Store trip details in lists to allow multiple trips per user
        self.tripdate = [t_date]
        self.startlocation = [s_loc]
        self.finaldestination = [f_des]

    # Add a new trip to an existing user based on invoice ID
    def AddTrip(self):
        invc_id = int(input("        Enter Invoice ID: "))
        for trip in trips:
            if trip.invoice == invc_id:
                # Take new trip details
                t_date = input("         Enter Trip Date: ")
                print("     Enter Trip Location: ")
                s_loc = input("           Start Location: ")
                f_des = input("        Final Destination: ")

                # Append to existing trip lists
                trip.tripdate.append(t_date)
                trip.startlocation.append(s_loc)
                trip.finaldestination.append(f_des)
                break

    # Edit an existing trip from a user based on invoice ID
    def EditTrip(self):
        invc_id = int(input("           Enter Invoice ID: "))
        for trip in trips:
            if trip.invoice == invc_id:
                for i in range(len(trip.tripdate)):
                    # Show current trip details
                    print("\nTrip Date:", trip.tripdate[i])
                    print("Start Location:", trip.startlocation[i])
                    print("Final Destination:", trip.finaldestination[i])
                    # Ask user if they want to edit
                    choice = input("Do you want to edit this trip? (Y/N): ")
                    if choice.lower() == 'y':
                        # Take updated trip details
                        t_date = input("         Enter Trip Date: ")
                        s_loc = input("           Start Location: ")
                        f_des = input("        Final Destination: ")

                        # Update trip information
                        trip.tripdate[i] = t_date
                        trip.startlocation[i] = s_loc
                        trip.finaldestination[i] = f_des
                        break

    # Delete a specific trip entry for a user
    def DeleteTrip(self):
        invc_id = int(input("       Enter Invoice ID: "))
        for trip in trips:
            if trip.invoice == invc_id:
                for i in range(len(trip.tripdate)):
                    # Display trip details
                    print("\nTrip Date:", trip.tripdate[i])
                    print("Start Location:", trip.startlocation[i])
                    print("Final Destination:", trip.finaldestination[i])
                    # Ask if user wants to delete
                    choice = input("Do you want to delete this trip? (Y/N): ")
                    if choice.lower() == 'y':
                        # Remove the selected trip from all lists
                        del trip.tripdate[i]
                        del trip.startlocation[i]
                        del trip.finaldestination[i]
                        break
                break

# Class to display and manage all user records
class ShowAllUser:
    # Display all user information and their trips
    def showUser(self):
        for trip in trips:
            print(f"\nInvoice ID: {trip.invoice}")
            print(f"Date: {trip.date}")
            print(f"User Name: {trip.name}")
            print(f"Address: {trip.address}")
            print(f"Phone No.: {trip.phoneno}")
            print(f"Email: {trip.email}")

            # Display all trips for the user
            for i in range(len(trip.tripdate)):
                print(f"\nTrip Date: {trip.tripdate[i]}")
                print("Trip Location:")
                print("--------------")
                print(f"Start Location: {trip.startlocation[i]}")
                print(f"Final Destination: {trip.finaldestination[i]}")
            print("\n")

    # Edit user information and reset trip list
    def EditUser(self):
        invc_id = int(input("Enter Invoice ID: "))
        for trip in trips:
            if trip.invoice == invc_id:
                # Update basic user details
                trip.date = input("               Enter New Date: ")
                trip.name = input("          Enter New User Name: ")
                trip.address = input("       Enter New User Address: ")
                trip.phoneno = input("      Enter New User Phone No: ")
                trip.email = input(" Enter New Email Address: ")

                # Clear previous trips
                trip.tripdate.clear()
                trip.startlocation.clear()
                trip.finaldestination.clear()

                # Add new trip info
                t_date = input("         Enter New Trip Date: ")
                s_loc = input("           New Start Location: ")
                f_des = input("        New Final Destination: ")

                # Store new trip
                trip.tripdate.append(t_date)
                trip.startlocation.append(s_loc)
                trip.finaldestination.append(f_des)
                break

    # Delete a full user record based on invoice ID
    def DeleteUser(self):
        invc_id = int(input("Enter Invoice ID: "))
        for i, trip in enumerate(trips):
            if trip.invoice == invc_id:
                del trips[i]
                break

# Global trip list to store all user trips
trips = []

# Global invoice counter
inv = 1

# Main program loop
def main():
    while True:
        print("="*75)
        print("Please choose your option between (1 to 8):")
        print("="*75)
        print("\t1. New Travel Trip")
        print("\t2. Show All Users")
        print("\t3. Edit User")
        print("\t4. Delete User")
        print("\t5. Add Trip")
        print("\t6. Edit Trip")
        print("\t7. Delete Trip")
        print("\t8. Exit Program")
        print()

        choice = input("Enter Your Choice: ")

        # Option 1: Create new trip and store in global list
        if choice == '1':
            print("\nYou have chosen option 1.")
            trips.append(NewTravelTrip())
            input("Your Data is Recorded. Press Enter to continue...")

        # Option 2: Show all user data
        elif choice == '2':
            print("\nYou have chosen option 2.")
            show = ShowAllUser()
            show.showUser()
            input("Press Enter to go to the main menu...")

        # Option 3: Edit existing user
        elif choice == '3':
            print("\nYou have chosen option 3.")
            show = ShowAllUser()
            show.EditUser()
            input("Your Data is Edited. Press Enter to continue...")

        # Option 4: Delete existing user
        elif choice == '4':
            print("\nYou have chosen option 4.")
            show = ShowAllUser()
            show.DeleteUser()
            input("Your Data is Deleted. Press Enter to continue...")

        # Option 5: Add trip to existing user
        elif choice == '5':
            print("\nYou have chosen option 5.")
            trip = NewTravelTrip()
            trip.AddTrip()
            input("Your Trip is Added. Press Enter to continue...")

        # Option 6: Edit a trip
        elif choice == '6':
            print("\nYou have chosen option 6.")
            trip = NewTravelTrip()
            trip.EditTrip()
            input("Your Trip is Edited. Press Enter to continue...")

        # Option 7: Delete a trip
        elif choice == '7':
            print("\nYou have chosen option 7.")
            trip = NewTravelTrip()
            trip.DeleteTrip()
            input("Your Trip is Deleted. Press Enter to continue...")

        # Option 8: Exit program
        elif choice == '8':
            print("Thank you! Exiting...")
            break

        # Invalid input
        else:
            input("Invalid choice! Press Enter to continue...")

# Start the program
if __name__ == "__main__":
    main()
