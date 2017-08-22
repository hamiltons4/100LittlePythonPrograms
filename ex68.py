d = dict(weather = "clima", earth = "terra", rain = "chuva")
d2 = {}

for key, value in d.items():
   # print(key)
   #print(str(key).upper())
    d2[str(key).upper()] = value #str(key).upper()
print(d2)


word = input("Enter word: ")
word2 = word.upper()

if word2 in d2:
    print("It's in there")
else:
    print("It's not in there")
        
'''
or
    d = dict(weather = "clima", earth = "terra", rain = "chuva")
    def vocabulary(word):
        try:
            return d[word]
        except KeyError:
            return "That word does not exist."
     
    word = input("Enter word: ").lower()
    print(vocabulary(word))
'''

