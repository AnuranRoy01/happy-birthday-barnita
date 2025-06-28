import streamlit as st
from PIL import Image
import base64
import os

# Page configuration
st.set_page_config(page_title="Happy Birthday Barnita 🎂", layout="centered")

# Title section
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday Barnita! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Balloons animation
st.balloons()

# Image display in 3 columns (unchanged)
cols = st.columns(3)
images = ["photo1.jpg", "photo3.jpg", "photo2.jpg"]
for i in range(3):
    with cols[i]:
        st.image(Image.open(images[i]), use_container_width=True)

# Play Music Button
if st.button("▶️ Play Birthday Song"):
    def play_music(filepath):
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                html_code = f"""
                    <audio autoplay loop>
                        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                """
                st.markdown(html_code, unsafe_allow_html=True)
        else:
            st.warning("Music file not found!")

    # Call the function with the audio file
    play_music("happy-birthday-357371.mp3")

# Footer
st.markdown("<p style='text-align: center;'>🎂 🎁 🎈</p>", unsafe_allow_html=True)
