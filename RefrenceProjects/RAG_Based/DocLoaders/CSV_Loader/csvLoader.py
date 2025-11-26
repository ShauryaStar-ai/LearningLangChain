from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path="C:/Users/sonuh/Downloads/random_data.csv")
docs = loader.load()
print(docs[2].page_content)
print(len(docs))
