import streamlit as st
from PIL import Image
import base64
import os
import time

# Page config
st.set_page_config(page_title="Happy Birthday Barnita 🎂", layout="centered")

# Custom dynamic background
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #fce4ec, #f8bbd0, #f48fb1, #f06292);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday Barnita! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Party popper animation
for _ in range(3):
    st.markdown("<p style='font-size:30px; text-align:center;'>🎊 🎉 🎈 🥳 🎁 🎂</p>", unsafe_allow_html=True)
    time.sleep(0.5)

# Music encode function
def get_audio_base64(audio_file):
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

audio_b64 = get_audio_base64("happy-birthday-357371.mp3")

# Interactive buttons with fancy styling
st.markdown("""
<style>
.button-row {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 20px;
    margin-bottom: 30px;
}
.stButton > button {
    background-color: #e91e63;
    color: white;
    font-weight: bold;
    font-size: 18px;
    padding: 0.7em 2em;
    border: none;
    border-radius: 12px;
    box-shadow: 0 0 10px #e91e63;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #c2185b;
    transform: scale(1.1);
    box-shadow: 0 0 20px #f06292;
}
</style>
""", unsafe_allow_html=True)

# Button interaction row
st.markdown('<div class="button-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    play = st.button("▶️ Play Birthday Song")
with col2:
    stop = st.button("⏹️ Stop Music")
st.markdown('</div>', unsafe_allow_html=True)

# Handle music control
if play and audio_b64:
    st.markdown(f"""
        <audio id="audio" autoplay loop>
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
        <script>
            const audio = document.getElementById("audio");
            audio.play();
        </script>
    """, unsafe_allow_html=True)

elif stop:
    st.markdown("""
        <script>
            const oldAudio = document.getElementById("audio");
            if (oldAudio) {
                oldAudio.pause();
                oldAudio.remove();
            }
        </script>
    """, unsafe_allow_html=True)

# Balloons every 3 seconds (simulated repeat)
for _ in range(3):
    st.balloons()
    time.sleep(3)

# Image gallery
cols = st.columns(3)
images = ["photo1.jpg", "photo3.jpg", "photo2.jpg"]
for i in range(3):
    with cols[i]:
        st.image(Image.open(images[i]), use_container_width=True)

# Footer
st.markdown("<p style='text-align: center; font-size:24px;'>🎂 🎁 🎈 With love and joy 💖</p>", unsafe_allow_html=True)
