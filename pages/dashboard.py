import streamlit as st

st.set_page_config(
    page_title="CareFlow AI",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏥 CareFlow AI")
st.subheader(
    "AI-Powered Healthcare Workflow & Care Coordination Platform"
)

st.divider()

st.write(
    "CareFlow AI helps healthcare organizations manage "
    "patients, documents, care tasks, follow-ups and appointments "
    "through one organized healthcare workflow."
)

# --------------------------------------------------
# GET SAVED INFORMATION
# --------------------------------------------------

patient = st.session_state.get("patient")
document_uploaded = st.session_state.get(
    "document_uploaded", False
)
care_task = st.session_state.get("care_task")
followup = st.session_state.get("followup")
appointment = st.session_state.get("appointment")

# --------------------------------------------------
# DASHBOARD SUMMARY
# --------------------------------------------------

st.header("📊 Healthcare Workflow Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "👤 Patient",
        "Added" if patient else "Pending"
    )

with col2:
    st.metric(
        "📄 Document",
        "Uploaded" if document_uploaded else "Pending"
    )

with col3:
    st.metric(
        "✅ Care Task",
        "Created" if care_task else "Pending"
    )

with col4:
    st.metric(
        "🔔 Follow-Up",
        "Scheduled" if followup else "Pending"
    )

with col5:
    st.metric(
        "📅 Appointment",
        "Scheduled" if appointment else "Pending"
    )

st.divider()

# --------------------------------------------------
# PATIENT DETAILS
# --------------------------------------------------

if patient:

    st.header("👤 Patient Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Name**")
        st.write(patient.get("name", "N/A"))

        st.write("**Age**")
        st.write(patient.get("age", "N/A"))

    with col2:
        st.write("**Gender**")
        st.write(patient.get("gender", "N/A"))

        st.write("**Symptoms**")
        st.write(patient.get("symptoms", "N/A"))

    with col3:
        st.write("**Patient ID**")
        st.write(patient.get("patient_id", "N/A"))

        st.write("**Status**")
        st.write("Active")

else:

    st.info(
        "👤 No patient details available yet. "
        "Please add a patient from Patient Details."
    )

st.divider()

# --------------------------------------------------
# WORKFLOW
# --------------------------------------------------

st.header("🔄 Patient Care Workflow")

col1, col2, col3, col4, col5 = st.columns(5)

# Patient
with col1:

    if patient:
        st.success("✅ Patient Details")
    else:
        st.warning("⏳ Patient Details")

# Document
with col2:

    if document_uploaded:
        st.success("✅ Document")
    else:
        st.warning("⏳ Document")

# Care Task
with col3:

    if care_task:
        st.success("✅ Care Task")
    else:
        st.warning("⏳ Care Task")

# Follow-up
with col4:

    if followup:
        st.success("✅ Follow-Up")
    else:
        st.warning("⏳ Follow-Up")

# Appointment
with col5:

    if appointment:
        st.success("✅ Appointment")
    else:
        st.warning("⏳ Appointment")

st.divider()

# --------------------------------------------------
# DETAILS OF WORKFLOW
# --------------------------------------------------

st.header("📋 Workflow Details")

if document_uploaded:

    st.success("📄 Patient document has been uploaded.")

else:

    st.info("📄 No document uploaded yet.")

if care_task:

    st.success(
        f"✅ Care Task: {care_task}"
    )

else:

    st.info("✅ No care task created yet.")

if followup:

    st.success(
        f"🔔 Follow-Up: {followup}"
    )

else:

    st.info("🔔 No follow-up scheduled yet.")

if appointment:

    st.success(
        f"📅 Appointment: {appointment}"
    )

else:

    st.info("📅 No appointment scheduled yet.")

st.divider()

# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

st.header("🏥 CareFlow AI Status")

if patient and document_uploaded and care_task and followup and appointment:

    st.success(
        "🎉 Complete patient workflow is available."
    )

else:

    st.warning(
        "⚠️ Patient workflow is partially completed. "
        "Complete the pending modules."
    )

st.divider()

st.caption(
    "CareFlow AI | Healthcare Workflow & Care Coordination Platform"
)