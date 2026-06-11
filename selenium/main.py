import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# aqui passa configs pro chrome
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--start-maximized")

# aponta para o chromedriver
chromedriver_path = Path(__file__).with_name("chromedriver.exe")
service = Service(str(chromedriver_path))

# inicia o driver com as configs passadas antes
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)

# abre a pagina do instagram e aguarda carregar
driver.get("https://instagram.com")
time.sleep(3)
print("Entramos na página do Instagram")

# preenche o edit do email
email = driver.find_element(By.NAME, "email")
email.send_keys("meuemail@email.com")

# preenche o edit da senha
senha = driver.find_element(By.NAME, "pass")
senha.send_keys("senha1234")
senha.send_keys(
    Keys.RETURN
)  # aqui faz dar o [enter] pra pegar o evento de submit mais facil

# execução de scripts na pagina
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.execute_script("arguments[0].scrollIntoView();", elemento)

# fala pro webdriver esperar até 30sec ate achar o elemento.
elemento = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "id do elemento"))
)
