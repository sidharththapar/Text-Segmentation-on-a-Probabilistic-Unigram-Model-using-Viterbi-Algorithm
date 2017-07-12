import re
from collections import Counter

# Using Viterbi Algorithm to find the hidden states in the given text
def viterbiAlgorithm(text):
    probs = [1.0]
    lasts = [0]
    for i in range(1, len(text) + 1):
        temp_prob_k = 0
        temp_k = 0
        for j in range(max(0, i - max_word_length), i):
            currProb = probs[j] * word_prob(text[j:i])
            if currProb > temp_prob_k:
                temp_prob_k = max(temp_prob_k, currProb)
                temp_k = j
        prob_k, k = temp_prob_k, temp_k
        probs.append(prob_k)
        lasts.append(k)
        #print "probK : ", temp_prob_k, "lastsK : ", temp_k
    words = []
    i = len(text)
    while i > 0:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words, probs[-1]

# find the frequency probability of a word from the Dictionary
def word_prob(word):
    if not wordPattern.match(word.lower()) and len(word) ==1:
        return 1

    prob = dictionary[word.lower()] / total
    return prob

def words(text):
    return re.findall('[a-z]+', text.lower())

wordPattern = re.compile('[a-z]+')
# Creating a frequency dictionary of words in the given file
dictionary = Counter(words(open('PrideAndPrejudice.txt').read()))

# Findind the length of the longest word in the dictionary
max_word_length = max(map(len, dictionary))

# Finding the total number of words in the dictionary
total = float(sum(dictionary.values()))
# The size of the longest word





