import requests
from bs4 import BeautifulSoup

bank_id = 1771062 #ID банка на сайте banki.ru
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
url = 'https://finviz.com/screener.ashx?v=111' #% (bank_id) # url страницы
r = requests.get(url, headers = headers)
with open('test.html', 'w', encoding="utf-8") as output_file:
  output_file.write(r.text)
  print(sdf)
  