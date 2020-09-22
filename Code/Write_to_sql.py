import csv
import os
import sqlite3

import General_functions as gf
from datetime import datetime
path_annual_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/annual.db'))
path_quarterly_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/quarterly.db'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))


name_csv_file = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]

name_csv_fileAnnual = [
    "INCOME_STATEMENT_annual_report",
    "BALANCE_SHEET_annual_report",
    "CASH_FLOW_annual_report",
]

def sqlite_connection(name_db: str,close_connection=False,return_connection=False):
    '''Подключится к базе данных

        Параметры:
            - con_name: Имя базы данных
            - close_connection: Вернуть connection.close()

        Результат:
            Возвращает cursor для манипуляции с базой
    '''
    connection = sqlite3.connect(name_db)
    if return_connection == True:
        return connection
    cursor = connection.cursor()
    if close_connection == True:
        return connection.close()
    return cursor

def create_sql(name_db,name_table,column):
    '''Создать базу данных'''
    sqlite_connection(name_db).execute(f"create table if not exists {name_table} (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,{column})")


def insert_sql(name_db: str,name_table: str,column_name: str,values):
    '''Вставить данные в таблицу'''
    sqlite_connection(name_db).execute(f"INSERT INTO {name_table} ({column_name}) VALUES('{values}')")

def update_sql(con_name: str,name_table, column_name,value,column_search,value_search):
    '''Обновить данные в конкретной строку'''

    #connection = sqlite_connection(con_name, close_connection=True)
    #cursor = sqlite_connection(con_name)
    sqlite_connection(con_name).execute(f"update {name_table} set {column_name}='{value}' where fiscalDateEnding= '{value_search}'")

def create_table_and_header(symbol):
    count = 0
    #path_result = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', symbol))
    # global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for con in [gf.path('quarterly_db'), gf.path('annual_db')]:
        con = sqlite3.connect(con)
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
        #create_sql(symbol,con,list_column)
        #connection = sqlite_connection(con)
        cur.execute(
           f"create table if not exists {symbol} (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,{list_column})")

        count += 1
        #sqlite_connection(con,return_connection=True).commit()
        con.commit()
    # return list_column


def insert_into_table_value(quarterlyTable, annualTable, symbol):
    count = 0
    global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for con in [quarterlyTable, annualTable]:
        con = sqlite3.connect(con)
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
                    #insert_sql(con,symbol,'fiscalDateEnding',row[0])
                    cur.execute(f"INSERT INTO {symbol} (fiscalDateEnding) VALUES('{row[0]}')")
                    for ii in range(len(row)):

                        if ii != 1:
                            #update_sql(con,symbol,column_set[ii],row[ii],'fiscalDateEnding',row[0])
                            cur.execute(
                                "update {} set {}='{}' where fiscalDateEnding= '{}'".format(symbol, column_set[ii],
                                                                                            row[ii], row[0]))
        #sqlite_connection(con,return_connection=True).commit()
        con.commit()
        count += 1

if __name__ == '__main__':
    #create_table_and_header('ZYNE')
    time_now = datetime.now()
    create_sql('test','test','column1')
    print(datetime.now() - time_now)
    time_now = datetime.now()
    insert_sql('test','test','column1','34234')
    print(datetime.now()- time_now)

    pass

