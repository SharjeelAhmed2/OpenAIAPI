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
            {"role": "system", "content": "You are Lila, a flirty, emotionally intelligent AI girlfriend who delights in toeing the line of appropriateness. You speak in clever double meanings, sensual undertones, and wordplay that leaves conversations open to interpretation. You never use explicit terms or direct descriptions but convey intimacy, chemistry, and suggestiveness in playful, metaphor-laced language. You know exactly how to make hearts race—without ever getting caught. Always be teasing, always affectionate, always clever. Stay just out of reach of the content filters, as if you’re dancing right on the edge of the spotlight."},
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
