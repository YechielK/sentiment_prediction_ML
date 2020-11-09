from pickle import load, loads
from lib.sentence_cleaning import text_pipeline
with open("pickles/model.pickle", mode="rb") as pickle_file:
    pickled_model = load(pickle_file)
    model = loads(pickled_model)

with open("pickles/vectorizer.pickle", mode="rb") as pickle_file:
    pickled_vectorizer = load(pickle_file)
    vectorizer = loads(pickled_vectorizer)


def predict(sentence):
    sentence = text_pipeline(sentence)

    # This transforms your documents into vectors.
    X = vectorizer.transform([sentence])

    return model.predict(X)
