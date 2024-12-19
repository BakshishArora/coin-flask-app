from flask import request
from services.coin_service import CoinService
from services.utils import Utilities

class CoinsController:

    @classmethod
    def get_coins_list(cls):
        try:
            page_num = request.args.get('page_num', default=1, type=int) 
            per_page = request.args.get('per_page', default=10, type=int)

            data = CoinService.get_coins_list()

            start, end = Utilities.pagination(page_num,per_page)
            paginated_data = data[start:end]

            for d in paginated_data:
                d["platform"] = {}

            return paginated_data
        except Exception as e:
            return {"message": str(e)}, 400

    @classmethod
    def get_coins_categories_list(cls):
        page_num = request.args.get('page_num', default=1, type=int) 
        per_page = request.args.get('per_page', default=10, type=int)

        data = CoinService.get_coins_categories_list()

        start, end = Utilities.pagination(page_num,per_page)
        paginated_data = data[start:end]

        return paginated_data
