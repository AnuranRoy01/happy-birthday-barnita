import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Happy Birthday Barnita 🎂", layout="centered")

# Custom Title
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Happy Birthday Ddidivalu! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Add confetti
st.balloons()

# Display images in a row
cols = st.columns(3)

images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
for i in range(3):
    with cols[i]:
        st.image(Image.open(images[i]), use_column_width=True)

# Background music
def add_bg_music(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

add_bg_music("happy_birthday.mp3")

# Optional: subtle footer or emoji
st.markdown("<p style='text-align: center;'>🎂 🎁 🎈</p>", unsafe_allow_html=True)
