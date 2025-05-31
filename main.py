import streamlit as st
import pyttsx3
import PyPDF2
import tempfile

st.set_page_config(page_title="PDF to Speech", layout="centered")
st.title("📖🔊 PDF to Speech Reader")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    if st.button("🔊 Read Aloud"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        pdfreader = PyPDF2.PdfReader(tmp_path)
        pages = len(pdfreader.pages)

        engine = pyttsx3.init()

        for num in range(pages):
            text = pdfreader.pages[num].extract_text()
            if text:
                st.write(f"Reading page {num + 1}...")
                engine.say(text)
                engine.runAndWait()
            else:
                st.warning(f"No text found on page {num + 1}")

        st.success("Finished reading the PDF aloud.")
