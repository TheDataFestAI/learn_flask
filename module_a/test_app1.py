from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! from <strong> 'module_a/test_app1.py' </strong>"