from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    age = Column(Integer)
    designation = Column(String(100))


class Designation(Base):
    __tablename__ = "designations"

    designation = Column(String(100), primary_key=True)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    gender = Column(String(45))
    dob = Column(Date)
    phone = Column(Integer)
    address = Column(String(100))


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    med_name = Column(String(45))
    med_type = Column(String(45))
    cost = Column(Float)


class Insurance(Base):
    __tablename__ = "insurances"

    id = Column(Integer, primary_key=True)
    provider_name = Column(String(45))
    exp_date = Column(Date)
    patient_id = Column(Integer)


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    dept_name = Column(String(45))
    building_name = Column(String(45))


class Doctor2Department(Base):
    __tablename__ = "doctor_2_department"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    dept_id = Column(Integer)


