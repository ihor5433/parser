import sqlite3
import requests
import pandas as pd

from General_functions import path

con = sqlite3.connect(path('quarterly_db'))
#engine = create_engine('sqlite:///C:/Users/idmytrenko/Documents/Prog/Python/db/annual.db')
cur = con.cursor()
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM ABIO")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#df = pd.read_sql_query('SELECT id_date, totalRevenue FROM AAL',con)
# lst = []
# for i in range(0,5):
#     a = cur.execute('SELECT id_date, fiscalDateEnding FROM AAL where id_date = {}'.format(i))
#
#     data = cur.fetchall()
#     lst += data
# c = pd.DataFrame(lst)
# print(c)
# a = cur.execute('SELECT id_date, totalRevenue FROM AAL where id_date = 1')
# data1 = cur.fetchall()
#
# con.close()
#rint(data)
#df = pd.read_sql_table('AA',engine)

# x = [1,1,2,3,3,5,7,8,9,10,
#      10,11,11,13,13,15,16,17,18,18,
#      18,19,20,21,21,23,24,24,25,25,
#      25,25,26,26,26,27,27,27,27,27,
#      29,30,30,31,33,34,34,34,35,36,
#      36,37,37,38,38,39,40,41,41,42,
#      43,44,45,45,46,47,48,48,49,50,
#      51,52,53,54,55,55,56,57,58,60,
#      61,63,64,65,66,68,70,71,72,74,
#      75,77,81,83,84,87,89,90,90,91
#      ]
#
# plt.style.use('ggplot')
# plt.hist(x, bins=10)
# plt.show()
try:
    a = requests.get('https://fidfnviz.com/')
except requests.ConnectionError:
    print('errer')