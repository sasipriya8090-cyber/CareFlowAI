import streamlit as st

st.set_page_config(
    page_title="Follow-Ups - CareFlow AI",
    page_icon="🔔",
    layout="wide"
)

# Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("🔔 Patient Follow-Ups")
st.subheader("Manage pending patient follow-ups")

st.divider()

# Get patient
patient = st.session_state.get("patient")

if not patient:
    st.warning("⚠️ Please submit patient details first.")
    st.stop()

st.header("👤 Current Patient")

st.write("**Name:**", patient["name"])
st.write("**Age:**", patient["age"])
st.write("**Symptoms:**", patient["symptoms"])

st.divider()

st.header("📅 Follow-Up Details")

followup_date = st.date_input("Follow-Up Date")

followup_reason = st.text_input(
    "Follow-Up Reason",
    placeholder="Example: Review test results"
)

assigned_to = st.selectbox(
    "Follow-Up Assigned To",
    ["Doctor", "Nurse", "Admin Staff"]
)

if st.button("🔔 Schedule Follow-Up", use_container_width=True):

    if followup_reason:

        st.session_state["followup"] = {
            "patient_name": patient["name"],
            "date": str(followup_date),
            "reason": followup_reason,
            "assigned_to": assigned_to
        }

        st.success("Follow-up scheduled successfully! ✅")

        st.write("### 📋 Follow-Up Details")
        st.write("**Patient:**", patient["name"])
        st.write("**Date:**", followup_date)
        st.write("**Reason:**", followup_reason)
        st.write("**Assigned To:**", assigned_to)

    else:
        st.warning("Please enter the follow-up reason.")