from mlab import mlab_connect
from models.service import service

from faker import Faker
from random import choice , randint

service_faker = Faker()
mlab_connect()
# print(service_faker.name())
# service.drop_collection()
for _ in range(30):
    services = service(name=service_faker.name(),
                  yob = randint(1987,1998),
                  gender = randint(0,1),
                  height = randint(150,180),
                  phone = "01111111",
                  occupied = choice([True,False]))
    services.save()
