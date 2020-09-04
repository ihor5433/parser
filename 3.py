import sqlite3
import pandas as pd
con = sqlite3.connect('quarterly.db')

# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM ABIO")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
df = pd.read_sql_query('SELECT * FROM ABIO',con)
print(df)
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt