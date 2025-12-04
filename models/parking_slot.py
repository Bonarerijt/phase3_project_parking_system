from database import Base
from sqlalchemy import Column, Integer, Boolean, String
from app import main
from sqlalchemy.orm import relationship, backref

class ParkingSlot(Base):
    __tablename__ = "parking_slots"

    id = Column(Integer(), primary_key=True)
    slot_number = Column(String(), unique=True, nullable=False)
    is_occupied = Column(Boolean(), default=False)

    parking_sessions = relationship("ParkingSession", backref=backref('parkingslot'))

    def __repr__(self):
        return f"<ParkingSlot {self.slot_number} occupied={self.is_occupied}>"

    if __name__ == '__main__':
        main()