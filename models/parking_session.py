from database import Base
from sqlalchemy import Column, Integer, String


class ParkingSession(Base):
    __tablename__ = "parking_sessions"

    id = Column(Integer(), primary_key=True)