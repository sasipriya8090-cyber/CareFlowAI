import streamlit as st

st.set_page_config(
    page_title="Care Tasks - CareFlow AI",
    page_icon="📝",
    layout="wide"
)

# Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("📝 Care Tasks")
st.subheader("Manage and coordinate healthcare tasks")

st.divider()

# Check patient details
patient = st.session_state.get("patient")

if not patient:
    st.warning("⚠️ Please submit patient details first.")
    st.stop()

# Current patient
st.header("👤 Current Patient")

col1, col2 = st.columns(2)

with col1:
    st.write("**Name:**", patient["name"])
    st.write("**Age:**", patient["age"])

with col2:
    st.write("**Gender:**", patient["gender"])
    st.write("**Symptoms:**", patient["symptoms"])

st.divider()

# Create task
st.header("➕ Create New Task")

task_name = st.text_input(
    "Task Name",
    placeholder="Example: Review patient report"
)

assigned_to = st.selectbox(
    "Assign To",
    [
        "Doctor",
        "Nurse",
        "Admin Staff",
        "Lab Team",
        "Pharmacy Team"
    ]
)

priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
)

status = st.selectbox(
    "Status",
    ["Pending", "In Progress", "Completed"]
)

if st.button("➕ Add Task", use_container_width=True):

    if task_name:

        # Save task
        st.session_state["care_task"] = {
            "patient_name": patient["name"],
            "task_name": task_name,
            "assigned_to": assigned_to,
            "priority": priority,
            "status": status
        }

        st.success("Task added successfully! ✅")

        st.divider()

        st.header("📋 Task Details")

        st.write("**Patient:**", patient["name"])
        st.write("**Task:**", task_name)
        st.write("**Assigned To:**", assigned_to)
        st.write("**Priority:**", priority)
        st.write("**Status:**", status)

    else:
        st.warning("Please enter a task name.")