from cli.vehicle_menu import vehicle_menu
from cli.slot_menu import slot_menu
from cli.session_menu import session_menu

def main_menu(session):
    while True:
        print("\n===== PARKING MANAGEMENT SYSTEM =====")
        print("1. Manage Vehicles")
        print("2. Manage Parking Slots")
        print("3. Manage Parking Sessions")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            vehicle_menu(session)
        elif choice == "2":
            slot_menu(session)
        elif choice == "3":
            session_menu(session)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")