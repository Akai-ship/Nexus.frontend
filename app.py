import streamlit as st
import requests

st.set_page_config(page_title="Nexus AI", layout="centered", page_icon="🤖")

st.markdown("# 🤖 Nexus AI")
st.markdown("Your self-improving, uncensored AI assistant. Ask anything. No filters.")

# Keep chat history in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_id = st.text_input("Your name", value="user123")
message = st.text_area("Ask Nexus anything...")

# Show full conversation
for entry in st.session_state.chat_history:
    st.markdown(f"**You:** {entry['user']}")
    st.markdown(f"**Nexus:** {entry['bot']}")

if st.button("Send"):
    if message.strip() != "":
        try:
            # Replace with your backend's actual URL
            api_url = "https://your-backend-url.onrender.com/nexus/chat"
            payload = {
                "user_id": user_id,
                "message": message
            }
            response = requests.post(api_url, json=payload, timeout=30)

            if response.status_code == 200:
                bot_reply = response.json().get("response", "No response from AI.")
                st.session_state.chat_history.append({
                    "user": message,
                    "bot": bot_reply
                })
                st.experimental_rerun()
            else:
                st.error(f"Server error: {response.status_code}")
        except Exception as e:
            st.error(f"Nexus crashed: {e}")
