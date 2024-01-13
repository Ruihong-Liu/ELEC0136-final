import json
from task1_1 import aqu_stock_data
from task1_2 import get_news_data
#API keys
api_key="NN2SRNCT5M2N98WP"
#api_key='TVQPPAU7D3SY0U1R'
##chose the company symbol
symbol  =   "MSFT"
##require data
stock_data = aqu_stock_data(symbol,api_key)
news_data = get_news_data(symbol,api_key)
if stock_data:
    # save the response content to a file
    with open("Task1/Microsoft Original.json", "w") as f:
        json.dump(stock_data, f)

    # read the response content from the file
    with open("Task1/Microsoft Original.json", "r") as f:
        stock_data_loaded = json.load(f)
        assert stock_data == stock_data_loaded
        print(stock_data_loaded)
else:
    print("data requests fail")