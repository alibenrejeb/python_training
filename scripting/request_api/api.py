# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

import requests
import json

# API REST
"""response = requests.get("https://codeavecjonathan.com/res/pizzas1.json", verify=False)

if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
    pizzas = json.loads(response.text)
    print("Nombre de pizzas :", len(pizzas))
else:
    print("ERREUR code : " + str(response.status_code))"""

response = requests.get("https://codeavecjonathan.com/res/exemple.html", verify=False)
if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
else:
    print("ERREUR code : " + str(response.status_code))
