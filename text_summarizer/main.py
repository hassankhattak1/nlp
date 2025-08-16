# main.py
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from transformers import pipeline
import nltk
from nltk.corpus import stopwords

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)  # CPU

# Create main window
app = tb.Window(themename="superhero")
app.title("Text Summarizer")
app.geometry("700x500")

# Input Text widget
text_input = tb.Text(app, height=10, font=("Arial", 12))
text_input.pack(fill="x", padx=20, pady=10)

# Output Text widget
result_output = tb.Text(app, height=8, font=("Arial", 12))
result_output.pack(fill="x", padx=20, pady=10)

# Summarization function
def summarize_text(event=None):  # Accept event from key press
    text = text_input.get("1.0", tk.END).strip()
    if text:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, summary[0]['summary_text'])
    else:
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, "Please enter some text to summarize.")

# Summarize button
summarize_btn = tb.Button(app, text="Summarize", bootstyle="success", command=summarize_text)
summarize_btn.pack(pady=10)

# Bind Enter key (or Ctrl+Enter) to summarization
text_input.bind("<Return>", summarize_text)        # Enter key
# text_input.bind("<Control-Return>", summarize_text)  # Optional: Ctrl+Enter

# Run the app
app.mainloop()
