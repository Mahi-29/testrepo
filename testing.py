from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mahis:Ki8PconYWZqYp4iD@pythonproject.lnqrejm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.get_database('myInfo')

d = {
    'name': 'mahish Kadam',
    'email': 'mahish@gmail.com',
    'role': 'datascientist',
    'position': 'manager'
}

collection = db.get_collection('deep')

collection.insert_one(d)

