from flask_restx import Namespace, Resource
from app.controllers.coins_controller import CoinsController
from app.api.parsers.coin_parsers import CoinParsers
from app.decorators.protect_route import protect_route

api = Namespace('coins', description='Coins related operations')


@api.route('/api/v1.0/coins/list', methods=['GET'])
class Coins(Resource):
    @api.expect(CoinParsers.pagination_parser())
    @protect_route
    def get(self):
        return CoinsController.get_coins_list()


@api.route('/api/v1.0/coins/categories/list', methods=['GET'])
class CoinCategories(Resource):
    @api.expect(CoinParsers.pagination_parser())
    @protect_route
    def get(self):
        return CoinsController.get_coins_categories_list()
    
@api.route('/api/v1.0/coins/markets', methods=['GET'])
class CoinDetails(Resource):
    @api.expect(CoinParsers.coin_details_parser())
    @protect_route
    def get(self):
        return CoinsController.get_coin_details()
