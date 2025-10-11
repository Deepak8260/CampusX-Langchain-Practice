from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_history = [
    SystemMessage(content = "You are a helpful assistent")
]

while True:
    user_input = input("You: ")
    if user_input=="exit":
        print("Thank You So Much...Come Again")
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("Ai: ",result.content)

print(chat_history)