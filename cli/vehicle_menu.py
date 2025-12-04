from models.vehicle import Vehicle

def vehicle_menu(session):
    while True:
        print("\n--- Manage Vehicles ---")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            plate_number = input("Plate number: ")
            owner_name = input("Owner name: ")
            
            vehicle = Vehicle(plate_number = plate_number, owner_name = owner_name)
            session.add(vehicle)
            session.commit()
            print("Vehicle added!")

        elif choice == "2":
            vehicles = session.query(Vehicle).all()
            for v in vehicles:
                print(v)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")