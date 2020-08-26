import csv, sqlite3
import pandas
from sqlalchemy import create_engine
con = sqlite3.connect("1.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
engine = create_engine('sqlite:///1.db')
#cur.execute("CREATE TABLE t") # use your column names here
#with open('1.csv',r) as f:
df = pandas.read_csv('data_file.csv')
df.to_sql('stocks', con=engine, if_exists='replace',index=True)
df = pandas.read_sql_table('stocks',engine)
#print(df)