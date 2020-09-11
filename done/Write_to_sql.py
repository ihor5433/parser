import csv
import os
import sqlite3

import General_functions as gf

path_annual_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/annual.db'))
path_quarterly_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/quarterly.db'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))


name_csv_file = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]

name_csv_fileAnnual = [
    "INCOME_STATEMENT_annual_report",
    "BALANCE_SHEET_annual_report",
    "CASH_FLOW_annual_report",
]


def create_table_and_header(symbol):
    count = 0
    #path_result = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', symbol))
    # global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for i in [gf.path('quarterly_db'), gf.path('annual_db')]:
        con = sqlite3.connect(i)
        cur = con.cursor()
        data = []
        list_column = ""
        if count == 1:
            f = f2
        for i in f:

            with open(os.path.join(gf.path('result'),symbol, i+'.csv')) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data + row
                    break
        data = list(dict.fromkeys(data))

        for i in data[1:]:
            list_column = list_column + i + ","
        list_column = list_column[:-1]

        cur.execute(
            f"create table if not exists {symbol} (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,{list_column})")

        count += 1
        con.commit()
    # return list_column


def insert_into_table_value(quarterlyTable, annualTable, symbol):
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
            with open(os.path.join(gf.path('result'),symbol, func+'.csv')) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                a = 0
                for row in reader:
                    if a == 0:
                        column_set = row
                        a += 1
                        continue
                    if len(row) == 0:
                        continue
                    cur.execute(f"INSERT INTO {symbol} (fiscalDateEnding) VALUES('{row[0]}')")
                    for ii in range(len(row)):
                        if ii != 1:
                            cur.execute(
                                "update {} set {}='{}' where fiscalDateEnding= '{}'".format(symbol, column_set[ii],
                                                                                            row[ii], row[0]))
        con.commit()
        count += 1





if __name__ == '__main__':
    create_table_and_header('ZYNE')
    pass

