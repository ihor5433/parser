import csv
import os
from Write_to_sql import path_csv
path = os.path.join(path_csv,'finviz_list.csv')
file = open(path)
data = csv.reader(file,quoting=csv.QUOTE_MINIMAL)

#     #for i in row:
#
# f = open(os.path.join(path_csv, 'ticker.txt'), 'r').read()
# n = f.replace(',',' ')
# f= n.split()
# print(n)
# print(f)
def write_ticker_in_many_files():
    a= 0
    b = 1
    f = read_ticker()
    for i in f:
        c = open(os.path.join(path_csv, 'ticker{}.csv'.format(b)), 'a', newline='')
        writer = csv.writer(c,delimiter=' ',quotechar='|')
        writer.writerow([i])
        if a != 0 and a % 100 == 0 :
            b+=1
            c = open(os.path.join(path_csv, 'ticker{}.csv'.format(b)), 'w')
        a+=1

def write_ticker_to_csv():
    a = 0
    file1 = (open(os.path.join(path_csv, 'ticker.csv'), 'w', newline=''))
    for row in data:
        name = []
        name.append(row[2])
        file1 = (open(os.path.join(path_csv, 'ticker.csv'), 'a', newline=''))
        with file1:
            writer = csv.writer(file1)
            writer.writerow(name)
def add_ticker_to_txt():
    string = ''
    for row in data:
        string += row[2] + ','
    string = string[:-1]
    f = open(os.path.join(path_csv, 'ticker.txt'), 'w')
    f.write(string)
    f.close()

def read_ticker():
    f = open(os.path.join(path_csv,'ticker.txt')).read()
    n = f.replace(',', ' ')
    f = n.split()
    return f

