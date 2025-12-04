from database import Base, engine, session
from sqlalchemy import Column, Integer, Boolean

class ParkingSlot(Base):
    __tablename__ = "parking_slots"

    id = Column(Integer(), primary_key=True)
    slot_number = Column(Integer())
    is_occupied = Column(Boolean, default=False)

    if __name__ == '__main__':
        Base.metadata.create_all(engine)