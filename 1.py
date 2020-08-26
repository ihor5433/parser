import sqlite3
import json
import pandas as pd
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute("INSERT INTO fundamental VALUES ('dfg','dfg')")
# conn.commit()
with open("data/fundamental/1.json", "r") as read:
    data = json.load(read)
print('netIncome' in data["annualReports"])
json_str = json.dumps(data)
resp = json.loads(str(json_str))
df = pd.read_json(data)
#print(resp["annualReports"]['totalRevenue'])
for i in data['annualReports']:
    for n in i:
        print(n, i[n])
#if 'totalRevenue' in data['']
print(data)
# print(data['annualReports'[0]])
for i in data['annualReports']:
    print(i)
print(sorted(data, key=lambda x: list(x.keys())))