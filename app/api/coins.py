from flask_restx import Namespace, Resource
from controllers.coins_controller import CoinsController


api = Namespace('coins', description='Coins related operations')


@api.route('/api/v1.0/coins/list', methods=['GET'])
class Coins(Resource):
    def get(self):
        return CoinsController.get_coins_list()


@api.route('/api/v1.0/coins/categories/list', methods=['GET'])
class CoinCategories(Resource):
    def get(self):
        return CoinsController.get_coins_categories_list()
    
@api.route('/api/v1.0/coins/markets', methods=['GET'])
class CoinDetails(Resource):
    def get(self):
        return CoinsController.get_coin_details()
