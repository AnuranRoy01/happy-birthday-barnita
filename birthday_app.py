import streamlit as st
from PIL import Image
import time

# Page config
st.set_page_config(page_title="Happy Birthday Barnita", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: hotpink;'>🎉 Happy Birthday Didivalu! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Background music
def add_bg_music(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

add_bg_music("happy-birthday-357371.mp3")  # File must be uploaded to GitHub repo

# Image Display Section
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Some Beautiful Memories</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    image1 = Image.open("IMG_5365.HEIC")
    st.image(image1, caption="💐 Barnita & You", use_container_width=True)

with col2:
    image2 = Image.open("IMG_5368.PNG")
    st.image(image2, caption="🌸 Puja Celebration", use_container_width=True)

with col3:
    image3 = Image.open("IMG_5367.PNG")
    st.image(image3, caption="🍰 Smiles & Peace", use_container_width=True)

# Closing note
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>Hope you liked this little surprise! 🎁</h4>", unsafe_allow_html=True)
st.balloons()
