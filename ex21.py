d = {"a":1, "b": 2, "c":3}

d = dict((k, v) for k, v in d.items() if v<= 1)

print(d)

#or

a = {"a":1, "b": 2, "c":3}


a = {k: v for k, v in d.items() if v <= 1}
print(a)
