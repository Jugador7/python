!pip install yfinance==0.2.4
#!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

#https://aroussi.com/post/python-yahoo-finance

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

apple_info['country']

apple_share_price_data = apple.history(period="max")

#A share is the single smallest part of a company's stock  that you can buy, the prices of these shares fluctuate over time. Using the <code>history()</code> method we can get the share price of the stock over a certain period of time. Using the `period` parameter we can set how far back from the present to get data. The options for `period` are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

apple_share_price_data.head()

#We can reset the index of the DataFrame with the reset_index function. 
#We also set the inplace paramter to True so the change takes place to the DataFrame itself.

apple_share_price_data.reset_index(inplace=True)

#We can plot the Open price against the Date:

apple_share_price_data.plot(x="Date", y="Open")

#Dividends
apple.dividends

apple.dividends.plot()


