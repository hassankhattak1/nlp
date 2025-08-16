import requests
import tkinter as tk
from tkinter import Canvas, Frame, Label, Scrollbar

# API Config
API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct"

# API Chat Function
def chat_with_ai(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are Hassan's helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Error: {response.status_code} - {response.text}"

# Function to add chat bubbles
def add_message(message, sender="bot"):
    bubble_color = "#25D366" if sender=="user" else "#E5E5EA"  # Green for user, gray for bot
    fg_color = "#fff" if sender=="user" else "#000"
    anchor = "e" if sender=="user" else "w"
    
    # Message frame
    msg_frame = Frame(scrollable_frame, bg="#ece5dd")
    msg_label = Label(msg_frame, text=message, bg=bubble_color, fg=fg_color,
                      wraplength=350, justify="left", font=("Helvetica", 12),
                      padx=10, pady=6, bd=0, relief="solid")
    msg_label.pack(anchor=anchor, padx=5, pady=2)
    msg_frame.pack(anchor=anchor, fill="both", padx=10, pady=2)
    
    # Auto scroll
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Function to send message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    add_message(user_input, sender="user")
    entry.delete(0, tk.END)
    reply = chat_with_ai(user_input)
    add_message(reply, sender="bot")

# GUI Setup
root = tk.Tk()
root.title("💬 Hassan's Chatbot")
root.geometry("600x500")
root.configure(bg="#ece5dd")  # WhatsApp-like background

# Chat Frame (expandable)
chat_frame = Frame(root, bg="#ece5dd")
chat_frame.pack(fill="both", expand=True)

# Canvas for scrolling
canvas = Canvas(chat_frame, bg="#ece5dd", highlightthickness=0)
scrollbar = Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#ece5dd")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Input Frame (fixed at bottom)
input_frame = Frame(root, bg="#ece5dd")
input_frame.pack(fill="x", side="bottom", padx=10, pady=10)

entry = tk.Entry(input_frame, font=("Helvetica", 14))
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(input_frame, text="Send 💌", bg="#128C7E", fg="white",
                        font=("Helvetica", 12, "bold"), command=send_message)
send_button.pack(side="right")

# Welcome message
add_message("🤖 Hello! I'm Hassan's Chatbot. Let's chat! 😄", sender="bot")

root.mainloop()
