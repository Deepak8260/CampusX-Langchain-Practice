from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

repo_id = "Qwen/Qwen3-Coder-30B-A3B-Instruct" # or u can use deepseek-ai/DeepSeek-R1-0528 or any other models from huggingface who have huggingface inference endpoints

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    # temperature=0.5,
    # huggingfacehub_api_token=hf_token
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is machine learning in easy words")

print(result.content)


