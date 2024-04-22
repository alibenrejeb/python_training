from bs4 import BeautifulSoup
import requests

response = requests.get("http://127.0.0.1:5500/site/recette.html")
response.encoding = "utf-8"
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

title_h1 = soup.find("h1").text
list_div_centre= soup.find_all("div", class_="centre")
description = list_div_centre[1].find("p", class_="description").text

div_info = soup.find("div", class_="info")
img = div_info.find("img")

print(img["src"])

print()
