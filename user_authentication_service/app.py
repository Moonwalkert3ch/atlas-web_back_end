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


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """response to the GET /profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """generate a token and respond with a 200 HTTP status"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    msg = {"email": email, "reset_token": reset_token}

    return jsonify(msg), 200

@app.route('/reset_password', methods=['PUT'])
def update_password():
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
    except KeyError:
        return jsonify({"message": "Missing required fields"}), 400

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        return jsonify({"message": "Invalid reset token"}), 403

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
