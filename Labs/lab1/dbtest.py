from pymongo import MongoClient
#connect to database
client = MongoClient("mongodb://admin:kirari124@ds127936.mlab.com:27936/c4e14-damtung")

#get default database
db = client.get_default_database()

#get collection
blog = db['blog']

# #insert document
# new_post = {
#     "title": "ngay 2",
#     "content": "toi di choi",
# }
# blog.insert_one(new_post)

posts = blog.find() #get all posts in blog
for post in posts:
    print(post)
