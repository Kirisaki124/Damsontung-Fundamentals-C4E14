from pymongo import MongoClient
from matplotlib import pyplot


client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.get_default_database()

blog = db["customers"]

posts = blog.find()

# print(posts['ref'].count("events"))
# #
ads = 0
wom = 0
event = 0

for post in posts:
    # print(post["ref"])
    if "events" in post["ref"]:
    # print(post["ref"].count("events"))
        event += 1
    elif "wom" in post["ref"]:
        wom += 1
    else:
        ads += 1
# print(event, wom, ads, sep="  ")






labels = ["events", "wom", "ads"]
colors = ["red", "blue", "yellow"]
date = [event, wom, ads]

pyplot.pie(date, labels = labels, colors = colors, shadow = True)
pyplot.axis("equal")
pyplot.show()
