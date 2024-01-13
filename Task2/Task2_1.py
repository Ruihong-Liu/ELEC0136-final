import pymongo
def up_mongoDB():
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
    ## initialise the Mongodb database and ready to collect any datas
    db.collection.drop()
    Microsofts=db.Microsoft

    insert_result = Microsofts.insert_one(stock_data)
    print("Data Inserted, ID:", insert_result.inserted_id)