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
    
    def exit_car(self, plate: str):
        plate = plate.upper()
        slot = self.session.query(Slot).filter_by(plate=plate, is_free=False).first()
        if not slot:
            return False, "Car not found in parking."

        now = datetime.now()
        duration = (now - slot.entry_time).total_seconds() / 60  # minutes
        amount = duration * self.RATE_PER_MIN

        # Save to history
        history = ParkingHistory(
            plate=plate,
            slot_name=slot.name,
            entry_time=slot.entry_time,
            exit_time=now,
            amount_paid=amount
        )
        self.session.add(history)

        # Free the slot
        slot.is_free = True
        slot.plate = None
        slot.entry_time = None
        self.session.commit()

        return True, {
            "plate": plate,
            "slot": slot.name,
            "entry_time": history.entry_time,
            "exit_time": history.exit_time,
            "amount_paid": history.amount_paid
        }
    def get_slots_status(self):
        slots = self.session.query(Slot).order_by(Slot.group, Slot.name).all()
        status = {"A": [], "B": []}
        for s in slots:
            duration = "-"
            if not s.is_free and s.entry_time:
                delta = datetime.now() - s.entry_time
                minutes = int(delta.total_seconds() // 60)
                seconds = int(delta.total_seconds() % 60)
                duration = f"{minutes}m {seconds}s"
            status[s.group].append({
                "name": s.name,
                "is_free": s.is_free,
                "plate": s.plate if s.plate else "-",
                "duration": duration
            })
        return status

    def get_history(self):
        return self.session.query(ParkingHistory).order_by(ParkingHistory.entry_time).all()









    