from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import Bygit remote add origin <repository_URL>
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

import json
import time

def scrape_prices(url, tag, classorid, classoridname):
    response = requests.get(url)
    
    if url == 'https://arzdigital.com/coins/bitcoin/':
        chrome_driver_path = r'chromedriver.exe'
        options = Options()
        options.add_argument("--headless")  # Add headless argument to options

        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        time.sleep(20)  # Adjust this time for the page to load

        div_element = driver.find_element(By.CLASS_NAME, 'arz-coin-page-data__coin-toman-price')
        text = div_element.text.strip().split()[0]
        driver.quit()
        return text
    
    elif url_2 == 'https://irarz.com/':
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find(tag, attrs={classorid: classoridname})
        return titles.text

DICT = OrderedDict()

for items in range(0, 5):
    if items == 0:
        url_1 = 'https://arzdigital.com/coins/bitcoin/'
        BTC = scrape_prices(url_1, "div", "class", "arz-coin-page-data__coin-toman-price")
        DICT["BTC"] = BTC
    else:
        url_2 = 'https://irarz.com/'
        USD = scrape_prices(url_2, "span", "id", "usdmax")
        DICT["USD"] = USD.strip()
        EUR = scrape_prices(url_2, "span", "id", "price_eur")
        DICT["EUR"] = EUR.strip()
        GOLD18 = scrape_prices(url_2, "span", "id", "geram18")
        DICT["GOLD18"] = GOLD18.strip()
        GOLD24 = scrape_prices(url_2, "span", "id", "geram24")
        DICT["GOLD24"] = GOLD24.strip()

with open(r'C:\xampp\htdocs\espadana\data.json', 'w') as outfile:
    json.dump(DICT, outfile)

print(DICT)