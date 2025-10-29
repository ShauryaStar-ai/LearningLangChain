from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    input_variables=["animal", "attribute"],
    template="Tell me about {animal} that has {attribute}. Under 25 words.",
)
template.save("my_prompt.json")