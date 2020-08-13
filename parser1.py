import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_table(table):#Функция разбора таблицы с вопросом
    res = pd.DataFrame()
    return(res)

bank_id = 1771062 #ID банка на сайте banki.ru
page=1
max_page=10
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

url = 'https://finviz.com/screener.ashx?v=111'# % (bank_id, page) # url страницы
result = pd.DataFrame()
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text)
tables = soup.find_all('table',{'bgcollor': '#d3d3d3'})
for item in tables:
    res = parse_table(item)
    result = result.append(res,ignore_index=True)
result.to_excel("1.xlsx")