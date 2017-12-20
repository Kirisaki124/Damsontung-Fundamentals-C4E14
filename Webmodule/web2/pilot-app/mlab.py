import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds159856.mlab.com:59856/warmwinter
                                #host              #port #db_name
host = "ds159856.mlab.com"
port = 59856
db_name = "warmwinter"
user_name = "admin"
password = "kirari124"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
