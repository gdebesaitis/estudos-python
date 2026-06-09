# sites para praticar:
# Site                | O que praticar
# books.toscrape.com  | Listas, paginação, categorias
# quotes.toscrape.com | Textos, tags, autores
# toscrape.com        | Vários exercícios

import requests
from bs4 import BeautifulSoup

link = "https://quotes.toscrape.com"

req = requests.get(link)
# print(req)
# print(req.text)

site = BeautifulSoup(req.text, "html.parser")
# print(site.prettify())

# selecionadores de elementos
#   find() -> retorna o primeiro elemento que bater com o critério. se nao achar, retorna none
#   find_all() -> retorna uma lista com todos os elementos. a lista pode ser vazia.
#   select() -> usa sintaxe css pura. sempre retorna uma lista. melhor pra estruturas aninhadas "div.card > h2"
#   select_one() -> igual ao select(), mas retorna só o primeiro find().
#   filtros que funcionam nos 4: class_="nome", id="id" ou dict de atributos attrs={}
titulo = site.find("title")
# print(titulo)

find = site.find("div", class_="col-md-4")
# print(find)

list_span = site.find_all("span")
# print(list_span)

span = site.find("span", class_="text")
# print(span.get_text())

# selecionando por css selector
#   .classe -> seleciona pelo nome da classe css
#   #id -> seleciona pelo id
#   tag.classe -> seleciona pela tag e classe, mais preciso
#   pai filho -> espaço entre os 2 seletores significa "descendente em qualquer nivel"
#   pai > filho -> pega o filho direto, 1 nivel apenas.

# css = site.select("p.text-muted")
# print(css)
paifilho = site.select("div span")
# print(paifilho)
filhodireto = site.select("div > span")
# print(filhodireto)

# extraindo conteudo
#   .text -> retorna todo o texto dentro do elemento, incluindo texto de tags filhas.
#   .get_text() -> igual ao .text mas nao retorna texto das tags filhas.
#   elemento["attr"] -> acessa qualquer atributo como "href" "src". Da erro se retorno for dict
#   .get("attr") -> mais seguro que o acesso por chave. retorna none se n existir sem levantar erro
for item in paifilho:
    print(item.get_text())

# navegando na arvore
#   .parent -> sobe um nivel no html. é encadeavel: .parent.parent sobe 2 niveis
#   .children -> gerador com filhos diretos. iterar com for.
#   .find_all -> busca apenas os filhos diretos, sem netos. (recursive = false). util para quando a page tem estruturas repetidas em varios niveis
#   .next_sibling -> elemento seguinte no mesmo nivel. geralmente retorna o primeiro vazio. para isso usar .find_next_sibling antes.


# orientações gerais:
# usando o devtools do navegador é mais certeiro pra pegar o seletor exato do css do elemento.
# preferivel usar select() quando o elemento tiver uma combinação de classe + posição na hierarquia. find() quando tiver um id ou classe única direta
# SEMPRE chegar se o find() retornou algo antes de tentar acessar o .text. se for none da erro.
# da pra usar o soup.prettify() pra ver o html melhor antes de raspar.
