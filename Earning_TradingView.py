from main_functions import *


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
url = "https://www.tradingview.com/markets/stocks-usa/earnings/"

soup = convert_html(url)

#r = rget(url, headers=hdr)

def tradingview_earning():
    if exists('w.csv'):
        remove('w.csv')
    if exists('res1.csv'):
        remove('res1.csv')
    if getTitle(url) != None:
        return getTitle(url)
    html = Request(url, headers=hdr)
    responce = urlopen(html)
    soup = bs(responce.read(), features="lxml")
    with open("output_test.html", "w", encoding="utf-8") as file:
        file.write(str(soup))
    mydivs = soup.find(
        "table", {"class": "tv-data-table tv-screener-table tv-screener-table--fixed"}
    )
    tables_row = soup.find_all(
        "tr")
    #print(soup.find_all('a').text)
    tags = soup.find_all(class_='tv-screener__symbol')
    # print(type(tags))
    # print(len(tags))
    a = 0
    texts = [i.text for i in tags if i.text]
    texts1 = [[texts] for texts in texts]
    res = []
    res1 = []
    c = 0
    row = []
    for tr in tables_row:
        td = tr.find_all("td")
        row = [tr.text for tr in td[:-3] if tr.text]
        if row:
            res.append(row)
        

    row1 = [i.insert(0,texts(1)) for i in res if c==len(res)]
    
    for i in res:
        n = texts[c]
        del i[0]
        i.insert(0,n)
        c+=1
        if c == len(res):
            break

    df = pd.DataFrame(res)
    print(df)
    df.to_csv('w.csv')
#tradingview_earning()


