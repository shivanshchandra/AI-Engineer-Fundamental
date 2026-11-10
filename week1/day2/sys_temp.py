import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# ==============================================================================
# 1. ENVIRONMENT SETUP & INITIALIZATION
# ==============================================================================
# load_dotenv() searches for the .env file in the current folder or parent folders
# and loads variables (like GROQ_API_KEY) into the environment.
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai? Please add GROQ_API_KEY in your .env file!")

# Initialize the Groq client with your API key
client = Groq(api_key=my_api_key)


# ==============================================================================
# 2. MODEL SELECTION
# ==============================================================================
# NOTE: 'llama-3.3-70b-versatile' has been retired/deprecated on Groq.
# We use 'openai/gpt-oss-20b' (fast, active model on GroqCloud).
model = "openai/gpt-oss-20b"


# ==============================================================================
# 3. ROLES EXPLAINED: SYSTEM vs USER
# ==============================================================================
# A) SYSTEM ROLE:
# Sets the "persona", rules, constraints, and instructions for the AI.
# The model follows this persona throughout the conversation.
# IMPORTANT: The dictionary key must be "content" (NOT "message").
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests names for companies. The name must be exactly ONE word. Suggest ONLY one name, nothing else."
}

# B) USER ROLE:
# The actual question, query, or prompt asked by the end user.
role = "user"
prompt = "Suggest a name for my clothing company"

message_user = {
    "role": role,
    "content": prompt
}

# Combine messages in sequential order: System prompt first, then User prompt
messages = [message_system, message_user]


# ==============================================================================
# 4. TEMPERATURE EXPLAINED (Range: 0.0 to 2.0)
# ==============================================================================
# Temperature controls the randomness/creativity of token selection:
#
# • 0.0 : Safe, strict & deterministic.
#         Picks the highest probability word every time. Best for coding, math,
#         or strict rules (e.g. single-word name generation).
#
# • 0.7 - 1.0 : Balanced & natural.
#         Default for general chat, writing, and explanations.
#
# • 1.5 - 2.0 : Highly creative & random.
#         Explores unusual vocabulary; values near 2.0 can cause hallucinations
#         or nonsensical output.
#
temperature = 0.0


# ==============================================================================
# 5. CALL THE API & EXTRACT THE RESPONSE
# ==============================================================================
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature
)

print("################# OUTPUT #################")
answer = response.choices[0].message.content
print(answer)
print("##########################################")
