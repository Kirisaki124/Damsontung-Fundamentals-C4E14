from flask import Flask, render_template, redirect, url_for, request, flash
from mlab import mlab_connect
from models.services import Service

app = Flask(__name__)
app.config["SECRET_KEY"] = "mekB'GU'w4A@<US#"
mlab_connect()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<game>')
def search(game):
    filtered_services = Service.objects(game = game)
    all_services = Service.objects()
    return render_template('all.html',all_services = filtered_services)

@app.route('/admin')
def admin():
    all_services = Service.objects()
    return render_template('admin.html', services= all_services)

@app.route('/delete/<service_id>')
def delete(service_id):
    if service is None:
        return "Not found"
    else:
        Service.objects(id = service_id).delete()
        return redirect(url_for('admin'))

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == "GET":
        return render_template('new.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        game = form['game']
        price = form['price']
        rate = 0
        des = form['des']
        new = Service(name = name, game = game, price = price, rate = rate ,des = des)
        new.save()
        flash('Đã đăng ký xong')
        return render_template('new.html')
@app.route('/info/<service_id>')
def info(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "not found"
    else:
        return render_template('info.html', service = service)

@app.route('/edit/<service_id>', methods = ['GET', 'POST'])
def edit_service(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not found"
    else:
        if request.method == "GET":
            return render_template('edit.html', service = service)
        elif request.method == "POST":
            form = request.form
            name = form['name']
            game = form['game']
            des = form['des']
            price = form['price']
            service.update(set__name = name, set__game = game, set__des = des, set__price = price)
            service.reload()
            return redirect(url_for('admin'))
if __name__ == '__main__':
  app.run(debug=True)
