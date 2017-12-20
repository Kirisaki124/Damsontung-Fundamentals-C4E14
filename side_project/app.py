from flask import Flask, render_template
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
if __name__ == '__main__':
  app.run(debug=True)
