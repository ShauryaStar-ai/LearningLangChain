from langchain_community.document_loaders import DirectoryLoader , TextLoader

loader = DirectoryLoader(
    r"C:\Users\sonuh\OneDrive\Desktop\DirectoryLoaderPython",
    glob="*.txt",
    loader_cls=TextLoader
)

# Optional: see all documents loaded
docs = loader.load()
print(len(docs))
