from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import langchain_anthropic
import os



#model 1 set up
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable
model1=ChatOpenAI(openai_api_key=my_api_key)
prompt1 = PromptTemplate(
    input_variables=["question"],  # list all placeholders used inside template
    template="Read the question and the provide me with 5 points of the {question}"
)
texttofill="Read the question and the provide me with 5 points of the {question}-----> {answer}"
print(texttofill.format(question="What is Black hole", answer="Black hole is a region of space where gravity is so strong that nothing, not even light, can escape from it."))
#res = model1.invoke(prompt1.format(question="What is Black hole"))
#print(res)