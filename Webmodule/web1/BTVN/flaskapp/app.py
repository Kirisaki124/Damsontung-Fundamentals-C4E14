from flask import Flask, render_template, redirect, url_for
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-me/')
def infor():
    information = [
    {
        "name": "Dam Son Tung",
        "age": "18",
        "school": "FPT university"
    }
    ]
    return render_template("about-me.html", information = information)

@app.route('/school')
def school():
    return redirect("http://techkids.vn/")


if __name__ == '__main__':
  app.run(debug=True)
