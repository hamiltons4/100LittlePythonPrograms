import string

letterString = string.ascii_lowercase
letterList = list(letterString)

for i in range(0, len(letterList)):
    ff = open(letterList[i]+".txt", "w")
    ff.write(letterList[i])
    ff.close()
    
'''    
import string, os

if not os.path.exists("letter"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")

'''     
