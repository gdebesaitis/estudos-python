from pathlib import Path
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

from database import DatabaseManager

db = DatabaseManager()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

chrome_driver_path = Path(__file__).with_name("chromedriver.exe")
service = Service(str(chrome_driver_path))

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)

# abre a pagina inicial
driver.get("https://realpython.github.io/fake-jobs/")

# pega uma lista dos cards
cards = driver.find_elements(By.CSS_SELECTOR, "div.column.is-half")

lista_vagas = []

linhas_do_banco = db.fetch_all("select titulo from vagas")

titulos_salvos = [linha["titulo"] for linha in linhas_do_banco]

for card in cards:
    url = None
    card_footer = card.find_element(By.CLASS_NAME, "card-footer")

    elements = card_footer.find_elements(By.CSS_SELECTOR, "a")

    for text in elements:
        if text.text == "Apply":
            url = text.get_attribute("href")

    if url is not None:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        titulo = soup.find("h1", class_="title is-2").text

        if titulo in titulos_salvos:
            print(f"A vaga {titulo} ja existe. Pulando...")
            continue

        empresa = soup.find("h2", class_="subtitle is-4 company").text
        localizacao = soup.select_one("#location").get_text()
        descricao = soup.find("div", class_="content").find("p").text

        lista_vagas.append(
            {
                "titulo": titulo,
                "empresa": empresa,
                "localizacao": localizacao,
                "descricao": descricao,
                "url": url,
                "coletado_em": datetime.now(),
            }
        )

for vaga in lista_vagas:
    sql = """ 
        insert into vagas(titulo, empresa, localizacao, descricao, url, coletado_em)
        values (%(titulo)s, %(empresa)s, %(localizacao)s, %(descricao)s, %(url)s, %(coletado_em)s);
    """

    dados = {
        "titulo": vaga["titulo"],
        "empresa": vaga["empresa"],
        "localizacao": vaga["localizacao"],
        "descricao": vaga["descricao"],
        "url": vaga["url"],
        "coletado_em": vaga["coletado_em"],
    }

    db.execute_query(query=sql, params=dados)
