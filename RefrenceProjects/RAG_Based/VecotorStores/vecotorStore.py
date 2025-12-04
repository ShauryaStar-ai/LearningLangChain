import os

from langchain_core.runnables import RunnableSequence
from langchain_openai import OpenAIEmbeddings , ChatOpenAI
from langchain_chroma import Chroma as c
from langchain_core.documents import Document
from langchain_classic.retrievers import MultiQueryRetriever


from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain



doc1 = Document(
    page_content="Jon Jones, nicknamed 'Bones', is considered one of the greatest light heavyweight fighters in UFC history. "
                 "Known for his wrestling, striking, and submission defense, he has dominated his opponents for years.",
    metadata={"weight_class": "Light Heavyweight", "nickname": "Bones"}
)

doc2 = Document(
    page_content="Israel Adesanya, also called 'The Last Stylebender', is a middleweight champion known for his precision striking, "
                 "movement, and kickboxing background. He has impressed fans with his creativity and technique in the octagon.",
    metadata={"weight_class": "Middleweight", "nickname": "The Last Stylebender"}
)

doc3 = Document(
    page_content="Amanda Nunes, 'The Lioness', is a dominant fighter in the bantamweight and featherweight divisions. "
                 "Her powerful striking and submissions have earned her multiple UFC titles and a legendary status.",
    metadata={"weight_class": "Bantamweight / Featherweight", "nickname": "The Lioness"}
)

doc4 = Document(
    page_content="Khabib Nurmagomedov, famously known as 'The Eagle', is undefeated in his lightweight career. "
                 "His wrestling, ground control, and pressure fighting made him one of the most feared fighters in UFC history.",
    metadata={"weight_class": "Lightweight", "nickname": "The Eagle"}
)




docs = [doc1, doc2, doc3, doc4]
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=50,
    openai_api_key=OPEN_AI_API_KEY
)

vectorStore = c(
    embedding_function=embedding_model,
    persist_directory='chromaDB',
    collection_name='ufc'
)

# Add documents to the vector store
vectorStore.add_documents(docs)

query = "who is best"

# 1️⃣ Standard similarity retriever
similarlity_retriever = vectorStore.as_retriever(search_kwargs={"k": 2})

# Use get_relevant_documents() for retriever
results = similarlity_retriever.invoke(query)
for r in results:
    print(r.page_content)

print("---------------------------------------------------------")



# Define the prompt
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following query based on the retrieved documents: {question}"
)

# Create a RunnableSequence: prompt | llm
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
    openai_api_key=OPEN_AI_API_KEY
)
#chain = RunnableSequence(prompt, llm)

# Create MultiQueryRetriever
multi_retriever = MultiQueryRetriever(
    retriever=similarlity_retriever,
    model = llm
)

# Run the query
results = multi_retriever.invoke(query)
"""for r in results:
    print(r.page_content)"""
