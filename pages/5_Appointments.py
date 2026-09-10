import streamlit as st

st.set_page_config(
    page_title="Appointments - CareFlow AI",
    page_icon="📅",
    layout="wide"
)

# Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("📅 Appointments")
st.subheader("Manage patient appointments")

st.divider()

# Get patient details
patient = st.session_state.get("patient")

if not patient:
    st.warning("⚠️ Please submit patient details first.")
    st.stop()

st.header("👤 Current Patient")

col1, col2 = st.columns(2)

with col1:
    st.write("**Name:**", patient["name"])
    st.write("**Age:**", patient["age"])

with col2:
    st.write("**Gender:**", patient["gender"])
    st.write("**Symptoms:**", patient["symptoms"])

st.divider()

st.header("📅 Schedule Appointment")

appointment_date = st.date_input("Appointment Date")

appointment_time = st.time_input("Appointment Time")

doctor = st.selectbox(
    "Select Doctor",
    ["General Physician", "Specialist Doctor", "Consultant"]
)

appointment_type = st.selectbox(
    "Appointment Type",
    ["Consultation", "Follow-Up", "Test Review"]
)

if st.button("📅 Schedule Appointment", use_container_width=True):

    st.session_state["appointment"] = {
        "patient_name": patient["name"],
        "date": str(appointment_date),
        "time": str(appointment_time),
        "doctor": doctor,
        "type": appointment_type
    }

    st.success("Appointment scheduled successfully! ✅")

    st.divider()

    st.header("📋 Appointment Details")

    st.write("**Patient:**", patient["name"])
    st.write("**Date:**", appointment_date)
    st.write("**Time:**", appointment_time)
    st.write("**Doctor:**", doctor)
    st.write("**Type:**", appointment_type)