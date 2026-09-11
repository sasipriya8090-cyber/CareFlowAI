import streamlit as st
import PyPDF2
import google.generativeai as genai
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

genai_model = genai.GenerativeModel("gemini-1.5-flash")
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="CareFlow AI",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏥 CareFlow AI")

st.subheader(
    "AI-Powered Healthcare Workflow & Care Coordination Platform"
)

st.divider()

st.write(
    "CareFlow AI helps healthcare organizations manage "
    "patients, documents, care tasks, follow-ups and "
    "appointments through one organized workflow."
)
# --------------------------------------------------
# PATIENT INTAKE - PHASE 2
# --------------------------------------------------

st.sidebar.header("👤 Patient Intake")

patient_name = st.sidebar.text_input("Patient Name")

patient_age = st.sidebar.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=0
)

patient_gender = st.sidebar.selectbox(
    "Gender",
    ["Select", "Male", "Female", "Other"]
)

patient_phone = st.sidebar.text_input("Phone Number")

patient_reason = st.sidebar.text_area(
    "Reason for Visit"
)

if st.sidebar.button("➕ Add Patient"):

    if patient_name and patient_gender != "Select":

        st.session_state["patient"] = {
            "Name": patient_name,
            "Age": patient_age,
            "Gender": patient_gender,
            "Phone": patient_phone,
            "Reason": patient_reason
        }

        st.success("✅ Patient added successfully!")

    else:

        st.warning(
            "Please enter Patient Name and select Gender."
        )


# --------------------------------------------------
# PATIENT INFORMATION
# --------------------------------------------------

if "patient" in st.session_state:

    st.header("👤 Patient Information")

    patient = st.session_state["patient"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Name:**", patient["Name"])

    with col2:
        st.write("**Age:**", patient["Age"])

    with col3:
        st.write("**Gender:**", patient["Gender"])

    st.write("**Phone:**", patient["Phone"])
    st.write("**Reason for Visit:**", patient["Reason"])

    st.divider()
    # --------------------------------------------------
# DOCUMENT UPLOAD - PHASE 2
# --------------------------------------------------

st.sidebar.header("📄 Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload Healthcare Document",
    type=["pdf", "txt"]
)
if uploaded_file is not None:

    st.header("📄 Patient Document")

    st.success(
        f"Document uploaded successfully: {uploaded_file.name}"
    )

    if uploaded_file.type == "text/plain":

        document_text = uploaded_file.read().decode("utf-8")

        st.subheader("Document Content")
        st.text_area(
            "Uploaded Text",
            document_text,
            height=250
        ) 
    elif uploaded_file.type == "application/pdf":

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        document_text = ""

        for page in pdf_reader.pages:
            document_text += page.extract_text() or ""

        st.subheader("🤖 AI Patient Summary")

        if st.button("✨ Generate AI Summary"):

            prompt = f"""
            Summarize this healthcare document.
            Use only the information present in the document.
            Do not invent information.

            Document:
            {document_text}
            """

            response = genai_model.generate_content(prompt)

            st.success("✅ AI Summary Generated")

            st.write(response.text)
            # --------------------------------------------------
# CARE TASKS - PHASE 2
# --------------------------------------------------

st.sidebar.header("✅ Care Tasks")

task_name = st.sidebar.text_input("Task")

task_assignee = st.sidebar.text_input("Assigned To")

task_priority = st.sidebar.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

if st.sidebar.button("➕ Add Task"):

    if task_name:

        st.session_state["care_task"] = {
            "Task": task_name,
            "Assigned To": task_assignee,
            "Priority": task_priority,
            "Status": "Pending"
        }

        st.success("✅ Care task added successfully!")

    else:

        st.warning("Please enter a task.")


# --------------------------------------------------
# CARE TASK INFORMATION
# --------------------------------------------------

if "care_task" in st.session_state:

    st.header("✅ Care Task")

    task = st.session_state["care_task"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Task:**", task["Task"])

    with col2:
        st.write("**Assigned To:**", task["Assigned To"])

    with col3:
        st.write("**Priority:**", task["Priority"])

    with col4:
        st.write("**Status:**", task["Status"])
        # --------------------------------------------------
# APPOINTMENTS - PHASE 2
# --------------------------------------------------

st.sidebar.header("📅 Appointments")

appointment_date = st.sidebar.date_input(
    "Appointment Date"
)

appointment_time = st.sidebar.time_input(
    "Appointment Time"
)

doctor_name = st.sidebar.text_input(
    "Doctor Name"
)

if st.sidebar.button("📅 Schedule Appointment"):

    st.session_state["appointment"] = {
        "Date": appointment_date,
        "Time": appointment_time,
        "Doctor": doctor_name,
        "Status": "Scheduled"
    }

    st.success("✅ Appointment scheduled successfully!")


# --------------------------------------------------
# APPOINTMENT INFORMATION
# --------------------------------------------------

if "appointment" in st.session_state:

    st.header("📅 Appointment")

    appointment = st.session_state["appointment"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Date:**", appointment["Date"])

    with col2:
        st.write("**Time:**", appointment["Time"])

    with col3:
        st.write("**Doctor:**", appointment["Doctor"])

    with col4:
        st.write("**Status:**", appointment["Status"])
        # --------------------------------------------------
# FOLLOW-UPS - PHASE 2
# --------------------------------------------------

st.sidebar.header("🔔 Follow-ups")

followup_date = st.sidebar.date_input(
    "Follow-up Date"
)

followup_reason = st.sidebar.text_input(
    "Follow-up Reason"
)

followup_person = st.sidebar.text_input(
    "Follow-up Assigned To"
)

if st.sidebar.button("🔔 Schedule Follow-up"):

    if followup_reason:

        st.session_state["followup"] = {
            "Date": followup_date,
            "Reason": followup_reason,
            "Assigned To": followup_person,
            "Status": "Pending"
        }

        st.success("✅ Follow-up scheduled successfully!")

    else:

        st.warning("Please enter follow-up reason.")


# --------------------------------------------------
# FOLLOW-UP INFORMATION
# --------------------------------------------------

if "followup" in st.session_state:

    st.header("🔔 Follow-up")

    followup = st.session_state["followup"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Date:**", followup["Date"])

    with col2:
        st.write("**Reason:**", followup["Reason"])

    with col3:
        st.write("**Assigned To:**", followup["Assigned To"])

    with col4:
        st.write("**Status:**", followup["Status"])
        # --------------------------------------------------
# NOTIFICATIONS - PHASE 2
# --------------------------------------------------

st.sidebar.header("🔔 Notifications")

notification_message = st.sidebar.text_area(
    "Notification Message"
)

notification_type = st.sidebar.selectbox(
    "Notification Type",
    ["Appointment Reminder", "Follow-up Reminder", "Task Reminder"]
)

if st.sidebar.button("📢 Send Notification"):

    if notification_message:

        st.session_state["notification"] = {
            "Type": notification_type,
            "Message": notification_message,
            "Status": "Sent"
        }

        st.success("✅ Notification sent successfully!")

    else:

        st.warning("Please enter a notification message.")


# --------------------------------------------------
# NOTIFICATION INFORMATION
# --------------------------------------------------

if "notification" in st.session_state:

    st.header("🔔 Notification")

    notification = st.session_state["notification"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Type:**", notification["Type"])

    with col2:
        st.write("**Message:**", notification["Message"])

    with col3:
        st.write("**Status:**", notification["Status"])
        # --------------------------------------------------
# ROLE-BASED ACCESS - PHASE 2
# --------------------------------------------------

st.sidebar.header("👥 User Role")

user_role = st.sidebar.selectbox(
    "Select Role",
    ["Doctor", "Nurse", "Receptionist", "Admin"]
)

st.session_state["user_role"] = user_role

st.header("👥 Current User Role")

st.info(f"Logged in as: {user_role}")

if user_role == "Doctor":
    st.write("🩺 Doctor can review patient documents and manage care tasks.")

elif user_role == "Nurse":
    st.write("👩‍⚕️ Nurse can manage follow-ups and patient care tasks.")

elif user_role == "Receptionist":
    st.write("🧑‍💼 Receptionist can manage patients and appointments.")

elif user_role == "Admin":
    st.write("👨‍💼 Admin can manage the overall healthcare workflow.")
    # --------------------------------------------------
# APPROVALS & DEPARTMENT WORKFLOW - PHASE 2
# --------------------------------------------------

st.sidebar.header("✅ Approvals")

department = st.sidebar.selectbox(
    "Department",
    ["Reception", "Nursing", "Doctor", "Laboratory", "Pharmacy"]
)

approval_item = st.sidebar.text_input("Approval Request")

if st.sidebar.button("✅ Submit for Approval"):

    if approval_item:
        st.session_state["approval"] = {
            "Department": department,
            "Request": approval_item,
            "Status": "Pending Approval"
        }

        st.success("✅ Approval request submitted!")
    else:
        st.warning("Please enter an approval request.")


if "approval" in st.session_state:

    st.header("✅ Department Approval")

    approval = st.session_state["approval"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Department:**", approval["Department"])

    with col2:
        st.write("**Request:**", approval["Request"])

    with col3:
        st.write("**Status:**", approval["Status"])