# Extracts words from each line in the list of Strings containing joined
#  words using Viterbi Algorithm
import Viterbi

def findingHiddenStates(sentences):
    foundHiddenWords = []
    f = open("compFile.txt","w+")   # Opening File pointer to store the joined lines
    for line in sentences:
    	# S
    	f.write(line)
        foundHiddenWords.append(Viterbi.viterbiAlgorithm(line.decode('utf-8')))
    for hiddenWord in foundHiddenWords: print hiddenWord
    return foundHiddenWords

