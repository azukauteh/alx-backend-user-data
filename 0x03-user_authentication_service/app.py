#!/usr/bin/env python3
"""flask Application"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    Register a new user route
    """
    email, password = request.form.get('email'), request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": "%s" % email, "message": "user created"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Login a valid user and set a session id"""
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email=email, password=password):
        session_id = AUTH.create_session(email)
        response_data = {"email": email, "message": "logged in"}
        response = make_response(jsonify(response_data))
        response.set_cookie("session_id", session_id)
        return response, 200
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logs out a login user
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
