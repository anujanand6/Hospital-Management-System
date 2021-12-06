import streamlit as st
import html_templates as html
from repositories import DoctorRepository, PatientRepository, \
    MedicineRepository, InsuranceRepository
from database import SessionLocal, engine


def main():
    """
    A Simple CRUD implementation
    """

    st.markdown(html.title_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    menu = ["Home", "View Doctors", "View Patients", "View Medicines", "View Insurances",
            "Find Doctor By ID", "Create Doctor", "Update Doctor", "Delete Doctor By ID"]
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
                st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name, rec.specialist),
                            unsafe_allow_html=True)

        elif choice == "Find Doctor By ID":
            st.subheader("Find Doctor By ID")
            doc_id = st.text_input('Enter Doctor ID')
            records = DoctorRepository.find_doctor_by_id(db, doc_id)
            for rec in records:
                st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name, rec.specialist),
                            unsafe_allow_html=True)

        elif choice == "Create Doctor":
            st.subheader("Create Doctor")
            fn = st.text_input("Enter first name")
            ln = st.text_input("Enter last name")
            sp = st.selectbox("Enter Specialist",
                              ["CARDIOLOGIST", "FAMILY PHYSICIAN", "ONCOLOGIST",
                               "PEDIATRICIAN", "RADIOLOGIST"])
            if st.button('Create'):
                DoctorRepository.create_doctor(db, fn, ln, sp)
                st.success("Doctor: {} {} successfully created!".format(fn, ln))

        elif choice == "Delete Doctor By ID":
            st.subheader("Delete Doctor By ID")
            doctor_ids = [doc.id for doc in DoctorRepository.find_all_doctors(db)]
            doc_id = st.selectbox("Choose Doctor ID", doctor_ids)
            if st.button('Delete'):
                DoctorRepository.delete_doctor_by_id(db, doc_id)
                st.success("Doctor: {} successfully deleted!".format(doc_id))

        elif choice == "Update Doctor":
            st.subheader("Update Doctor")
            doctor_ids = [doc.id for doc in DoctorRepository.find_all_doctors(db)]
            id = st.selectbox("Choose Doctor ID", doctor_ids)
            fn = st.text_input("Enter first name")
            ln = st.text_input("Enter last name")
            sp = st.selectbox("Enter Specialist",
                              ["CARDIOLOGIST", "FAMILY PHYSICIAN", "ONCOLOGIST",
                               "PEDIATRICIAN", "RADIOLOGIST"])
            if st.button('Update'):
                DoctorRepository.update_doctor(db, id, fn, ln, sp)
                st.success("Doctor: {} {} successfully updated!".format(fn, ln))

        elif choice == "View Patients":
            st.subheader("View Patients")
            records = PatientRepository.find_all_patients(db)
            for rec in records:
                st.markdown(html.view_patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                           rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "View Medicines":
            st.subheader("View Medicines")
            records = MedicineRepository.find_all_medicines(db)
            for record in records:
                st.markdown(html.view_medicines_temp.format(record.id, record.med_name,
                                                            record.med_type, record.cost),
                            unsafe_allow_html=True)

        elif choice == "View Insurances":
            st.subheader("View Insurances")
            records = InsuranceRepository.find_all_insurances(db)
            for record in records:
                st.markdown(html.view_insurances_temp.format(record.insurance_number, record.provider_name,
                                                             record.exp_date, record.patient_id),
                            unsafe_allow_html=True)

    finally:
        db.close()


if __name__ == '__main__':
    main()
