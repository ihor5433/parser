from bs4 import BeautifulSoup
import prettify
import pandas as pd
with open('AdaptHealth Corp. (AHCO) Earnings.html', 'r') as file:
    soup = BeautifulSoup(file.read(), features="lxml")
    mydivs = soup.find("table", {"class": "earning_history"})
    tables_row = mydivs.find_all('tr')
res = []
res1 = []
for tr in tables_row:
    td = tr.find_all('td')
    row = [tr.text for tr in td if tr.text]
    if row:
        res.append(row)
for tr in tables_row:
    th = tr.find_all('th')
    row = []
    a = 0
    for tr in th:
        if a == 1 or a == 9 or a == 10:
            a += 1
            continue
        #if tr.text:
        row.append(tr.text)
        a += 1
    if row:
        res1.append(row)

df = pd.DataFrame(res, columns=res1)
df.to_excel('1.xlsx')
print(df)
