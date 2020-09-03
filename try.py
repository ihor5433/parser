import sqlite3
import csv

#con_annual = sqlite3.connect("annual.db")
con = sqlite3.connect("1.db")  # change to 'sqlite:///your_filename.db'
cur = con.cursor()

functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]

a = 0
n=1
v = 1
with open("data/fundamental/CASH_FLOW.csv",'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        a += 1
        if a == 1:
            column_set = row
        if a % 2 == 1 and a != 1:
            cur.execute("INSERT INTO stocks_test1 (fiscalDateEnding) VALUES(\'"+row[0]+"\')") #создаю первую коло
            con.commit()
            for i in range(len(row)):
                if i != 0:
                    cur.execute('update stocks_test1 set '+column_set[i]+'=\''+row[i]+'\' where fiscalDateEnding= \"'+row[0]+'\"')
            con.commit()
    
    # a = 0
    # n = 1
    # v=1
    # print(5345)
    # for data in column_set:
    #     print(len(data))
    #     if a <3:
    #         continue
            
            
    #         #     for value in data:
    #                 #print(value)
    #         # if n==len(data):
    #     for i in range(len(data)):
    #         print('update stocks_test1 set '+column_set[n]+'='+data[v]+' where fiscalDateEnding= \"'+data[0]+'\"')
    #         #cur.execute('update stocks_test1 set '+column_set[n]+'='+data[v]+' where fiscalDateEnding= \"'+data[0]+'\"')
    
    #         if n==len(data):
    #             break
    #         n+=1
    #         v+=1
#cur.execute("update stocks_test1 set reportedCurrency='USD' where fiscalDateEnding='2018-12-31'")
#con.commit()