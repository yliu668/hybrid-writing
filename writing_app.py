import streamlit as st
import openai

from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🔎 Reflective Writing")

"""
In this exercise, you will write a short paragraph on this topic:
"Reflect on a time when you questioned or challenged a belief or idea. What prompted your thinking? What was the outcome?"

You will chat with the chatbot to help you organize your thoughts and think deeper about your experiences.

You can ask the chatbot anything. Once you feel that you are able to get started, please click the "continue" button.
"""



