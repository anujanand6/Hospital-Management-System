from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from database import Base


class Doctor(Base):
    """
    ORM model for table doctors
    """
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    age = Column(Integer)
    designation = Column(String(100))


class Designation(Base):
    """
    ORM model for table designations
    """
    __tablename__ = "designations"

    designation = Column(String(100), primary_key=True)


class Department(Base):
    """
    ORM model for table departments
    """
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    dept_name = Column(String(45))
    building_name = Column(String(45))


class Doctor2Department(Base):
    """
    ORM model for table doctor_2_department
    """
    __tablename__ = "doctor_2_department"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    dept_id = Column(Integer)


class Patient(Base):
    """
    ORM model for table patients
    """
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    gender = Column(String(45))
    dob = Column(Date)
    phone = Column(Integer)
    address = Column(String(100))


class Appointment(Base):
    """
    ORM model for table appointments
    """
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    created = Column(Date)
    appt_date = Column(Date)
    appt_time = Column(Date)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)


class Medicine(Base):
    """
    ORM model for table medicines
    """
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True)
    med_name = Column(String(45))
    med_type = Column(String(45))
    cost = Column(Float)


class PrescribedMedicine(Base):
    """
    ORM model for table prescribed_meds
    """
    __tablename__ = "prescribed_meds"

    id = Column(Integer, primary_key=True)
    num_of_days = Column(Integer)
    time = Column(Date)
    patient_id = Column(Integer)
    medicine_id = Column(Integer)


class Insurance(Base):
    """
    ORM model for table insurances
    """
    __tablename__ = "insurances"

    id = Column(Integer, primary_key=True)
    provider_name = Column(String(45))
    exp_date = Column(Date)
    patient_id = Column(Integer)


class Bill(Base):
    """
    ORM model for table bills
    """
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True)
    doctor_charge = Column(Float)
    medicine_charge = Column(Float)
    patient_id = Column(Integer)
    insurance_id = Column(Integer)


class LabFee(Base):
    """
    ORM model for table lab_fees
    """
    __tablename__ = "lab_fees"

    id = Column(Integer, primary_key=True)
    test_name = Column(String(45))
    test_date = Column(Date)
    test_type = Column(String(45))
    test_charge = Column(Float)


class RoomFee(Base):
    """
    ORM model for table room_fees
    """
    __tablename__ = "room_fees"

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer)
    room_type = Column(String(45))
    num_of_beds = Column(Integer)
    num_of_days = Column(Integer)
    room_charge = Column(Float)

