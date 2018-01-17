import os
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import random
import pickle


tickers = []
random.seed(0)
for i in pd.read_csv("tickers.csv").values:
    if '.' not in i[0] and '-' not in i[0]:
        tickers += i.tolist()
print len(tickers)



# Define which online source one should use
data_source = 'yahoo'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

count = 0

stocks = {}

for ticker in tickers:
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    try:
        stocks[ticker] = data.DataReader(ticker, data_source, start_date, end_date)
        count += 1
        print count
    except:
        print "no data available for", ticker
        continue

output = open('data.pkl', 'wb')
pickle.dump(stocks, output)
output.close()