d = dict(a = list(range(1,11)), b = list(range(11, 21)), c = list(range(21, 31)))

#print(d["b"])
#print("b has value " + d["b"])
s = "b has value " + str(d["b"])
t = "c has value " + str(d["c"])
u = "a has value " + str(d["a"])


print(s)
print(t)
print(u)

for key, value in d.items():
    print(key, "has value", value)
    
