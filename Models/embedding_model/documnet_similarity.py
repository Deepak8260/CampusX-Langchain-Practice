from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about Sachin"

doc_embed = embedding.embed_documents(documents)
query_embed = embedding.embed_query(query)

result = cosine_similarity([query_embed],doc_embed)[0]

# print(sorted(list(enumerate(result)),key = lambda x:x[1])[-1])

score = list(enumerate(result))

index,score1 = max(score,key=lambda x:x[1])# another way of doing the same is print(sorted(list(enumerate(result)),key = lambda x:x[1])[-1])

print(query)
print(documents[index]) 

print('Similarity Score is ',score1)
