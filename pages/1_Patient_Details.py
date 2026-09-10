import streamlit as st

st.set_page_config(
    page_title="Patient Details - CareFlow AI",
    page_icon="👤",
    layout="wide"
)

# Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("👤 Patient Details")
st.subheader("Enter patient information below.")

st.divider()

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=0,
    max_value=120,
    step=1
)

gender = st.selectbox(
    "Gender",
    ["Select", "Male", "Female", "Other"]
)

symptoms = st.text_area("Symptoms")

if st.button("Submit Patient Details", use_container_width=True):

    if name and gender != "Select" and symptoms:

        # Save patient details
        st.session_state["patient"] = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms
        }

        st.success("Patient details submitted successfully! ✅")

        st.write("### 📋 Patient Summary")
        st.write("**Name:**", name)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)
        st.write("**Symptoms:**", symptoms)

    else:
        st.warning("Please fill all required details.")