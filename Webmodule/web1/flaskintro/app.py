from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    post_list = ["2 con than lan con", "qua nho", "anh muon gi nao","linh"]
    return render_template('index.html',
                            article_title = "1 little duck",
                            posts = post_list)

@app.route('/blog')
def blog():
    posts = [
        {
        "content": "2 con than lan con",
        "author": "Thanh"
        },
        {
        "content": "anh muon gi nao",
        "author": "Huong"
        },
        {
        "content": "qua nho",
        "author": "quan"
        },
    ]
    return render_template("blog.html",posts = posts)

@app.route('/me')
def me():
    return "hello me"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "hello " + name

# @app.route('/add/<a>/<b>')
# def add(a,b):
#     return str(int(a)+int(b))

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return str(a+b)

@app.route('/heading')
def heading():
    return "<h1>  heading 1  </h1>"

if __name__ == '__main__':
  app.run(debug=True)
