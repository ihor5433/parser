#Dependencies
import requests
import datetime as dt
import urllib.request as req
import time
import pyodbc
import csv
 
#Get today's datetime information
date = dt.datetime.now()
 
#API KEY from Alpha Vantage
api_key = ''
 
#value used to iterate through the syms list
i = 0
 
#list of stock symbols to track
syms = ['MSFT', 'SPY', 'AAPL', 'DIA', 'QQQ', 'GS', 'GE', 'IBM', 'JPM', 'XLF', 'AA', 'BABA', 'TWTR', 'XHB', 'INTC', 'C', 'CZR', 'MGM'
    'SQ','BAC', 'AMD', 'FB', 'VXX', 'TSLA', 'IWM', 'GLD', 'SVXY', 'EEM', 'FCX', 'WMT']
 
#variables to store year/month/day numbers to append to file name.
y = date.strftime("%Y")
m = date.strftime("%m")
d = date.strftime("%d")
 
#connects to SQL database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=your server here;'
                      'Database= your database here;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()
 
#for loop to iterate through the symbol list
for sym in syms:
     
#sleep for 15 seconds to avoid API call limit
    time.sleep(15)
    i+=1
 
#Create the URL for the API call
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + syms[i] + '&interval=1min&outputsize=full&apikey='+ api_key+'&datatype=csv'
 
#create the file path to save the csv
    save_path = 'your save path here'+ syms[i] + y + m + d + '.csv'
 
    print(url)
   
#read the page and store it   
    get_url = req.urlopen(url)
    data = get_url.read()
    get_url.close()
 
#write the data to a file    
    tnsfile = open(save_path,'wb')
    tnsfile.write(data)
     
#close python connection to the file
    tnsfile.close()
 
#create the table name 
    tableName = syms[i] + y + m + d   
 
#set the database you want to use, create the table
    cursor.execute('use YOUR DATABASE HERE; Create Table ' + tableName + '(symID int IDENTITY(1,1) NOT FOR REPLICATION NOT NULL, sym varchar(5), [timestamp] datetime ,[open] float,[high] float,[low] float,[close] float, [volume] float)')
 
#Open the csv file, build the query.   
    with open (save_path, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader) 
        query = "insert into " + tableName +" (sym, timestamp,[open],[high],[low],[close],[volume]) values (" +"'"+ syms[i]+"'"+ ",{1})"
        query = query.format(','.join(columns), ','.join('?' * len(columns)))
        cursor = conn.cursor()
        #print(query)
 
#write the query to the database
        for rows in reader:
            #print(rows)
            #print(query)
            cursor.execute(query, rows)
        cursor.commit()