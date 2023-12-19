'''
Task 1

'''
##import the libaray of requests and json
import  requests
import json
import pymongo
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
        return response.json()
    else:
        print("could not use API")
##input API key and choose the company which is Microsoft
##API key
#api_key='ON5BZ9UVB3BC2CCA'
api_key='TVQPPAU7D3SY0U1R'


##chose the company symbol
symbol  =   "MSFT"

##require data
stock_data = aqu_stock_data(symbol,api_key)

url='mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

try:
    client.admin.command('ping')
    print("Pinged your deplyment. You successfully connected to MongoDB")
except Exception as e:
    print(e)