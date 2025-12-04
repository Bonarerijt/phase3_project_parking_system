from database.db import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from datetime import datetime



class ParkingSession(Base):
    __tablename__ = "parking_sessions"

    id = Column(Integer(), primary_key=True)
    
    vehicle_id = Column(Integer(), ForeignKey("vehicles.id"), nullable=False)
    slot_id = Column(Integer(), ForeignKey("parking_slots.id"), nullable=False)

    time_in = Column(DateTime, default=datetime.utcnow)
    time_out = Column(DateTime, nullable=True)
    total_fee = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Session vehicle={self.vehicle_id} slot={self.slot_id}>"