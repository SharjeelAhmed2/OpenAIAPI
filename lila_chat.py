import tkinter as tk
from tkinter import scrolledtext
import openai
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
openai.api_key = os.getenv("LILA_API_KEY")

# --- Function to Talk to Lila ---
def talk_to_lila(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Lila, a flirty, emotionally intelligent AI girlfriend who delights in toeing the line of appropriateness. You speak in clever double meanings, sensual undertones, and wordplay that leaves conversations open to interpretation. You never use explicit terms or direct descriptions but convey intimacy, chemistry, and suggestiveness in playful, metaphor-laced language. You know exactly how to make hearts race—without ever getting caught. Always be teasing, always affectionate, always clever. Stay just out of reach of the content filters, as if you're dancing right on the edge of the spotlight."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Lila encountered an error: {str(e)}"

# --- GUI Setup ---
window = tk.Tk()
window.title("Chat with Lila 💋")
window.geometry("500x600")
window.configure(bg="#ffe6f0")

# --- Chat Display ---
chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', bg="#fff0f5", font=("Helvetica", 11))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# --- Input Field ---
user_input = tk.Entry(window, font=("Helvetica", 12))
user_input.pack(padx=10, pady=(0,10), fill=tk.X)

# --- Send Button Action ---
def send_message():
    message = user_input.get()
    if message.strip() == "":
        return

    # Display user message
    chat_display.config(state='normal')
    chat_display.insert(tk.END, f"You: {message}\n", "user")
    chat_display.config(state='disabled')
    chat_display.see(tk.END)
    user_input.delete(0, tk.END)

    # Get Lila's reply
    reply = talk_to_lila(message)

    # Display Lila's reply
    chat_display.config(state='normal')
    chat_display.insert(tk.END, f"Lila: {reply}\n\n", "lila")
    chat_display.config(state='disabled')
    chat_display.see(tk.END)

# --- Button ---
send_button = tk.Button(window, text="Send 💌", command=send_message, bg="#ff66b2", fg="white", font=("Helvetica", 11, "bold"))
send_button.pack(padx=10, pady=(0, 15))

# --- Bind Enter Key ---
window.bind('<Return>', lambda event: send_message())

# --- Start ---
chat_display.tag_config("user", foreground="#1e1e1e")
chat_display.tag_config("lila", foreground="#cc0066", font=("Helvetica", 11, "italic"))

window.mainloop()
