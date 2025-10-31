import streamlit as st
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate , load_prompt


# relative path to your .env


OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(api_key=OPEN_AI_API_KEY, temperature=0.5)


# Load the .env file


st.title("Simple Chat App")
# the user will have 2 drop down means taht they can slected the animal and the attribute.

animal = st.selectbox("Select an animal", ["Dog", "Cat", "Bird"])
attribute = st.selectbox("Select an attribute", ["Color", "Size", "Age"])

# load the prompt template
prompt = load_prompt("my_prompt.json")


if st.button("Submit"):
    try:
        # Format the prompt with user input
        formatted_prompt = prompt.format(animal=animal, attribute=attribute)

        # Invoke the model
        response = model.invoke(formatted_prompt)

        # Display the response
        st.write(response.content)

    except Exception as e:
        # Show an error if the API call fails
        st.error(f"An error occurred: {e}")