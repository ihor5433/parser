from bs4 import BeautifulSoup as bs
import prettify
import pandas as pd
from urllib.request import urlopen
import urllib.request
import urllib.error as ur  # import HTTPError
from urllib import robotparser
import requests as rq
from selenium import webdriver
import random
hdr = {
    'Host': 'www.kicksusa.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.121 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,tr;q=0.7',
    'Cookie': 'visid_incap_...=put here your visid_incap_ value; incap_ses_...=put here your incap_ses_ value',}
url = 'https://www.streetinsider.com/ec_earnings.php?day=2020-08-13'
# html = urllib.request.Request(url,headers=hdr)
# responce = urlopen(html)
# print(responce.read())

url = "https://www.streetinsider.com/ec_earnings.php?day=2020-08-13"
UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

ua = UAS[random.randrange(len(UAS))]

hdr = {'user-agent': ua}
r = rq.get(url, headers=hdr)
print(r)


html = urllib.request.Request(url, headers=hdr)
responce = urlopen(html)
soup = bs(responce.read(), features='lxml')
with open("output_test.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
mydivs = soup.find("table", {"class": "earning_hystory"})
tables_row = mydivs.find('tr')
res = []
for tr in tables_row:
    td = tr.find_all('td')
    row = [tr.text for tr in td if tr.text]
    if row:
        res.append(row)

df = pd.DataFrame(res)

df.to_csv('2.csv', mode='a', header=False)
