from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
load_dotenv('../.env')


with open('lang_api_key.txt', 'r') as file:
    LANGCHAIN_API_KEY = file.read()

os.environ['LANGCHAIN_API_KEY'] = LANGCHAIN_API_KEY

app = FastAPI(
    title = 'Langchain server',
    version = '1.0',
    description = 'A simple API server'
)

llm = OllamaLLM(model = 'llama2')

prompt1 = ChatPromptTemplate.from_template('Write essay on {topic} in 50 words')
prompt2 = ChatPromptTemplate.from_template('Write poem on {topic} in 50 words')

add_routes(
    app,
    prompt1|llm,
    path = '/essay'
)

add_routes(
    app,
    prompt2|llm,
    path = '/poem'
)

if __name__ == '__main__':
    uvicorn.run(app, host = 'localhost', port = 8000)