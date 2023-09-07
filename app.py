from flask import Flask
from modules.TestQuestion import TestQuestion

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return TestQuestion().answer()