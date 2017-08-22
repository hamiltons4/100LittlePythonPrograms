wordlist = list()

def fileWordCount(s):
#   with open(s, "r") as f:
#       wordlist.append(f.read())
#    print(wordlist)
#    wordNum = wordlist.split()
#    return len(wordNum)

    fileWrapper = open(s)
    wordString = fileWrapper.read()
    
    wordList = wordString.split()
    return len(wordList)

print(fileWordCount("words1.txt"))
