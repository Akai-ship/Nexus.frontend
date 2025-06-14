
import streamlit as st
import requests

st.set_page_config(page_title="Nexus AI", layout="centered", page_icon="🧠")

st.title("🤖 Nexus AI")
st.markdown("Talk to your self-improving AI bot.")

user_id = st.text_input("Your name", value="user123")
message = st.text_area("Your message")

if st.button("Send"):
    if message.strip() != "":
        res = requests.post("https://nexus-backend.onrender.com/nexus/chat", json={"user_id": user_id, "message": message})
res = requests.post("https://nexus-backend.onrender.com/nexus/chat", json={"user_id": user_id, "message": message})

        st.markdown(res.json()['response'])
