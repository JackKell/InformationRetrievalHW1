import re
import string


def cleanText(text):
    cleanedText = text
    # Remove line endings
    cleanedText = cleanedText.replace("\r", "").replace("\n", " ")
    # To lowercase
    cleanedText = cleanedText.lower()
    # Remove Punctuation
    cleanedText = removePunctuation(cleanedText)
    return cleanedText


def removePunctuation(text):
    return re.sub("[" + string.punctuation + "]", "", text)
