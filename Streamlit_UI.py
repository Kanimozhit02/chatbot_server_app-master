# ============================================================
# Streamlit_UI.py
# Project: OpenAI_API_Python
# Course: Designing Conversational AI
#
# Purpose:
# This file creates a web-based chatbot interface using Streamlit.
#
# Key Architecture Principle:
# - Streamlit = UI only
# - CLI_Chatbot.py = AI brain
# - SAME backend logic, DIFFERENT UI
#
# Supports:
# - OpenAI
# - Gemini
# - Claude
# ============================================================


# ------------------------------------------------------------
# Import required libraries
# ------------------------------------------------------------

import streamlit as st

from CLI_Chatbot import get_chatbot_response


# ------------------------------------------------------------
# Page configuration (MUST be first Streamlit command)
# ------------------------------------------------------------

st.set_page_config(
    page_title="OpenAI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ------------------------------------------------------------
# Custom CSS Styling for Chat Interface
# ------------------------------------------------------------

st.markdown("""
<style>
.chat-container {
    max-width: 700px;
    margin: auto;
}

.user-box {
    background-color: #e8f0fe;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.bot-box {
    background-color: #e6f4ea;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.user-label {
    font-weight: bold;
    color: #1a73e8;
}

.bot-label {
    font-weight: bold;
    color: #137333;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Page Title and Caption
# ------------------------------------------------------------

st.markdown(
    "<div class='chat-container'>",
    unsafe_allow_html=True
)

st.title("🤖 OpenAI Conversational AI Chatbot")

st.caption("Multi-LLM Support: OpenAI | Gemini | Claude")


# ------------------------------------------------------------
# LLM Provider Selection
# ------------------------------------------------------------

provider = st.selectbox(
    "Choose AI Provider",
    ["gemini", "openai", "claude"]
)


# ------------------------------------------------------------
# Initialize Session State for Chat Memory
# ------------------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ------------------------------------------------------------
# User Input Section
# ------------------------------------------------------------

user_input = st.text_input(
    "You:",
    placeholder="Type your message here..."
)


# ------------------------------------------------------------
# Handle Send Button Click
# ------------------------------------------------------------

if st.button("Send") and user_input.strip():

    # Remove unnecessary spaces before processing
    cleaned_input = user_input.strip()

    # Send cleaned input to the chatbot backend
    response = get_chatbot_response(
        cleaned_input,
        provider
    )

    # Save conversation in session memory
    st.session_state.chat_history.append(
        ("You", cleaned_input)
    )

    st.session_state.chat_history.append(
        ("Bot", response)
    )


# ------------------------------------------------------------
# Display Chat History
# ------------------------------------------------------------

for sender, message in st.session_state.chat_history:

    if sender == "You":

        st.markdown(
            f"""
            <div class="user-box">
                <span class="user-label">You:</span><br>
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="bot-box">
                <span class="bot-label">Chatbot:</span><br>
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# Close the chat container
# ------------------------------------------------------------

st.markdown(
    "</div>",
    unsafe_allow_html=True
)
