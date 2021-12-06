import models


class DoctorRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_doctors(db):
        records = db.query(models.Doctor).all()
        return records


class PatientRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_patients(db):
        records = db.query(models.Patient).all()
        return records


class MedicineRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_medicines(db):
        records = db.query(models.Medicine).all()
        return records

class InsuranceRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_insurances(db):
        records = db.query(models.Insurance).all()
        return records
