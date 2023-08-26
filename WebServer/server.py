from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template('index.html')
print(home)

# @app.route("/about.html")
# def about():
#     return render_template('about.html') 

# @app.route("/user/<username>/<int:post_id>")
# def user(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs"

# @app.route("/favicon.ico")
# def blog():
#     return "These are my thoughts on blogs"