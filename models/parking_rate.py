from sqlalchemy import Column, Integer, String
from database import Base, engine

class ParkingRate(Base):
    __tablename__ = "parking_rates"

    id = Column(Integer(), primary_key=True)
    rate_per_hour = Column(Integer())