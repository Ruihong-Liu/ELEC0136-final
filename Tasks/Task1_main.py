from task1_1 import aqu_stock_data
from task1_2 import get_news_data
def main1():
    #API keys
    api_key="NN2SRNCT5M2N98WP"
    #api_key='TVQPPAU7D3SY0U1R'
    ##chose the company symbol
    symbol  =   "MSFT"
    ##request data
    stock_data = aqu_stock_data(symbol,api_key)
    news_data = get_news_data(symbol,api_key)
    return stock_data,news_data