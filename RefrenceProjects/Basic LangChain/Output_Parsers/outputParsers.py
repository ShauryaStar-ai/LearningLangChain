from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

templateUSA = PromptTemplate(
    template="What were the cause of {incident in usa}?",
    input_variables=["incident in usa"]
)

templateUK = PromptTemplate(
    template="How did the UK react to {usa_action}?",
    input_variables=["usa_action"]
)
chain = templateUSA | model | StrOutputParser() | templateUK | model | StrOutputParser()

print(chain.invoke({"incident in usa": "Boston Tea Party"}))

