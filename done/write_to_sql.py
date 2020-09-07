import csv, sqlite3

#from . import Alphavantage as av
import time
import os
import Alphavantage as av
# import cython
from datetime import datetime
# con = sqlite3.connect("1.db")
# cur = con.cursor()
import tqdm


path_annual_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/annual.db'))
path_quarterly_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db/quarterly.db'))
path_stocks = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','stocks.txt'))
path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'fundamental'))
if os.path.exists(path_annual_db):
    os.remove(path_annual_db)
if os.path.exists(path_quarterly_db):
    os.remove(path_quarterly_db)




symbol = open(path_stocks, 'r').read()
symbol = symbol.split()

basedir = os.path.abspath(os.path.dirname('data/fundamental/'))


print(os.path.join('data','fundamental'))
functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]
name_csv_file = ["INCOME_STATEMENT.csv", "BALANCE_SHEET.csv", "CASH_FLOW.csv"]


name_csv_fileAnnual = [
    "INCOME_STATEMENT_annual_report.csv",
    "BALANCE_SHEET_annual_report.csv",
    "CASH_FLOW_annual_report.csv",
]


def create_table_and_header(
        name_table, create_table=True, circle=True
):
    count = 0
    global name_csv_file, name_csv_fileAnnual
    f = name_csv_file
    f2 = name_csv_fileAnnual
    for i in [path_quarterly_db, path_annual_db]:
        #print(path_db + i)
        con = sqlite3.connect(i)
        cur = con.cursor()
        data = []
        listColumn = ""
        if count == 1:
            f = f2
        for i in f:

            with open(os.path.join(path_csv,i)) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data + row
                    break
        data = list(dict.fromkeys(data))

        for i in data[1:]:  # add if
            listColumn = listColumn + i + ","
        listColumn = listColumn[:-1]

        cur.execute(
            "create table if not exists "
            + name_table
            + " (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,"
            + listColumn
            + ")"
        )

        count += 1
    con.commit()
    # con.close()
    return listColumn


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
            with open(os.path.join(path_csv,func)) as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                a = 0
                for row in reader:
                    a += 1
                    if a == 1:
                        column_set = row
                    if a != 1: #a % 2 == 1 and
                        cur.execute("INSERT INTO " + name + " (fiscalDateEnding) VALUES('" + row[0] + "')")

                        for c in range(len(row)):
                            if c != 1:
                                cur.execute("update " + name + " set " + column_set[c] + "='" + row[c] + "' where fiscalDateEnding= \"" + row[0] + '"')
                        con.commit()
        count += 1




h = 0
start_time1 = datetime.now()
for stock in symbol:
    if h == 3:
        break
    start_time = datetime.now()
    for param in functions:

        av.get_data_alphavantage(stock, param)
        av.read_data_from_json(param)
    print('Обработка запроса  ',datetime.now() - start_time)
    create_table_and_header(stock)
    insert_into_table_value(path_quarterly_db, path_annual_db, stock)
    print("Прошел " + str(h) + " цыкл")
    for t in tqdm.tgrange(60):
        #print("Осталось ждать " + str(t) + " секунд")
        time.sleep(1)
    h += 1
print(datetime.now() - start_time1)
create_table_and_header('aame')
insert_into_table_value(path_quarterly_db, path_annual_db, 'aame')


#todo сделать 5-10 api и начать выкачивать данные в json. потом я автоматом переведу в sql.