from database import Base, engine
from sqlalchemy import Column, Integer, String

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer(), primary_key=True)
    plate_number = Column(String())
    owner_name = Column(String())

    if __name__ == '__main__':
        Base.metadata.create_all(engine)