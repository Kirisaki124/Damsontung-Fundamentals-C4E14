from mlab import mlab_connect
from models.services import service
mlab_connect()
all_services = service.objects()
for services in all_services:
    print(service.name)
