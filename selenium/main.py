from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument("--start-maximized")

service = Service("./chromedriver.exe")