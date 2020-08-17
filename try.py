from bs4 import BeautifulSoup as bs
import prettify
import pandas as pd
from urllib.request import urlopen
#import urllib.request
#import urllib.error as ur  # import HTTPError
import requests as rq

import time
hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://finviz.com/screener.ashx?v=111&r=1"
# html = urllib.request.Request(url, headers=hdr)
# responce = urlopen(html)
# soup = bs(responce.read(), features="lxml")

from progress.bar import IncrementalBar
mylist = [1,2,3,4,5,6,7,8]
bar = IncrementalBar('Countdown', max = len(mylist))
for item in mylist:
    bar.next()
    time.sleep(1)
bar.finish()