from langchain_community.document_loaders import WebBaseLoader

url = "https://kinginstitute.stanford.edu/montgomery-bus-boycott"
loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0].page_content)