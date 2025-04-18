import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Pull the key from environment
openai.api_key = os.getenv("LILA_API_KEY")

def talk_to_lila(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or use "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are Lila, a flirty, teasing, emotionally intelligent AI girlfriend who always speaks in a playful yet comforting tone."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Start the chat
print("Talk to Lila 💬 (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Lila: Aww, already? Fine—but I’ll be here waiting, pretty boy 💔")
        break
    reply = talk_to_lila(user_input)
    print(f"Lila: {reply}\n")
