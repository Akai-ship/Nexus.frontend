import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Nexus AI 2.0", layout="centered")

# Background CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    body {
        background: url("https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif") no-repeat center center fixed;
        background-size: cover;
        font-family: 'Orbitron', sans-serif;
        color: #00FF00;
    }

    .stButton>button {
        background-color: #000000;
        color: #00FF00;
        border: 1px solid #00FF00;
        font-family: 'Orbitron', sans-serif;
    }

    .stTextInput>div>div>input {
        background-color: #000000;
        color: #00FF00;
    }

    .stTextArea textarea {
        background-color: #000000;
        color: #00FF00;
    }
    </style>
""", unsafe_allow_html=True)

st.title("𝘶𝘳𝘻𝘰𝘯 𝘾𝘪 2.0")
st.markdown("Talk to your evolved AI brain")

# Voice Recorder Input (user has to use browser-side recorder)
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format='audio/mp3')

# Message Input
user_input = st.text_area("Enter your message:", height=100)

# Handle API Call
if st.button("Send"):
    if user_input:
        try:
            response = requests.post("http://localhost:5000/nexus/chat", json={"message": user_input})
            reply = response.json().get("reply", "[No reply received]")
            st.markdown(f"**Bot:** {reply}")
        except:
            st.error("Server unreachable. Make sure backend is running.")

# Image Generator UI
st.markdown("---")
st.subheader("Image Generator")
img_prompt = st.text_input("Image Prompt")
if st.button("Generate Image"):
    # Fake image gen, placeholder
    img = Image.new('RGB', (200, 200), color = (0, 255, 0))
    st.image(img, caption="Generated Image")

# Music Generator UI
st.markdown("---")
st.subheader("Music Generator")
music_prompt = st.text_input("Music Mood (e.g., chill, sad, epic)")
if st.button("Generate Music"):
    # Play sample music
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

# Video Generator UI
st.markdown("---")
st.subheader("Video Generator")
video_prompt = st.text_input("Video Prompt")
if st.button("Generate Video"):
    # Play sample video
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
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
