from flask import Flask

app = Flask(__name__)

@my-app.route("/")
def hello():
    return "Hello World"

@my-app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
