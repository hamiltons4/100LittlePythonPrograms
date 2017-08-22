import string

letterString = string.ascii_lowercase
letterList = list(letterString)

with open("my_file44.txt", "w") as f:
    for i in range(0,len(letterList), 3):
        if i+2 <=len(letterList)-2:
            print(letterList[i] + letterList[i+1] + letterList[i+2])
            f.write(letterList[i] + letterList[i+1]+ letterList[i + 2] + "\n")
        else:
            print(letterList[i] + letterList[i+1])
            f.write(letterList[i] + letterList[i+1]+ "\n")

'''
    import string
     
    letters = string.ascii_lowercase + " "
     
    slice1 = letters[0::3]
    slice2 = letters[1::3]
    slice3 = letters[2::3]
     
    with open("letters.txt", "w") as file:
        for s1, s2, s3 in zip(slice1, slice2, slice3):
            file.write(s1 + s2 + s3 + "\n")

'''

