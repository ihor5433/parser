# from urllib.request import urlopen
# import urllib.request
# import bs4
# hdr = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# url = ('https://finviz.com/screener.ashx?v=211')
# html = urllib.request.Request(url,headers=hdr)
# responce = urlopen(html)
# print(responce.read())
url = ('https://finviz.com/screener.ashx?v=111')
a = 21
for i in range(4):
    
    a += 20
    url1 = 'https://finviz.com/screener.ashx?v=111&r='
    url = url1 + str(a)
    print(url)