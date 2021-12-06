from models import Doctor, Patient, Medicine, Insurance


class DoctorRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_doctors(db):
        records = db.query(Doctor).all()
        return records

    @staticmethod
    def find_doctor_by_id(db, id):
        records = db.query(Doctor).where(Doctor.id == id)
        return records

    @staticmethod
    def create_doctor(db_session, fn, ln, sp):
        new_doc = Doctor(first_name=fn, last_name=ln, specialist=sp)
        db_session.add(new_doc)
        db_session.commit()

    @staticmethod
    def delete_doctor_by_id(db_session, id):
        db_session.query(Doctor).where(Doctor.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_doctor(db_session, id, fn, ln, sp):
        db_session.query(Doctor).where(Doctor.id == id).update(
            {Doctor.first_name: fn, Doctor.last_name: ln, Doctor.specialist: sp}
        )
        db_session.commit()



class PatientRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_patients(db):
        records = db.query(Patient).all()
        return records


class MedicineRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_medicines(db):
        records = db.query(Medicine).all()
        return records


class InsuranceRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_insurances(db):
        records = db.query(Insurance).all()
        return records
