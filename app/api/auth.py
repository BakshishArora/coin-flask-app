from flask import Flask, request
from flask_restx import Resource, Namespace
from app.controllers.auth_controller import AuthController
from app.api.parsers.credential_parser import Credentials

api1 = Namespace('authorize', description='Authorization')

@api1.route('/login', methods=['POST'])
class Login(Resource):
    @api1.expect(Credentials.parse_credentials())
    def post(self):
        data = dict()
        parser = Credentials.parse_credentials().parse_args()
        data['username']= parser['username']
        data['password']= parser['password']
        if data:
            if not data.get('username') and not data.get('password'):
                return {'error': 'Username or Password is missing'}, 400
        
        return AuthController.get_credentials(data)
    
@api1.route('/protected', methods=['GET'])
class Protected(Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {"error": "Authorization header is missing"}, 401
        
        return AuthController.authorize(auth_header)