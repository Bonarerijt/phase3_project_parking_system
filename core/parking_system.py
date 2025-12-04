from database.db import Session, Slot, ParkingHistory
from datetime import datetime



class ParkingSystem:
    RATE_PER_MINUTE = 5  #KES per minute

    def __init__(self):
        self.session = Session()

    def park_car(self, plate: str):
        plate = plate.upper()

        #Checks if car is already parked
        parked = parked = self.session.query(Slot).filter_by(plate=plate, is_free=False).first()
        if parked:
            return False, f"Car {plate} is already parked."
        
        # Finds free slot in group A first, then B
        slot = self.session.query(Slot).filter_by(is_free=True).order_by(Slot.group, Slot.name).first()
        if not slot:
            return False, "No available slots."
        
        slot.is_free = False
        slot.plate = plate
        slot.entry_time = datetime.now()
        self.session.commit()
        return True, f"✔ Car {plate} parked in slot {slot.name}."



    