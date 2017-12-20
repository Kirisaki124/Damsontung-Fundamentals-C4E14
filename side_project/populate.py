from mlab import mlab_connect
from models.services import service
from faker import Faker
from random import randint

name_faker = Faker()
mlab_connect()

for _ in range(5):
    services = service(
                        name = name_faker.name(),
                        des = "danh ngu vl",
                        rate = randint(0,5))
    services.save()
