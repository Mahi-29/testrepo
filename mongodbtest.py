from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mahis:Ki8PconYWZqYp4iD@pythonproject.lnqrejm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connectiona

client.admin.command('ping')
db = client.db
print(db)
print("Pinged your deployment. You successfully connected to MongoDB!")

d = {
    'name': "Mahish",
    'email': 'mahish.kadam@gmail.com',
    'surname': 'kumar'
}
db1 = client['Mongotest']
coll = db1['test']
coll.insert_one(d)
