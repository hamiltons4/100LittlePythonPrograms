a = [1,2,3]

b = (4,5,6)
#for i, j in zip(a,b):
 #   print(i + j) The old way. I did it as below.
    


#c = zip(a,b)

#listc = list(c)

#d = map(sum, listc)

#e = list(d)

e = list(map(sum,list(zip(a,b))))
for item in e:
   # print(str(item) + "\n")
    print(str(item))
    
    
