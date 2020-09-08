# from Html import *
import csv
import json
import os

from requests import get as rget

i = "INCOME_STATEMENT"
b = "BALANCE_SHEET"
c = "CASH_FLOW"

path_json = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental', 'temp'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))


def get_data_alphavantage(symbol, function):
    """
    Получаем json из alphavantage по критериям
    
    """
    url = "https://www.alphavantage.co/query?"
    api_key = "UQGWFV8GJ5UKWK2T"
    params = {"function": function, "symbol": symbol, "apikey": api_key}
    r = rget(url, params=params).json()
    """Записываем ответ в json"""
    with open(os.path.join(path_json, function) + ".json", "w") as f:
        json.dump(r, f)


def read_data_from_json(function):
    with open(os.path.join(path_json, function) + ".json") as js:
        data = json.load(js)
    annualReports = data["annualReports"]
    quarterlyReports = data["quarterlyReports"]
    data_file = open(os.path.join(path_csv, function) + ".csv", "w")
    data_file_annual_report = open(os.path.join(path_csv, function) + "_annual_report.csv", "w")
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


read_data_from_json('INCOME_STATEMENT')
