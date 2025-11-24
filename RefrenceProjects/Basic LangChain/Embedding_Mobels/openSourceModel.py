from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅ older version

# Load environment variables
load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("HF_API_KEY")

# Model name
model_name = "sentence-transformers/all-MiniLM-L6-v2"

# Create the embedding object with API key
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    huggingfacehub_api_token=API_KEY  # ✅ this is accepted here
)

# Example usage
texts = ["This is an example sentence", "Each sentence is converted"]
embeddings_list = embeddings.embed_documents(texts)

print(embeddings_list)
