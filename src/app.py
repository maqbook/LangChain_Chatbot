import streamlit as st
from langchain_ollama import ChatOllama

st.title("Converse with LLAMA 🦙")

st.write("Chat away with LLAMA! 💬")

with st.form("llm-form"):
    text = st.text_area("What would like to talk about?")
    submit = st.form_submit_button("Enter")

def generate_response(input_text):
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434/")

    response = model.chat(input_text)
    return response.content

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

if submit and text:
    with st.spinner("LLAMA is typing..."):
        response = generate_response(text)
        st.session_state['chat_history'].append(("user": text, "LLAMA": response))
        st.write(response)
    response = generate_response(text)

st.write("## Chat History")
for chat in st.session_state['chat_history']:
    st.write(f"User: {chat['user']}")
    st.write(f"LLAMA: {chat['LLAMA']}")
    st.write("----")
