from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda
from pydantic import BaseModel
from typing import Literal
import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)

# ----------------- Pydantic Model -----------------
class ComplaintType(BaseModel):
    type: Literal["complain", "refund", "query"]

pydanticParser = PydanticOutputParser(pydantic_object=ComplaintType)

# ----------------- Prompts -----------------
promptDetermineType = PromptTemplate(
    template=(
        "Determine the type of complaint from the text. "
        "The type must be one of 'complain', 'refund', or 'query'. "
        "Return ONLY valid JSON in this format: {{\"type\": <type>}} "
        "Complaint: {complain}"
    ),
    input_variables=["complain"]
)

promptComplain = PromptTemplate(
    template="You are a helpful assistant that answers questions about a complaint. The complaint is: {complain}.",
    input_variables=["complain"]
)

promptRefund = PromptTemplate(
    template="You are a helpful assistant that answers questions about a refund. The refund is: {refund}.",
    input_variables=["refund"]
)

promptGeneralQuery = PromptTemplate(
    template="You are a helpful assistant that answers questions about a general query. The query is: {query}.",
    input_variables=["query"]
)

# ----------------- Parsers -----------------
str_parser = StrOutputParser()

# ----------------- Runnable Sequences -----------------
determineType = RunnableSequence(promptDetermineType, model, pydanticParser)
complain_chain = RunnableSequence(promptComplain, model, str_parser)
refund_chain = RunnableSequence(promptRefund, model, str_parser)
query_chain = RunnableSequence(promptGeneralQuery, model, str_parser)

# ----------------- Conditional Branching -----------------
branch_chain = RunnableBranch(
    (lambda x: x.type == "complain", complain_chain),
    (lambda x: x.type == "refund", refund_chain),
    (lambda x: x.type == "query", query_chain),
    # fallback if none matches
    RunnableLambda(lambda x: "Could not determine complaint type")
)

# ----------------- Full Pipeline -----------------
full_pipeline = RunnableSequence(
    determineType,  # outputs ComplaintType
    branch_chain    # chooses appropriate sequence
)

# ----------------- Run -----------------
user_input = "Your service is very bad"
result = full_pipeline.invoke(user_input)
print(result)
