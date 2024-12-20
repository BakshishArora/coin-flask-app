from flask_restx import reqparse

class CoinParsers:
    
    @classmethod
    def coin_details_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('coin_id', type=str, help='id of the coin')
        parser.add_argument('category', type=str, help='category of the coin')
        parser.add_argument('page_num', type=int, help='page number')
        parser.add_argument('per_page', type=int, help='items per page')

        return parser
    
    @classmethod
    def pagination_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('page_num', type=int, help='page number')
        parser.add_argument('per_page', type=int, help='items per page')
        
        return parser