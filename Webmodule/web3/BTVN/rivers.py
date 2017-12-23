from mlab import *
from mongoengine import *

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
mlab_connect()


# rivers = river.objects(continent="Africa")
#
# for river in rivers:
#     print(river.name)


rivers = river.objects(continent="S. America",length__lt = 1000)
for river in rivers:
    print(river.name)
