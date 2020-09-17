import csv
import os
from Write_to_sql import path_csv
from datetime import datetime
from progress.bar import IncrementalBar
from Alphavantage import read_ticker
from alive_progress import alive_bar


def write_ticker_in_many_files():
    print('Разбиваю тикеры по файлам')
    count = 0
    b = 1
    f = read_ticker()
    with alive_bar(len(f)//100) as bar:
        for i in f:
            c = open(os.path.join(path_csv, 'ticker{}.csv'.format(b)), 'a', newline='')
            writer = csv.writer(c, delimiter=' ', quotechar='|')
            writer.writerow([i])
            if count != 0 and count % 100 == 0:
                b += 1
                bar()
            count += 1



def write_ticker_to_csv(name_csv='ticker.csv'):
    print('Записываю тикеры в файл csv из finviz_list')
    path_file = os.path.join(path_csv, name_csv)
    path = os.path.join(path_csv, 'finviz_list.csv')
    data = csv.reader(open(path), quoting=csv.QUOTE_MINIMAL)
    row_count = sum(1 for row in data)  # длина файла для прогрес бара
    data = csv.reader(open(path), quoting=csv.QUOTE_MINIMAL)
    if os.path.exists(path_file):
        os.remove(path_file)
    with alive_bar(row_count) as bar:
        for row in data:
            bar()
            name = []
            name.append(row[2])
            file1 = (open(os.path.join(path_csv, name_csv), 'a', newline=''))
            with file1:
                writer = csv.writer(file1)
                writer.writerow(name)



def add_ticker_to_txt():
    path = os.path.join(path_csv, 'finviz_list.csv')
    string = ''
    file = open(path)
    data = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
    for row in data:
        string += row[2] + ','
    string = string[:-1]
    f = open(os.path.join(path_csv, 'ticker.txt'), 'w')
    f.write(string)
    f.close()





# time_now = datetime.now()
# #write_ticker_to_csv()
# write_ticker_in_many_files()
# print(datetime.now() - time_now)
