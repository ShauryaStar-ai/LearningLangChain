from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)
parser = StrOutputParser()
prompt1 = PromptTemplate(template=
"""
You give me a brief report on the following question: {question}
""",input_variables=["question"],
                        )

prompt2 = PromptTemplate(template=
"""
You give me a 5 most important bullet point report on the following report: {report}
You must respond in the way suggested by thr parser, which is JSON.
""",input_variables=["report"],
                        )
chain = prompt1 | model | parser| prompt2 | model| parser
res =  chain.invoke({"question":"Jordan 1s "})
print(res)

