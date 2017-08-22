import string

letterString = string.ascii_lowercase
letterList = list(letterString)
'''
with open("my_file43.txt", "w") as f:
    for i, letter in enumerate(letterList):
        if i+1 <= len(letterList)-1:
           # print(i, i+1)
            print(letterList[i] + letterList[i+1]) #doesn't print next two.

with open("my_file43.txt", "w") as f:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")
        
'''        
with open("my_file43.txt", "w") as f:
    for i in range(0,len(letterList), 2):
            print(letterList[i] + letterList[i+1])
            f.write(letterList[i] + letterList[i+1]+ "\n")
                    
