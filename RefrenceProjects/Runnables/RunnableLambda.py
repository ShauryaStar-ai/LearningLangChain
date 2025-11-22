# In this function there would be an extention of the sentiemtn review
# but there weree would be a sentiment clean up function whom I will make into a runnable parallel
def clean_review(input_data):
    # Case 1: If LangChain passes a dict
    if isinstance(input_data, dict):
        review = input_data["review"]
        return {"review": review.replace("!", "")}

    # Case 2: If it's already a string
    if isinstance(input_data, str):
        return input_data.replace("!", "")

    # fallback
    return input_data

# loading the sentiment review function
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
clear_review = RunnableLambda(clean_review)

chain = clear_review | classiferChain | branch_chain

review = "This is a very good !!!!"

print(chain.invoke({"review": review}))
