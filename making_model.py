# Import pandas for data handling
import pandas as pd


# Import our text vectorizers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Import our classifiers
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier


# Import some ML helper function
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report


# Import our metrics to evaluate our model
from sklearn import metrics
from sklearn.metrics import classification_report


# Library for plotting
import matplotlib.pyplot as plt
import seaborn as sns

import pickle

from lib.sentence_cleaning import text_pipeline

colNames = ['text', 'sentiment']
imdb = pd.read_csv('data/imdb_labelled.txt', delimiter='\t',
                   names=colNames, header=None)
yelp = pd.read_csv('data/yelp_labelled.txt', delimiter='\t',
                   names=colNames, header=None)
amazon = pd.read_csv('data/amazon_cells_labelled.txt',
                     delimiter='\t', names=colNames, header=None)
df = pd.concat([imdb, yelp, amazon])

df["clean_message"] = df["text"].apply(text_pipeline)

X = df["clean_message"]
y = df["sentiment"]

# Initialize our vectorizer
vectorizer = TfidfVectorizer()

# This makes your vocab matrix
vectorizer.fit(X)
export_vectorizer = pickle.dumps(vectorizer)
with open("pickles/vectorizer.pickle", mode='wb') as pickle_file:
    pickle.dump(export_vectorizer, pickle_file)

# This transforms your documents into vectors.
X = vectorizer.transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

classes = ["negative", "positive"]

export_model = pickle.dumps(model)
with open("pickles/model.pickle", mode='wb') as pickle_file:
    pickle.dump(export_model, pickle_file)
