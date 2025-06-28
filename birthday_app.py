import streamlit as st
from PIL import Image
import base64
import os

# Page configuration
st.set_page_config(page_title="Happy Birthday Barnita 🎂", layout="centered")

# Title section
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday Barnita! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Music controls (styled & interactive)
col_play, col_stop = st.columns([1, 1])
with col_play:
    play = st.button("▶️ Play Birthday Song", use_container_width=True)
with col_stop:
    stop = st.button("⏹️ Stop Music", use_container_width=True)

# Background music logic
def embed_audio(audio_file, play=True):
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            html = f"""
            <audio id="audio" {'autoplay' if play else ''} loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <script>
                var audio = document.getElementById("audio");
                {'audio.play();' if play else 'audio.pause(); audio.currentTime = 0;'}
            </script>
            """
            st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Music file not found!")

if play:
    embed_audio("happy-birthday-357371.mp3", play=True)
elif stop:
    embed_audio("happy-birthday-357371.mp3", play=False)

# Balloons
st.balloons()

# Image display
cols = st.columns(3)
images = ["photo1.jpg", "photo3.jpg", "photo2.jpg"]
for i in range(3):
    with cols[i]:
        st.image(Image.open(images[i]), use_container_width=True)

# Footer
st.markdown("<p style='text-align: center;'>🎂 🎁 🎈</p>", unsafe_allow_html=True)
