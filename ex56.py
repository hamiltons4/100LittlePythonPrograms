import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                    {"firstName": "Anna", "lastName": "Smith"},
                    {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
              {"firstName": "Jessy", "lastName": "Petter"}]}

print(json.dumps(d, sort_keys=True, indent=4))
#print(type(d))


ff = open("company1.json", "w")
ff.write(json.dumps(d, sort_keys=True, indent=4))
ff.close()

