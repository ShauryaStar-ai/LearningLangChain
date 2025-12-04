from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    r"C:\Users\sonuh\OneDrive\Desktop\rough.txt",
    encoding="utf-8"  # explicitly set encoding
)
docs = loader.load()
print(docs[0].page_content)


spliter = RecursiveCharacterTextSplitter(chunk_size=20, chunk_overlap=0)    
result = spliter.split_documents(docs)
print(result)



