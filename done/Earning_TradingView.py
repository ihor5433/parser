from General_functions import *


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://www.tradingview.com/markets/stocks-usa/earnings/"

soup = convert_html(url)

# r = rget(url, headers=hdr)


def tradingview_earning(output_if_file_html=False, output=False):
    if exists("data/tview_earning.csv"):
        remove("data/tview_earning.csv")
    if getTitle(url) != None:
        return getTitle(url)
    html = Request(url, headers=hdr)
    responce = urlopen(html)
    soup = bs(responce.read(), features="lxml")
    if output_if_file_html == True:
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
    if output == True:
        print(df)
    df.to_csv("data/tview_earning.csv")

