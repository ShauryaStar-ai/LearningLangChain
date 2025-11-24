from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

# Define a chat template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Amazon Customer Service Assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Load chat history
chat_history = []
with open("chat.txt", "r") as f:
    for line in f:
        chat_history.append(HumanMessage(content=line.strip()))

# Invoke the prompt
formattedPrompt = prompt.invoke({
    "history": chat_history,
    "input": "When will the refund be there?"
})

responce = model.invoke(formattedPrompt)
print(responce)