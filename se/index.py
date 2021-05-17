import json

from collections import defaultdict
from .normalizer import clean_text


class Index:
    def __init__(self, index):
        self.index = index

    def find(self, query_term):
        return self.index[query_term] if query_term in self.index else []

    def countWords(self, query_term, doc_number):
        try:
            return (
                self.index[query_term][doc_number]
                if doc_number in self.index[query_term]
                else 0
            )
        except KeyError as k:
            return 0


def make_index(docs):
    index = defaultdict(lambda: defaultdict(int))

    for k, doc in enumerate(docs):
        words = set(doc)
        words = map(clean_text, words)

        for word in words:
            index[word][k] += 1

    return index


def save_index(index, path):
    with open(path, "w") as file:
        json.dump(index, file, indent=4)


def load_index(path):
    with open(path, "r") as file:
        return json.load(file)
