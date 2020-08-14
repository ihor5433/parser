from bs4 import BeautifulSoup as bs
import prettify
import pandas as pd
from urllib.request import urlopen
import urllib.request
import urllib.error as ur  # import HTTPError
import requests as rq

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
url = ('https://finviz.com/screener.ashx?v=111')

# def getTitle(url):
#     try:
#         html = urllib.request.Request(url,headers=hdr)
#         responce = urlopen(html)
#     except ur.HTTPError:  # если ошибка то выводим сообщение
#         return 'Http Error or Access denite'
#     except ur.URLError:
#         return "Bad Link"
#     try:
#         html = urllib.request.Request(url,headers=hdr)
#         responce = urlopen(html)
#         bsObj = bs(responce.read(), features='lxml')
#         title = bsObj.body.tr
#     except AttributeError:  # если нету атрибута то выводим сообщение
#         return 'Title could not be found'
#     title = bs(responce.read(), features='lxml')
#     return title
# #getTitle(url)

#soup = bs(getTitle(url).read(), features="lxml")
a = 21
for i in range(377):
    a = a + 20
    html = urllib.request.Request(url,headers=hdr)
    responce = urlopen(html)
    soup = bs(responce.read(), features='lxml')

    #проверка выводимого текста
    # with open("output1.html", "w",encoding='utf-8') as file:
    #     file.write(str(soup))
    #print(soup.get_text().encode('utf-8'))
    mydivs = soup.find("table", {"bgcolor": "#d3d3d3"})
    tables_row = mydivs.find_all('tr')
    res = []
    res1 = []
    for tr in tables_row:
        td = tr.find_all('td')
        row = [tr.text for tr in td if tr.text]
        if row:
            res.append(row)


    df = pd.DataFrame(res)
    df.to_csv('1.csv', mode='a', header=False)
    print(df)
    url1 = 'https://finviz.com/screener.ashx?v=111&r='
    url = url1 + str(a)
