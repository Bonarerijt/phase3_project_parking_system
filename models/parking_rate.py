from sqlalchemy import Column, Integer, Float
from database import Base
from app import main

class ParkingRate(Base):
    __tablename__ = "parking_rates"

    id = Column(Integer(), primary_key=True)
    rate_per_hour = Column(Float(), nullable=False)

    def __repr__(self):
        return f"<ParkingRate {self.rate_per_hour}/hr>"

    if __name__ == '__main__':
        main()