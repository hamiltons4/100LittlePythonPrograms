import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
#print(r.text[::])
count = 0

text = r.text
#print(text)
s = str(r.text)
#print(s)
for letter in s:  
    if letter == "a":
        count += 1

print(count)
