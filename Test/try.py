import os

from requests import get as rget

path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental', 'temp'))

def aaa():
    url = "https://www.alphavantage.co/query?"
    api_key = "UQGWFV8GJ5UKWK2T"
    params = {"function": 'INCOME_STATEMENT', "symbol": 'AIQ', "apikey": api_key}
    r = rget(url, params=params)
    """Записываем ответ в json"""
    a = {"Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."}

    if r.json() == a:
        print('Превышенно к-ство запросов')
        return
    r = r.json()

    print(len(r))
    print(r)
    print(len(r['annualReports']))
aaa()
# import pandas_datareader.data as web
# import pandas as pd
# import numpy as np
# import datetime
#
# start = datetime.datetime(2006,1,1)
# end = datetime.datetime(2016,1,1)
# BAC = web.DataReader('BAC', 'av-daily', start, end,api_key='UQGWFV8GJ5UKWK2T')
#
# print(BAC)