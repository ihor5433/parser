import csv
import os
import sqlite3
import time
from datetime import datetime

from tqdm import trange

import Alphavantage as av

path_annual_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/annual.db'))
path_quarterly_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/quarterly.db'))
path_stocks = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Files_txt', 'stocks.txt'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))

symbol = open(path_stocks, 'r').read()
symbol = symbol.split()

functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]
name_csv_file = ["INCOME_STATEMENT.csv", "BALANCE_SHEET.csv", "CASH_FLOW.csv"]

name_csv_fileAnnual = [
    "INCOME_STATEMENT_annual_report.csv",
    "BALANCE_SHEET_annual_report.csv",
    "CASH_FLOW_annual_report.csv",
]


def create_table_and_header(name_table):
    count = 0
    global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for i in [path_quarterly_db, path_annual_db]:
        con = sqlite3.connect(i)
        cur = con.cursor()
        data = []
        listColumn = ""
        if count == 1:
            f = f2
        for i in f:
            with open(os.path.join(path_csv, i)) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data + row
                    break
        data = list(dict.fromkeys(data))

        for i in data[1:]:  # add if
            listColumn = listColumn + i + ","
        listColumn = listColumn[:-1]

        cur.execute(
            "create table if not exists {} (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,{})".format(
                name_table, listColumn))

        count += 1
        con.commit()
    # return listColumn


def insert_into_table_value(quarterlyTable, annualTable, name):
    count = 0
    global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for i in [quarterlyTable, annualTable]:
        con = sqlite3.connect(i)
        cur = con.cursor()
        if count == 1:
            f = f2
        for func in f:
            with open(os.path.join(path_csv, func)) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                a = 0
                for row in reader:
                    if a == 0:
                        column_set = row
                        a += 1
                        continue
                    if len(row) == 0:
                        continue
                    cur.execute("INSERT INTO {} (fiscalDateEnding) VALUES('{}')".format(name, row[0]))
                    for ii in range(len(row)):
                        if ii != 1:
                            cur.execute(
                                "update {} set {}='{}' where fiscalDateEnding= '{}'".format(name, column_set[ii],
                                                                                            row[ii], row[0]))
        con.commit()
        count += 1


def DownloadData(symbol, api):
    start_time1 = datetime.now()
    av.delete_folder(symbol)
    for param in functions:
        av.get_data_alphavantage(symbol, param, api)
        av.read_data_from_json(symbol, param)
    # av.delete_temp_files(symbol,param)
    create_table_and_header(symbol)
    insert_into_table_value(path_quarterly_db, path_annual_db, symbol)
    # print("Прошел " + str(h) + " цыкл")
    print(datetime.now() - start_time1)


if __name__ == '__main__':
    # create_table_and_header('AMD')
    # insert_into_table_value(path_quarterly_db, path_annual_db, 'AMD')
    if os.path.exists(path_annual_db):
        os.remove(path_annual_db)
    if os.path.exists(path_quarterly_db):
        os.remove(path_quarterly_db)
    DownloadData('AMD', 'JOHTN3ROUBPZM8ED')
# todo сделать 5-10 api и начать выкачивать данные в json. потом я автоматом переведу в sql.
