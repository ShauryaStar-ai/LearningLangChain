import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import os

# --- Configuration ---
# Set your OpenAI API Key as an environment variable
# (e.g., in your terminal: export OPEN_AI_API_KEY='your_key_here')
API_KEY = os.getenv("OPEN_AI_API_KEY")

# --- Page Setup ---
st.set_page_config(page_title="Gennie Chat", page_icon="🤖")
st.title("🤖 Gennie Chatbot")
st.caption("A simple Streamlit chatbot that remembers your conversation.")

# --- Model and API Key Check ---
if not API_KEY:
    st.error("OPEN_AI_API_KEY environment variable not set.")
    st.info("Please set the OPEN_AI_API_KEY environment variable to run this app.")
    st.stop()

try:
    # Initialize the ChatOpenAI model
    # Using a slightly larger max_tokens for better responses
    model = ChatOpenAI(openai_api_key=API_KEY, max_tokens=150)
except Exception as e:
    st.error(f"Failed to initialize the AI model: {e}")
    st.stop()

# --- Session State for Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant named Gennie.")
    ]

# --- Display Chat History ---
# Iterate over messages in session state, skipping the initial system message
for message in st.session_state.messages:
    if isinstance(message, SystemMessage):
        # Don't display the system prompt to the user
        continue
    elif isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# --- Chat Input and Response Logic ---
if user_input := st.chat_input("You:"):

    # 1. Add user's message to history and display it
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Gennie is thinking..."):
            try:
                # Pass the *entire* chat history to the model
                response = model.invoke(st.session_state.messages)
                response_content = response.content

            except Exception as e:
                response_content = f"Sorry, an error occurred: {e}"

            # Display the AI's response
            st.markdown(response_content)

    # 3. Add AI's response to history
    st.session_state.messages.append(AIMessage(content=response_content))
