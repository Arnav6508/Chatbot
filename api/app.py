from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv('../.env')


os.environ['LANGCHAIN_API_KEY'] = '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'

app = FastAPI(
    title = 'Langchain server',
    version = '1.0',
    description = 'A simple API server'
)

llm = Ollama(model = 'llama2')

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