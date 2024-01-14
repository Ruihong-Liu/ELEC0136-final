"""
task1_1 request of the stock data
"""
##import the libaray of requests and json
import requests
import json
##creat the function that use to apply the data
def aqu_stock_data(symbol,api_key):
    ##endpoint API from alpha vantage
    url="https://www.alphavantage.co/query"
    params={
        ##requests data daily
        "function":"TIME_SERIES_DAILY",
        ##choosing company
        "symbol":symbol,
        ##size of the data
        "outputsize":"full",
        ##user API key
        "apikey":api_key
    }
    ##requests from URL
    response = requests.get(url,params)
    ##check if the data requried is successed
    if response.status_code == 200:
        data=response.json()
        with open("data/stock_data.json", "w") as file:
            json.dump(data, file)
        return data

