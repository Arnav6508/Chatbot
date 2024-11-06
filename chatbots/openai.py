from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('OPENAI_API_KEY')
# Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("System", "You are a helpful assistant. Please respond to user queries."),
        ("User", "Question: {question}")
    ]
)

## Streamlit framework
st.title('Chatbot with Langchain and genAI')
input_text = st.text_input('Search the topic you want!')

## OpenAI LLM
llm = ChatOpenAI(model = 'gpt-3.5-turbo')
ouput_parser = StrOutputParser()
chain = prompt|llm|ouput_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))