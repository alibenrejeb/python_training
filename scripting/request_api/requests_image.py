import requests

response = requests.get("https://codeavecjonathan.com/res/papillon.jpg", verify=False)
if response.status_code == 200:
    f = open("papillon.jpg", "wb")
    f.write(response.content)
    f.close()
    print("Ecriture terminée")
else:
    print("ERREUR ", response.status_code)