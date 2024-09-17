import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

if groq_api_key:
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name='mixtral-8x7b-32768')
    print("API key is working.")
else:
    print("Failed to load API key.")
