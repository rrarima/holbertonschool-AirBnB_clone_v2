#!/usr/bin/python3
"""Script that start Flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/is_fun", strict_slashes=False)
def c_is_fun():
    return "C is fun"


@app.route("/c/cool", strict_slashes=False)
def c_cool():
    return "C cool"



if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
