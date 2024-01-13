from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# 连接到MongoDB数据库
# MongoDB 连接
client = MongoClient("mongodb+srv://sui1223:Lrh118828769@cluster0.4axd2vy.mongodb.net/?retryWrites=true&w=majority")
db = client["StockPrice"]
collection = db["Microsoft"]

# CRUD操作
@app.route('/create', methods=['POST'])
def create():
    item = request.json
    result = collection.insert_one(item)
    return jsonify(success=result.acknowledged), 201

@app.route('/read', methods=['GET'])
def read():
    query = request.args.to_dict()
    results = collection.find(query)
    return jsonify([str(item) for item in results]), 200

@app.route('/update', methods=['PUT'])
def update():
    item_id = request.args.get('id')
    properties = request.json
    result = collection.update_one({'_id': ObjectId(item_id)}, {'$set': properties})
    return jsonify(success=result.modified_count > 0), 200

@app.route('/delete', methods=['DELETE'])
def delete():
    item_id = request.args.get('id')
    result = collection.delete_one({'_id': ObjectId(item_id)})
    return jsonify(success=result.deleted_count > 0), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)