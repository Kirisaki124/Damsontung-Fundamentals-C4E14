# from flask import Flask, render_template, redirect, url_for, request, flash
from flask import *
from mlab import mlab_connect
from models.service import Service

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf hfieji iasjd2u3 412 dfkjdsf23 fdsfasf23 "
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
    filtered_services = Service.objects(gender = gender, occupied = False)
    all_services = Service.objects()
    # first_service = all_services[0]
    return render_template('search.html',all_services = filtered_services)

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    if Service is None:
        return "not found"
    else:
        Service.objects(id = service_id).delete()
        return redirect(url_for('admin'))

@app.route('/new_service', methods = ['GET', 'POST'])
def new_service():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        # print(name, phone)

        new_service = Service(name = name, phone = phone, yob = yob, gender = gender, height = height, occupied = False)
        new_service.save()
        flash("Đã đăng ký thành công")
        return render_template('new_service.html')

@app.route('/edit/<service_id>', methods = ['POST','GET'])
def edit_service(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not found"
    else:
        if request.method == "GET":
            return render_template('edit_service.html', service = service)
        elif request.method == "POST":
            form = request.form
            name = form['name']
            phone = form['phone']
            yob = form['yob']
            gender = form['gender']
            height = form['height']
            service.update(set__name = name, set__phone = phone, set__yob = yob, set__gender = gender, set__height = height)
            service.reload()
            flash("Đã sửa thành công")
            return render_template('edit_service.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
