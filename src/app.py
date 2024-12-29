import streamlit as st
from langchain_ollama import ChatOllama

# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
local_css("styles.css")
st.title("Chat with LLAMA3.2 🦙")
st.write("Welcome to the chatbot interface for LLAMA3.2! Type your message to begin the conversation. 💬" )

with st.form("llm-form"):
    text = st.text_area("What do you want to talk about?")
    col1, col2 = st.columns([3, 1])
    with col1:
        submit = st.form_submit_button("Enter")
    with col2:
        if st.form_submit_button("Clear Chat History"):
            st.session_state["chat_history"] = []
            st.success("Chat history cleared!")



def generate_response(input_text):
    model = ChatOllama(model="llama3.2", base_url="http://localhost:11434/")

    response = model.invoke(input_text)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if submit and text:
    with st.spinner("LLAMA is generating a response..."):
        response = generate_response(text)
        st.session_state["chat_history"].append({"user": text, "ollama": response})
        st.write(response)

st.write("📜 Chat History 📜")
for chat in st.session_state["chat_history"]:
    with st.expander(f"🧍User: {chat['user']}", expanded=False):
        st.write(f"🦙LLAMA: {chat['ollama']}")

