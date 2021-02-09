from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/')
def puppy_love():
    return 'I love puppies!'