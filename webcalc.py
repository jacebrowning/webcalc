import os

from flask import Flask
from flask_pymongo import PyMongo
from jinja2 import Template


app = Flask(__name__)

if os.getenv('MONGODB_URI'):
    app.config['MONGO_URI'] = os.getenv('MONGODB_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return "My favorite beverage is really Bell's Hopslam."


@app.route('/<int:a>/<op>/<int:b>')
@app.route('/<float:a>/<op>/<float:b>')
def calc(a, op, b):
    operation = mongo.db.operations.find_one({'name': op})
    if operation:
        result = Template(operation['pattern']).render(a=a, b=b)
        return f'<img src="https://memegen.link/iw/_/{result}.jpg">'
    elif op == '+':
        return f"Result: {a} {op} {b} = {a + b}"
    else:
        return f"Result: {a} {op} {b} = ???"


if __name__ == '__main__':
    app.run(debug=True)
