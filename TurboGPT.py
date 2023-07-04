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