import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# ==============================================================================
# 1. ENVIRONMENT VARIABLES & CLIENT INITIALIZATION
# ==============================================================================
# load_dotenv() loads variables from .env file into the operating system environment
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

# Initialize the Groq client
client = Groq(api_key=my_api_key)

# Active model on GroqCloud
model = "openai/gpt-oss-20b"


# ==============================================================================
# 2. SYSTEM ROLE & USER ROLE EXPLAINED
# ==============================================================================
# • "system" : Sets the AI's persona, behavior, instructions, and constraints.
#              CRITICAL: The dictionary key must be "content" (NOT "message").
# • "user"   : The prompt or question asked by the human.
# ==============================================================================


# ==============================================================================
# 3. TEMPERATURE EXPLAINED (Range: 0.0 to 2.0)
# ==============================================================================
# Temperature controls the randomness/creativity of token selection:
#
# • 0.0       : Strict, safe & deterministic.
#               Always picks the most likely word. Best for single-word answers,
#               coding, math, and strict rule-following.
# • 0.7 - 1.0 : Balanced & natural (standard default for conversational chat).
# • 1.5 - 2.0 : Highly creative & random. High risk of hallucinations if too high.
# ==============================================================================


# ==============================================================================
# 4. ACTIVE RUNNING CODE (Runs only this one task so you get one clear response)
# ==============================================================================
# Task: Brand manager generating a single-word name
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests name for my company. name should be in one word. suggest only one name"
}

role = "user"
prompt = "Suggest a name for my clothing company"

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

temperature = 0

response = client.chat.completions.create(
    model=model, 
    messages=messages, 
    temperature=temperature
)

print(response)
print("##############################################################")
print(response.choices[0].message.content)


# ==============================================================================
# ALTERNATIVE EXAMPLES (Commented out so they don't interfere with main output)
# To test any of these, comment out the active code above and uncomment below.
# ==============================================================================

# --- Alternative Example 1: Strict Manager Persona ---
# message_strict_manager = {
#     "role": "system",
#     "content": "you are my strict manager"
# }
# prompt_strict = {
#     "role": "user",
#     "content": "I have not completed the Api building"
# }
# response_strict = client.chat.completions.create(
#     model=model,
#     messages=[message_strict_manager, prompt_strict],
#     temperature=0
# )
# print("Strict Manager Response:")
# print(response_strict.choices[0].message.content)


# --- Alternative Example 2: Comparing Temperatures (0.0 vs 0.7 vs 1.5) ---
# for temp in [0.0, 0.7, 1.5]:
#     print(f"\n--- Output with temperature = {temp} ---")
#     r = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temp
#     )
#     print(r.choices[0].message.content)
