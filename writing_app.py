import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("🔎 Reflective Writing")

st.write("""
In this exercise, you will write a short paragraph on this topic:
"Reflect on a time when you questioned or challenged a belief or idea. What prompted your thinking? What was the outcome?"
You will chat with the chatbot to help you organize your thoughts and think deeper about your experiences.
You can ask the chatbot anything. Once you feel that you are able to get started, please write your paragraph below.
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant for reflective writing exercises."}
    ]

# Chatbot Interaction
st.subheader("Chat with the Bot")
user_input = st.text_input("Your Message", placeholder="Ask me anything to organize your thoughts...", key="input")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get the bot's response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state["messages"]
        )
        bot_message = response["choices"][0]["message"]["content"]
        st.session_state["messages"].append({"role": "assistant", "content": bot_message})
    except openai.OpenAIError as e:
        bot_message = f"Error: {e}"
        st.session_state["messages"].append({"role": "assistant", "content": bot_message})

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Bot:** {msg['content']}")

# Writing Box
st.subheader("Reflective Writing")
writing = st.text_area(
    "Write your reflective paragraph here:",
    placeholder="Start writing your reflection...",
    height=200,
    key="writing_area"
)

if st.button("Submit"):
    if writing.strip():
        st.success("Your reflective writing has been submitted successfully!")
    else:
        st.error("Please write something before submitting.")



