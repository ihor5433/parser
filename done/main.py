import Screener_parser
import Earning_TradingView
import Write_to_sql
import Alphavantage as av
import test
import os
import time
from datetime import datetime
path_api = av.path_api
api = open(path_api)
#ticker = open(os.path.join(Write_to_sql.path_csv, 'ticker1.csv'), 'r')

Write_to_sql.DownloadData('AMD','1BAA30IPROBZOYMM')
exit()
print('1) Finviz screener\n2) TradingView earning\n3) Finviz and TradingView\n4) Write data to SQL' )
if __name__ =="__main__":
    a = int(input())
    if a == 1:
        print('1 - Вывести весь список\n2 - Только которые ниже 10$ ')

        b = int(input())
        if b == 1:
            Screener_parser.finviz_all_stocks()
        elif b == 2:
            Screener_parser.finviz_all_stocks(all_ticker=False)
        else:
            print("Неправильное значение!")
    elif a == 2: 
        Earning_TradingView.tradingview_earning()
    elif a ==3:
        Earning_TradingView.tradingview_earning()
        Screener_parser.finviz_all_stocks()
    elif a ==4:
        print('1) Выкачать только данные?\n2) Вставить данные в таблицу')
        #b = input()
        count = 1
        f = av.read_ticker()
        api = av.read_api_key()
        for i in range(0,100,10):
            now_time = datetime.now()
            Write_to_sql.DownloadData(f[i],api[0])
            print("1 прошел")
            Write_to_sql.DownloadData(f[i+1],api[1])
            print("2 прошел")
            Write_to_sql.DownloadData(f[i+2],api[2])
            print("3 прошел")
            Write_to_sql.DownloadData(f[i+3],api[3])
            print("4 прошел")
            Write_to_sql.DownloadData(f[i+4],api[4])
            print("5 прошел")
            Write_to_sql.DownloadData(f[i+5],api[5])
            print("6 прошел")
            Write_to_sql.DownloadData(f[i+6],api[6])
            print("7 прошел")
            Write_to_sql.DownloadData(f[i+7],api[7])
            print("8 прошел")
            Write_to_sql.DownloadData(f[i+8],api[8])
            print("9 прошел")
            Write_to_sql.DownloadData(f[i+9],api[9])
            print("10 прошел")
            print(datetime.now()- now_time)
            print('Спим')
            time.sleep(10)
            break

        #av.get_data_alphavantage()
        #Write_to_sql.run_script()

    #av.get_data_alphavantage('AMD',)



