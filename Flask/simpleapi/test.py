from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<h2>Hello From Flask!</h2>"