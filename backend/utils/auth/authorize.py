import logging
from functools import wraps
from flask_restful import request

from models.user import User
from utils.auth.token import JWT

logger = logging.getLogger(__name__)


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        user_id = None
        try:
            token = request.headers['Authorization']
            user_id = JWT.decode_token(token)  # decode the token

            if isinstance(user_id, int):
                user = User.query.get(user_id)

                if user:
                    response = ("login was successful", 200)
                else:
                    response = ("Invalid token, please login again", 401)
            else:
                response = (user_id, 401)
                user_id = None

        except KeyError as err:
            response = ("Please login to access your bucketlists", 401)
            logger.error(err)  # log the error

        updated_kwargs = {
            "response": response,
            "user_id": user_id
        }

        # append updated_kwargs with the existing kwargs values
        for key, value in kwargs.items():
            updated_kwargs[key] = value

        return func(*args, **updated_kwargs)
    return decorated
