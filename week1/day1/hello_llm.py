import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# ==============================================================================
# 1. LOAD ENVIRONMENT VARIABLES & SETUP CLIENT
# ==============================================================================
# load_dotenv() searches up the directory tree to find your .env file
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error: GROQ_API_KEY not found in environment (.env file).")

# Initialize the Groq client
client = Groq(api_key=my_api_key)

# Active model on GroqCloud (llama-3.3-70b-versatile was deprecated)
model = "openai/gpt-oss-20b"


# ==============================================================================
# 2. UNDERSTANDING ROLES: USER & ASSISTANT
# ==============================================================================
# In LLM APIs, conversations are lists of message dictionaries with "role" and "content".
#
# 1. "user": The human sending prompts or questions.
# 2. "assistant": The AI's previous replies.
#
# WHY DO WE USE THE "assistant" ROLE?
# LLMs are stateless — they have no built-in memory!
# If you want the AI to remember what it said earlier, you must send the past
# conversation back to the API by including previous "user" and "assistant" turns.

# Example 1: Basic Single-Turn Request (Just User)
basic_messages = [
    {
        "role": "user",
        "content": "Hi, my name is Shivansh!"
    }
]

# Example 2: Multi-Turn Conversation (User + Assistant History)
# Notice how past replies are tagged with role: "assistant"
conversation_history = [
    {
        "role": "user",
        "content": "Hi, my name is Shivansh!"
    },
    {
        "role": "assistant",
        "content": "Hello Shivansh! Nice to meet you. How can I help you today?"
    },
    {
        "role": "user",
        "content": "What is my name?"  # The model knows because of the history above!
    }
]


# ==============================================================================
# 3. SENDING THE REQUEST TO GROQ
# ==============================================================================
# Choose which message list to send:
messages_to_send = conversation_history

response = client.chat.completions.create(
    model=model,
    messages=messages_to_send
)


# ==============================================================================
# 4. PRINTING THE RESULT
# ==============================================================================
print("Full API Response Object:")
print(response)

print("\n" + "=" * 50)
print("Assistant's Extracted Answer:")
print("=" * 50)
print(response.choices[0].message.content)
