import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

chrome_driver_path = Path(__file__).with_name("chromedriver.exe")
service = Service(str(chrome_driver_path))

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(3)

# preencher campos do login
name = driver.find_element(By.NAME, "username")
name.send_keys("tomsmith")

password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")

btn = driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

time.sleep(10)
