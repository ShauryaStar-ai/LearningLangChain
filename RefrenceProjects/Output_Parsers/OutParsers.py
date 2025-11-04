from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

# Define a chat template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Amazon Customer Service Assistant."),
    ("human", "{input}")
])


# Invoke the prompt
formattedPrompt = prompt.invoke({
    "input": "Who is the founder of Microsoft"
})

responce = model.invoke(formattedPrompt)
print(responce)