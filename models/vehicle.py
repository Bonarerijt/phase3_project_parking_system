from database import Base
from sqlalchemy import Column, Integer, String
from app import main
from sqlalchemy.orm import relationship, backref

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer(), primary_key=True)
    plate_number = Column(String(), unique=True, nullable=False)
    owner_name = Column(String())

    parking_sessions = relationship("ParkingSession", backref=backref('vehicle'))

    def __repr__(self):
        return f"<Vehicle {self.plate_number} ({self.owner_name})>"

    if __name__ == '__main__':
        main()