""""
require stock news data
"""
import requests

def get_news_data(symbol,api_key):
    #URL for Using news API
    url = "https://www.alphavantage.co/query"
    params={
        #requests data daily
        "function":"NEWS_SENTIMENT",
        #choosing company
        "tickers":symbol,
        #limit the number of news
        "limit":"1000",
        #time stating
        "time_from":"20190401T0000",
        #time ending
        "time_to":"20230331T0000",
        ##user API key
        "apikey":api_key
        }
    response = requests.get(url,params)
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
    else:
        print("cannot requests from API, status code:", response.status_code)
    return data
