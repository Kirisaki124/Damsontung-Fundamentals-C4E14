from mongoengine import Document, StringField, IntField

class Service(Document):
    name = StringField()
    des = StringField()
    rate = IntField()
    game = StringField()
    price = IntField()
