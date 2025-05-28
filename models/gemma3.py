import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemma3_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3, google_api_key=os.getenv('GOOGLE_API_KEY')) | StrOutputParser()