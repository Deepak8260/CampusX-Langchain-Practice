from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

result = model.invoke("current finance minister of india")
print(result.content)
