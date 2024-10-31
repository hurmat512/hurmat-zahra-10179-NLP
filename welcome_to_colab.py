# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

from google.colab import drive
drive.mount('/content/drive')

/content/drive/MyDrive/archive.zip

import os # Import the os module for file operations

file_path = '/content/drive/MyDrive/archive.zip'  # Store the file path in a variable
# Now you can work with the file, e.g., check if it exists
if os.path.exists(file_path):
  print(f"File found at: {file_path}")
else:
  print(f"File not found at: {file_path}")

#  To further operate with the file you can use other functionalities
#  For example, to read content from it, extract it, etc.

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
nlp = spacy.load("en_core_web_sm")

text = "Running is better than walking and it's a great exercise!"


text = text.lower()


tokens = word_tokenize(text)


stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]


doc = nlp(" ".join(filtered_tokens))
lemmatized_tokens = [token.lemma_ for token in doc]


print("Original Text:", text)
print("Filtered Tokens:", filtered_tokens)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)

import gensim
from gensim.models import Word2Vec

# Sample sentences for training
sentences = [
    ["i", "love", "natural", "language", "processing"],
    ["deep", "learning", "is", "a", "subfield", "of", "machine", "learning"],
    ["word", "embeddings", "are", "useful", "for", "text", "analysis"],
    ["word2vec", "is", "a", "popular", "algorithm", "for", "word", "embeddings"],
]

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# Save the model
model.save("word2vec.model")

# Load the model
loaded_model = Word2Vec.load("word2vec.model")

# Example: Get the vector for a word
vector = loaded_model.wv["natural"]
print("Vector for 'natural':", vector)

# Example: Find similar words
similar_words = loaded_model.wv.most_similar("language", topn=3)
print("Most similar words to 'language':", similar_words)

from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love natural language processing.",
    "Natural language processing is fascinating.",
    "I enjoy learning about machine learning."
]

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents
X_bow = vectorizer.fit_transform(documents)

# Convert to array and get feature names
bow_array = X_bow.toarray()
feature_names = vectorizer.get_feature_names_out()

# Display results
print("Bag of Words Array:")
print(bow_array)
print("Feature Names:", feature_names)

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "I love natural language processing and it's fascinating."

# Process the text with spaCy
doc = nlp(text)

# Display the words with their corresponding POS tags
print("Word\t\tPOS Tag")
print("-" * 20)
for token in doc:
    print(f"{token.text}\t\t{token.pos_}")

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Sample text
text_vader = "I love this product! It's absolutely wonderful."

# Initialize VADER Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Get sentiment scores
scores = sia.polarity_scores(text_vader)

# Display results
print("VADER Sentiment Analysis:")
print(scores)

from textblob import TextBlob

# Sample text
text_blob = "I love this product! It's absolutely wonderful."

# Create a TextBlob object
blob = TextBlob(text_blob)

# Get sentiment polarity and subjectivity
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Display results
print("TextBlob Sentiment Analysis:")
print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking at buying U.K. startup for $1 billion. Tim Cook announced this."

# Process the text with spaCy
doc = nlp(text)

# Display the recognized entities
print("Named Entities, Phrases, and Concepts:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_} (Confidence: {ent.kb_id_})" if ent.kb_id_ else f"{ent.text} - {ent.label_}")