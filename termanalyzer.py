from utility import cleanText
from termdataitem import TermDataItem
import os


class TermAnalyzer:
    def __init__(self):
        self._termFrequencyByDocument = {}
        self._documentFrequencyMap = {}
        self._termFrequencyMap = {}

    def analyzeFile(self, filePath, filename):
        # Read and clean the file contents
        with open(filePath, 'r') as content_file:
            text = content_file.read()
        # Clean the text
        text = cleanText(text)
        # Split the text into words
        words = text.split()
        currentDocumentTermFrequency = {}
        # Get the term frequency data for each document
        for word in words:
            # Increment the document term frequency for the database
            if word not in currentDocumentTermFrequency.keys():
                totalTermFrequency = self._documentFrequencyMap.get(word, 0)
                self._documentFrequencyMap[word] = totalTermFrequency + 1
            # Increment the term frequency for the document
            currentTermFrequency = currentDocumentTermFrequency.get(word, 0)
            currentDocumentTermFrequency[word] = currentTermFrequency + 1
            # Increment the term frequency for all documents
            termFrequencyValue = self._termFrequencyMap.get(word, 0)
            self._termFrequencyMap[word] = termFrequencyValue + 1
        # Add the current document's term frequency to the map of all document term frequencies
        self._termFrequencyByDocument[filename] = currentDocumentTermFrequency

    def analyzeDirectory(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filePath = os.path.join(directory, filename)
                self.analyzeFile(filePath, filename)

    def getDocumentCount(self):
        return len(self._termFrequencyByDocument.keys())

    def getUniqueTermsCount(self):
        return len(self._termFrequencyMap.keys())

    def getTermsCount(self):
        totalTerms = 0
        for term, tf in self._termFrequencyMap.items():
            totalTerms += tf
        return totalTerms

    def getSingletonTermCount(self):
        singletonDatabaseWords = 0
        for term, df in self._documentFrequencyMap.items():
            if df == 1:
                singletonDatabaseWords += 1
        return singletonDatabaseWords

    def getAverageTermsPerDocument(self):
        return self.getTermsCount() / self.getDocumentCount()

    def getTermData(self, topN=30, reverse=True):
        termData = []
        for term, tf in self._termFrequencyMap.items():
            df = self._documentFrequencyMap[term]
            termDataItem = TermDataItem(term, tf, df, self.getDocumentCount(), self.getTermsCount())
            termData.append(termDataItem)
        termData = sorted(termData,
                          key=lambda currentTermDataItem: currentTermDataItem.termFrequency,
                          reverse=reverse)[:topN]
        return termData

    def printTermData(self, topN=30, reverse=True, padding=9):
        print("Top", topN, "Terms:")
        print("Term".ljust(padding),
              "TF".ljust(padding),
              "DF".ljust(padding),
              "IDF".ljust(padding),
              "TF.IDF".ljust(padding),
              "Probability (%)")
        for termDataItem in self.getTermData(topN, reverse):
            print(termDataItem.term.ljust(padding),
                  str(termDataItem.termFrequency).ljust(padding),
                  str(termDataItem.documentFrequency).ljust(padding),
                  str(round(termDataItem.inverseDocumentFrequency(), 3)).ljust(padding),
                  str(round(termDataItem.tfidf(), 3)).ljust(padding),
                  str(round(termDataItem.probability(), 3),).ljust(padding)
                  )

    def printStats(self, topN=30, reverse=True):
        print("Terms Count:", self.getTermsCount())
        print("Unique Terms Count:", self.getUniqueTermsCount())
        print("Singleton Database Words:", self.getSingletonTermCount())
        print("Average Terms Per Document:", round(self.getAverageTermsPerDocument(), 3))
        self.printTermData(topN, reverse)

