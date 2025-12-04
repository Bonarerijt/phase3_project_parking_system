from core.parking_system import ParkingSystem

class ParkingCLI:
    def __init__(self):
        self.sys = ParkingSystem()

    def start(self):
        while True:
            print("\n==== CAR PARKING SYSTEM ====")
            print("1. Park Car")
            print("2. Exit Car")
            print("3. Parking Status")
            print("4. View History")
            print("5. Quit")
            choice = input("Choose option: ").strip()

            if choice == "1":
                plate = input("Enter plate: ")
                success, msg = self.sys.park_car(plate)
                print(msg)
            
            elif choice == "2":
                plate = input("Enter plate: ")
                success, result = self.sys.exit_car(plate)
                if success:
                    print("\n===== BILL =====")
                    print(f"Plate: {result['plate']}")
                    print(f"Slot: {result['slot']}")
                    print(f"Entry: {result['entry_time']}")
                    print(f"Exit: {result['exit_time']}")
                    print(f"Amount Paid: KES {result['amount_paid']:.2f}")
                    print("================")
                else:
                    print(result)
            
            elif choice == "3":
                status = self.sys.get_slots_status()
                print("\n--- PARKING STATUS ---")
                for group in ["A", "B"]:
                    print(f"\nGroup {group}:")
                    print("Slot | Status    | Plate    | Duration")
                    print("----------------------------------------")
                    for s in status[group]:
                        state = "Free" if s["is_free"] else "Occupied"
                        print(f"{s['name']:4} | {state:9} | {s['plate']:7} | {s['duration']}")
            
            elif choice == "4":
                hist = self.sys.get_history()
                if not hist:
                    print("No history.")
                else:
                    print("\n--- Parking History ---")
                    for h in hist:
                        print(f"Plate: {h.plate} | Slot: {h.slot_name} | Entry: {h.entry_time} | Exit: {h.exit_time} | Paid: KES {h.amount_paid:.2f}")
            
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("❌ Invalid choice")

if __name__ == "__main__":
    from database.db import init_db
    init_db()
    ParkingCLI().start()

