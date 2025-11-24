import os
from dotenv import load_dotenv
import langchain_anthropic

# Load variables from the .env file into the environment

API_KEY = os.getenv("ANTHROPIC_API_KEY")
#print(API_KEY)
model = "claude-3-5-haiku-20241022"
ChatModel = langchain_anthropic.ChatAnthropic(model=model, api_key=API_KEY, temperature=0.7)
#, temperature=1.5
#(model="claude-2.0", api_key=API_KEY)
"""res=ChatModel.invoke("Spit me some game")
print(res.content)
"""