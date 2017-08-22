checklist = ["Portugal", "Germany", "Munster", "Spain"]
with open("countries-cleaned.txt","r") as f:
    listf = list(f)
    #print(listf)
    cleaned = [str(item).strip("\n") for item in listf]
    #print(cleaned)
    reallyCountries = [item for item in checklist if item in cleaned]
    print(reallyCountries)
'''
    checklist = ["Portugal", "Germany", "Munster", "Spain"]
     
    with open("countries_clean.txt", "r") as file:
        content = file.readlines()
     
    content = [i.rstrip('\n') for i in content]
    checked = [i for i in content if i in checklist]
     
    print(checked)
'''
