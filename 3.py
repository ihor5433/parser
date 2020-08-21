from requests import get as rget
import requests
from pandas import pandas as pd
import json
from bs4 import BeautifulSoup as bs
import seaborn


url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IMBI&apikey=UQGWFV8GJ5UKWK2T'
r = rget(url).json()
#soup = bs(r,features='lxml').get_text()
print(type(r))
#print(r)
# d = json.loads(r)
# c = json.dumps(r)
# print(type(c))

with open('data.json','w') as f:
    json.dump(r,f)
with open('data.json','r') as read:
    data = json.load(read)

df = pd.DataFrame.from_dict(r, orient='index')
#df.transpose()
#print(df)

a = pd.read_json(r'data.json',orient='index')
print(a)
      #data = seaborn.load_dataset(soup)
#print(data.head())
#print(df)

df.to_csv('1112.csv',index=None)
#a.to_json('1111.json')
# base_url = 'https://www.alphavantage.co/query?'
# params = {'function': 'INCOME_STATEMENT',
#   'symbol': 'IMBI', 
#   'apikey': 'UQGWFV8GJ5UKWK2T'}

# response = rget(base_url, params=params)
# response_dict = response.json()
# header = response.json()
# df = pd.DataFrame(response_dict)
# print(df)


params = {'function': 'i' , 
          'symbol':  'i' ,
         'apikey': 'i'

}