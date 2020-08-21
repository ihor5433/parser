from bs4 import BeautifulSoup as bs
import prettify
import pandas as pd
from urllib.request import urlopen
#import urllib.request
#import urllib.error as ur  # import HTTPError
import requests as rq
from pprint import pprint
import time
import yfinance as yf
import json
import yahoo_finance

cyh = yf.Ticker('MSFT')

#fd = pd.DataFrame(cyh.info)
#print(json.dumps(cyh.info, indent=1,sort_keys=True))
pprint(cyh.quarterly_earnings)
print(cyh.earnings)