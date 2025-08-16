💬 Hassan's Chatbot

A WhatsApp-style AI chatbot built in Python using Tkinter for the GUI and OpenRouter API (Mistral 7B model) for AI responses. This chatbot features realistic chat bubbles, scrollable chat area, colored messages, and a bottom input field, making it look and feel like WhatsApp.

Features:

WhatsApp-like interface: user messages in green bubbles (right-aligned), bot messages in light gray/blue bubbles (left-aligned), rounded and padded message bubbles.

Scrollable chat area with auto-scroll to latest message.

Input field fixed at the bottom; send messages with Enter key or Send button.

Real AI responses using Mistral-7B-Instruct model via OpenRouter API.

Responsive design with resizable window, clear fonts, and spacing.

Technologies Used:

Python 3.x

Tkinter for GUI

Requests for API calls

OpenRouter API for AI model (Mistral 7B)

Installation:

Clone the repository or download the files.

Install required Python packages:

pip install requests


(Optional: If using emojis with emoji module)

pip install emoji


Run the chatbot:

python hassanchatbot.py


How to Use:

Run the chatbot (python hassanchatbot.py).

Type your message in the input field at the bottom.

Press Enter or click Send.

The AI will respond in the bot chat bubble.

Customization:

Change bubble colors:

# User bubble
bubble_color = "#25D366"
# Bot bubble
bubble_color = "#E5E5EA"


Change fonts and padding:

font=("Helvetica", 12)
padx=10, pady=6


Replace Mistral API key:

API_KEY = "YOUR_API_KEY_HERE"


Future Enhancements:

Add tail arrows for chat bubbles

Add profile icons for user and bot

Add timestamps for each message

Add emoji support in messages

Enhance styling to look identical to WhatsApp mobile app

License:
This project is open-source. You can use and modify it freely.