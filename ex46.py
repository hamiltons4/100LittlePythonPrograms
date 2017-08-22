import string

letterString = string.ascii_lowercase
letterList = list(letterString)
my_list = list()


for i in letterList:
        print(i)
        ff = open(i+".txt", "r")
        #a = str(f.read())
        my_list.append(ff.read())
        ff.close()


print(my_list)

        
        
        
