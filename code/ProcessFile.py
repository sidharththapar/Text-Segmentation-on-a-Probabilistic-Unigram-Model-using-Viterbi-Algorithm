import FormatText
import HiddenStates
import Viterbi
import os
import accuracyChecks

class ProcessingFile:

    # Reading PrideAndPrejudiceChapter3.txt and storing each of its line
    #  into a list(sentences)
    fp = open("PrideAndPrejudiceChapter3.txt")
    sentences = fp.readlines()

    # Joins the extracted words and inserts spaces at
    #  the correct locations.
    # Writes the formatted text into an output file
    #  after the output is encoded into UTF8 format
    f = open("opFile.txt", "w+")
    for line in HiddenStates.findingHiddenStates(FormatText.removeSpaces(sentences)):
        for x in line[0]:
            utf8string = x.encode("UTF-8")
            if utf8string == "." or utf8string == "," or utf8string == "-" \
            or utf8string == '"':
                f.seek(-1, os.SEEK_CUR) 
            elif utf8string == "\n":
                f.write(utf8string)
                continue
            f.write(utf8string + " ")

    # Comparing the original text with the original using the proposed comparison
    #   technique
    ratio = FormatText.percentageMatching(FormatText.getOriginalText(sentences),
                                           FormatText.getOriginalText(sentences))

    # Reading the output file
    opFile = open("opFile.txt")
    sentences2 = opFile.readlines()

    # Checking the percentage accuracy of our output file after applying Viterbi
    ratio2 = FormatText.percentageMatching(FormatText.getOriginalText(sentences),
                                            FormatText.getOriginalText(sentences2))
    # Check the accuracy ratio of the output file versus original text
    #   considering the cosine similarity of the words in the original text
    cosSimilarity = accuracyChecks.cosineSimilarity\
        ('PrideAndPrejudiceChapter3.txt', 'opFile.txt')

    # Returns the ratio of the spaces wrong placed in the output file
    #  to the placement of spaces in the original text
    spacesError = accuracyChecks.calculateSpaces\
        ('PrideAndPrejudiceChapter3.txt', 'opFile.txt')

    print "---=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=---"
    print 'ratiocheck : ', ratio
    print 'ratiocheck2 : ', ratio2
    print 'cosine similarity : ', cosSimilarity
    print 'spaces error percentage : ', spacesError

    applyVertibi2 = Viterbi.viterbiAlgorithm('Iamfast')
    applyVertibi3 = Viterbi.viterbiAlgorithm('Letusmeetafternoon')
    # applyVertibi = Viterbi.viterbi_segment('itseasyformetosplitlongruntogetherblocks')
    #
    # print applyVertibi
    print applyVertibi3
    # print Virtebi.word_prob("therefore")
    # print Virtebi.word_prob("attacked")
    # print Virtebi.word_prob("proudest")
    # print len(Virtebi.dictionary)
    # print applyVertibi3