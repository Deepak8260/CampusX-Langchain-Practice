from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

class ReviewRequest(TypedDict):
    summary: str
    sentiment: str

strctured_model = model.with_structured_output(ReviewRequest)

result = strctured_model.invoke("what is machine learning in easy words")
print(result)














