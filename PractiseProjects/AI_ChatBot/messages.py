from langchain_core.messages import SystemMessage , AIMessage , HumanMessage
from langchain_openai import ChatOpenAI
import os
API_KEY = os.environ.get('OPEN_AI_API_KEY')
model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=50)

message = [SystemMessage(content="You are a world histroy and geography homework helper.All of the responces should be well explained and in a academic tone."),
           HumanMessage(content="Tell me about the war of 1812"),

]
res = model.invoke(message)
res = res.content
message.append(AIMessage(content=res))
print(message)
