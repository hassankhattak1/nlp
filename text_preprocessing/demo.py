import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (only the first time)
nltk.download('punkt')

# Sample text
text = "Natural Language Processing is amazing! Hassan is learning NLP."

# Tokenize the text
tokens = word_tokenize(text)

print("Tokens:", tokens)
