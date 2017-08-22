''' make alphabet list. open files according to the alpha name. make results list.
    read file. make file content into string.

'''
import string
letterString = string.ascii_lowercase
letterList = list(letterString)
my_list = list()
checkList = ["p", "y", "t", "h", "o", "n"]

for i in letterList:
    ff = open(i + ".txt", "r")
    a = str(ff.read())
    if a in checkList:
        my_list.append(a)
    ff.close()

print(my_list)


