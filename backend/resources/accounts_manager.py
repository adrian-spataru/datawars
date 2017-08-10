import logging
from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from models.user import User
from utils.db import save_record
from utils.auth.token import JWT

logger = logging.getLogger(__name__)


class LoginResource(Resource):
    """this class handles login and authentication"""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username",
                                 type=str,
                                 required=True,
                                 help="username is required",
                                 location="json")

        self.parser.add_argument("password",
                                 type=str,
                                 required=True,
                                 help="password is required",
                                 location="json")

    def post(self):
        args = self.parser.parse_args()
        username = args.get("username").strip()
        password = args.get("password").strip()

        if any(arg == "" for arg in [username, password]):
            response = ("message", "username and password is required", 400)
        else:
            user = User.query.filter_by(username=username).first()
            if user:
                if user.verify_password(password):
                    token = JWT.create_token(user.id)
                    response = ("token", token, 200)
                else:
                    response = ("message",
                                "username or password is incorrect", 401)
            else:
                response = ("message",
                            "username or password is incorrect", 401)

        return make_response(jsonify({
            response[0]: response[1]
        }), response[2])


class RegisterResource(Resource):
    """docstring for AccountsManager."""
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username",
                                 type=str,
                                 required=True,
                                 help="username is required",
                                 location="json")

        self.parser.add_argument("password",
                                 type=str,
                                 required=True,
                                 help="password is required",
                                 location="json")

    def post(self):
        args = self.parser.parse_args()

        username = args.get("username").strip()
        password = args.get("password").strip()

        if any(arg == "" for arg in [username, password]):
            response = ("username and password is required", 400)

        elif not username.isalpha():
            response = ("username should not contain special characters", 400)

        elif len(password) < 6:
            response = ("password should be more than 6 characters", 400)

        elif User.find_by_username(username):
            response = ("username already exists", 409)
        else:
            user = User(username, password)
            print("\n\nhello\n\n\n")
            # save the user data to the database
            save_record(user)

            response = ("user registered successfully", 201)

        return make_response(jsonify({
            "message": response[0]
        }), response[1])
