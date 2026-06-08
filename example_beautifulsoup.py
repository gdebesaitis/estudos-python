# sites para praticar:
# Site                | O que praticar
# books.toscrape.com  | Listas, paginação, categorias
# quotes.toscrape.com | Textos, tags, autores
# toscrape.com        | Vários exercícios

import requests
from bs4 import BeautifulSoup

link = "https://quotes.toscrape.com"

req = requests.get(link)
print(req)
# print(req.text)

site = BeautifulSoup(req.text, "html.parser")
# print(site.prettify())

titulo = site.find("title")
print(titulo)

list_span = site.find_all("span")
print(list_span)

span = site.find("span", class_="text")
print(span)
