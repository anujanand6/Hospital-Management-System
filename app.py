import streamlit as st
import html_templates as html
from repositories import DoctorRepository, PatientRepository, \
    MedicineRepository, InsuranceRepository, DepartmentRepository
from database import SessionLocal, engine


def main():
    st.markdown(html.title_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    menu = ["Home", "View Doctors", "View Patients", "View Medicines", "View Insurances",
            "Find Doctor By ID", "Create Doctor", "Update Doctor", "Delete Doctor By ID",
            "Find Patient By ID", "Create Patient", "Update Patient", "Delete Patient By ID",
            "Find Medicine By ID", "Create Medicine", "Update Medicine", "Delete Medicine By ID",
            "Find Insurance By ID", "Create Insurance", "Update Insurance", "Delete Insurance By ID"]
    choice = st.sidebar.selectbox("Menu", menu)

    try:
        db = SessionLocal()

        if choice == "Home":
            st.text("This is the front end interface.")
            # st.markdown(html.home_temp, unsafe_allow_html=True)

        if choice == "View Doctors":
            st.subheader("View Doctors")
            records = DoctorRepository.find_all_doctors(db)
            for rec in records:
                st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name,
                                                          rec.age, rec.designation),
                            unsafe_allow_html=True)

            # if st.button("View Doctor by Department ID"):
            #     record_ids = [record.id for record in DepartmentRepository.find_all_departments(db)]
            #     dept_id = st.selectbox("Choose Department ID", record_ids)
            #     records = DoctorRepository.find_doctor_by_dept_id(db, dept_id)
            #     for rec in records:
            #         st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name,
            #                                                   rec.age, rec.designation),
            #                     unsafe_allow_html=True)

        elif choice == "Find Doctor By ID":
            record_ids = [record.id for record in DoctorRepository.find_all_doctors(db)]
            doc_id = st.selectbox("Choose Doctor ID", record_ids)
            records = DoctorRepository.find_doctor_by_id(db, doc_id)
            for rec in records:
                st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name,
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

        elif choice == "View Patients":
            st.subheader("View Patients")
            records = PatientRepository.find_all_patients(db)
            for rec in records:
                st.markdown(html.view_patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                           rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "Find Patient By ID":
            st.subheader("Find Patient By ID")
            record_ids = [record.id for record in PatientRepository.find_all_patients(db)]
            patient_id = st.selectbox("Choose Patient ID", record_ids)
            records = PatientRepository.find_patient_by_id(db, patient_id)
            for rec in records:
                st.markdown(html.view_patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                           rec.gender, rec.dob, rec.phone,
                                                           rec.address),
                            unsafe_allow_html=True)

        elif choice == "Create Patient":
            st.subheader("Create Patient")
            fn = st.text_input("Enter first name")
            ln = st.text_input("Enter last name")
            gen = st.text_input("Enter gender")
            dob = st.text_input("Enter DOB")
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
            dob = st.text_input("Enter DOB", value=record.dob)
            phone = st.text_input("Enter phone number", value=record.phone)
            address = st.text_input("Enter address", value=record.address)
            if st.button('Update'):
                PatientRepository.update_patient(db, id, fn, ln, gen, dob, phone, address)
                st.success("Patient: {} {} successfully updated!".format(fn, ln))

        elif choice == "View Medicines":
            st.subheader("View Medicines")
            records = MedicineRepository.find_all_medicines(db)
            for record in records:
                st.markdown(html.view_medicines_temp.format(record.id, record.med_name,
                                                            record.med_type, record.cost),
                            unsafe_allow_html=True)

        elif choice == "Find Medicine By ID":
            st.subheader("Find Medicine By ID")
            record_ids = [record.id for record in MedicineRepository.find_all_medicines(db)]
            medicine_id = st.selectbox("Choose Medicine ID", record_ids)
            records = MedicineRepository.find_medicine_by_id(db, medicine_id)
            for rec in records:
                st.markdown(html.view_medicines_temp.format(rec.id, rec.med_name, rec.med_type, rec.cost),
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

        elif choice == "View Insurances":
            st.subheader("View Insurances")
            records = InsuranceRepository.find_all_insurances(db)
            for record in records:
                st.markdown(html.view_insurances_temp.format(record.id, record.provider_name,
                                                             record.exp_date, record.patient_id),
                            unsafe_allow_html=True)

        elif choice == "Find Insurance By ID":
            st.subheader("Find Insurance By ID")
            record_ids = [record.id for record in InsuranceRepository.find_all_insurances(db)]
            insurance_id = st.selectbox("Choose Insurance ID", record_ids)
            records = InsuranceRepository.find_insurance_by_id(db, insurance_id)
            for rec in records:
                st.markdown(html.view_insurances_temp.format(rec.id, rec.provider_name,
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

    finally:
        db.close()


if __name__ == '__main__':
    main()
