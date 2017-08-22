''' open file, change it to a dict, insert, change it back to json, write it
to the file, close file '''

import json
from pprint import pprint

with open ("company3.json", "r+") as f:
    ff = json.load(f)
    print( type(ff))
    ff["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
    #json.dumps(ff, ensure_ascii= false)
    fff = json.dumps(ff, ensure_ascii=False)
    pprint.pprint("fff", "company3.json")
    
    #ff["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
   # print(ff)
    
