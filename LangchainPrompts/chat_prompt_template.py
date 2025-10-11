from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_template = ChatPromptTemplate([
    SystemMessage(content = "You are a helpful {domain} expert"),
    HumanMessage(content = "Explain in easy to understadn words , what is {topic}")
])

prompt = chat_template.invoke({'domain':'machine Learning' , 'topic':'Linear Regression'})

print(prompt)