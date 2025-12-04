from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
import os

# -------------------------
# Documents
# -------------------------
doc1 = Document(
    page_content="The Eiffel Tower attracts millions of visitors every year. "
                 "Polar bears can swim for several miles without resting. "
                 "Some programming languages are designed specifically for embedded systems.",
    metadata={"topic": "Mixed Facts 1"}
)

doc2 = Document(
    page_content="Electric guitars rely on magnetic pickups to transmit sound. "
                 "The average lifespan of a butterfly is surprisingly short. "
                 "High-frequency trading systems execute orders in microseconds.",
    metadata={"topic": "Mixed Facts 2"}
)

doc3 = Document(
    page_content="Volcanoes form when magma rises through cracks in the Earth's crust. "
                 "Many people believe classical music enhances concentration. "
                 "Modern skyscrapers often use tuned mass dampers to reduce sway.",
    metadata={"topic": "Mixed Facts 3"}
)

doc4 = Document(
    page_content="Cloud storage providers replicate data across multiple regions. "
                 "Blue whales communicate using low-frequency vocalizations. "
                 "Some board games require cooperative strategies instead of competition.",
    metadata={"topic": "Mixed Facts 4"}
)

docs = [doc1, doc2, doc3, doc4]

# -------------------------
# Embeddings + Vector DB
# -------------------------
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=50)

vectorStore = Chroma(
    embedding_function=embedding,
    persist_directory='chromaDBFactsVectorStore',
    collection_name='randomFacts'
)
vectorStore.add_documents(docs)

# Base retriever
base_retriever = vectorStore.as_retriever(search_kwargs={"k": 3})

# -------------------------
# Proper extractor prompt
# -------------------------
extract_prompt = PromptTemplate.from_template(
"""
You are a document compressor. Your job is to extract ONLY the parts of the content
that directly answer the user question.

QUESTION:
{question}

CONTEXT:
{context}

Return ONLY the useful extracted text. If nothing is useful, return an empty string.
"""
)

model = ChatOpenAI(openai_api_key=OPEN_AI_API_KEY)

llm_chain = LLMChain(prompt=extract_prompt, llm=model)

compressor = LLMChainExtractor.from_llm(llm_chain)

compressive_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# -------------------------
# RUN QUERY — CORRECT METHOD
# -------------------------
query = "Which document mentions anything related to ocean animals?"

result_docs = compressive_retriever.get_relevant_documents(query)

for d in result_docs:
    print("-----------")
    print(d.page_content)
    print(d.metadata)
