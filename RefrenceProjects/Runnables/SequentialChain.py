from langchain_classic.chains.llm import LLMChain
from langchain_core.runnables import Runnable, RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Tell me a funny joke about {topic}.",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Tell me the meaning of the joke {joke}.",
    input_variables=["joke"]
)

#llm_chain = LLMChain(llm=model, prompt=prompt, output_parser=parser)

chain = RunnableSequence(prompt, model, parser,  prompt2, model,parser) # one can have the parts( lego blocks) in the same easy order as
# they will be called to run in the order they are in the sequence
res = chain.invoke({"topic": "wenier"})
print(res)