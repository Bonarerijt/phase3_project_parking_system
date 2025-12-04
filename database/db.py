from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///parking.db", echo = False)
Session = sessionmaker(bind=engine)

# My Models
class Slot(Base):
    __tablename__ = "slots"
    id = Column(Integer(), primary_key=True)
    name = Column(String, unique=True)
    group = Column(String)
    is_free = Column(Boolean, default=True)
    plate = Column(String, nullable=True)
    entry_time = Column(DateTime, nullable=True)