from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    specialist = Column(String(45))


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    gender = Column(String(45))
    dob = Column(Date)
    phone = Column(Integer)
    address = Column(String(100))


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    med_name = Column(String(45))
    med_type = Column(String(45))
    cost = Column(Float)


class Insurance(Base):
    __tablename__ = "insurances"

    insurance_number = Column(Integer, primary_key=True, index=True)
    provider_name = Column(String(45))
    exp_date = Column(Date)
    patient_id = Column(Integer)
