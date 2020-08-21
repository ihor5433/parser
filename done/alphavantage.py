from main_functions import *
import json
url = "https://www.alphavantage.co/query?"
function = "INCOME_STATEMENT"
symbol = "CYH"
api_key = "UQGWFV8GJ5UKWK2T"
params = {"function": function, "symbol": symbol, "apikey": api_key}

r = rget(url, params=params).json()

with open("done/data.json", "w") as f:
    json.dump(r, f)

df = pd.DataFrame.from_dict(r, orient="index")

print(df)
