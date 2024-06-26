
#Graphing data Attempt
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf 
import matplotlib.pyplot as plt

end = dt.datetime.now()
start = end - dt.timedelta(days=10) #alternative:dt.datetime(2000,1,1) for jan 1 2000 to be the start
print(start, '\n' ,end)

#Selecting stocks

#Example for Aussie stocks
stockList = ['CBA','NAB','WBC','ANZ']
stocks = [i + '.AX' for i in stockList]

stocks=['TSLA','NFLX']

print(stocks)

yf.pdr_override()#don't know just use to deal with str and indices problem/ may be use a different library

# pulling stocks
df = pdr.get_data_yahoo(stocks, start, end)

#good ways to check the data in question
print(df.head())#first 5 lines
print(df.index)#leftmost column or the colum in common
print(df.columns)#the name of each column

#Isolating data or mnolding the original dataset for my purposes
close = df.Close #This pulls data from the Close column in the original data set
print(close)

#Gaining insights on the dataset using describe
print(close.describe(percentiles=[0.1,0.5,0.9]))#the percentile portion in the () of describe is not necessary but allows for percentile values
print(close[close.index>end-dt.timedelta(days=5)].describe(percentiles=[0.1,0.5,0.9]))#even more specific

#Matplotlib vs plotly
close.plot()






