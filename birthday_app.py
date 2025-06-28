
import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Barnita", page_icon="🎉", layout="centered")

st.markdown("<h1 style='text-align: center; color: hotpink;'>🎂 Happy Birthday Barnita! 🎉</h1>", unsafe_allow_html=True)

# Show loading spinner
with st.spinner("Preparing your birthday surprise..."):
    time.sleep(2)

st.balloons()

# Custom message
st.markdown("""
<div style='text-align: center;'>
    <h3 style='color: purple;'>Happy Birthday Didivalu. Many Many Happiest Returns of the Day.. 💖</h3>
</div>
""", unsafe_allow_html=True)

# Show images
st.image("photo1.jpg", caption="✨ Sweet Memories ✨", use_column_width=True)
st.image("photo2.jpg", caption="🌸 Smile and Shine 🌸", use_column_width=True)
st.image("photo3.jpg", caption="💞 Forever Moments 💞", use_column_width=True)

# Play birthday song
audio_file = open("happy_birthday.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

# Confetti emojis
st.markdown("<div style='text-align: center; font-size: 30px;'>🎉🥳🎁🎈🎂💝✨</div>", unsafe_allow_html=True)
