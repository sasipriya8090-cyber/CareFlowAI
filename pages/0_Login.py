import streamlit as st

st.set_page_config(
    page_title="CareFlow AI - Login",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 CareFlow AI")
st.subheader("Healthcare Workflow & Care Coordination")

st.divider()

st.header("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

role = st.selectbox(
    "Select Role",
    ["Doctor", "Nurse", "Admin Staff"]
)

if st.button("🔓 Login", use_container_width=True):

    if username and password:
        st.success(f"Login successful! Welcome, {username} 👋")
        st.session_state["logged_in"] = True
        st.session_state["role"] = role
    else:
        st.warning("Please enter username and password.")