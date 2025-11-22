from langchain_classic.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)
parser = StrOutputParser()
prompt1 = PromptTemplate(template=
"""
answer following question: {question}
""",input_variables=["question"],
                        )

chain = LLMChain(llm=model, prompt=prompt1, output_parser=parser)

question = "What is the capital of France?"
question = input("Enter your question: ")
output = chain.run(question=question)

print(output)

