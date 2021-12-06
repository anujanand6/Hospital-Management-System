import streamlit as st
import repositories
from database import SessionLocal, engine


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


head_message_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h6>First Name: {}</h6>
	<h6>Last Name: {}</h6>
	<h6>Specialist: {}</h6>
	</div>
	"""

# full_message_temp = """
# 	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
# 		<p style="text-align:justify;color:black;padding:10px">{}</p>
# 	</div>
# 	"""

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


def main():
    """
    A Simple CRUD implementation
    """

    html_temp = """
    	<div style="background-color:{};padding:10px;border-radius:10px">
    	<h1 style="color:{};text-align:center;"> Hospital Management System </h1>
    	</div>
    	"""

    st.markdown(html_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    menu = ["Home", "View Doctors", "View Patients", "View Medicines", "View Insurances"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Choose one table")
        st.text("Doctors")
        st.text("Patients")
        st.text("Medicines")
        st.text("Insurances")

    elif choice == "View Doctors":
        st.subheader("View Doctors")
        db = SessionLocal()
        records = repositories.DoctorRepository.find_all_doctors(db)
        for rec in records:
            st.markdown(head_message_temp.format(rec.first_name, rec.last_name, rec.specialist), unsafe_allow_html=True)
        db.close()

    elif choice == "Add Doctors":
        st.subheader("Add")

    elif choice == "Search Doctors":
        st.subheader("Search")

    elif choice == "Manage Doctors":
        st.subheader("Manage")


if __name__ == '__main__':
    main()
