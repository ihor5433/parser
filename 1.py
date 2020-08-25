import yahoofinancials as yf
import requests as rq
from pprint import pprint
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from tabulate import tabulate

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
import csv

querystring = {"region": "US", "symbol": "GOOG"}

headers = {
    "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    "x-rapidapi-key": "41e8c2f57fmsh5f8f653c42e7215p101b0cjsn77a87c79d165",
}
hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
# response = requests.request("GET", url, headers=headers, params=querystring)


response = requests.request("GET", url, headers=headers, params=querystring)
print(type(response))
# print(response.json())
# response = response.json()

# soup  = bs(response, features = 'lxml' ).encode('utf-8')
# print(type(soup))
# with open('data.csv','wb') as f:
#    csv.writer(f).writerows((k,)+v for k, v in response.iter)
# df = pd.DataFrame.from_dict(a)
# print(df)
# df.to_csv('324.csv')
# print(tabulate(response, headers= 'keys'))
df = pd.DataFrame(response.json())
df.to_json("23.json")
# df.to_csv('21.csv')
# print(df)

