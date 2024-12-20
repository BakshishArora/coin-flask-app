from flask_restx import reqparse

class Credentials:

    @classmethod
    def parse_credentials(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help='Enter username')
        parser.add_argument('password',type=str,required=True,help='Enter password')

        return parser
    