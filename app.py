import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Student Registration",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Registration Portal")
st.subheader("Smart Attendance System")
st.write("Register for face-recognition-based attendance.")

st.info("Please enter your correct student details.")

with st.form("student_registration"):

    student_id = st.text_input("Student ID")
    student_name = st.text_input("Full Name")

    st.write("### Face Registration")
    photo = st.camera_input("Capture your face")

    consent = st.checkbox(
        "I consent to the collection and use of my face image "
        "for the Smart Attendance System."
    )

    submitted = st.form_submit_button(
        "Submit Registration",
        use_container_width=True
    )

    if submitted:

        if not student_id or not student_name:
            st.error("Please enter your Student ID and Name.")

        elif not consent:
            st.warning("Consent is required to register.")

        elif photo is None:
            st.warning("Please capture your face using the camera.")

        else:
            st.success("Registration form completed successfully!")
            st.write("Student ID:", student_id)
            st.write("Student Name:", student_name)
            st.write("Registration Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

            st.info(
                "Your details have been submitted in this prototype. "
                "Permanent registration and attendance database integration "
                "will be configured in the next step."
            )

st.divider()
st.caption("Smart Attendance System | Student Registration")
