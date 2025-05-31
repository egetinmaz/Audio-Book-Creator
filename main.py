import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import os
import tempfile

st.set_page_config(page_title="PDF to Speech", layout="centered")

st.title("📚 PDF to Speech Reader")
st.markdown("Upload a PDF and listen to it as audio.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    try:
        # Read the PDF
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        if text.strip() == "":
            st.warning("Couldn't extract any text from the PDF.")
        else:
            # Convert text to speech using gTTS
            tts = gTTS(text)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                st.audio(tmp_file.name, format="audio/mp3")
                st.success("✅ Audio generated successfully!")

    except Exception as e:
        st.error(f"⚠️ Something went wrong: {e}")
