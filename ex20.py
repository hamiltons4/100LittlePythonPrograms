d = {"a": 1, "b": 2, "c": 3}
summed = 0

for n in d:
   
  summed += d[n]

print(summed)

d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))
