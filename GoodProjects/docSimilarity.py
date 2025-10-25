from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity # this will be used to find the closness of the vecotrs
load_dotenv()

model = 'text-embedding-3-small'
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
embedding_model = OpenAIEmbeddings(model=model,dimensions=300 ,openai_api_key=OPEN_AI_API_KEY)

docments = ["Cat can mew mew ", "Dog can bark bark", "Lion can roar","Wolf can howl"]
docments_embeding = embedding_model.embed_documents(docments)
query = "What is the cat can do"
query_embedding = embedding_model.embed_query(query)

similarity = cosine_similarity([query_embedding], docments_embeding)

# Find the index of the document with the highest similarity
# Since similarity is a 2D array (1, N), we take the first row [0]
highest_similarity_index = np.argmax(similarity[0])

# Get the document corresponding to that index
most_similar_document = docments[highest_similarity_index]

print(most_similar_document)
