from models import Doctor, Patient, Department, \
    Medicine, Insurance, Designation, Doctor2Department, \
    Bill, Appointment, LabFee, RoomFee

"""
This file contains repositories for each model in the DB.

Each repository has the functions to implement the following functions:
1) Find all records
2) Find by ID
3) Create a new record
4) Delete by ID
5) Update by ID

"""


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
    def create_doctor(db_session, fn, ln, age, desig):
        new_record = Doctor(first_name=fn, last_name=ln,
                            age=age, designation=desig)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_doctor_by_id(db_session, id):
        db_session.query(Doctor).where(Doctor.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_doctor(db_session, id, fn, ln, age, desig):
        db_session.query(Doctor).where(Doctor.id == id).update(
            {"first_name": fn, "last_name": ln, "age": age,
             "designation": desig}
        )
        db_session.commit()

    @staticmethod
    def find_all_designations(db_session):
        records = db_session.query(Designation).all()
        return records


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


class DepartmentRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_departments(db):
        records = db.query(Department).all()
        return records

    @staticmethod
    def find_department_by_id(db, id):
        records = db.query(Department).where(Department.id == id)
        return records

    @staticmethod
    def create_department(db_session, dept_name, build_name):
        new_record = Department(dept_name=dept_name, building_name=build_name)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_department_by_id(db_session, id):
        db_session.query(Department).where(Department.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_department(db_session, id, dept_name, build_name):
        db_session.query(Department).where(Department.id == id).update(
            {"dept_name": dept_name, "building_name": build_name}
        )
        db_session.commit()


class Doctor2DepartmentRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_doctor_by_dept_id(db, dept_id):
        records = db.query(Doctor2Department).where(
            Doctor2Department.dept_id == dept_id
        )
        doc_ids = [r.doctor_id for r in records]
        return doc_ids

    @staticmethod
    def find_dept_by_doc_id(db, doc_id):
        records = db.query(Doctor2Department).where(
            Doctor2Department.doctor_id == doc_id
        )
        dept_ids = [r.dept_id for r in records]
        return dept_ids


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

    @staticmethod
    def find_patient_by_insurance_id(db, id):
        records = db.query(Insurance).where(Insurance.id == id)
        pids = [r.patient_id for r in records]
        return pids

    @staticmethod
    def find_insurances_by_patient_id(db, id):
        records = db.query(Insurance).where(Insurance.patient_id == id)
        return records


class BillRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_bills(db):
        records = db.query(Bill).all()
        return records

    @staticmethod
    def find_bill_by_id(db, id):
        records = db.query(Bill).where(Bill.id == id)
        return records

    @staticmethod
    def create_bill(db_session, dchar, medchar, pid, iid):
        new_record = Bill(doctor_charge=dchar, medicine_charge=medchar,
                          patient_id=pid, insurance_id=iid)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_bill_by_id(db_session, id):
        db_session.query(Bill).where(Bill.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_bill(db_session, id, dchar, medchar):
        db_session.query(Bill).where(Bill.id == id).update(
            {"doctor_charge": dchar, "medicine_charge": medchar}
        )
        db_session.commit()

    @staticmethod
    def find_insurance_by_bill_id(db, id):
        records = db.query(Bill).where(Bill.id == id)
        iids = [r.insurance_id for r in records]
        return iids

    @staticmethod
    def find_bills_by_insurance_id(db, id):
        records = db.query(Bill).where(Bill.insurance_id == id)
        return records


class AppointmentRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_appts(db):
        records = db.query(Appointment).all()
        return records

    @staticmethod
    def find_appt_by_id(db, id):
        records = db.query(Appointment).where(Appointment.id == id)
        return records

    @staticmethod
    def create_appt(db_session, created, date, time, pid, did):
        new_record = Appointment(created=created, appt_date=date, appt_time=time,
                                 patient_id=pid, doctor_id=did)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def delete_appt_by_id(db_session, id):
        db_session.query(Appointment).where(Appointment.id == id).delete()
        db_session.commit()

    @staticmethod
    def update_appt(db_session, id, created, date, time, pid, did):
        db_session.query(Appointment).where(Appointment.id == id).update(
            {"created": created, "appt_date": date, "appt_time": time,
             "patient_id": pid, "doctor_id": did}
        )
        db_session.commit()

    @staticmethod
    def find_doctor_by_patient_id(db, pid):
        records = db.query(Appointment).where(
            Appointment.patient_id == pid
        )
        doc_ids = [r.doctor_id for r in records]
        return doc_ids

    @staticmethod
    def find_patient_by_doctor_id(db, did):
        records = db.query(Appointment).where(
            Appointment.doctor_id == did
        )
        pids = [r.patient_id for r in records]
        return pids


class LabFeeRepository:

    def __init__(self):
        pass

    @staticmethod
    def find_all_labfees(db):
        records = db.query(LabFee).all()
        return records

    @staticmethod
    def find_labfee_by_id(db, id):
        records = db.query(LabFee).where(LabFee.id == id)
        return records

    @staticmethod
    def delete_labfee_by_id(db_session, id):
        db_session.query(LabFee).where(LabFee.id == id).delete()
        db_session.commit()

    @staticmethod
    def create_labfee(db_session, id, tname, tdate, type, cost):
        new_record = LabFee(id=id, test_name=tname, test_date=tdate,
                            test_type=type, test_charge=cost)
        db_session.add(new_record)
        db_session.commit()

    @staticmethod
    def update_labfee(db_session, id, tname, tdate, type, cost):
        db_session.query(LabFee).where(LabFee.id == id).update(
            {"test_name": tname, "test_date": tdate,
             "test_type": type, "test_charge": cost}
        )
        db_session.commit()
