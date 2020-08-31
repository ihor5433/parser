import csv, sqlite3
import pandas
from sqlalchemy import create_engine
from alphavantage import *
import json
import csv
from pandas import read_csv 
import csv_to_sqlite
con = sqlite3.connect("1.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
engine = create_engine('sqlite:///1.db')
#cur.execute("CREATE TABLE t") # use your column names here
#with open('1.csv',r) as f:
df = pandas.read_csv('data_file2.csv')
df.to_sql('stocks1', con=con, if_exists='append',index=True)
income = 'INCOME_STATEMENT'
b = 'BALANCE_SHEET'
c = 'CASH_FLOW'

#df = pandas.read_sql_table('stocks',engine)
#print(df)

def read_data_from_json():
    with open("data/fundamental/0.json") as js:
        data = json.load(js)
    stock = data['symbol']
    annualReports = data["annualReports"]
    quarterlyReports = data['quarterlyReports']
    data_file = open("data_file2.csv", "w")

    csv_writer = csv.writer(data_file)
    count = 0


    #csv_writer.writerow(stock)
    for rep in annualReports:
        if count == 0:
            header = rep.keys()
            #header[0] ='sdfd'
            #csv_writer.writerow('symbol')
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(rep.values())
    for rep in quarterlyReports:
        # if count == 0:
        #     header = 'quarterlyReports'
        #     csv_writer.writerow(header)
        #     count += 1
        
        csv_writer.writerow(rep.values())
    #con.execute('CREATE TABLE stock')

#read_data_from_json()


def open_csv_file(csv_file_path):
    """
    Open and read data from a csv file without headers (skipping the first row)
    :param csv_file_path: path of the csv file to process
    :return: a list with the csv content
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        data = list()
        for row in reader:
            data.append(row)

        return data
#print(open_csv_file('data_file2.csv'))
# data = read_csv('data_file1.csv')
# for i in data:
#     print(i)
with open('data_file2.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    #for row in reader:
        #print(row['fiscalDateEnding'])

def test(i,circle=False):
    data = []
    functions = ['INCOME_STATEMENT','BALANCE_SHEET','CASH_FLOW']
    if circle == True:
        for i in functions: 
            with open('data/fundamental/'+i+'.csv') as file:
                reader  = csv.reader(file,quoting =csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data +row
                    break
    with open('data/fundamental/'+i+'.csv') as file:
        reader  = csv.reader(file,quoting =csv.QUOTE_MINIMAL)
        for row in reader:
            data = data +row
            break
    return data
#g = test()
#g = list(dict.fromkeys(g))
# for row in g:
#     b = len(g)
    
#     cur.execute('alter table stocks_test1 add column  '+row)
#con.commit()
def sdf():
    a = 0   
    # with open('data_file1.csv','r') as csvfile:
    #     reader1 = csv.reader(csvfile,quoting =csv.QUOTE_MINIMAL)
    #     for row in reader1:
    #         b = len(row)
    #         if a ==0:
    #             for i in range(b):
    #                 cur.execute('alter table stocks_test add column  '+row[i])
    #             a+=1
    #         con.commit()
    #         break
    with open('data_file1.csv','r') as csvfile:
        reader1 = csv.reader(csvfile,quoting =csv.QUOTE_MINIMAL)
        for row in reader1:
            b = len(row)
            if a ==0:
                for i in range(2,b):
                    cur.execute('alter table stocks_test add column  '+row[i])
                a+=1
            con.commit()
            break



#print(g)
#print(list(dict.fromkeys(g)))
k=''
with open('data/fundamental/INCOME_STATEMENT.csv','r') as csvfile:
    reader1 = csv.reader(csvfile,quoting =csv.QUOTE_MINIMAL)
    o = 0
    
    for row in reader1:
        if o == 3:
            break
        k = row
        o+=1
t = ''
u=''
print(k)

h = ['2019-12-31', 'USD', '6731000000', '2237000000', '3863000000', '2868000000', '466000000', '341000000', '1547000000', 'None', '372000000', 'None', '750000000', '-165000000', '631000000', '-60000000', '94000000', '31000000', '15000000', '-79000000', '13000000', 'None', 'None', '31000000', '-180000000', 'None', '341000000', '341000000', 'None']
print(len(h))
h1 ='2019-12-31,USD,6731000000,2237000000,3863000000,2868000000,466000000,341000000,1547000000,None,372000000,None,750000000,-165000000,631000000,-60000000,94000000,31000000,15000000,-79000000,13000000,None,None,31000000,-180000000,None,341000000,341000000,None'
#print(len(list(h1)))
for i in k:
    t=t+i+","
t = t[:-1]
print(t)
#cur.executemany('insert into stocks_test1 values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',h)
#con.commit()
print(len(test(income)))
for i in test(income):
    u=u+i+","
u = u[:-1]
print(u)
sql = 'insert into stocks_test1 ('+u+') values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
print(sql)
#cur.executemany(sql,t)
cur.execute('insert into stocks_test1 ('+u+') values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',h)
con.commit()