from flask import Flask

app = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World"



    
