import os
import openai
import streamlit as st

os.environ["OPENAI_API_KEY"] = "api-key"
openai.api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(
    page_title="Audio Transcription & Feedback Tool",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.image("https://via.placeholder.com/300x100?text=Transcription+Tool", use_column_width=True)
    st.title("Navigation")
    st.markdown(
        """
        **Steps**:
        1. Upload an audio file.
        2. Get transcription in text.
        3. Translate to your target language.
        4. Receive grammar and pronunciation feedback.
        """
    )
    st.markdown("✨ Built for interactive and multi-language analysis.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🎙️ Audio Transcription, Translation, and Feedback Tool")
st.write("Analyze your audio files using OpenAI's Whisper and ChatGPT models.")

uploaded_file = st.file_uploader("📂 Upload an audio file (MP3, WAV)", type=["mp3", "wav"])

target_language = st.selectbox(
    "🌐 Select the target language for translation:",
    ["French", "Tamil", "Spanish", "German", "Hindi"],
)

target_text = st.text_area(
    "🗣️ Enter a target pronunciation sentence to compare with:",
    "Heat brings out flavor, cold restores, salt complements ham, tacos are a favorite, and hot cross buns are zestful.",
)

if uploaded_file is not None:
    with st.spinner("🔍 Processing audio..."):
        with open("uploaded_audio.mp3", "wb") as f:
            f.write(uploaded_file.read())

        with open("uploaded_audio.mp3", "rb") as audio_file:
            transcription_response = openai.Audio.transcribe("whisper-1", audio_file)
            transcription_text = transcription_response["text"]

        st.subheader("📜 Transcription")
        st.write(transcription_text)

        st.session_state.chat_history.append({"role": "system", "content": transcription_text})

        with st.spinner(f"🌐 Translating transcription to {target_language}..."):
            translation_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": f"Please translate the following text to {target_language}: {transcription_text}",
                    },
                ],
            )
            translated_text = translation_response["choices"][0]["message"]["content"]

        st.subheader(f"🌍 Translation ({target_language})")
        st.write(translated_text)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": translated_text}
        )

        with st.spinner("✍️ Providing grammar feedback..."):
            grammar_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a language learning assistant providing grammar feedback.",
                    },
                    {
                        "role": "user",
                        "content": f"Please correct any grammar mistakes in the following text and provide feedback: {translated_text}",
                    },
                ],
            )
            grammar_feedback = grammar_response["choices"][0]["message"]["content"]

        st.subheader("✅ Grammar Feedback")
        st.write(grammar_feedback)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": grammar_feedback}
        )

        with st.spinner("🗣️ Providing pronunciation feedback..."):
            pronunciation_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a language learning assistant providing pronunciation feedback.",
                    },
                    {
                        "role": "user",
                        "content": f"I said: {transcription_text}. How close is it to: {target_text}? Give feedback.",
                    },
                ],
            )
            pronunciation_feedback = pronunciation_response["choices"][0]["message"]["content"]

        st.subheader("🗣️ Pronunciation Feedback")
        st.write(pronunciation_feedback)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": pronunciation_feedback}
        )

st.markdown("## 💬 Chat History")
for entry in st.session_state.chat_history:
    role = "🟢 Assistant" if entry["role"] == "assistant" else "🟠 System/User"
    st.markdown(f"**{role}:** {entry['content']}")
