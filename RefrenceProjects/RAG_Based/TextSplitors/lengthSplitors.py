from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\sonuh\code\shaurya\python\Python AI\Langchain\Learning\RefrenceProjects\RAG_Based\DocLoaders\Text Loader\hello.txt")
docs = loader.load()
print(docs[0].page_content)
