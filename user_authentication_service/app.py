#!/usr/bin/env python3
"""create a basic flask app"""
import flask
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def first_message():
    message = {"message": "Bienvenue"}
    return flask.jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
