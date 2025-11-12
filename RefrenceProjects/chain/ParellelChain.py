from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import langchain_anthropic
import os
my_api_key = os.getenv("OPEN_AI_API_KEY")  # the windows reteiver of the env variable

model1=ChatOpenAI(openai_api_key=my_api_key)

API_KEY = os.getenv("ANTHROPIC_API_KEY")
model = "claude-3-5-haiku-20241022"
model2 = langchain_anthropic.ChatAnthropic(model=model, api_key=API_KEY, temperature=0.7)

