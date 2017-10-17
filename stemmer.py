import re


class Stemmer(object):
    verbPattern = re.compile("\w+(?:ed|edly|ing|ingly)")
    endingPattern = re.compile("\w+(at|bl|iz)")
    endsInDoublePattern = re.compile(r"\w+(\w)\1")

    @staticmethod
    def stemWords(words):
        stemmedWords = words.copy()
        for index in range(len(stemmedWords)):
            stemmedWords[index] = Stemmer.stem(stemmedWords[index])
        return stemmedWords

    @staticmethod
    def stem(word):
        # Replace sses by ss
        stemmedWord = re.sub("sses", "ss", word)
        # Remove 's' plurals
        stemmedWord = re.sub("(?<=[^aeious])s", "", stemmedWord)
        # Replace ied and ies with i or ie
        stemmedWord = re.sub("(^[a-zA-Z])(?:ied|ies)", r"\1ie", stemmedWord)
        stemmedWord = re.sub("([a-zA-Z]{2,})(?:ied|ies)", r"\1i", stemmedWord)
        # Replace eed and eedly with ee
        stemmedWord = re.sub("([aeiuo][^aeiuo]+)(?:eed|eedly)", r"\1ee", stemmedWord)

        if Stemmer.verbPattern.match(stemmedWord):
            tempStemmedWord = re.sub("(?:ed|edly|ing|ingly)", "", stemmedWord)
            if Stemmer.endingPattern.match(tempStemmedWord):
                stemmedWord = re.sub("(at|bl|iz)", r"\1e", tempStemmedWord)
            elif Stemmer.endsInDoublePattern.match(tempStemmedWord):
                stemmedWord = re.sub(r"([^lsz])\1", r"\1", tempStemmedWord)
        return stemmedWord
