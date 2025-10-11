from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_history = []

while True:
    user_input = input("You: ")
    if user_input=="exit":
        print("Thank You So Much...Come Again")
        break
    chat_history.append(user_input)
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("Ai: ",result.content)

print(chat_history)