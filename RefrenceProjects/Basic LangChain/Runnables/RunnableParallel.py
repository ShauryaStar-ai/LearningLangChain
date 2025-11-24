from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
import langchain_anthropic
import os


#model 1 set up
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable
model1=ChatOpenAI(openai_api_key=my_api_key)
prompt1 = PromptTemplate(
    input_variables=["topic"],  # list all placeholders used inside template
    template="Give me the linkedIn post about {topic} in 100 words"
)

#model 2 set up
API_KEY = os.getenv("ANTHROPIC_API_KEY")
model = "claude-3-5-haiku-20241022"
model2 = langchain_anthropic.ChatAnthropic(model=model, api_key=API_KEY, temperature=0.7)

prompt2 = PromptTemplate(input_variables=["topic"], template="Give me the twitter post about {topic} in 5 words")

chain_LinkedIn = RunnableSequence(
prompt1,
    model1

    #output_parser=StrOutputParser()
)
chain_Twitter = RunnableSequence(
    prompt2,
    model2
    #output_parser=StrOutputParser()
)
chain = RunnableParallel(
    linkedin=chain_LinkedIn,
    twitter=chain_Twitter)
res = chain.invoke({"topic": "I made a 100 on the math exam"})
print(res["linkedin"].content)
print(res["twitter"].content)
