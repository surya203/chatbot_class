# A simple chatbot using streamlit and OpenAI API in terminal

import streamlit as st
from openai import OpenAI
import os
from langchain_community.tools import YouTubeSearchTool 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

#Streamlit chatbot application with UI and OpenAI API
st.set_page_config(page_title="Chatbot with OpenAI API", page_icon=":robot:")   
st.title("Chatbot with OpenAI API")

#chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Enter your question: "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(get_response(prompt))
    st.session_state.messages.append({"role": "assistant", "content": get_response(prompt)})

#input field for youtube search
"""
tool = YouTubeSearchTool()

tool.run("Logiqgen ai nestham product")
"""
input_field = st.text_input("Enter a YouTube search query: ")
if st.button("Search"):
    st.write(YouTubeSearchTool().run(input_field))









