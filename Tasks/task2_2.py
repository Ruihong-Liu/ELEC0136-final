from flask import Flask, jsonify, request
from pymongo import MongoClient
import bson

app = Flask(__name__)
client = MongoClient('your_mongodb_url')
db = client['your_database']

@app.route('/create', methods=['POST'])
def create():
    item = request.json
    result = db['your_collection'].insert_one(item)
    return jsonify(success=bool(result.inserted_id)), 201

@app.route('/read', methods=['GET'])
def read():
    query = request.args.get('query')
    items = list(db['your_collection'].find({'$text': {'$search': query}}))
    return jsonify(items), 200

@app.route('/update', methods=['PATCH'])
def update():
    item_id = request.json.get('id')
    properties = request.json.get('properties')
    result = db['your_collection'].update_one({'_id': bson.ObjectId(item_id)}, {'$set': properties})
    return jsonify(success=result.modified_count > 0), 200

@app.route('/delete', methods=['DELETE'])
def delete():
    item_id = request.args.get('id')
    result = db['your_collection'].delete_one({'_id': bson.ObjectId(item_id)})
    return jsonify(success=bool(result.deleted_count)), 200

if __name__ == '__main__':
    app.run(debug=True)
