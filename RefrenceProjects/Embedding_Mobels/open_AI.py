from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
print("About to make a call to OpenAI")
embedding_model=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=50,openai_api_key=OPEN_AI_API_KEY)
res = embedding_model.embed_query("Good morning, how are you doing ")
print(str(res))
