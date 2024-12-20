from functools import wraps
from flask import request
from services.auth import AuthService

def protect_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {"message": "Authorization header is missing"}, 403
        
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return {"message": "Invalid Authorization"}, 403

        token = parts[1]
        result = AuthService.decode(token)

        if "error" in result:
            return {"error": "Invalid headers"}, 403
        
        return f(*args, **kwargs)
    
    return decorated_function

        

