# in this folder there is another file named huggingface_chat_api.py, in which I have explicitely used huggingface token id in the same code as below and here i am not using huggingface token id explicitely but also it wokrs

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


repo_id = "Qwen/Qwen3-Coder-30B-A3B-Instruct" # or u can use deepseek-ai/DeepSeek-R1-0528 or any other models from huggingface who have huggingface inference endpoints

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is machine learning in easy words")

print(result.content)


