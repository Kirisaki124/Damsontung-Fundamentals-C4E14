from mongoengine import Document, StringField, IntField

class service(Document):
    name = StringField()
    des = StringField()
    rate = IntField()
    game = StringField()
