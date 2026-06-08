import requests
from bs4 import BeautifulSoup

avaliacaoes = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def converte_avaliacao(avaliacao: str):
    return avaliacaoes.get(avaliacao)


URL = "https://books.toscrape.com"
req = requests.get(URL)
soup = BeautifulSoup(req.text, "html.parser")

# lista para os livros -> a lista de livros comeca no "article"
livros = soup.find_all("article", class_="product_pod")

# lista para guardar os dados
catalogo = []

# itera nos livros
for livro in livros:
    # livro vai ter toda estrutura de article. entao tem que navegar ate o title pelo "h3" e depois pelo "a"
    titulo = livro.find("h3").find("a").get("title")

    avaliacao = livro.find("p", class_="star-rating").get("class")

    preco = livro.find("p", class_="price_color").text.strip()

    disponivel = livro.find("p", class_="instock").text.strip()

    catalogo.append(
        {
            "titulo": titulo,
            "avaliacao": converte_avaliacao(avaliacao[1]),
            "preco": preco,
            "disponivel": disponivel,
        }
    )

# exibe os 5 primeiros
for item in catalogo[:5]:
    print(
        f"{item['titulo']} | {item['avaliacao']} estrelas | {item['preco']} | {item['disponivel']}"
    )
