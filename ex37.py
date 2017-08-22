import re

def wordCount(s):
    fileWrapper = open(s)
    wordString = fileWrapper.read()

    wordList = re.split(',| ', wordString)
    print(wordList)
    return len(wordList)

print(wordCount("words2.txt"))
