from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "My favorite beverage is Bell's Hopslam."


if __name__ == '__main__':
    app.run(debug=True)
