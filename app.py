import streamlit as st

def main():
    """
    A Simple CRUD implementation
    """
    st.title("Hospital Management System")

    menu = ["Home", "View Posts", "Add posts",
            "Search", "Manage"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "View Posts":
        st.subheader("View Posts")

    elif choice == "Add Posts":
        st.subheader("Add Posts")

    elif choice == "Search":
        st.subheader("Search")

    elif choice == "Manage":
        st.subheader("Manage")


if __name__ == '__main__':
    main()