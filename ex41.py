import string

letterString = string.ascii_lowercase
letterList = list(letterString)

with open("my_file.txt", "w") as f:
    for letter in letterList:
        f.write(letter + "\n")
        
