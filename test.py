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
import os
hdr = {
    "Host": "www.kicksusa.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/72.0.3626.121 Safari/537.36",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,tr;q=0.7",
    "Cookie": "visid_incap_...=put here your visid_incap_ value; incap_ses_...=put here your incap_ses_ value",
}


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://www.tradingview.com/markets/stocks-usa/earnings/"
# html = urllib.request.Request(url,headers=hdr)
# responce = urlopen(html)
# print(responce.read())


UAS = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
)


r = rq.get(url, headers=hdr)
print(r)

if os.path.exists('w.csv'):
    os.remove('w.csv')
if os.path.exists('res1.csv'):
    os.remove('res1.csv')
html = urllib.request.Request(url, headers=hdr)
responce = urlopen(html)
soup = bs(responce.read(), features="lxml")
with open("output_test.html", "w", encoding="utf-8") as file:
    file.write(str(soup))
mydivs = soup.find(
    "table", {"class": "tv-data-table tv-screener-table tv-screener-table--fixed"}
)
tables_row = soup.find_all(
    "tr")
#print(soup.find_all('a').text)
tags = soup.find_all(class_='tv-screener__symbol')
# print(type(tags))
# print(len(tags))
a = 0
texts = [i.text for i in tags if i.text]
texts1 = [[texts] for texts in texts]
res = []
res1 = []
c = 0
row = []
#print(tables_row.text())
for tr in tables_row:
    td = tr.find_all("td")
    row = [tr.text for tr in td[:-3] if tr.text]
    if row:
        res.append(row)
       

row1 = [i.insert(0,texts(1)) for i in res if c==len(res)]
print(row1)
for i in res:
    n = texts[c]
    del i[0]
    i.insert(0,n)
    c+=1
    if c == len(res):
        break

df = pd.DataFrame(res)
print(df)
df.to_csv('w.csv')
df = pd.DataFrame(res1)
df.to_csv('res1.csv')

