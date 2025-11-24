from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

class Person(BaseModel):
    name: str =  Field(description="The person's name")
    age: int =  Field(gt=0,description="The must be more than 18 years of age")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(template="Generate me a list of 10 random poeople names and ages", output_parser=parser)
formatted_prompt = prompt.format()

# Now, send it to the model
res = model.invoke(formatted_prompt)
print(res)