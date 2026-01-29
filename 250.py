#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk


# In[8]:


from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer =WordNetLemmatizer()
text ='pizzas'
res= lemmatizer.lemmatize(text)
print(res)


# In[9]:


from nltk.corpus import stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
text = ["this", "is", "a", "sample", "sentence"]
res = [word for word in text if word.lower() not in stop_words]
print(res)


# In[6]:


def levenshtein_distance(a, b):
  m, n = len(a), len(b)
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  for i in range(m + 1):
      dp[i][0] = i
  for j in range(n + 1):
      dp[0][j] = j

  for i in range(1, m + 1):
      for j in range(1, n + 1):
          if a[i - 1] == b[j - 1]:
              cost = 0
          else:
              cost = 1

          dp[i][j] = min(
              dp[i - 1][j] + 1,      # deletion
              dp[i][j - 1] + 1,      # insertion
              dp[i - 1][j - 1] + cost # substitution
          )

  return dp[m][n]


word1 = "START"
word2 = "STARE"

print("Levenshtein Distance:", levenshtein_distance(word1, word2))

   


# In[7]:



import re

sentence = """The quick,Brown foxes...
they are JUMPING over
10 lazy dogs!"""

stop_words = {"the", "they", "are", "over"}

def clean_sentence(text):
    # lowercase
    text = text.lower()

    # remove punctuation & numbers
    text = re.sub(r"[^a-z\s]", "", text)

    words = text.split()

    # remove stop words
    words = [w for w in words if w not in stop_words]

    # basic normalization
    normalized = []
    for w in words:
        if w.endswith("ing"):
            w = w[:-3]
        if w.endswith("es"):
            w = w[:-2]
        normalized.append(w)

    return normalized


output = clean_sentence(sentence)
print(output)


# In[8]:


spam_words = ["win", "free", "prize"]

message = "you are winning a free prize now!"

def spam_filter(text, spam_list):
    text = text.lower()
    for word in spam_list:
        if word in text:
            return "spam"
    return "not spam"


result = spam_filter(message, spam_words)
print(result)


# In[ ]:




