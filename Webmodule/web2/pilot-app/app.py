from flask import Flask, render_template
from mlab import mlab_connect
from models.service import service

app = Flask(__name__)

# 1. connect to database
mlab_connect()

# 2. design database

# ngan = service(name = "Ngann",yob = 1993, gender = 0, height = 165, phone = "0212312313", occupied = False)
# ngan.save()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/service/<int:gender>')
def search(gender):
    filtered_services = service.objects(gender = gender, occupied = False)
    all_services = service.objects()
    # first_service = all_services[0]
    return render_template('search.html',all_services = filtered_services)


if __name__ == '__main__':
  app.run(debug=True)
