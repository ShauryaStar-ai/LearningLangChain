from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever(top_k_results=3,language='en')

query = "What is the capital of France?"
docs = retriever.invoke(query)

for doc in docs:
    print(doc.page_content)
