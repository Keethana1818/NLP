import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')

sentence = "The quick BROWN foxes...they are JUMPING over 10 lazy dogs!"


sentence = sentence.lower()


tokens = word_tokenize(sentence)


tokens = [word for word in tokens if word.isalpha()]

stop_words = set(stopwords.words('english'))
clean_tokens = [word for word in tokens if word not in stop_words]

clean_sentence = " ".join(clean_tokens)

print("Tokens after cleaning:")
print(clean_tokens)

print("\nFinal cleaned output:")
print(clean_sentence)
