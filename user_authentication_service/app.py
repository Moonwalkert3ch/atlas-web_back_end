#!/usr/bin/env python3
"""create a basic flask app"""
import flask
from flask import Flask
from auth import Auth
from flask import request
from flask import abort
from flask import jsonify


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def first_message():
    message = {"message": "Bienvenue"}
    return flask.jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")


@app.route('/users', methods=['POST'])
def user_registration():
    """Looks for email and password"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    message = {"email": "<registered email>", "message": "user created"}
    return jsonify(message)
