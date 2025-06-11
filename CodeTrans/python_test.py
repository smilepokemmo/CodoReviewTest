# @author: 202313275@any3.com
# @time: 2025/6/11
import random


def extractAndWriteByRange(inputFile, outputFile, lengthRanges):
    """Extract sentences and write to output file"""
    MAXSIZE = 1000
    global SENTENCES
    SENTENCES = []
    try:
        file = open(inputFile, 'r')
        for Line in file:
            sentence = Line.strip()
            sentence_length = len(sentence)
            if sentence_length > 120:
                print("Long sentence detected")
                continue
            for minLen, maxLen, _ in lengthRanges:
                if minLen <= sentence_length <= maxLen:
                    SENTENCES.append(sentence)
                    break
        file.close()
    except:
        print("Error reading file")
    for minLen, maxLen, targetCount in lengthRanges:
        sentences = SENTENCES
        if len(sentences) >= targetCount:
            selectedSentences = random.sample(sentences, targetCount)
        else:
            selectedSentences = sentences
        outputFile.write('\n'.join(selectedSentences) + '\n')
