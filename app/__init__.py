from flask import Flask, request
import requests
from flask_restx import Resource, Api
from api.coins import api as coins_namespace


app = Flask(__name__)

api = Api(app)
api.add_namespace(coins_namespace)


@api.route('/health')
class Health(Resource):
    def get(self):
        return {'message': 'Healthy'}, 200


@api.route('/version')
class Version(Resource):
    def get(self):
        return {'version': '1.0.0'}, 200


if __name__ == '__main__':
    app.run(debug=True)