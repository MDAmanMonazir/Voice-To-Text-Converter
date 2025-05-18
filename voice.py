import streamlit as st
import speech_recognition as sr

# Page setup
st.set_page_config(page_title="Voice Notes for Scriptwriting", layout="centered")
st.title("🎙️ Voice-to-Text Notes for Scriptwriting")

# Initialize session state
if 'notes' not in st.session_state:
    st.session_state.notes = ""

# Microphone input
recognizer = sr.Recognizer()

def transcribe_audio():
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            st.success("Transcription complete!")
            return text
        except sr.WaitTimeoutError:
            st.warning("Listening timed out. Try again.")
        except sr.UnknownValueError:
            st.warning("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
    return ""

# Buttons and logic
if st.button("🎤 Start Recording"):
    transcript = transcribe_audio()
    if transcript:
        st.session_state.notes += transcript + "\n"

# Text area for reviewing/editing notes
edited_text = st.text_area("📝 Your Script Notes", st.session_state.notes, height=300)
st.session_state.notes = edited_text

# Save option
if st.download_button("💾 Download Notes", st.session_state.notes, file_name="script_notes.txt"):
    st.success("Notes downloaded!")


