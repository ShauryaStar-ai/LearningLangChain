from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage , AIMessage , HumanMessage

API_KEY = os.environ.get('OPEN_AI_API_KEY')
model = ChatOpenAI(openai_api_key=API_KEY,max_tokens=50)
# the model is fully set up and ready to use
chatHistroy = [SystemMessage(content="You are a world histroy and geography homework helper.All of the responces should be well explained and in a academic tone.")]
while True:
    user_input = input("User: ")
    chatHistroy.append(HumanMessage(content=user_input))
    if user_input == "exit":
        print(chatHistroy)
        break
    res = model.invoke(chatHistroy)
    res = res.content
    chatHistroy.append(AIMessage(content=res))

    print("AI: ",res)