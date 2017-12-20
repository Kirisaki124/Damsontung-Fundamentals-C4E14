from pymongo import *
from mongoengine import document

client = MongoClient("mongodb://admin:kirari124@ds159856.mlab.com:59856/warmwinter")

db = client.get_default_database()
service = db['service']

# x = document.objects.get(id='5a362a76f4cb0e0ce01d7197')
x = db.service.find({"_id": '5a362a76f4cb0e0ce01d7197'})
print(x)
# for document in x:
#     print(document)
