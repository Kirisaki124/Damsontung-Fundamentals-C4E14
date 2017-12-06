from pymongo import MongoClient
client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()

blog = db["posts"]

new_post ={
    "title": "Đàm Tùng",
    "author": "Đàm",
    "content": "Em nộp bài này thôi bài khác chưa xong"
}
blog.insert_one(new_post)
posts = blog.find()
for post in posts:
    print(post)
