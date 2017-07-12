import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Calculate the cosine similarity of given two file names
def cosineSimilarity(file1,file2):
	text_files = [file1,file2]
	documents = [open(f) for f in text_files]
	tfidf = TfidfVectorizer().fit_transform(documents[1].readlines(),documents[0].readlines)
	# no need to normalize, since Vectorizer will return normalized tf-idf
	pairwise_similarity = tfidf * tfidf.T
	return 1-(pairwise_similarity.A)[0,1]

def calculateSpaces(file1,file2):
	f1 = open(file1).readlines()
	f2 = open(file2).readlines()
	count1 = 0.0
	count2 = 0.0
	for lines in f1:
		count1 += lines.count(" ")
	for lines in f2:
		count2 += lines.count(" ")
	return math.fabs((count1-count2)/count2)