import re
import difflib

# generating formatted original text of the given Chapter of the book for
# comparison with result
def getOriginalText(sentences):
    longString = ""
    for lines in sentences:
        longString +=lines
    # splitting strippedText into sentences ending at '.'
    return re.split('[.]', longString)

# Removes spaces from the given list of Strings "sentences"
def removeSpaces(sentences):
    modelLines = []
    for line in getOriginalText(sentences):
        # print line
        line = line.replace(" ", "")
        line += "."
        modelLines.append(line)
    return modelLines

# extract words from a string
def getWords(text):
    return re.compile('\w+').findall(text)

# returns mean of the given list
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

# get the ratio of correct words and total words of the Viterbi result
def percentageMatching(originalText, opText):
    matchRatio = []
    for lineNum in range(len(originalText)):
        matchRatio.append(difflib.SequenceMatcher(None,originalText[lineNum],
                                                  opText[lineNum]).ratio())
    return mean(matchRatio)

