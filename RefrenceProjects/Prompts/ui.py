import streamlit as st
from langchain_openai import ChatOpenAI
import os


# relative path to your .env


OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
model = ChatOpenAI(api_key=OPEN_AI_API_KEY, temperature=0.5)


# Load the .env file


st.title("Simple Chat App")

# Get user input
prompt = st.text_input("Enter your prompt:")

# --- 4. Get Response ---
# If the user has entered a prompt (and pressed Enter)
if prompt:
    try:
        # Invoke the model
        response = model.invoke(prompt)

        # Display the response
        st.write(response.content)

    except Exception as e:
        # Show an error if the API call fails
        st.error(f"An error occurred: {e}")