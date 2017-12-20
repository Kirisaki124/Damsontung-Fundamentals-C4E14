from pymongo import *
from mongoengine import *
from bson.objectid import ObjectId

client = MongoClient("mongodb://admin:kirari124@ds159856.mlab.com:59856/warmwinter")

db = client.get_default_database()
service = db['service']

# x = document.objects.get(id='5a362a76f4cb0e0ce01d7197')


i = []
id_to_find = '5a362a76f4cb0e0ce01d7197'
x = db.service.find({"_id": ObjectId(id_to_find)})
# print(x)
for document in x:
    i.append(document)
print(i)

# db.service.objects.get(_id="5a362a76f4cb0e0ce01d7197")
