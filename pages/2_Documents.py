import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="Documents - CareFlow AI",
    page_icon="📄",
    layout="wide"
)

# Login protection
if not st.session_state.get("logged_in", False):
    st.warning("🔐 Please login first.")
    st.stop()

st.title("📄 Patient Documents")
st.subheader("Upload, read and summarize patient documents")

st.divider()

# Get patient details
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

# Document upload
st.header("📤 Upload Patient Document")

uploaded_file = st.file_uploader(
    "Choose a PDF or TXT file",
    type=["pdf", "txt"]
)

if uploaded_file:

    # Save document upload status
    st.session_state["document_uploaded"] = True

    st.success("Document uploaded successfully! ✅")

    st.write("### 📋 Document Information")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)

    st.write(
        "**File Size:**",
        f"{uploaded_file.size / 1024:.2f} KB"
    )

    # Extract text
    document_text = ""

    if uploaded_file.type == "application/pdf":

        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                document_text += text + "\n"

    elif uploaded_file.type == "text/plain":

        document_text = uploaded_file.read().decode(
            "utf-8"
        )

    # Show document content
    if document_text.strip():

        st.divider()

        st.header("📄 Document Content")

        st.text_area(
            "Extracted Text",
            document_text,
            height=250
        )

        st.divider()

        # Summary
        st.header("🤖 AI Document Summary")

        if st.button(
            "✨ Generate Summary",
            use_container_width=True
        ):

            words = document_text.split()

            if len(words) > 80:
                summary = " ".join(words[:80]) + "..."
            else:
                summary = document_text

            st.success(
                "Summary generated successfully! ✅"
            )

            st.write("### 📋 Summary")

            st.write(summary)

            st.write("### 🔍 Key Information")

            st.write(
                f"**Document Length:** {len(words)} words"
            )

            st.write(
                "**Patient:**",
                patient["name"]
            )

            st.write(
                "**Status:** Document successfully processed"
            )

    else:

        st.warning(
            "⚠️ No readable text found in this document."
        )