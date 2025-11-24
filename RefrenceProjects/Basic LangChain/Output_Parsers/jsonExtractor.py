from langchain_openai import ChatOpenAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(openai_api_key=API_KEY)

# Define parser
schema = {
    "sentence1": "string",
    "sentence2": "string",
    "sentence3": "string"   # you can add more if needed
}

parser = JsonOutputParser(schema=schema)

# ============================
# Define the prompt
# ============================
template = PromptTemplate(
    template="""
You are a helpful translator.
Translate the following English sentences into {output_language}.
Return your response ONLY in valid JSON following this schema:

{format_instructions}

Input sentences:
{input_sentences}
""",
    input_variables=["input_sentences", "output_language"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# ============================
# Create the full chain
# ============================
chain = template | model | parser

# ============================
# Input text to translate
# ============================
sentences = """
sentence1: I am a good boy
sentence2: I eat 1 apple a day to keep the doctor away
sentence3: I like to play football after school
"""

# ============================
# Run the chain
# ============================
result = chain.invoke({
    "input_sentences": sentences,
    "output_language": "French"
})

# ============================
# Output the results
# ============================
print(result)
print(type(result))