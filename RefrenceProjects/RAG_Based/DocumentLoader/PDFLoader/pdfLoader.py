from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("elaWork.pdf")
pages = loader.load()
print(pages[0].metadata)