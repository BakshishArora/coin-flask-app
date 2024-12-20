import datetime
from datetime import timezone
import jwt
from config import Config

class AuthService:
    
    @classmethod
    def generate_jwt(cls, username): 
        payload = {
            "username": username,
            "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=120)
            }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
        return token

    @classmethod
    def decode(cls, token):
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')
            return payload
        except jwt.ExpiredSignatureError:
            return "error"
        except jwt.InvalidTokenError:
            return "error"
    
     
        