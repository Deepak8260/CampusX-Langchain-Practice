from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

messages = [
    SystemMessage(content = "You are a helpful assistent"),
    HumanMessage(content = "What is Langchain? Why to use it? explain me in easy to understand words")
]

result = model.invoke(messages)
ai_msg = AIMessage(content = result.content)
messages.append(ai_msg)
print(messages)
