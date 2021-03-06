from os import remove
from os.path import exists, join
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup as bs

from Code.General_functions import get_title, convert_html, path

hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://www.tradingview.com/markets/stocks-usa/earnings/"


# r = rget(url, headers=hdr)


def tradingview_earning(output_if_file_html=False, output=False):
    """
    Выкачивает отчеты за сегодня с TradingView
    """
    # soup = convert_html(url)
    if exists(join(path('csv'), 'tview_earning.csv')):
        remove(join(path('csv'), 'tview_earning.csv'))
    if get_title(url) is not None:
        return get_title(url)
    html = Request(url, headers=hdr)
    responce = urlopen(html)
    soup = bs(responce.read(), features="lxml")
    if output_if_file_html:
        with open("output_test.html", "w", encoding="utf-8") as file:
            file.write(str(soup))

    tables_row = soup.find_all("tr")
    tags = soup.find_all(class_="tv-screener__symbol")
    texts = [i.text for i in tags if i.text]
    res = []
    c = 0
    row = []
    for tr in tables_row:
        td = tr.find_all("td")
        row = [tr.text for tr in td[:-3] if tr.text]
        if row:
            res.append(row)
    for i in res:
        n = texts[c]
        del i[0]
        i.insert(0, n)
        c += 1
        if c == len(res):
            break

    df = pd.DataFrame(res)
    if output:
        print(df)
    df.to_csv(join(path('csv'), 'tview_earning.csv'))
