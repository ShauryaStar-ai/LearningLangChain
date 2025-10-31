from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from dotenv import load_dotenv
import os

load_dotenv()
llm = HuggingFacePipeline.from_model_id(
    model_id="ibm-granite/granite-4.0-h-tiny",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100}
)
model = ChatHuggingFace(
    llm=llm
)

res = model.invoke("Hello, how are you?")
print(res.content)

