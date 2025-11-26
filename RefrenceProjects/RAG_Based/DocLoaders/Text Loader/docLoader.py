from click import prompt
from langchain_classic.chains.llm import LLMChain
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)
loader = TextLoader("hello.txt")
doc = loader.load()

parser = StrOutputParser()
prompt = PromptTemplate(template="tell me the purpose of the docuemnt from the following: {doc}",
                        input_variables=["doc"])

chain = prompt | model | parser
res = chain.invoke({"doc": doc})
print(res)