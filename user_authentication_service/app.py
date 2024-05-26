#!/usr/bin/env python3
"""create a basic flask app"""
import flask
from flask import Flask
from auth import Auth
from flask import request, make_response, redirect
from flask import abort
from flask import jsonify


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def first_message():
    message = {"message": "Bienvenue"}
    return flask.jsonify(message)


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


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """validates user credentials, creates a session if valid and
    responds appropriately"""
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
                })
            response.set_cookie('session_id', session_id)

            return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """destroys the session and redirect to get"""
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None:
        abort(403)

    AUTH.destroy_session(user.id)
    response = redirect('/')
    response.delete_cookie('session_id')

    return response


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """request cookies to find user respond
    with 200 if found"""
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": "<user email>"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
