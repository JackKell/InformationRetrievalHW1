from stemmer import Stemmer


def testStemming():
    words = ["stresses", "gaps", "gas", "ties", "cries", "stress", "agreed", "feed", "fished",
             "pirating", "falling", "dripping"]
    print(words)
    print(Stemmer.stemWords(words))