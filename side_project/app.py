from flask import Flask, render_template
from mlab import mlab_connect
from models.services import service

app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lol')
def lol():
    return render_template('lol.html')

@app.route('/csgo')
def csgo():
    return render_template('csgo.html')

@app.route('/dota')
def dota():
    return render_template('dota.html')

@app.route('/search')
def search():
    filtered_services = service.objects
    return render_template('all.html',all_services = filtered_services)
if __name__ == '__main__':
  app.run(debug=True)
