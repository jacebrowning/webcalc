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
    return "My favorite beverage is Bell's Hopslam."


@app.route('/<int:a>/<name>/<int:b>')
@app.route('/<float:a>/<name>/<float:b>')
def calc(a, name, b):
    operation = mongo.db.operations.find_one({'name': name})
    if operation:
        return Template(operation['pattern']).render(a=a, b=b)
    else:
        return f"Result: {a} {name} {b} = ???"


if __name__ == '__main__':
    app.run(debug=True)
