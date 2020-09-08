# from Html import *
import csv
import json
import os, shutil

from requests import get as rget

i = "INCOME_STATEMENT"
b = "BALANCE_SHEET"
c = "CASH_FLOW"

path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental', 'temp'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))
path_api = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Files_txt', 'api_key.txt'))
path_result = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
file = ''
def get_data_alphavantage(symbol, function,api_key,only_var =False):
    """
    Получаем json из alphavantage по критериям
    
    """
    global file
    if only_var:
        file = os.path.join(path_json, symbol + '_' + function) + ".json"
        return
    file = os.path.join(path_json, symbol + '_' + function) + ".json"
    url = "https://www.alphavantage.co/query?"
    api_key = "UQGWFV8GJ5UKWK2T"
    params = {"function": function, "symbol": symbol, "apikey": api_key}
    r = rget(url, params=params).json()
    """Записываем ответ в json"""

    with open(file, "w") as f:
        json.dump(r, f)


def read_data_from_json(symbol,function):
    with open(file) as js:
        data = json.load(js)
    path = os.path.join(path_result,symbol)
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)
    annualReports = data["annualReports"]
    quarterlyReports = data["quarterlyReports"]
    data_file = open(os.path.join(path, function) + ".csv", "w")
    data_file_annual_report = open(os.path.join(path, function) + "_annual_report.csv", "w")
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

def delete_temp_files(file):
    if os.path.exists(file):
        os.remove(file)
def read_ticker():
    f = open(os.path.join(path_csv,'ticker.txt')).read()
    f = f.split()
    return f
def read_api_key(path_api=path_api):
    f = open(path_api,'r').read()
    f = f.split()
    return f
#read_api_key(path_api)
#get_data_alphavantage('AMD',i,read_api_key()[0],only_var=True)
#os.remove(file)
#read_data_from_json('AMD',i)
#read_data_from_json('INCOME_STATEMENT')
if __name__ =="__main__":
    print(read_ticker())
