import os

import pandas as pd
import tqdm

from Code.General_functions import get_title, path, convert_html

hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://finviz.com/screener.ashx?v=111&r="
url_two = "https://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_price_u10&r="
url_without_exFund = 'https://finviz.com/screener.ashx?v=111&f=ind_stocksonly&r='


# soup = convert_html(url)




def last_page(url):
    """Ищет последнюю старницу для цикла"""
    soup = convert_html(url)
    print(int(soup("a", href=True)[-3].get_text()))
    return int(soup("a", href=True)[-3].get_text())


def finviz_all_stocks(url=url_without_exFund, output=False, output_in_file_html=False,all_ticker=True):
    """собирает все акции с финвиза"""

    #url = url
    global url_two
    # url = url_two
    if all_ticker == False:
        url = url_two
    if os.path.exists(os.path.join(path('csv'), 'finviz_list.csv')):
        os.remove(os.path.join(path('csv'), 'finviz_list.csv'))
    if get_title(url) != None:
        return get_title(url)
    page_code = 1
    url1 = url + str(page_code)
    for i in tqdm.trange(last_page(url) + 1):

        soup = convert_html(url1)
        if output_in_file_html:
            # проверка выводимого текста
            with open("output_test.html", "w", encoding="utf-8") as file:
                file.write(str(soup))
            return
        mydivs = soup.find("table", {"bgcolor": "#d3d3d3"})
        tables_row = mydivs.find_all("tr")
        res = []
        for tr in tables_row[1:]:
            td = tr.find_all("td")
            row = [tr.text for tr in td[:-3] if tr.text]
            if row:
                res.append(row)

        df = pd.DataFrame(res)

        df.to_csv(os.path.join(path('csv'), 'finviz_list.csv'), mode="a", header=False)

        if output:
            print(df)
        page_code += 20
        url1 = url + str(page_code)

