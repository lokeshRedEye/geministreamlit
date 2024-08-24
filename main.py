import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCt4QGnM8GpCKqBm55tsbaJw0gB54zMVWU")

st.set_page_config(page_title="Gemini Chat", page_icon=":robot_face:", layout="centered")

# Custom CSS to style the app
st.markdown("""
    <style>
    .chat-message {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 80%;
    }
    .user-message {
        background-color: black;
        text-align: right;
    }
    .bot-message {
        background-color: black;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Welcome to Gemini Chat :robot_face:")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Callback function to update session state
def submit():
    if st.session_state["input"]:
        # Append user message to history
        st.session_state.history.append({"role": "user", "content": st.session_state["input"]})
        
        # Load the generative model and start chat
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        
        # Get the response from the model
        response = chat.send_message(st.session_state["input"])
        
        # Append bot response to history
        st.session_state.history.append({"role": "bot", "content": response.text})
        
        # Clear the input box after sending
        st.session_state["input"] = ""

# Input for user question with a callback
st.text_input("Enter your question", key="input", on_change=submit)

# Display chat history
for message in st.session_state.history:
    if message['role'] == 'user':
        st.markdown(f"<div class='chat-message user-message'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-message bot-message'>{message['content']}</div>", unsafe_allow_html=True)
