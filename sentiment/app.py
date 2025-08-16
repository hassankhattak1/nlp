from textblob import TextBlob
import streamlit as st

# --- Custom CSS for Tailwind-like look ---
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .textarea {
        border-radius: 0.5rem;
        padding: 0.75rem;
        border: 2px solid #3b82f6;
    }
    .button {
        background-color: #3b82f6;
        color: white;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        transition: all 0.3s ease;
    }
    .button:hover {
        background-color: #2563eb;
        transform: scale(1.05);
        cursor: pointer;
    }
    .result {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1rem;
    }
    .positive { color: #16a34a; }
    .negative { color: #dc2626; }
    .neutral { color: #f59e0b; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📝 Sentiment Analysis App</div>', unsafe_allow_html=True)

# Input text area
user_input = st.text_area("Enter your text here:", height=150)

# Sentiment analysis function
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊", "positive"
    elif polarity < 0:
        return "Negative 😢", "negative"
    else:
        return "Neutral 😐", "neutral"

# Analyze button
if st.button("Analyze", key="analyze"):
    result_text, sentiment_class = analyze_sentiment(user_input)
    st.markdown(f'<div class="result {sentiment_class}">Sentiment: {result_text}</div>', unsafe_allow_html=True)
