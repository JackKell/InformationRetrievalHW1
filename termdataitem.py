import math


class TermDataItem:
    def __init__(self, term, termFrequency, documentFrequency, totalDocuments, totalTokens):
        self.term = term
        self.termFrequency = termFrequency
        self.documentFrequency = documentFrequency
        self.totalDocuments = totalDocuments
        self.totalTokens = totalTokens

    def __str__(self):
        return str({"term": self.term, "tf": self.termFrequency, "df":self.documentFrequency,
                    "idf": self.inverseDocumentFrequency(), "tf.idf": self.tfidf(),
                    "probability": self.probability()})

    def __repr__(self):
        return str(self)

    def inverseDocumentFrequency(self):
        return math.log2(self.totalDocuments / self.documentFrequency)

    def tfidf(self):
        return self.termFrequency * self.inverseDocumentFrequency()

    def probability(self):
        return (self.termFrequency / self.totalTokens) * 100