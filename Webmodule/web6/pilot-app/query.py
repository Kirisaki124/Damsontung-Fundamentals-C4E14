from mlab import mlab_connect
from models.service import service
mlab_connect()
all_services = service.objects()

# first_service = all_services[1]
# print(first_service.name)
for service in all_services:
    print(service.name)
