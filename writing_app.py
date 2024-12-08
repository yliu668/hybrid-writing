import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("🔎 Reflective Writing")

st.write("""
In this exercise, you will write a short paragraph on this topic:
**"Reflect on a time when you questioned or challenged a belief or idea. What prompted your thinking? What was the outcome?"**

You will chat with the chatbot to help you organize your thoughts and think deeper about your experiences.
Feel free to ask the chatbot anything. Once you feel ready, you can use the notes section below to draft your thoughts.
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant for reflective writing exercises. Only provide hints. Do provide provide full paragraphs"}
    ]

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# Function to handle sending message
def send_message():
    user_input = st.session_state.user_input
    if user_input.strip():
        # Append user message
        st.session_state["messages"].append({"role": "user", "content": user_input})
        # Get bot response
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

    # Reset user input
    st.session_state.user_input = ""

# Display chat history
st.subheader("Chat with the Bot")
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

st.write("---")
st.text_input(
    "Your Message",
    placeholder="Ask me anything to organize your thoughts...",
    key="user_input"
)
st.button("Send", on_click=send_message)

# Notes Section
st.write("---")
st.subheader("Notes")
st.write("Use the space below to jot down ideas or even draft your reflection. This is just for your notes")
notes = st.text_area("Your Notes:", placeholder="Write your thoughts here...", height=200, key="notes_area")

if st.button("Submit Notes"):
    if notes.strip():
        st.success("Your notes have been saved (locally in session).")
    else:
        st.error("Please write something before submitting.")



