import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (run once)
nltk.download('punkt')

# Spam words list
spam_words = ["win", "cash", "free", "prize"]

# Input text
text = "You are WINNING a free prize now"

# Normalize text
text = text.lower()

# Tokenize
tokens = word_tokenize(text)

# Check for spam words
is_spam = any(word in tokens for word in spam_words)

print(is_spam)
