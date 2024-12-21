from flask import request
from app.services.coin_service import CoinService
from app.services.utils import Utilities
from app.config import Config

class CoinsController:

    @classmethod
    def get_coins_list(cls):
        try:
            page_num = request.args.get('page_num', default=1, type=int) 
            per_page = request.args.get('per_page', default=Config.DEFAULT_PAGE_SIZE, type=int)

            data = CoinService.get_coins_list()

            start, end = Utilities.pagination(page_num,per_page)
            paginated_data = data[start:end]

            for d in paginated_data:
                d["platform"] = {}

            return paginated_data
        
        except Exception as e:
            return {"message": str(e)}, 500

    @classmethod
    def get_coins_categories_list(cls):
        try:
            page_num = request.args.get('page_num', default=1, type=int) 
            per_page = request.args.get('per_page', default=Config.DEFAULT_PAGE_SIZE,type=int)

            data = CoinService.get_coins_categories_list()

            start, end = Utilities.pagination(page_num,per_page)
            paginated_data = data[start:end]

            return paginated_data
                
        except Exception as e:
            return {"message": str(e)}, 500

    @classmethod
    def get_coin_details(cls):
        try:
            # requesting page number and items per page 
            page_num = request.args.get('page_num', default=1, type=int) 
            per_page = request.args.get('per_page', default=Config.DEFAULT_PAGE_SIZE, type=int)


            # requesting Coin ID or Category from the User
            coin_id = request.args.get('id')  
            category = request.args.get('category')

            data = CoinService.get_coin_details(Config.VS_CURRENCY)

            start, end = Utilities.pagination(page_num,per_page)
            paginated_data = data[start:end]
            
            return paginated_data
        
        except Exception as e:
            return {"message": str(e)}, 500