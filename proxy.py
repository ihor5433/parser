import requests
from lxml import html
from bs4 import BeautifulSoup as bs


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
class Proxy(object):
    proxy_url = 'https://hidemy.name/ru/proxy-list/?country=DERUUA&type=h#list'
    proxy_list = []

    def __init__(self):
        r = requests.get(self.proxy_url)
        str = html.fromstring(r.content)
        result = str.xpath('/html/body/div[1]/div[4]/div/div[4]/table/tbody/tr[1]/td[1]/text()')
        self.proxy_list = result
        print(result)
def proxy():
    proxy_url = 'https://hidemy.name/ru/proxy-list/?country=DERUUA&maxtime=300&type=h#list'
    proxy_url_all = 'https://hidemy.name/ru/proxy-list/?country=ALARAMAUATBHBDBYBJBWBRBGBIKHCACOCZDKDOECEGFRGEDEHNHKHUINIDIRIQITJPKZKEKRLALVMWMXMDMNNPNLNGPKPAPEPLRORURSSGSKSISOZAESSESYTWTZTHTRUAGBUSUYVEVNZW&maxtime=300&type=h#list'
    proxy_list = []
    r = requests.get(proxy_url_all,headers=hdr).text
    a = open('proxy.html','r',encoding="utf-8")
    soup = bs(r,features="lxml")
    divs = soup.find('div',{'class':'table_block'})
    tables_row = divs.find_all('tr')
    soup = bs(tables_row,features="lxml")
    print(soup)
    #tables_row1 = tables_row.find_all('td')
    count = 0

    for row in tables_row:

        #a = row.split()
        #print(a)

        print(row)
        # with open('prox.txt', 'a', newline='') as w:
        #     w.write(a[0]+'\n')
        count+=5

def handler(proxy):
    link = 'http://icanhazip.com/'
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        responce = requests.get(link,proxies=proxies,timeout=2).text
        print(f'IP: {responce.strip()}')
    except:
        print('Прокси не валидный')


#handler('176.9.119.170:8080')#
proxy()