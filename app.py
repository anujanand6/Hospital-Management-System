import streamlit as st

from menu import OPTION_LIST
import html_templates as html
from database import SessionLocal, engine
from repositories import DoctorRepository, PatientRepository, \
    MedicineRepository, InsuranceRepository, DepartmentRepository, \
    Doctor2DepartmentRepository, BillRepository, AppointmentRepository, \
    LabFeeRepository


def create_db_session():
    db = SessionLocal()
    return db


def main():
    # Create new DB Session
    db = create_db_session()

    # Display title
    st.markdown(html.title_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    # Choose option from sidebar
    choice = st.sidebar.radio("Menu", OPTION_LIST)

    try:

        if choice == "Home":
            st.markdown(html.home_temp, unsafe_allow_html=True)

        ##############
        # Doctor
        ##############

        elif choice == "View Doctors":
            st.subheader("View Doctors")
            records = DoctorRepository.find_all_doctors(db)
            for rec in records:
                st.markdown(html.doctors_temp.format(rec.id, rec.first_name, rec.last_name,
                                                     rec.age, rec.designation),
                            unsafe_allow_html=True)

        elif choice == "Find Doctor By ID":
            record_ids = [record.id for record in DoctorRepository.find_all_doctors(db)]
            # List IDs of all available doctors in the DB
            doc_id = st.selectbox("Choose Doctor ID", record_ids)
            records = DoctorRepository.find_doctor_by_id(db, doc_id)
            for rec in records:
                st.markdown(html.doctors_temp.format(rec.id, rec.first_name, rec.last_name,
                                                     rec.age, rec.designation),
                            unsafe_allow_html=True)

        elif choice == "Find Doctor by Department ID":
            st.subheader("Find Doctors by Department ID")
            dept_ids = [record.id for record in DepartmentRepository.find_all_departments(db)]
            dept_id = st.selectbox("Choose Department ID", dept_ids)
            doc_ids = Doctor2DepartmentRepository.find_doctor_by_dept_id(db, dept_id)
            doc_records = [DoctorRepository.find_doctor_by_id(db, id)[0] for id in doc_ids]
            for rec in doc_records:
                st.markdown(html.doctors_temp.format(rec.id, rec.first_name, rec.last_name,
                                                     rec.age, rec.designation),
                            unsafe_allow_html=True)

        elif choice == "Create Doctor":
            st.subheader("Create Doctor")
            fn = st.text_input("Enter first name")
            ln = st.text_input("Enter last name")
            age = st.text_input("Enter age")
            designation_list = [d.designation for d in DoctorRepository.find_all_designations(db)]
            designation = st.selectbox("Enter designation", designation_list)
            if st.button('Create'):
                DoctorRepository.create_doctor(db, fn, ln, age, designation)
                st.success("Doctor: {} {} successfully created!".format(fn, ln))

        elif choice == "Delete Doctor By ID":
            st.subheader("Delete Doctor By ID")
            record_ids = [doc.id for doc in DoctorRepository.find_all_doctors(db)]
            doc_id = st.selectbox("Choose Doctor ID", record_ids)
            if st.button('Delete'):
                DoctorRepository.delete_doctor_by_id(db, doc_id)
                st.success("Doctor: {} successfully deleted!".format(doc_id))

        elif choice == "Update Doctor":
            st.subheader("Update Doctor")
            record_ids = [doc.id for doc in DoctorRepository.find_all_doctors(db)]
            id = st.selectbox("Choose Doctor ID", record_ids)
            record = DoctorRepository.find_doctor_by_id(db, id)[0]
            fn = st.text_input("Enter first name", value=record.first_name)
            ln = st.text_input("Enter last name", value=record.last_name)
            age = st.text_input("Enter age", value=record.age)
            designation_list = [d.designation for d in DoctorRepository.find_all_designations(db)]
            d_index = designation_list.index(record.designation)
            designation = st.selectbox("Enter designation", designation_list, index=d_index)
            if st.button('Update'):
                DoctorRepository.update_doctor(db, id, fn, ln, age, designation)
                st.success("Doctor: {} {} successfully updated!".format(fn, ln))

        elif choice == "Find Departments by Doctor ID":
            st.subheader("View Departments by Doctor ID")
            doc_ids = [record.id for record in DoctorRepository.find_all_doctors(db)]
            doc_id = st.selectbox("Choose Doctor ID", doc_ids)
            dept_ids = Doctor2DepartmentRepository.find_dept_by_doc_id(db, doc_id)
            dept_records = [DepartmentRepository.find_department_by_id(db, id)[0] for id in dept_ids]
            for rec in dept_records:
                st.markdown(html.departments_temp.format(rec.id, rec.dept_name, rec.building_name),
                            unsafe_allow_html=True)

        elif choice == "Find Doctors by Patient ID":
            st.subheader("Find Doctors by Patient ID")
            pids = [record.id for record in PatientRepository.find_all_patients(db)]
            patient_id = st.selectbox("Choose Patient ID", pids)
            doc_ids = AppointmentRepository.find_doctor_by_patient_id(db, patient_id)
            doc_records = [DoctorRepository.find_doctor_by_id(db, id)[0] for id in doc_ids]
            for rec in doc_records:
                st.markdown(html.doctors_temp.format(rec.id, rec.first_name, rec.last_name,
                                                     rec.age, rec.designation),
                            unsafe_allow_html=True)

        ##############
        # Patient
        ##############

        elif choice == "View Patients":
            st.subheader("View Patients")
            records = PatientRepository.find_all_patients(db)
            for rec in records:
                st.markdown(html.patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                      rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "Find Patient By ID":
            st.subheader("Find Patient By ID")
            record_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            patient_id = st.selectbox("Choose Patient ID", record_ids)
            records = PatientRepository.find_patient_by_id(db, patient_id)
            for rec in records:
                st.markdown(html.patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                      rec.gender, rec.dob, rec.phone,
                                                      rec.address),
                            unsafe_allow_html=True)

        elif choice == "Find Patients By Insurance ID":
            st.subheader("Find Patients By Insurance ID")
            ins_ids = [record.id for record in InsuranceRepository.find_all_insurances(db)]
            insurance_id = st.selectbox("Choose Insurance ID", ins_ids)
            patient_ids = InsuranceRepository.find_patient_by_insurance_id(db, insurance_id)
            patient_records = [PatientRepository.find_patient_by_id(db, id)[0] for id in patient_ids]
            for rec in patient_records:
                st.markdown(html.patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                      rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "Find Patients By Doctor ID":
            st.subheader("Find Patients By Doctor ID")
            dids = [record.id for record in DoctorRepository.find_all_doctors(db)]
            doctor_id = st.selectbox("Choose Doctor ID", dids)
            patient_ids = AppointmentRepository.find_patient_by_doctor_id(db, doctor_id)
            patient_records = [PatientRepository.find_patient_by_id(db, id)[0] for id in patient_ids]
            for rec in patient_records:
                st.markdown(html.patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                      rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "Create Patient":
            st.subheader("Create Patient")
            fn = st.text_input("Enter first name")
            ln = st.text_input("Enter last name")
            gen = st.text_input("Enter gender")
            dob = st.text_input("Enter DOB (YYYY-MM-DD)")
            phone = st.text_input("Enter phone number")
            address = st.text_input("Enter address")
            if st.button('Create'):
                PatientRepository.create_patient(db, fn, ln, gen, dob, phone, address)
                st.success("Patient: {} {} successfully created!".format(fn, ln))

        elif choice == "Delete Patient By ID":
            st.subheader("Delete Patient By ID")
            record_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            patient_id = st.selectbox("Choose Patient ID", record_ids)
            if st.button('Delete'):
                PatientRepository.delete_patient_by_id(db, patient_id)
                st.success("Patient: {} successfully deleted!".format(patient_id))

        elif choice == "Update Patient":
            st.subheader("Update Patient")
            record_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            id = st.selectbox("Choose Patient ID", record_ids)
            record = PatientRepository.find_patient_by_id(db, id)[0]
            fn = st.text_input("Enter first name", value=record.first_name)
            ln = st.text_input("Enter last name", value=record.last_name)
            gen = st.text_input("Enter gender", value=record.gender)
            dob = st.text_input("Enter DOB (YYYY-MM-DD)", value=record.dob)
            phone = st.text_input("Enter phone number", value=record.phone)
            address = st.text_input("Enter address", value=record.address)
            if st.button('Update'):
                PatientRepository.update_patient(db, id, fn, ln, gen, dob, phone, address)
                st.success("Patient: {} {} successfully updated!".format(fn, ln))

        ##############
        # Medicine
        ##############

        elif choice == "View Medicines":
            st.subheader("View Medicines")
            records = MedicineRepository.find_all_medicines(db)
            for record in records:
                st.markdown(html.medicines_temp.format(record.id, record.med_name,
                                                       record.med_type, record.cost),
                            unsafe_allow_html=True)

        elif choice == "Find Medicine By ID":
            st.subheader("Find Medicine By ID")
            record_ids = [record.id for record in MedicineRepository.find_all_medicines(db)]
            medicine_id = st.selectbox("Choose Medicine ID", record_ids)
            records = MedicineRepository.find_medicine_by_id(db, medicine_id)
            for rec in records:
                st.markdown(html.medicines_temp.format(rec.id, rec.med_name, rec.med_type, rec.cost),
                            unsafe_allow_html=True)

        elif choice == "Create Medicine":
            st.subheader("Create Medicine")
            mname = st.text_input("Enter medicine name")
            mtype = st.text_input("Enter medicine type")
            cost = st.text_input("Enter cost")
            if st.button('Create'):
                MedicineRepository.create_medicine(db, mname, mtype, cost)
                st.success("Medicine: {} successfully created!".format(mname))

        elif choice == "Delete Medicine By ID":
            st.subheader("Delete Medicine By ID")
            record_ids = [record.id for record in MedicineRepository.find_all_medicines(db)]
            medicine_id = st.selectbox("Choose Medicine ID", record_ids)
            if st.button('Delete'):
                MedicineRepository.delete_medicine_by_id(db, medicine_id)
                st.success("Medicine: {} successfully deleted!".format(medicine_id))

        elif choice == "Update Medicine":
            st.subheader("Update Medicine")
            record_ids = [record.id for record in MedicineRepository.find_all_medicines(db)]
            id = st.selectbox("Choose Medicine ID", record_ids)
            record = MedicineRepository.find_medicine_by_id(db, id)[0]
            mname = st.text_input("Enter medicine name", value=record.med_name)
            mtype = st.text_input("Enter medicine type", value=record.med_type)
            cost = st.text_input("Enter cost", value=record.cost)
            if st.button('Update'):
                MedicineRepository.update_medicine(db, id, mname, mtype, cost)
                st.success("Medicine: {} successfully updated!".format(mname))

        ##############
        # Insurance
        ##############

        elif choice == "View Insurances":
            st.subheader("View Insurances")
            records = InsuranceRepository.find_all_insurances(db)
            for record in records:
                st.markdown(html.insurances_temp.format(record.id, record.provider_name,
                                                        record.exp_date, record.patient_id),
                            unsafe_allow_html=True)

        elif choice == "Find Insurance By ID":
            st.subheader("Find Insurance By ID")
            record_ids = [record.id for record in InsuranceRepository.find_all_insurances(db)]
            insurance_id = st.selectbox("Choose Insurance ID", record_ids)
            records = InsuranceRepository.find_insurance_by_id(db, insurance_id)
            for rec in records:
                st.markdown(html.insurances_temp.format(rec.id, rec.provider_name,
                                                        rec.exp_date, rec.patient_id),
                            unsafe_allow_html=True)

        elif choice == "Create Insurance":
            st.subheader("Create Insurance")
            pname = st.text_input("Enter Provider name")
            edate = st.text_input("Enter Expiry Date")
            record_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            patient_id = st.selectbox("Choose Patient ID", record_ids)
            if st.button('Create'):
                InsuranceRepository.create_insurance(db, pname, edate, patient_id)
                st.success("Insurance: {} successfully created!".format(pname))

        elif choice == "Delete Insurance By ID":
            st.subheader("Delete Insurance By ID")
            record_ids = [record.id for record in InsuranceRepository.find_all_insurances(db)]
            insurance_id = st.selectbox("Choose Insurance ID", record_ids)
            if st.button('Delete'):
                InsuranceRepository.delete_insurance_by_id(db, insurance_id)
                st.success("Insurance: {} successfully deleted!".format(insurance_id))

        elif choice == "Update Insurance":
            st.subheader("Update Insurance")
            record_ids = [record.id for record in InsuranceRepository.find_all_insurances(db)]
            id = st.selectbox("Choose Insurance ID", record_ids)
            record = InsuranceRepository.find_insurance_by_id(db, id)[0]
            pname = st.text_input("Enter provider name", value=record.provider_name)
            edate = st.text_input("Enter expiry date", value=record.exp_date)
            patient_id = st.text_input("Enter patient id", value=record.patient_id)
            if st.button('Update'):
                InsuranceRepository.update_insurance(db, id, pname, edate, patient_id)
                st.success("Insurance: {} successfully updated!".format(pname))

        elif choice == "Find Insurances By Patient ID":
            st.subheader("Find Insurances By Patient ID")
            rec_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            rec_id = st.selectbox("Choose Patient ID", rec_ids)
            records = InsuranceRepository.find_insurances_by_patient_id(db, rec_id)
            for rec in records:
                st.markdown(html.insurances_temp.format(rec.id, rec.provider_name,
                                                        rec.exp_date, rec.patient_id),
                            unsafe_allow_html=True)

        elif choice == "Find Insurances By Bill ID":
            st.subheader("Find Insurances By Bill ID")
            rec_ids = [record.id for record in BillRepository.find_all_bills(db)]
            rec_id = st.selectbox("Choose Bill ID", rec_ids)
            insurance_ids = BillRepository.find_insurance_by_bill_id(db, rec_id)
            records = [InsuranceRepository.find_insurance_by_id(db, id)[0] for id in insurance_ids]
            for rec in records:
                st.markdown(html.insurances_temp.format(rec.id, rec.provider_name,
                                                        rec.exp_date, rec.patient_id),
                            unsafe_allow_html=True)

        ##############
        # Bills
        ##############

        elif choice == "View Bills":
            st.subheader("View Bills")
            records = BillRepository.find_all_bills(db)
            for record in records:
                st.markdown(html.bills_temp.format(record.id, record.medicine_charge, record.doctor_charge,
                                                   record.patient_id, record.insurance_id),
                            unsafe_allow_html=True)

        elif choice == "Find Bill By ID":
            st.subheader("Find Bill By ID")
            record_ids = [record.id for record in BillRepository.find_all_bills(db)]
            bill_id = st.selectbox("Choose Bill ID", record_ids)
            records = BillRepository.find_bill_by_id(db, bill_id)
            for record in records:
                st.markdown(html.bills_temp.format(record.id, record.medicine_charge, record.doctor_charge,
                                                   record.patient_id, record.insurance_id),
                            unsafe_allow_html=True)

        elif choice == "Create Bill":
            st.subheader("Create Bill")
            dchar = st.text_input("Enter Doctor Charge")
            mchar = st.text_input("Enter Medicine Charge")
            pid = st.selectbox("Choose Patient ID",
                               [record.id for record in PatientRepository.find_all_patients(db)])
            iid = st.selectbox("Choose Insurance ID",
                               [record.id for record in InsuranceRepository.find_insurances_by_patient_id(db, pid)])
            if st.button('Create'):
                BillRepository.create_bill(db, dchar, mchar, pid, iid)
                st.success("Bill successfully created!")

        elif choice == "Delete Bill By ID":
            st.subheader("Delete Bill By ID")
            record_ids = [record.id for record in BillRepository.find_all_bills(db)]
            bill_id = st.selectbox("Choose Bill ID", record_ids)
            if st.button('Delete'):
                BillRepository.delete_bill_by_id(db, bill_id)
                st.success("Bill: {} successfully deleted!".format(bill_id))

        elif choice == "Update Bill":
            st.subheader("Update Bill")
            record_ids = [record.id for record in BillRepository.find_all_bills(db)]
            bill_id = st.selectbox("Choose Bill ID", record_ids)
            record = BillRepository.find_bill_by_id(db, bill_id)[0]
            dchar = st.text_input("Enter Doctor Charge", value=record.doctor_charge)
            mchar = st.text_input("Enter Medicine Charge", value=record.medicine_charge)
            if st.button('Update'):
                BillRepository.update_bill(db, bill_id, dchar, mchar)
                st.success("Bill: {} successfully updated!".format(bill_id))

        elif choice == "Find Bills By Insurance ID":
            st.subheader("Find Bills By Insurance ID")
            rec_id = st.selectbox("Choose Insurance ID",
                                  [record.id for record in InsuranceRepository.find_all_insurances(db)])
            records = BillRepository.find_bills_by_insurance_id(db, rec_id)
            for record in records:
                st.markdown(html.bills_temp.format(record.id, record.medicine_charge, record.doctor_charge,
                                                   record.patient_id, record.insurance_id),
                            unsafe_allow_html=True)

        ##############
        # Lab Fees
        ##############

        elif choice == "View Lab Fees":
            st.subheader("View Lab Fees")
            labfees_records = LabFeeRepository.find_all_labfees(db)
            for labfee in labfees_records:
                bill = BillRepository.find_bill_by_id(db, labfee.id)[0]
                st.markdown(html.labfees_temp.format(labfee.id, labfee.test_name, labfee.test_date,
                                                     labfee.test_type, labfee.test_charge, bill.doctor_charge,
                                                     bill.medicine_charge, bill.patient_id, bill.insurance_id),
                            unsafe_allow_html=True)

        elif choice == "Find Lab Fees By Bill ID":
            st.subheader("Find Lab Fees By Bill ID")
            record_ids = [record.id for record in LabFeeRepository.find_all_labfees(db)]
            labfee_id = st.selectbox("Choose Lab Fee ID", record_ids)
            labfees_records = LabFeeRepository.find_labfee_by_id(db, labfee_id)
            for labfee in labfees_records:
                bill = BillRepository.find_bill_by_id(db, labfee.id)[0]
                st.markdown(html.labfees_temp.format(labfee.id, labfee.test_name, labfee.test_date,
                                                     labfee.test_type, labfee.test_charge, bill.doctor_charge,
                                                     bill.medicine_charge, bill.patient_id, bill.insurance_id),
                            unsafe_allow_html=True)

        elif choice == "Delete Lab Fee By ID":
            st.subheader("Delete Lab Fee By ID")
            record_ids = [record.id for record in LabFeeRepository.find_all_labfees(db)]
            labfee_id = st.selectbox("Choose Bill ID", record_ids)
            if st.button('Delete'):
                LabFeeRepository.delete_labfee_by_id(db, labfee_id)
                st.success("Lab Fee: {} successfully deleted!".format(labfee_id))

        # TODO
        elif choice == "Create Lab Fees":
            st.subheader("Create Lab Fees")
            record_ids = [record.id for record in BillRepository.find_all_bills(db)]
            bill_id = st.selectbox("Choose Bill ID", record_ids)
            tname = st.text_input("Enter test name")
            tdate = st.text_input("Enter test date (YYYY-MM-DD)")
            ttype = st.text_input("Enter test type")
            cost = st.text_input("Enter test charge")
            if st.button('Create'):
                LabFeeRepository.create_labfee(db, bill_id, tname, tdate, ttype, cost)
                st.success("Lab Fee for Bill ID: {} successfully created!".format(bill_id))

        elif choice == "Update Lab Fees":
            st.subheader("Update Lab Fees")
            record_ids = [record.id for record in LabFeeRepository.find_all_labfees(db)]
            labfee_id = st.selectbox("Choose Lab Fee ID", record_ids)
            labfee = LabFeeRepository.find_labfee_by_id(db, labfee_id)[0]
            bill = BillRepository.find_bill_by_id(db, labfee.id)[0]

            tname = st.text_input("Enter test name", value=labfee.test_name)
            tdate = st.text_input("Enter test date (YYYY-MM-DD)", value=labfee.test_date)
            ttype = st.text_input("Enter test type", value=labfee.test_type)
            cost = st.text_input("Enter test charge", value=labfee.test_charge)
            dchar = st.text_input("Enter Doctor Charge", value=bill.doctor_charge)
            mchar = st.text_input("Enter Medicine Charge", value=bill.medicine_charge)

            if st.button('Update'):
                BillRepository.update_bill(db, labfee_id, dchar, mchar)
                LabFeeRepository.update_labfee(db, labfee_id, tname, tdate, ttype, cost)
                st.success("Lab Fees: {} successfully updated!".format(labfee_id))

    finally:
        db.close()


if __name__ == '__main__':
    main()
