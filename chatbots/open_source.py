from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv('../.env')


with open('lang_api_key.txt', 'r') as file:
    LANGCHAIN_API_KEY = file.read()

os.environ['LANGCHAIN_API_KEY'] = LANGCHAIN_API_KEY
os.environ['LANGCHAIN_TRACING_V2'] = "true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

## LLM, parser && chain
# first download local copy of model by running ollama run llm_name
llm = OllamaLLM(model='llama2')
ouput_parser = StrOutputParser()
chain = prompt|llm|ouput_parser

## Streamlit framework
st.title('Chatbot with Langchain and genAI')
input_text = st.text_input('Search the topic you want!')

if input_text:
    st.write(chain.invoke({'question': input_text}))