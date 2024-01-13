""""
require stock news data
"""
import requests
import json
def get_news_data(symbol,api_key):
    #URL for Using news API
    url = "https://www.alphavantage.co/query"
    params={
        #requests data daily
        "function":"NEWS_SENTIMENT",
        #choosing company
        "tickers":symbol,
        #time stating
        "time_from":"20190401T0000",
        #
        "time_to":"20230331T0000",
        ##user API key
        "apikey":api_key
        }
    response = requests.get(url,params)
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        if data:
            # save the response content to a file
            with open("Task1/Microsoft Original news.json", "w") as f:
                json.dump(data, f)

            # read the response content from the file
            with open("Task1/Microsoft Original news.json", "r") as f:
                stock_data_loaded = json.load(f)
                assert data == stock_data_loaded
                print(stock_data_loaded)    
    else:
        print("cannot requests from API, status code:", response.status_code)
        
    
    return response
