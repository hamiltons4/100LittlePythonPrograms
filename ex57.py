import json
from pprint import pprint
'''
ff = open("company2.json", "r")
#f = str(ff.read)
json.load(f)
print(f)
'''
with open("company2.json", "r") as f:
    fdict = json.load(f)
    pprint(fdict)
    
    #print(f.read)

    
