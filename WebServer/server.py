from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/user/<username>/<int:post_id>")
def user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/blog")
def blog():
    return "These are my thoughts on blogs"

# @app.route("/favicon.ico")
# def blog():
#     return "These are my thoughts on blogs"