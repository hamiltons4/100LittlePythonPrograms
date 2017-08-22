import string

with open("countries-raw.txt", "r+") as f:
    #print(f.read())
    #print(type(f))
    #print(list(f))
    listf = list(f)
    #filter the variable
    cleaned = [item for item in listf if item != "Top of Page\n"]
    
    #append the variable to a new list
    #print(cleaned)
   

    cleaned2 = [item for item in cleaned if item != "\n"]
    #print(cleaned2)

    #cleanedagain = [item for item in cleaned2 if item not in list(string.ascii_uppercase)]
    #print(cleanedagain)
    
    cleaned3 = [str(item).replace("\n", "") for item in cleaned2 ]
    print(cleaned3)

    cleanedagain = [item for item in cleaned3 if item not in list(string.ascii_uppercase)]
    print(cleanedagain)
    
      
    with open("countries-cleaned.txt", "w") as f:
        for item in cleanedagain:
            f.write(str(item)+ "\n")
        
        
    
