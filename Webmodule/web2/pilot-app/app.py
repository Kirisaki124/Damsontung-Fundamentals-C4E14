from flask import Flask, render_template, redirect, url_for
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

@app.route('/admin')
def admin():
    return render_template('admin.html', services = service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    if service is None:
        return "not found"
    else:
        service.objects(id = service_id).delete()
        return redirect(url_for('admin'))
if __name__ == '__main__':
  app.run(debug=True)
