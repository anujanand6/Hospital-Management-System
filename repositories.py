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
        new_record = Doctor(first_name=fn, last_name=ln, specialist=sp)
        db_session.add(new_record)
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

    @staticmethod
    def find_patient_by_id(db, id):
        records = db.query(Patient).where(Patient.id == id)
        return records

    @staticmethod
    def create_patient(db_session, fn, ln, gen, dob, ph, add):
        new_record = Patient(first_name=fn, last_name=ln, gender=gen,
                             dob=dob, phone=ph, address=add)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_patient_by_id(db_session, id):
        db_session.query(Patient).where(Patient.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_patient(db_session, id, fn, ln, gen, dob, ph, add):
        db_session.query(Patient).where(Patient.id == id).update(
            {"first_name": fn, "last_name": ln, "gender": gen, "dob": dob,
             "phone": ph, "address": add}
        )
        db_session.commit()


class MedicineRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_medicines(db):
        records = db.query(Medicine).all()
        return records

    @staticmethod
    def find_medicine_by_id(db, id):
        records = db.query(Medicine).where(Medicine.id == id)
        return records

    @staticmethod
    def create_medicine(db_session, mname, mtype, cost):
        new_record = Medicine(med_name=mname, med_type=mtype, cost=cost)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_medicine_by_id(db_session, id):
        db_session.query(Medicine).where(Medicine.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_medicine(db_session, id, mname, mtype, cost):
        db_session.query(Medicine).where(Medicine.id == id).update(
            {"med_name": mname, "med_type": mtype, "cost": cost}
        )
        db_session.commit()


class InsuranceRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_insurances(db):
        records = db.query(Insurance).all()
        return records

    @staticmethod
    def find_insurance_by_id(db, id):
        records = db.query(Insurance).where(Insurance.id == id)
        return records

    @staticmethod
    def create_insurance(db_session, pname, edate, pid):
        new_record = Insurance(provider_name=pname, exp_date=edate, patient_id=pid)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_insurance_by_id(db_session, id):
        db_session.query(Insurance).where(Insurance.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_insurance(db_session, id, pname, edate, pid):
        db_session.query(Insurance).where(Insurance.id == id).update(
            {"provider_name": pname, "exp_date": edate, "patient_id": pid}
        )
        db_session.commit()
