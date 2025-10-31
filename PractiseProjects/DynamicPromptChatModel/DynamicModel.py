from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
import os

# --- SETUP ---
API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

# Define a chat template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant named Gennie."),
    ("human", "{input}")
])

# Keep chat history
messages = []

# --- CHAT LOOP ---
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add user message
    messages.append(HumanMessage(content=user_input))

    # Format the full prompt with the latest input
    formatted_prompt = prompt.format_messages(input=user_input)

    # Get response from model
    response = model.invoke(formatted_prompt)

    print("Gennie:", response.content)

    # Add assistant message to history
    messages.append(AIMessage(content=response.content))

print("Printing chat history:")
print(messages)
