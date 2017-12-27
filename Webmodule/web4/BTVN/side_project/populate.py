from mlab import mlab_connect
from models.services import service
from faker import Faker
from random import randint, choice

name_faker = Faker()
mlab_connect()

for _ in range(100):
    services = service(
                        name = name_faker.name(),
                        des = choice(["really stupid","normal","godlike"]),
                        rate = randint(0,5),
                        game = choice(["LOL","DOTA","CSGO"]),
                        price = choice(["10000","20000","30000"]))
    services.save()
