from flask import request
from app.services.auth import AuthService

users = {'Bakshish': 'BakshishPassword'}

class AuthController:

    @classmethod
    def get_credentials(cls, data):
        username = data.get('username')
        password = data.get('password')
        if username in users and users[username]==password:
            token = AuthService.generate_jwt(username)
            return {'access_token': token}, 200
        return {'error': 'Invalid User Credentials'}
        
    @classmethod
    def authorize(cls, auth_header):
        token = auth_header.split(" ")[1]
        decoded_payload = AuthService.decode(token)
        if decoded_payload == 'error':
            return {'error': 'Invalid Payload'}

        return {"logged_in_as": decoded_payload['username']}
