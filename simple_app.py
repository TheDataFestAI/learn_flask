from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! from <strong> simple_app.py </strong>"
