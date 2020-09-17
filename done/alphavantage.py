# from Html import *
import csv
import json
import os
import shutil
from urllib3.exceptions import ConnectionError
import requests

import General_functions as gf

i = "INCOME_STATEMENT"
b = "BALANCE_SHEET"
c = "CASH_FLOW"





def get_data_alphavantage_and_check_requests(symbol, function, api_key=1,other = False):
    '''Возвращает ошибки которые могут быть при запросе
    Если их нет, возвращает результат

    Параметры:
        - url: адрес
        - params: параметры для api

    Результат:
        - 1: 'ConnectionError'
        - 2: 'Превишен лимит минутный или дневной'
        - 3: 'Empty': если полученный запрос не содержит данных
        - requests: ответ в виде данных в json
    '''
    url = "https://www.alphavantage.co/query?"
    # api_key = "UQGWFV8GJ5UKWK2T"
    session = requests.session()
    session.proxies = {"http":"176.9.119.170:3128",
               "https":"176.9.119.170:3128"}
    proxies = {"http": "128.199.202.122:8080",} # "https": "128.199.202.122:8080"
    params = {"function": function, "symbol": symbol, "apikey": api_key}
    bad_responce = {
        "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."}
    bad_responce_2={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for INCOME_STATEMENT.'}
    try:
        #req = requests.get(url, params=params,proxies=proxies)
        req = requests.get(url, params=params)
        #req =session.get(url, params=params)
    except requests.ConnectionError:
        print('ConnectionError')
        file = open(gf.path('missed'), 'a')
        file.write(symbol + '\n')
        return 'ConnectionError'
    req = req.json()
    if req == bad_responce:
        print('Превишен лимит минутный или дневной')
        return 'error'
    elif req == bad_responce_2:
        print('Нету акции в базе')
        return 'NotData'
    if other == False:
        if len(req) == 0 or len(req['annualReports']) == 0:
            file = open(gf.path('missed'),'a')
            file.write(symbol+'\n')
            print('Тикер не имеет данных: {}'.format(symbol))
            return 'EmptyData'
    return req


def write_to_json(requests,symbol,function):
    """Записывает данные в json

    Параметры:
        - requests: запрос который был получен с api
        - symbol: название акции(для обозначания файла)
        - function: название функции(для обозначания файла)

    Результат:
        Файл в формате symbol_functions.json
    """
    path_json = os.path.join(gf.path('json'),symbol+'_'+function) +'.json'
    with open(path_json, "w") as file:
        json.dump(requests, file)


def convert_json_to_csv(symbol, function: list):
    '''Записать данные с json в csv

    Результат:
        6 файлов разбитые по категориям с квартальными и годовыми отчетами
    '''
    folder = os.path.join(gf.path('result'), symbol)
    if not os.path.exists(folder):
        os.mkdir(folder)
    for func in function:
        with open(os.path.join(gf.path('json'), symbol + '_' + func + ".json")) as file:
            data = json.load(file)
        result = os.path.join(gf.path('result'), symbol, func)
        annualReports = data["annualReports"]
        quarterlyReports = data["quarterlyReports"]
        data_file = open(result + ".csv", "w")
        data_file_annual_report = open(result + "_annual_report.csv", "w")
        csv_writer = csv.writer(data_file)
        csv_writer_anu_rep = csv.writer(data_file_annual_report)
        count = 0

        for rep in annualReports:
            if count == 0:
                header = rep.keys()
                csv_writer_anu_rep.writerow(header)
                count += 1
            csv_writer_anu_rep.writerow(rep.values())
        for rep in quarterlyReports:
            if count == 1:
                header = rep.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(rep.values())


def delete_temp_files(symbol, function):
    '''Удалить файлы json'''
    for i in function:
        file = os.path.join(gf.path('json'),symbol+'_'+i + '.json')
        if os.path.exists(file):
            os.remove(file)


def read_ticker():
    f = open(gf.path('ticker')).read()
    n = f.replace(',', ' ')
    f = n.split()
    return f


def read_api_key():
    f = open(gf.path('api'), 'r').read()
    f = f.split()
    return f


def delete_folder(symbol):
    path_result = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    path = os.path.join(path_result, symbol)
    if os.path.exists(path):
        shutil.rmtree(path)




name_csv_file = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]

if __name__ == "__main__":
    a = read_ticker()
    # print(a[:100])
    # read_data_from_json('A', 'INCOME_STATEMENT')
    # print(requests_check("https://www.alphavantage.co/query?"))
    #for i in name_csv_file:

        #write_to_json(b,'ZYNE',i)

    #print(get_data_alphavantage_and_check_requests('ZYNE', 'OVERVIEW',other=True))
    #file = gf.path('json')+'ZYME.json'

    # with open(os.path.join(gf.path('json'),'ZYNE.json')) as js:
    #     data = json.load(js)
    # print(data)