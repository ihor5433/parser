from requests import get as rget
from bs4 import BeautifulSoup as bs
from colorama import Fore, Style, init
from googletrans import Translator
init()
translator = Translator()

def get_html(stock):
    global request_finviz, request_market_watch, request_finance
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    request_finviz = rget(f'https://finviz.com/quote.ashx?t={stock}', headers=headers).text
    request_market_watch = rget(
        f'https://www.marketwatch.com/investing/stock/{stock}/financials/balance-sheet/quarter').text
    request_finance = rget(f'https://finance.yahoo.com/quote/{stock}/key-statistics?p={stock}').text
    return request_finviz, request_market_watch, request_finance


def market_cap_and_exchange_from_finviz(html):
    soup = bs(html, features='lxml')
    try:
        exchange = soup.find('span', {'class': 'body-table'}).get_text()
    except AttributeError:
        print("Неверный тикер ")
        print('\n')
        return 'Continue', 'Continue'
    market_cap_finviz = soup.find_all('tr', {'class': 'table-dark-row'})
    for i in market_cap_finviz:
        count = 0
        td = i.find_all('td')
        for c in td:
            if c.get_text() == 'Market Cap':
                count += 1
                continue
            if count == 1:
                mark_cap = c.get_text()
                count = 0
    return mark_cap, exchange


while True:
    stock = input('\nНазвание акции:     ')
    print('\n')
    request_finviz, request_market_watch, request_finance = get_html(stock)
    market_cap_finviz, exchange_finviz = market_cap_and_exchange_from_finviz(request_finviz)
    if market_cap_finviz == 'Continue':
        continue
    print(f'Symbol\t\t\t\t\t\t{stock.upper()}', end='\t\t')
    if exchange_finviz == '[NASD]':
        print(Fore.GREEN + exchange_finviz[1:-1], Style.RESET_ALL)
    else:
        print(Fore.YELLOW + exchange_finviz[1:-1], Style.RESET_ALL)
    soup = bs(request_finance, features='lxml')
    table = soup.find_all('tr')


    def change_string_to_int(string):
        new_string = ''
        if string[0] == '(':
            string = string[1:-1]

        if string[-1] == 'M':
            new_string = float(string[:-1])
            new_string *= 1000000
        elif string[-1] == 'B':
            new_string = float(string[:-1])
            new_string *= 1000000000
        elif string[-1] == 'T':
            new_string = float(string[:-1])
            new_string *= 1000000000000
        elif string == 'N/A':
            new_string = 'N/A'
        return new_string


    temp_iter_for_sharesShort = 0
    for i in table:

        count = 0
        a = i.find_all('td')

        for td in a:
            c = td.get_text()
            if c == 'Float ':
                print(Fore.GREEN + c, Style.RESET_ALL, end='\t')
                count += 1
                continue
            elif c == 'Total Cash (mrq)':
                print(c, end='\t')
                count += 2
                continue
            elif c == 'Market Cap (intraday) 5':
                print(c, end='\t')
                count += 3
                continue
            elif c == 'Revenue (ttm)':
                print(c, end='\t')
                count += 4
                continue
            elif 'Shares Short' in c and temp_iter_for_sharesShort == 0:
                print(c[:12], end='\t')
                temp_iter_for_sharesShort += 1
                count += 5
                continue

            elif 'Short % of Float' in c:
                print(c[:16], end='\t')
                count += 6
                continue

            if count == 1:  # float
                if float(c[:-1]) < 5:
                    print(Fore.GREEN + '\t\t\t\t    >>  ' + c, Style.RESET_ALL)
                elif 5 < float(c[:-1]) <= 10:
                    print(Fore.YELLOW + '\t\t\t\t    >>  ' + c, Style.RESET_ALL)
                else:
                    print(Fore.RED + '\t\t\t\t    >>  ' + c, Style.RESET_ALL)

            elif count == 2:  # Total Cash (mrq)
                print(Fore.RED + '\t\t\t' + c, Style.RESET_ALL)
                total_cash = change_string_to_int(c)
            elif count == 3:  # Market Cap (intraday) 5
                count += 10
                print(Fore.RED + '\t\t\t' + c, Style.RESET_ALL, end='\t\t')
                print(market_cap_finviz)
                market_cap = change_string_to_int(c)
            elif count == 4:  # Revenue (ttm)
                print(Fore.RED + '\t\t\t\t' + c, Style.RESET_ALL)
                revenue = change_string_to_int(c)
            elif count == 5:  # Shares Short
                print(Fore.RED + '\t\t\t\t' + c, Style.RESET_ALL)
            elif count == 6:  # Short % of Float
                if c != 'N/A':
                    if float(c[:-1]) < 5:
                        print(Fore.GREEN + '\t\t\t' + c, Style.RESET_ALL)
                    elif 5 < float(c[:-1]) <= 10:
                        print(Fore.YELLOW + '\t\t\t' + c, Style.RESET_ALL)
                    elif 10 < float(c[:-1]):
                        print(Fore.RED + '\t\t\t' + c, Style.RESET_ALL)
                else:
                    print(Fore.WHITE + '\t\t\t' + c, Style.RESET_ALL)

    soup = bs(request_market_watch, features='lxml')
    table = soup.find_all('tr')
    for i in table:

        count = 0
        a = i.find_all('td')
        for td in a:
            c = td.get_text()
            if count == 0:
                name = c
            if name == 'Retained Earnings' and count < 6:
                if count == 0:
                    print(c, end='\t')
                    count += 1
                else:
                    count += 1
            if count == 6:
                if c[0] == '(':
                    print(Fore.RED + '\t\t\t' + c, Style.RESET_ALL)
                    retained_earnings = change_string_to_int(c)
                    break
                else:
                    print(Fore.GREEN + '\t\t\t' + c, Style.RESET_ALL)
                    retained_earnings = change_string_to_int(c)
                    break

    print('Cash to cap', end='\t\t\t\t\t')
    if total_cash != 'N/A':
        if market_cap > total_cash:
            print(Fore.RED + str(round(abs((total_cash / market_cap) * 100), 2)) + ' %', Style.RESET_ALL)
        else:
            print(Fore.GREEN + str(round(abs((market_cap / total_cash) * 100), 2)) + ' %', Style.RESET_ALL)
    else:
        print('N/A')
    print('Def to cap', end='\t\t\t\t\t')
    if retained_earnings != 'N/A':
        if market_cap > retained_earnings:
            a = (round(abs((retained_earnings / market_cap) * 100), 2))
            if a < 30:
                print(Fore.GREEN + str(a) + ' %', Style.RESET_ALL)
            elif 30 < a < 100:
                print(Fore.YELLOW + str(a) + ' %', Style.RESET_ALL)
        else:
            print(Fore.RED + str(round(abs((retained_earnings / market_cap) * 100), 2)) + ' %', Style.RESET_ALL)
        print('\n')
    else:
        print('N/A')
    soup = bs(request_finviz, features='lxml')
    news = soup.find_all('table', {'class': 'fullview-news-outer'})
    for i in news:
        one_news = i.find_all('a', {'class': 'tab-link-news'})
        date_news = i.find_all('td', {'width': '130'})
    for c in one_news:
        count += 1
        if count == 1:
            news1 = c.get_text()
            #print(c.get_text())
            result = translator.translate(str(c.get_text()),src='en',dest='ru').text
            #print(result.text)
        elif count == 2:
            news2 = c.get_text()
            result2 = translator.translate(str(c.get_text()), src='en', dest='ru').text
    count = 0
    for c in date_news:
        count += 1
        if count == 1:
            print(Fore.GREEN + c.get_text(), '\t',result, Style.RESET_ALL, '\n\t\t\t',news1)
        elif count == 2:
            print(Fore.GREEN + c.get_text(), '\t',result2, Style.RESET_ALL, '\n\t\t\t',news2)

