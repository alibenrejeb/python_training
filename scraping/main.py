import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://books.toscrape.com/'
response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all("img")
pprint(images)
# body = soup.find_all_previous('body')
# print(type(body))
# print(soup.prettify())

# Fonction pour parcourir le DOM
# def traverse_dom(element, level=0):
#     # Afficher l'element actuel
#     if element.name:
#         print(f"{' ' * level}<{element.name}>")

#     if hasattr(element, 'children'):
#         for child in element.children:
#             traverse_dom(child, level+1)

# traverse_dom(soup)


# url = "https://www.google.com"
# try:
#     response = requests.get(url)
#     response.raise_for_status()
#     with open("index.html", "w") as file:
#         file.write(response.text)
# except requests.exceptions.HTTPError as errorh:
#     print("Http error:", errorh)
# except requests.exceptions.ConnectionError as errorc:
#     print("Error connection:", errorc)
# except requests.exceptions.Timeout as errort:
#     print("Timeout error:", errort)
# except requests.exceptions.RequestException as error:
#     print("Error request:", error)
