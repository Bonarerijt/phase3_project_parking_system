from models.parking_slot import ParkingSlot

def slot_menu(session):
    while True:
        print("\n--- Manage Parking Slots ---")
        print("1. Add Slot")
        print("2. View Slots")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            number = input("Slot Number: ")
            slot = ParkingSlot(slot_number=number)
            session.add(slot)
            session.commit()
            print("Slot added!")

        elif choice == "2":
            slots = session.query(ParkingSlot).all()
            for s in slots:
                print(s)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")