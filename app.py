import streamlit as st
import html_templates as html
import repositories
from database import SessionLocal, engine


def main():
    """
    A Simple CRUD implementation
    """

    st.markdown(html.title_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    menu = ["Home", "View Doctors", "View Patients", "View Medicines", "View Insurances"]
    choice = st.sidebar.selectbox("Menu", menu)

    try:
        db = SessionLocal()

        if choice == "Home":
            st.subheader("Choose one table")
            st.markdown(html.home_temp, unsafe_allow_html=True)

        elif choice == "View Doctors":
            st.subheader("View Doctors")
            records = repositories.DoctorRepository.find_all_doctors(db)
            for rec in records:
                st.markdown(html.view_doctors_temp.format(rec.id, rec.first_name, rec.last_name, rec.specialist),
                            unsafe_allow_html=True)

        elif choice == "View Patients":
            st.subheader("View Patients")
            records = repositories.PatientRepository.find_all_patients(db)
            for rec in records:
                st.markdown(html.view_patients_temp.format(rec.id, rec.first_name, rec.last_name,
                                                           rec.gender, rec.dob, rec.phone, rec.address),
                            unsafe_allow_html=True)

        elif choice == "View Medicines":
            st.subheader("View Medicines")
            records = repositories.MedicineRepository.find_all_medicines(db)
            for record in records:
                st.markdown(html.view_medicines_temp.format(record.id, record.med_name,
                                                            record.med_type, record.cost),
                            unsafe_allow_html=True)

        elif choice == "View Insurances":
            st.subheader("View Insurances")
            records = repositories.InsuranceRepository.find_all_insurances(db)
            for record in records:
                st.markdown(html.view_insurances_temp.format(record.insurance_number, record.provider_name,
                                                             record.exp_date, record.patient_id),
                            unsafe_allow_html=True)

    finally:
        db.close()


if __name__ == '__main__':
    main()
