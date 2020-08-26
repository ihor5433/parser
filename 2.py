
from bs4 import BeautifulSoup as bs
import pandas as pd
from os.path import exists
from os import remove
from urllib.request import Request, urlopen
import urllib.error as ur  # import HTTPError
from requests import get as rget
import time
from progress.bar import IncrementalBar
import tqdm
import json

url = 'https://www.streetinsider.com/ec_earnings.php?q=adi'
url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IMBI&apikey=UQGWFV8GJ5UKWK2T'
#import Earning_TradingView 
hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
# def soup():
#     soup = bs(responce, features="lxml")
#     return soup
#responce = rget(url, headers=hdr)
def convert_html(url):
    responce = rget(url, headers=hdr).text
    soup = bs(responce, features="lxml") 
    return soup

def getTitle(url):
    """Проверка ссылки на ошибки"""
    try:
        html = Request(url, headers=hdr)
        html = urlopen(html)
    except ur.HTTPError:  # если ошибка то выводим сообщение
        return "Http Error or Access denite"
    except ur.URLError:
        return "Bad Link"
#print(responce.text)
a = convert_html(url).get_text()
d = json.loads(a)
df = pd.DataFrame.from_dict(d, orient = 'index')
df.to_csv('json.csv')
#a = convert_html(url).text
#df=pd.DataFrame(responce.json())
#print(df)