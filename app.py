import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="text_summarizer", device=-1)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def summarize(text, max_len, min_len):
    with st.spinner("Summarizing the given text..."):
        summarized_text = summarizer(text, max_length=max_len, min_length=min_len)
    st.info(summarized_text[0]['summary_text'])

st.header("Text Summarizer")

input_text = st.text_area("Input Text to Summarize")

minimum_length = st.slider('Minimum length of the summary', 10, 30, 20)
maximum_length = st.slider('Maximum length of the summary', 30, 150, 120)

summarize_button = st.button("Summarize")

if summarize_button:
    summarize(input_text, max_len=maximum_length, min_len=minimum_length)

