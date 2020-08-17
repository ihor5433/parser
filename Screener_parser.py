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


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://finviz.com/screener.ashx?v=111&r="




def convert_html(url):
    responce = rget(url, headers=hdr).text
    
    global soup
    soup = bs(responce, features="lxml") 


def getTitle(url):
    """Проверка ссылки на ошибки"""
    try:
        html = Request(url, headers=hdr)
        html = urlopen(html)
    except ur.HTTPError:  # если ошибка то выводим сообщение
        return "Http Error or Access denite"
    except ur.URLError:
        return "Bad Link"


def last_page():
    """Ищет последнюю старницу для цикла"""
    convert_html(url)
    return int(soup("a", href=True)[-3].get_text())


def finviz_all_stocks(url, output=False, output_in_file_html=False):
    """собирает все акции с финвиза"""
    if exists ('2.csv'):
        remove('2.csv')
    if getTitle(url) != None:
        return getTitle(url)
    page_code = 1
    url1 = url + str(page_code)
    for i in tqdm.trange(last_page()+1):
     
        convert_html(url1)
        if output_in_file_html == True:
            # проверка выводимого текста
            with open("output_test.html", "w", encoding="utf-8") as file:
                file.write(str(soup))
            return
        mydivs = soup.find("table", {"bgcolor": "#d3d3d3"})
        tables_row = mydivs.find_all("tr")
        res = []
        for tr in tables_row[1:]:
            td = tr.find_all("td")
            row = [tr.text for tr in td[:-3] if tr.text]
            if row:
                res.append(row)

        df = pd.DataFrame(res)
        
        df.to_csv("2.csv", mode="a", header=False)

        if output == True:
            print(df)
        page_code += 20
        url1 = url + str(page_code)
        
        

        


finviz_all_stocks(url, output=False)
