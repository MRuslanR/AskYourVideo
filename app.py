import streamlit as st
import tempfile
import os

from utils.audio_processing import convert_video_to_audio
from utils.speech_recognition import transcribe_audio
from utils.text_processing import load_qwen_model, generate_response


st.title("AskYourVideo")

# Инициализация состояния сессии
if "transcription" not in st.session_state:
    st.session_state.transcription = None
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []


video_file = st.file_uploader("Загрузите видео для распознования речи на нем: ", type=["mp4"])

# Загрузка модели Qwen
model, tokenizer = load_qwen_model()

if video_file:
    with tempfile.TemporaryDirectory() as tmpdir:
        video_path = os.path.join(tmpdir, "video.mp4")

        with open(video_path, "wb") as f:
            f.write(video_file.read())

        audio_path = convert_video_to_audio(video_path, tmpdir)

        if st.session_state.transcription is None:
            with st.spinner("Идет распознавание аудио..."):
                st.session_state.transcription = transcribe_audio(audio_path)

    st.subheader("Результат распознавания:")
    st.write(st.session_state.transcription["text"])

if st.session_state.transcription:
    st.subheader("Задайте вопрос нейросети по содержанию:")

    # Отображение истории чата
    for user_question, response in st.session_state.qa_history:
        with st.chat_message("user"):
            st.write(user_question)
        with st.chat_message("assistant"):
            st.write(response)

    user_question = st.chat_input("Задайте вопрос по содержанию видео:")

    if user_question:
        with st.chat_message("user"):
            st.write(user_question)

        with st.spinner("Генерация ответа..."):
            full_context = st.session_state.transcription["text"]
            response = generate_response(model, tokenizer, user_question, full_context)

        st.session_state.qa_history.append((user_question, response))

        with st.chat_message("assistant"):
            st.write(response)
