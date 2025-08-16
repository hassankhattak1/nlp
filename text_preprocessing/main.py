import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as tb
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Download resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# ---------------- NLP FUNCTIONS ----------------
def preprocess_text(text):
    results = {}

    # Original text
    results["Original Text"] = text

    # Tokenization
    tokens = word_tokenize(text)
    results["Tokenization"] = tokens

    # Stopwords Removal
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
    results["Stopwords Removed"] = filtered_tokens

    # Stemming
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(w) for w in filtered_tokens]
    results["Stemming"] = stemmed_tokens

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    results["Lemmatization"] = lemmatized_tokens

    return results

# ---------------- PROCESS FUNCTION ----------------
def process_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        return

    results = preprocess_text(text)

    # Clear output
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)

    # Colors for each step
    colors = {
        "Original Text": "yellow",
        "Tokenization": "orange",
        "Stopwords Removed": "red",
        "Stemming": "lightgreen",
        "Lemmatization": "cyan"
    }

    # Insert results step by step
    for step, result in results.items():
        color = colors[step]
        output_text.insert(tk.END, f"{step}:\n", step)
        output_text.insert(tk.END, f"{result}\n\n", step)

        # Tag config for colors
        output_text.tag_config(step, foreground="black", background=color)

    output_text.config(state=tk.DISABLED)

# ---------------- UI ----------------
app = tb.Window(themename="cyborg")
app.title("NLP Preprocessing Tool")
app.geometry("800x600")

title_label = tb.Label(app, text="NLP Preprocessing Tool", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Input text
input_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=8, font=("Arial", 12))
input_text.pack(pady=10)

# Process button
process_button = tb.Button(app, text="Process Text", bootstyle="success outline", command=process_text)
process_button.pack(pady=10)

# Output area
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=15, font=("Arial", 12))
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)

# Run app
app.mainloop()
