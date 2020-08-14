from bs4 import BeautifulSoup as bs
import prettify
import pandas as pd
from urllib.request import urlopen
import urllib.request
import urllib.error as ur  # import HTTPError
import requests as rq

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
url = ('https://finviz.com/screener.ashx?v=111&r=1')

def getTitle(url):
    try:
        html = urllib.request.Request(url,headers=hdr)
        html = urlopen(html)
    except ur.HTTPError:  # если ошибка то выводим сообщение
        return 'Http Error or Access denite'
    except ur.URLError:
        return "Bad Link"
        
print(getTitle(url))




def finviz_all_stocks(url, output=False, output_in_file_html=False):
    """собирает все акции с финвиза"""
    if getTitle(url) != None:
        return getTitle(url)
    a = 20
    for i in range(375):
        
        html = urllib.request.Request(url, headers=hdr)
        responce = urlopen(html)
        soup = bs(responce.read(), features='lxml')
        if output_in_file_html == True:
            # проверка выводимого текста
            with open("output_test.html", "w", encoding='utf-8') as file:
                file.write(str(soup))
                #print(soup.get_text().encode('utf-8'))
            return 
        mydivs = soup.find("table", {"bgcolor": "#d3d3d3"})
        tables_row = mydivs.find_all('tr')
        res = []
        for tr in tables_row[1:]:
            td = tr.find_all('td')
            row = [tr.text for tr in td[:-3] if tr.text]
            if row:
                res.append(row)

        df = pd.DataFrame(res)

        df.to_csv('2.csv', mode='a', header=False)
     
        if output == True:
            print(df)
        url1 = 'https://finviz.com/screener.ashx?v=111&r='
        url = url1 + str(a)
        
        a = a + 20


finviz_all_stocks(url,output=True)
