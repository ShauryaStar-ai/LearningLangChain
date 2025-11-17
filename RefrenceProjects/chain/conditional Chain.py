from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
import langchain_anthropic
from pydantic import BaseModel, Field
from typing import Literal
import os

#model 1 set up
my_api_key = os.getenv("OPEN_AI_API_KEY")
model1=ChatOpenAI(openai_api_key=my_api_key)
parser1 = StrOutputParser()

class Feedback(BaseModel):
    feedback: Literal["positive", "negative"] = Field(description="Give the positive or negative sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    input_variables=["review"],  # list all placeholders used inside template
    template="Classify the feedback of the given user review. {review} {formatInstructions}",
    partial_variables={"formatInstructions": parser2.get_format_instructions()})

classiferChain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template="Write an appropriate postivie responce based on the given review. {sentiment}",
    input_variables=["sentiment"],
)
prompt3 = PromptTemplate(
    template="Write an appropriate negetive  responce based on the given review. {sentiment}",
    input_variables=["sentiment"],
)
branch_chain = RunnableBranch(
    (lambda x:x.feedback == 'positive', prompt2 | model1 | parser1),
    (lambda x:x.feedback == 'negative', prompt3 | model1 | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classiferChain | branch_chain

print(chain.invoke({'review': 'This is a bad and horribe  phone'}))