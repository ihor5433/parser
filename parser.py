from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests as r

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
#html = r.get('https://finviz.com/screener.ashx?v=211',headers = headers)
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read())
print(bs.td)
# print(html.text.encode("utf-8"))

try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)
