import streamlit as st
from langchain_ollama import ChatOllama

st.title("Chat with LLAMA3.2 🦙")
st.write("Welcome to the chatbot interface for LLAMA3.2! Type your message to begin the conversation. 💬" )

with st.form("llm-form"):
    text = st.text_area("What do you want to talk about?")
    submit = st.form_submit_button("Submit")

def generate_response(input_text):
    model = ChatOllama(model="llama3.2", base_url="http://localhost:11434/")

    response = model.invoke(input_text)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if submit and text:
    with st.spinner("LLAMA is typing...:"):
        response = generate_response(text)
        st.session_state["chat_history"].append({"user": text, "ollama": response})
        st.write(response)

st.write("Chat History")
for chat in st.session_state["chat_history"]:
    st.write(f"User: {chat['user']}")
    st.write(f"LLAMA: {chat['ollama']}")
    st.write("----")
