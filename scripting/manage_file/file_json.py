import json

# Sérialiser data (json -> txt)  dumps
# personne = {
#     "nom": "Paul",
#     "age": 25,
#     "amis": ["Sophie", "Marie", "Jean"]
# }
# f = open("file.json", "w")
# f.write(json.dumps(personne))
# f.close()

# Deséraliser data (txt -> json) loads
f = open("file.json", "r")
data = f.read()
personne = json.loads(data)
print(personne)
f.close()
