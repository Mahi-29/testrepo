from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mahis:Ki8PconYWZqYp4iD@pythonproject.lnqrejm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.test
print(db)

data = {
    "name": "Deepali",
    "email": "deepakadam@yahoo.co.uk",
    "subject": ["MSCIT", "Coraldraw", "AutoCad", "photoshop"]
}

database = client["myInfo"]
coll = database["deep"]
coll.insert_one(data)

