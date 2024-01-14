import pymongo
from pymongo import MongoClient
def up_mongoDB(stock_data,news_data):
    ## URL of my MongoDB and test if I could connect it
    url='mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(url)
    try:
        client.admin.command('ping')
        print("Pinged your deplyment. You successfully connected to MongoDB")
    except Exception as e:
        print(e)
    ## create a database called StockPrice and name the collection Microsoft
    db=client.StockPrice
    db2=client.Newsdata
    ## initialise the Mongodb database and ready to collect any datas
    Microsofts=db.Microsoft
    Microsofts_news=db2.MicrosoftNews
    Microsofts.delete_many({}) #delete all the data in the collection
    Microsofts_news.delete_many({})
    insert_result = Microsofts.insert_one(stock_data)
    insert_result2=Microsofts_news.insert_one(news_data)
    ## print the ID of saving action
    print("Stock Data Inserted, ID:", insert_result.inserted_id)
    print("News Data Inserted, ID:", insert_result2.inserted_id)