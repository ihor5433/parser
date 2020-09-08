import Screener_parser
import Earning_TradingView
import Write_to_sql
import Alphavantage as av
import test
import os
path_api = av.path_api
api = open(path_api)
ticker = open(os.path.join(Write_to_sql.path_csv, 'ticker1.csv'), 'r')

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
        b = input()
        for i in ticker:
            for i in api:
                av.get_data_alphavantage(i,)

        # av.get_data_alphavantage()
        # Write_to_sql.run_script()

    #av.get_data_alphavantage('AMD',)





