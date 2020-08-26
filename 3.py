import json
import csv
from pandas import read_csv 
with open("data/fundamental/0.json") as js:
    data = json.load(js)
stock = data['symbol']
annualReports = data["annualReports"]
quarterlyReports = data['quarterlyReports']
data_file = open("data_file.csv", "w")

csv_writer = csv.writer(data_file)
count = 0


for rep in annualReports:
    if count == 0:
        header = rep.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(rep.values())
for rep in quarterlyReports:
    # if count == 0:
    #     header = 'quarterlyReports'
    #     csv_writer.writerow(header)
    #     count += 1
    
    csv_writer.writerow(rep.values())
# csv_writer.writerow(['sdfsdf'])
# data_file.close()
   
# with open('1.csv', 'w') as f:
#     writer = csv.DictWriter(f,fieldnames= annualReports[0])
#     writer.writeheader()
    
# df = read_csv('data_file.csv')
# df['Ticker'] = stock
# df.to_csv('data_file.csv',index=False)


#     for d in annualReports:
#         writer.writerow(d)
#     for d in quarterlyReports:
#         writer.writerow(d)

# # with open('1.csv', newline='') as fd:
# #     r = csv.reader(fd)
# #     data1 = [line for line in r]
    
# # with open('1.csv', 'a', newline='') as fd:
# #     w = csv.writer(fd)
# #     w.writerow(['dsfsdf','fdgdfg'])
# #     w.writerow(data1)

# df = read_csv('1.csv')
# df['new_column'] = ''
# df.to_csv('1.csv',index=False)
