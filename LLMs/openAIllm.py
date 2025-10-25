import os
from langchain_openai import OpenAI

# check both common names
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable
print(
    "OpenAI API Key:", my_api_key
)  # print the key to verify it's being read correctly
llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key=my_api_key)
response = llm.invoke("What is the capital of France?")
print(response)
