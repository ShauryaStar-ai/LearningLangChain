from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    input_variables=["war", "year"],
    template="Tell me about the us {war} that happend  in {year} year",
)
template.save("my_prompt.json")