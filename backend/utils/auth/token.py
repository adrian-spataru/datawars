import os
from datetime import datetime, timedelta

import jwt

secret = os.getenv("TOKEN_SECRET")


class JWT:
    @classmethod
    def create_token(cls, user_id):
        utcnow = datetime.utcnow()
        user_data = {
            'user_id': user_id,
            'iat': utcnow,
            'exp': utcnow + timedelta(seconds=int(604800)),
        }
        return jwt.encode(user_data,
                          secret,
                          algorithm='HS256').decode('utf-8')

    @classmethod
    def decode_token(cls, token):
        try:
            user = jwt.decode(token, secret)
            return user['user_id']
        except jwt.exceptions.InvalidTokenError:
            return "Invalid Token, please login again"
        except jwt.exceptions.ExpiredSignatureError:
            return "Token has expired, please login again"
