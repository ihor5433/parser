import os
import urllib.error as ur
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs
from requests import get as rget

hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}

def path(path:str):
    '''Вернуть путь к файлу

        Параметры path: 'api', 'result', 'json', 'csv','ticker','annual_db','quarterly_db','missed'

        Результат:
            Абсолютный путь к файлу

        '''
    path_ticker = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Files_txt', 'ticker.txt'))
    path_api = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Files_txt', 'api_key.txt'))
    path_result = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data','Stocks'))
    path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental', 'temp'))
    path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))
    path_annual_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/annual.db'))
    path_quarterly_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/quarterly.db'))
    missed_stock = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Files_txt', 'missed_stocks.txt'))

    if path == 'api':
        return path_api
    elif path == 'result':
        return path_result
    elif path == 'json':
        return path_json
    elif path == 'csv':
        return path_csv
    elif path == 'ticker':
        return path_ticker
    elif path == 'annual_db':
        return path_annual_db
    elif path == 'quarterly_db':
        return path_quarterly_db
    elif path == 'missed':
        return missed_stock

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


