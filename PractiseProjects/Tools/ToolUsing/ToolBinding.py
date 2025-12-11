from langchain_openai import ChatOpenAI
import os
from langchain_community.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import requests
API_KEY = os.environ.get('OPEN_AI_API_KEY')
model = ChatOpenAI(openai_api_key=API_KEY,max_tokens=50)


@tool
def square_number(number: int) -> int:
    """
    Returns the square of a given number.
    """
    return number * number

llm = ChatOpenAI(api_key=API_KEY)

llm_with_tools=llm.bind_tools([square_number])
query = HumanMessage(content="What is the square of 11")
messages = [query]
res = llm_with_tools.invoke(messages)
messages.append(res)
tool_result = square_number.invoke(res.tool_calls[0])
messages.append(tool_result)


print(llm_with_tools.invoke(messages).content)

