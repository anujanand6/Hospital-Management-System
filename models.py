
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    specialist = Column(String(45))

