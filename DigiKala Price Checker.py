import os #import OS // to clear screen
from typing import Text #to make clear screen
import requests #import request to get url
from bs4 import BeautifulSoup
from unidecode import unidecode #import unidecode to convert AR / FA numbers to EN numbers
print ("Get price from DIGIKALA")
getdigikalaurl = input("Enter an address from DigiKala website:")
os.system('cls' if os.name == 'nt' else 'clear') # clear screen code
# Get URL from DIGIKALA
URL = getdigikalaurl
# set user agents
headers = {"user-agents" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page = requests.get(URL , headers= headers)
# parse html page
soup = BeautifulSoup(page.content , 'html.parser')
# find title elements
title = soup.find(class_ = "c-product__title").get_text()
# find price elements
price = soup.find(class_ = "c-product__seller-price-pure js-price-value").get_text()
#convert arabic / farsi numbers to english numbers
enprice = unidecode (price)
# print title of the product
print(title.strip())
# print price
print(enprice.strip() + " Toman")