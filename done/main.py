import Screener_parser
import Earning_TradingView



print('1) Finviz screener\n2) TradingView earning\n3) All' )
if __name__ =="__main__":
    a = int(input())
    if a == 1:
        Screener_parser.finviz_all_stocks()
    elif a == 2: 
        Earning_TradingView.tradingview_earning()
    elif a ==3:
        Earning_TradingView.tradingview_earning()
        Screener_parser.finviz_all_stocks()
        