import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# ==============================================================================
# 1. ENVIRONMENT VARIABLES & CLIENT INITIALIZATION
# ==============================================================================
# load_dotenv() searches up the directory tree to find your .env file
# and loads your secret keys into environment variables.
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error: GROQ_API_KEY not found in environment (.env file).")

# Initialize the Groq client
client = Groq(api_key=my_api_key)

# Active model on GroqCloud (llama-3.3-70b-versatile was deprecated)
model = "openai/gpt-oss-20b"


# ==============================================================================
# 2. UNDERSTANDING ROLES IN LLM APIS
# ==============================================================================
# LLM APIs represent conversations as a list of dictionaries with "role" and "content".
#
# The standard roles are:
# 1. "user"      : The human asking questions or giving tasks.
# 2. "assistant" : The AI's previous responses (used to give the AI memory).
# 3. "system"    : Instructions and persona set before the chat begins.
# 4. "tool"      : Results from external functions/APIs when using tool calling.
#
# WHY DO WE USE THE "assistant" ROLE?
# LLMs are stateless — they have no built-in memory!
# If you want the AI to remember earlier messages, you must include previous
# "user" and "assistant" turns in the messages list.
# ==============================================================================

# --- ACTIVE CODE (Only this runs so you get one clear response) ---
role = "user"
prompt = "Do you know Padho with Pratyush"

message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(
    model=model, 
    messages=messages
)

print(response)
print("##############################################################")
print(response.choices[0].message.content)


# ==============================================================================
# ALTERNATIVE EXAMPLES (Commented out so they don't interfere with main output)
# To test any of these, comment out the active code above and uncomment the block below.
# ==============================================================================

# --- Example: Multi-Turn Conversation using the "assistant" role for Memory ---
# conversation_history = [
#     {
#         "role": "user",
#         "content": "Hi, my name is Shivansh!"
#     },
#     {
#         "role": "assistant",
#         "content": "Hello Shivansh! Nice to meet you. How can I help you today?"
#     },
#     {
#         "role": "user",
#         "content": "What is my name?"  # The model knows because the assistant reply is above!
#     }
# ]
#
# response = client.chat.completions.create(
#     model=model, 
#     messages=conversation_history
# )
# print("Memory test answer:")
# print(response.choices[0].message.content)
