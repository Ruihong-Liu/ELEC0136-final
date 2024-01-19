import pymongo
url='mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)
db = client['StockPrice']
def Create(collection,data):
    collection = db['Microsoft']
    try:
        collection.insert_one(data)
        print('Create Success')
        return True
    except Exception as e:
        print(e)

def Read(collection,query):
    collection = db['Microsoft']
    try:
        data=[]
        for i in collection.find(query):
            data.append(i)
            print(i)
        return data
    except Exception as e:
        print(e)

def Update(collection,query,new_value):
    collection = db['Microsoft']
    try:
        collection.update_one(query,{'$set':new_value})
        print('Update Success')
    except Exception as e:
        print(e)

def Delete(collection,id):
    collection = db['Microsoft']
    try:
        collection.delete_one(id)
        print('Delete Success')
    except Exception as e:
        print(e)