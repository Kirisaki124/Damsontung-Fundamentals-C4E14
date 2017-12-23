from flask import Flask, render_template, redirect, url_for
from mlab import mlab_connect
from models.services import service

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<game>')
def search(game):
    filtered_services = service.objects(game = game)
    all_services = service.objects()
    return render_template('all.html',all_services = filtered_services)

@app.route('/admin')
def admin():
    all_services = service.objects()
    return render_template('admin.html', services= all_services)

@app.route('/delete/<service_id>')
def delete(service_id):
    if service is None:
        return "Not found"
    else:
        service.objects(id = service_id).delete()
        return redirect(url_for('admin'))

@app.route('/info/<service_id>')
def info(service_id):
    if service is None:
        return "not found"
    else:
        services = service.objects().with_id(service_id)
        return render_template('info.html', service = services)
if __name__ == '__main__':
  app.run(debug=True)
