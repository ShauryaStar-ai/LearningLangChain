from langchain_openai import ChatOpenAI
import os
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable

chatModel=ChatOpenAI(model="gpt-4", openai_api_key=my_api_key, temperature=1.9, max_tokens=500)
res = chatModel.invoke("Best hiking idea")
print(res.content)