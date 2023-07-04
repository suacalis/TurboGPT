#Author Tushar Aggarwal(https://www.tushar-aggarwal.com/)(https://github.com/tushar2704)
# TurboGPT

import streamlit as st
import openai

# Application title and body
st.set_page_config(page_title="🤖TurboGPT🤖",
                   page_icon="🤖",
                   layout='wide')
# Title of application
st.title("🤖TurboGPT")
st.markdown("### By [Tushar Aggarwal](https://www.tushar-aggarwal.com/)")

# Initialize OpenAI API

st.sidebar.markdown("## OpenAI API Key")

api_key = st.sidebar.text_input("Enter your OpenAI API key")
if not api_key:
    st.write("Please enter your OpenAI API key first. Don't worry this will not be stored.")
    st.stop()

openai.api_key = api_key

#model session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"]="gpt-3.5-turbo"


#initializing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#react to user input
prompt = st.chat_input("How can i help you today?")

if prompt:
    #display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #adding user message to chat history
    st.session_state.messages.append({"role":"user", "content":prompt})
    
    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        full_response=""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role":m["role"], "content":m['content']}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response+=response.choices[0].delta.get("content","")
            message_placeholder.markdown(full_response +"")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant", "content":full_response})
    
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)























