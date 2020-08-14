from urllib.request import urlopen
import urllib.error as ur  # import HTTPError
from bs4 import BeautifulSoup as bs


def getTitle(url):
    try:
        html = urlopen(url)
    except ur.HTTPError:  #если ошибка то выводим сообщение
        return 'Http Error or Access denite'
    except ur.URLError:
        return "Bad Link"
    try:
        bsObj = bs(html.read(), features='lxml')
        title = bsObj.body.h1
    except AttributeError: # если нету атрибута то выводим сообщение
        return 'Title could not be found'
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")

print(title.get_text())
