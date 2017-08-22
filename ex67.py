d = dict(weather = "clima", earth = "terra", rain = "chuva")

word = input("Enter word: ")
if word in d:
    print(d[word])
else:
    print("We couldn't find that word")
        
    
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find that."
word = input("Enter word: ")
print(vocabulary(word))

