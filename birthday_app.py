import streamlit as st
from PIL import Image
import base64
import os

# Page configuration
st.set_page_config(page_title="Happy Birthday Barnita 🎂", layout="centered")

# Set a birthday image background
st.markdown("""
<style>
.stApp {
    background-image: url("https://i.ibb.co/7JfqXxB/birthday-bg.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday Barnita! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Load and base64 encode the audio file
def get_audio_base64(audio_file):
    if os.path.exists(audio_file):
        with open(audio_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

audio_b64 = get_audio_base64("happy-birthday-357371.mp3")

# Music control buttons with enhanced styling
st.markdown("""
<style>
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    gap: 30px;
}
.stButton > button {
    background-color: #ff69b4;
    color: white;
    padding: 0.6em 2em;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 0 15px #ff69b4;
    transition: all 0.3s ease-in-out;
}
.stButton > button:hover {
    background-color: #ff1493;
    transform: scale(1.08);
    box-shadow: 0 0 25px #ff1493;
}
</style>
""", unsafe_allow_html=True)

# Interactive play/stop buttons
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    play = st.button("▶️ Play Birthday Song")
with col2:
    stop = st.button("⏹️ Stop Music")
st.markdown('</div>', unsafe_allow_html=True)

# Music control logic
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

# Balloons
st.balloons()

# Image display
cols = st.columns(3)
images = ["photo1.jpg", "photo3.jpg", "photo2.jpg"]
for i in range(3):
    with cols[i]:
        st.image(Image.open(images[i]), use_container_width=True)

# Footer
st.markdown("<p style='text-align: center; font-size: 24px;'>🎂 🎁 🎈 With love and joy 💖</p>", unsafe_allow_html=True)
