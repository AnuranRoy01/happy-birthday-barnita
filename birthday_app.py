import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Happy Birthday Barnita", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: hotpink;'>🎉 Happy Birthday Didivalu! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Many Many Happiest Returns of the Day.. 💖</h3>", unsafe_allow_html=True)

# Background music with autoplay using custom HTML
def add_bg_music(file_path):
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{file_path}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """,
        unsafe_allow_html=True
    )

add_bg_music("happy-birthday-357371.mp3")  # Make sure this file is uploaded in GitHub

# Image Display Section
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Some Beautiful Memories</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    image1 = Image.open("IMG_5365_converted.PNG")  # <-- Replace this with converted version of the .HEIC file
    st.image(image1, caption="💐 Me & You", use_container_width=True)

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
