from models.parking_session import ParkingSession
from models.vehicle import Vehicle
from models.parking_slot import ParkingSlot
from datetime import datetime

def session_menu(session):
    while True:
        print("\n--- Manage Parking Sessions ---")
        print("1. Start Session")
        print("2. End Session")
        print("3. View Sessions")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            vehicle_id = int(input("Vehicle ID: "))
            slot_id = int(input("Slot ID: "))

            new_session = ParkingSession(vehicle_id=vehicle_id, slot_id=slot_id)

            # Mark slot as occupied
            slot = session.get(ParkingSlot, slot_id)
            slot.is_occupied = True

            session.add(new_session)
            session.commit()
            print("Session started!")

        elif choice == "2":
            session_id = int(input("Session ID: "))
            psession = session.get(ParkingSession, session_id)

            if not psession:
                print("Session not found.")
                continue

            psession.time_out = datetime.utcnow()

            # Calculate fee (simple example: 50 per hour)
            duration = (psession.time_out - psession.time_in).seconds / 3600
            psession.total_fee = round(duration * 50, 2)

            # Free the slot
            psession.slot.is_occupied = False

            session.commit()
            print(f"Session ended. Fee: {psession.total_fee}")

        elif choice == "3":
            sessions = session.query(ParkingSession).all()
            for s in sessions:
                print(s)

        elif choice == "4":
            break
        else:
            print("Invalid option.")